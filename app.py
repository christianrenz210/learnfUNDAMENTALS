import glob
import json
import os
import queue
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import threading
import time
import urllib.error
import urllib.request
import uuid
from datetime import datetime

from flask import (
    Flask,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text as sa_text
from werkzeug.security import check_password_hash, generate_password_hash

from lessons_data import LESSONS, LONG_QUIZZES

SECTION_ORDER = ["Fundamentals", "Advanced Database System", "SQL Injection"]
SECTION_LESSON_MINUTES = {"Fundamentals": 40, "Advanced Database System": 45}
AVAILABLE_LESSONS = [l for l in LESSONS if not l.get("coming_soon")]

LAB_POINTS_PER_LAB = 2
LAB_LESSON_IDS = {19, 20}
LAB_ROUTES = {19: "sql_lab", 20: "sql_lab_2"}

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "change-this-secret-key-in-production")

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///students.db")
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

ALLOWED_AVATAR_EXT = {"png", "jpg", "jpeg", "gif", "webp"}
AVATAR_DIR = os.path.join(app.root_path, "static", "uploads")

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = "Please log in to access that page."
login_manager.login_message_category = "warning"


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    avatar = db.Column(db.String(200), nullable=True)
    lab_completed = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    progress = db.relationship("LessonProgress", backref="user", cascade="all, delete-orphan")
    quiz_scores = db.relationship("QuizScore", backref="user", cascade="all, delete-orphan")
    section_quiz_scores = db.relationship("SectionQuizScore", backref="user", cascade="all, delete-orphan")


class LessonProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    lesson_id = db.Column(db.Integer, nullable=False)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)


class QuizScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    lesson_id = db.Column(db.Integer, nullable=False)
    best_score = db.Column(db.Integer, nullable=False)
    total_questions = db.Column(db.Integer, nullable=False)
    attempts = db.Column(db.Integer, default=1, nullable=False)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class SectionQuizScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    section = db.Column(db.String(100), nullable=False)
    best_score = db.Column(db.Integer, nullable=False)
    total_questions = db.Column(db.Integer, nullable=False)
    attempts = db.Column(db.Integer, default=1, nullable=False)
    last_answers = db.Column(db.Text, nullable=True)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class LabProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    lesson_id = db.Column(db.Integer, nullable=False)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


def is_lab_completed(user, lesson_id):
    if user is None:
        return False
    return (
        db.session.query(LabProgress)
        .filter_by(user_id=user.id, lesson_id=lesson_id)
        .first()
        is not None
    )


def get_completed_lab_ids(user):
    if user is None:
        return set()
    return {lp.lesson_id for lp in LabProgress.query.filter_by(user_id=user.id).all()}


def mark_lab_completed(user, lesson_id):
    if not is_lab_completed(user, lesson_id):
        db.session.add(LabProgress(user_id=user.id, lesson_id=lesson_id))
        db.session.commit()


def unmark_lab_completed(user, lesson_id):
    row = (
        db.session.query(LabProgress)
        .filter_by(user_id=user.id, lesson_id=lesson_id)
        .first()
    )
    if row:
        db.session.delete(row)
        db.session.commit()


def get_completed_ids(user):
    if user is None:
        return set()
    return {p.lesson_id for p in user.progress}


def get_quiz_scores(user):
    if user is None:
        return {}
    return {qs.lesson_id: qs for qs in user.quiz_scores}


def get_leaderboard():
    rows = db.session.query(QuizScore, User.username).join(
        User, QuizScore.user_id == User.id
    ).all()
    stats = {}
    for qs, username in rows:
        entry = stats.setdefault(
            qs.user_id,
            {
                "username": username,
                "points": 0,
                "quizzes": 0,
                "attempts": 0,
                "labs": 0,
                "lab_points": 0,
            },
        )
        entry["points"] += qs.best_score
        entry["quizzes"] += 1
        entry["attempts"] += qs.attempts
    lab_rows = (
        db.session.query(LabProgress, User.username)
        .join(User, LabProgress.user_id == User.id)
        .all()
    )
    for lp, username in lab_rows:
        entry = stats.setdefault(
            lp.user_id,
            {
                "username": username,
                "points": 0,
                "quizzes": 0,
                "attempts": 0,
                "labs": 0,
                "lab_points": 0,
            },
        )
        entry["labs"] += 1
        entry["lab_points"] += LAB_POINTS_PER_LAB
    for entry in stats.values():
        entry["points"] += entry["lab_points"]
    board = sorted(stats.values(), key=lambda e: (-e["points"], e["attempts"]))
    for i, entry in enumerate(board, start=1):
        entry["rank"] = i
    return board


def get_lesson_labs_leaderboard(lesson_id):
    rows = (
        db.session.query(User.username, db.func.count(LabProgress.id))
        .outerjoin(
            LabProgress,
            db.and_(LabProgress.user_id == User.id, LabProgress.lesson_id == lesson_id),
        )
        .group_by(User.id, User.username)
        .all()
    )
    board = sorted(
        (
            {
                "username": username,
                "labs": labs_done,
                "points": labs_done * LAB_POINTS_PER_LAB,
            }
            for username, labs_done in rows
            if labs_done > 0
        ),
        key=lambda e: (-e["labs"], e["username"].lower()),
    )
    for i, entry in enumerate(board, start=1):
        entry["rank"] = i
    return board


def get_lesson_leaderboard(lesson_id):
    rows = db.session.query(QuizScore, User.username).join(
        User, QuizScore.user_id == User.id
    ).filter(QuizScore.lesson_id == lesson_id).all()
    board = sorted(
        (
            {
                "username": username,
                "best_score": qs.best_score,
                "total": qs.total_questions,
            }
            for qs, username in rows
        ),
        key=lambda e: (-e["best_score"], e["username"].lower()),
    )
    for i, entry in enumerate(board, start=1):
        entry["rank"] = i
    return board


def password_errors(password):
    errors = []
    if len(password) < 8:
        errors.append("at least 8 characters")
    if not re.search(r"[A-Z]", password):
        errors.append("one uppercase letter")
    if not re.search(r"[a-z]", password):
        errors.append("one lowercase letter")
    if not re.search(r"\d", password):
        errors.append("one number")
    if not re.search(r"[^A-Za-z0-9]", password):
        errors.append("one special character")
    return errors


@app.context_processor
def inject_user_stats():
    if current_user.is_authenticated:
        return {"user_done": len(get_completed_ids(current_user)), "user_total": len(AVAILABLE_LESSONS)}
    return {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/faq")
def faq():
    return render_template("faq.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/compiler")
@login_required
def compiler():
    return render_template("compiler.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        confirm = request.form.get("confirm_password", "")

        if not username or not email or not password:
            flash("All fields are required.", "danger")
        elif password != confirm:
            flash("Passwords do not match.", "danger")
        elif password_errors(password):
            flash(
                "Password must contain: " + ", ".join(password_errors(password)) + ".",
                "danger",
            )
        elif User.query.filter_by(username=username).first():
            flash("That username is already taken.", "danger")
        elif User.query.filter_by(email=email).first():
            flash("An account with that email already exists.", "danger")
        else:
            user = User(
                username=username,
                email=email,
                password_hash=generate_password_hash(password),
            )
            db.session.add(user)
            db.session.commit()
            flash("Account created successfully! You can now log in.", "success")
            return redirect(url_for("login", registered=1))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash("Welcome back, " + user.username + "!", "success")
            return redirect(url_for("dashboard"))
        flash("Invalid username or password.", "danger")
    return render_template("login.html", registered=request.args.get("registered") == "1")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("index"))


@app.route("/profile", methods=["POST"])
@login_required
def update_profile():
    username = request.form.get("username", "").strip()
    email = request.form.get("email", "").strip()
    new_password = request.form.get("new_password", "")
    confirm = request.form.get("confirm_password", "")
    avatar_file = request.files.get("avatar")
    remove_avatar = request.form.get("remove_avatar") == "yes"

    avatar_error = None
    avatar_data = None
    avatar_ext = ""
    if avatar_file and avatar_file.filename:
        avatar_ext = (
            avatar_file.filename.rsplit(".", 1)[-1].lower()
            if "." in avatar_file.filename
            else ""
        )
        if avatar_ext not in ALLOWED_AVATAR_EXT:
            avatar_error = "Only PNG, JPG, JPEG, GIF, or WebP images are allowed."
        else:
            avatar_data = avatar_file.read()
            if len(avatar_data) > 2 * 1024 * 1024:
                avatar_error = "Image must be 2 MB or smaller."

    if not username or not email:
        flash("Username and email are required.", "danger")
    elif User.query.filter(User.username == username, User.id != current_user.id).first():
        flash("That username is already taken.", "danger")
    elif User.query.filter(User.email == email, User.id != current_user.id).first():
        flash("An account with that email already exists.", "danger")
    elif new_password and new_password != confirm:
        flash("Passwords do not match.", "danger")
    elif new_password and password_errors(new_password):
        flash(
            "Password must contain: " + ", ".join(password_errors(new_password)) + ".",
            "danger",
        )
    elif avatar_error:
        flash(avatar_error, "danger")
    else:
        current_user.username = username
        current_user.email = email
        if new_password:
            current_user.password_hash = generate_password_hash(new_password)
        if avatar_data is not None:
            for old in glob.glob(os.path.join(AVATAR_DIR, f"avatar_{current_user.id}.*")):
                os.remove(old)
            fname = f"avatar_{current_user.id}.{avatar_ext}"
            with open(os.path.join(AVATAR_DIR, fname), "wb") as f:
                f.write(avatar_data)
            current_user.avatar = fname
        elif remove_avatar:
            for old in glob.glob(os.path.join(AVATAR_DIR, f"avatar_{current_user.id}.*")):
                os.remove(old)
            current_user.avatar = None
        db.session.commit()
        flash("Profile updated successfully.", "success")
    return redirect(url_for("dashboard"))


@app.route("/dashboard")
@login_required
def dashboard():
    completed = get_completed_ids(current_user)
    total = len(AVAILABLE_LESSONS)
    done = len(completed)
    percent = round((done / total) * 100) if total else 0
    scores = get_quiz_scores(current_user)
    quiz_points = sum(qs.best_score for qs in scores.values())
    quiz_count = len(scores)
    lab_ids = get_completed_lab_ids(current_user)
    lab_count = len(lab_ids)
    lab_points = lab_count * LAB_POINTS_PER_LAB
    total_points = quiz_points + lab_points
    sections = {}
    for lesson in LESSONS:
        sections.setdefault(lesson.get("section", "Fundamentals"), []).append(lesson)
    for name in SECTION_ORDER:
        sections.setdefault(name, [])
    locked_ids = set()
    for name in SECTION_ORDER:
        sec = sections.get(name, [])
        for i, l in enumerate(sec):
            if l.get("coming_soon"):
                continue
            if i > 0 and sec[i - 1]["id"] not in completed:
                locked_ids.add(l["id"])
    section_quiz_map = {
        q.section: q
        for q in SectionQuizScore.query.filter_by(user_id=current_user.id).all()
    }
    section_stats = []
    for name in SECTION_ORDER:
        sec_lessons = [l for l in sections.get(name, []) if not l.get("coming_soon")]
        if not sec_lessons:
            continue
        sec_done = len([l for l in sec_lessons if l["id"] in completed])
        quiz_row = section_quiz_map.get(name)
        est_minutes = sum(l.get("minutes", SECTION_LESSON_MINUTES.get(name, 45)) for l in sec_lessons)
        section_stats.append(
            {
                "name": name,
                "total": len(sec_lessons),
                "done": sec_done,
                "percent": round((sec_done / len(sec_lessons)) * 100) if sec_lessons else 0,
                "quiz_best": quiz_row.best_score if quiz_row else None,
                "quiz_total": quiz_row.total_questions if quiz_row else None,
                "quiz_attempts": quiz_row.attempts if quiz_row else None,
                "estimate": est_minutes,
                "has_quiz": name in LONG_QUIZZES,
            }
        )
    return render_template(
        "dashboard.html",
        sections=sections,
        section_stats=section_stats,
        locked_ids=locked_ids,
        completed=completed,
        scores=scores,
        leaderboard=get_leaderboard(),
        total=total,
        done=done,
        percent=percent,
        quiz_points=quiz_points,
        quiz_count=quiz_count,
        total_points=total_points,
        lab_points=lab_points,
        lab_count=lab_count,
        all_lessons=AVAILABLE_LESSONS,
        section_minutes=SECTION_LESSON_MINUTES,
        lab_completed=bool(lab_count),
        completed_lab_ids=lab_ids,
    )


@app.route("/certificate/<path:name>")
@login_required
def certificate(name):
    completed = set(get_completed_ids(current_user))
    if name == "Full Course":
        if len(completed) < len(AVAILABLE_LESSONS):
            flash(
                f"Complete all {len(AVAILABLE_LESSONS)} lessons to unlock your full course certificate.",
                "warning",
            )
            return redirect(url_for("dashboard"))
        cert_title = "Course Completion"
        cert_subtitle = "Complete Curriculum - Programming Fundamentals and Advanced Database Systems"
        sec_num = 0
    else:
        sec_lessons = [
            l
            for l in LESSONS
            if l.get("section", "Fundamentals") == name and not l.get("coming_soon")
        ]
        if not sec_lessons:
            flash("Certificate not found.", "danger")
            return redirect(url_for("dashboard"))
        done_count = len([l for l in sec_lessons if l["id"] in completed])
        if done_count < len(sec_lessons):
            flash(f"Complete all {len(sec_lessons)} lessons in the {name} section to unlock this certificate.", "warning")
            return redirect(url_for("dashboard"))
        cert_title = f"{name} Completion"
        cert_subtitle = f"All {len(sec_lessons)} lessons in the {name} section"
        sec_num = (SECTION_ORDER.index(name) + 1) if name in SECTION_ORDER else 0
    issued = datetime.utcnow()
    cert_no = f"CF-{issued.year}-{current_user.id:03d}{sec_num:02d}"
    return render_template(
        "certificate.html",
        cert_no=cert_no,
        cert_title=cert_title,
        cert_subtitle=cert_subtitle,
        section=name,
        issued=issued,
    )


def assistant_reply(message):
    text = message.lower().strip()

    def brief(lesson_id, lead):
        lesson = next((l for l in LESSONS if l["id"] == lesson_id), None)
        if not lesson:
            return lead
        section_lessons = [
            l for l in LESSONS
            if l.get("section", "Fundamentals") == lesson.get("section", "Fundamentals")
        ]
        num = next(i + 1 for i, l in enumerate(section_lessons) if l["id"] == lesson_id)
        pts = " | ".join(lesson["key_points"][:3])
        return f'{lead}\n\nLesson {num} - {lesson["title"]}:\n{pts}'

    def has(*keywords):
        return any(re.search(r"(?<!\w)" + re.escape(k) + r"(?!\w)", text) for k in keywords)

    rules = [
        (lambda: has("long quiz", "section quiz"), "Each section ends with a Long Quiz: 15 questions with 20 seconds per question, and you get 2 attempts total. Your best score is saved on the dashboard. Unlock it by completing every lesson in the section, then find it on your dashboard under By Section, or use the Proceed to Long Quiz button after the last lesson. After taking it you can view the answer review to see which questions you got right or wrong."),
        (lambda: has("quiz", "quizzes", "attempt"), "Each lesson ends with a quiz. You get one attempt per quiz, so answer carefully! Your score is saved on your dashboard and added to the lesson and global leaderboards."),
        (lambda: has("leaderboard", "rank", "ranking", "points", "compete"), "Leaderboards rank users by total points: quiz scores plus lab bonuses. Completing a SQL Injection Lab earns 2 points per lab. There is a global leaderboard on your dashboard and a separate one for each lesson page."),
        (lambda: has("progress", "completed", "dashboard"), "Your dashboard shows your progress: lessons completed, quiz stats, and total points. Mark a lesson complete from the lesson page, then watch your progress bar grow."),
        (lambda: has("vs"), "You learn Python, C++, and Java side by side. Python is interpreted and uses indentation; C++ and Java are compiled and use braces {} and semicolons. Every lesson shows the same concept in all three languages, so you can compare them directly in the lessons."),
        (lambda: has("c++", "cpp", "c plus plus"), "C++ is a compiled language: a compiler turns your source code into a fast machine program before it runs. It is used for games, operating systems, and performance-heavy software. C++ uses braces {} and requires semicolons at the end of each statement."),
        (lambda: has("java"), "Java is a compiled, object-oriented language that runs on the Java Virtual Machine (JVM), so the same code can run on many devices. It is widely used for Android apps and enterprise systems. Like C++, Java uses braces {} and semicolons, and you must declare variable types."),
        (lambda: has("python"), "Python is an interpreted language: it runs line by line, which makes it quick to test. Its readable syntax uses indentation instead of braces, which is why it is so beginner-friendly. Python is popular in data science, web apps, and automation."),
        (lambda: has("language", "languages", "syntax"), "You learn Python, C++, and Java side by side. Python is interpreted and uses indentation; C++ and Java are compiled and use braces {} and semicolons. Every lesson shows the same concept in all three languages."),
        (lambda: has("sql", "database", "dbms", "normaliz", "er model", "entity", "foreign key", "primary key", "ddl", "dml", "dql", "join"), "The Advanced Database System section covers databases and SQL: DBMS overview, ER model and keys, normalization, DDL (CREATE/ALTER/DROP), DML (INSERT/UPDATE/DELETE), SELECT and filtering, JOINs, and subqueries with aggregates. The SQL examples in those lessons run right in your browser against a live database engine."),
        (lambda: has("error", "debug", "compile", "bug"), "Debugging tips: read the error message first, check semicolons and braces in C++/Java, check indentation in Python, and add print statements to see what your code is doing. The code editor lets you test changes instantly."),
        (lambda: has("register", "sign up", "account", "free"), "Creating an account is free and takes seconds. It saves your progress, quiz scores, profile picture, and leaderboard standing."),
        (lambda: has("how it works", "how does this work", "site work"), "It is simple: create an account, read the lessons, run code live in the browser, take the quiz after each lesson, and climb the leaderboard. The Fundamentals section covers programming basics, while the Advanced Database System section teaches databases and SQL."),
        (lambda: has("variable", "variables", "data type", "datatype", "integer", "boolean", "float", "string", "char"), brief(2, "Variables store values in memory. Python infers the type automatically; C++ and Java require you to declare it before the name.")),
        (lambda: has("logical"), brief(5, "Logical operators combine true/false values. Python: and, or, not. C++/Java: &&, ||, !. Both conditions are checked to build bigger conditions.")),
        (lambda: has("operator", "operators", "arithmetic", "modulo", "remainder"), brief(4, "Operators do math and comparisons. Arithmetic: + - * / %. Relational: == != < > <= >=. Comparison always produces true or false.")),
        (lambda: has("conditional", "if else", "if-else", "elif", "else if", "decision"), brief(6, "Conditionals make decisions. Python uses if/elif/else with colons; C++ and Java use if/else if/else with braces and parentheses.")),
        (lambda: has("loop", "loops", "for loop", "while", "repeat", "iteration"), brief(7, "Loops repeat a block of code. For loops run a fixed number of times; while loops repeat while a condition is true. Beware of infinite loops!")),
        (lambda: has("function", "functions", "methods", "def", "return"), brief(8, "A function is a reusable block of code. It takes parameters and can return a result. Python uses def; C++/Java declare a return type.")),
        (lambda: has("array", "arrays", "list", "lists", "vector", "collection", "index"), brief(9, "Collections store multiple values. Python uses lists, C++ arrays/vectors, Java arrays/ArrayLists. Indexing always starts at 0.")),
        (lambda: has("problem solving", "solve problem", "pseudocode", "plan"), brief(10, "Problem solving is a process: understand the problem, plan the steps (pseudocode), write the code, then test with simple examples.")),
        (lambda: has("programming", "what is code", "what is a program"), brief(1, "Programming is writing instructions that a computer can follow. Source code is human-readable, then translated or interpreted for the machine.")),
        (lambda: has("who are you", "your name", "eren", "story", "about you"), "I am E.R.E.N — Educational Response Engine for Novices. My story started at 2 AM in a dorm room: a frustrated first-year CS student kept failing a quiz about loops, so they built me to explain concepts the way a patient friend would. Every question a classmate asked that I could not answer became a new rule, and here I am. Ask me anything!"),
        (lambda: has("hi", "hello", "hey", "good morning", "good afternoon", "good evening"), "Hello! I am E.R.E.N, your CodeFundamentals assistant. Ask me about variables, operators, logical operators, conditionals, loops, functions, arrays, the long quiz, quizzes, or the leaderboard."),
        (lambda: has("thanks", "thank you", "salamat"), "You are welcome! Happy coding."),
        (lambda: has("help", "what can you do"), "I can explain lessons and concepts, quiz and long quiz rules, leaderboard rules, debugging tips, and how the site works. Try asking: 'explain loops', 'how does the long quiz work?', or 'how does the quiz work?'"),
    ]
    for condition, reply in rules:
        if condition():
            return reply
    return "I am not sure about that one yet. Try asking about variables, operators, logical operators, conditionals, loops, functions, arrays, quizzes, the long quiz, or the leaderboard."


@app.route("/assistant", methods=["POST"])
@login_required
def assistant():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()
    if not message:
        return jsonify({"ok": False, "error": "Please type a message."}), 400
    return jsonify({"ok": True, "reply": assistant_reply(message)})


@app.route("/lesson/<int:lesson_id>")
@login_required
def lesson(lesson_id):
    lesson = next((l for l in LESSONS if l["id"] == lesson_id), None)
    if lesson is None:
        flash("Lesson not found.", "danger")
        return redirect(url_for("dashboard"))
    if lesson.get("coming_soon"):
        flash("SQL Injection is coming soon — check back later!", "info")
        return redirect(url_for("dashboard"))
    section_lessons = [
        l
        for l in LESSONS
        if l.get("section", "Fundamentals") == lesson.get("section", "Fundamentals")
        and not l.get("coming_soon")
    ]
    idx = next(i for i, l in enumerate(section_lessons) if l["id"] == lesson_id)
    completed_ids = get_completed_ids(current_user)
    if idx > 0 and section_lessons[idx - 1]["id"] not in completed_ids:
        flash(
            f'Complete Lesson {idx} ({section_lessons[idx - 1]["title"]}) first to unlock this lesson.',
            "danger",
        )
        return redirect(url_for("lesson", lesson_id=section_lessons[idx - 1]["id"]))
    completed = lesson_id in completed_ids
    quiz_score = get_quiz_scores(current_user).get(lesson_id)
    has_lab = lesson_id in LAB_LESSON_IDS
    labs_leaderboard = get_lesson_labs_leaderboard(lesson_id) if has_lab else []
    lab_completed = is_lab_completed(current_user, lesson_id) if has_lab else False
    lab_route = LAB_ROUTES.get(lesson_id)
    prev_lesson_id = section_lessons[idx - 1]["id"] if idx > 0 else None
    next_lesson_id = section_lessons[idx + 1]["id"] if idx < len(section_lessons) - 1 else None
    return render_template(
        "lesson.html",
        lesson=lesson,
        lesson_num=idx + 1,
        section_total=len(section_lessons),
        completed=completed,
        quiz_score=quiz_score,
        lesson_leaderboard=get_lesson_leaderboard(lesson_id),
        has_lab=has_lab,
        labs_leaderboard=labs_leaderboard,
        lab_completed=lab_completed,
        lab_route=lab_route,
        total_lessons=len(AVAILABLE_LESSONS),
        prev_lesson_id=prev_lesson_id,
        next_lesson_id=next_lesson_id,
        section_minutes=SECTION_LESSON_MINUTES,
        section_has_quiz=lesson.get("section", "Fundamentals") in LONG_QUIZZES,
        section_lessons=section_lessons,
        completed_ids=completed_ids,
    )


@app.route("/lesson/<int:lesson_id>/leaderboard", methods=["GET"])
@login_required
def lesson_leaderboard(lesson_id):
    if not any(l["id"] == lesson_id for l in LESSONS):
        return jsonify({"ok": False, "error": "Lesson not found."}), 404
    return jsonify({"ok": True, "leaderboard": get_lesson_leaderboard(lesson_id)})


@app.route("/lesson/<int:lesson_id>/quiz", methods=["POST"])
@login_required
def submit_quiz(lesson_id):
    lesson = next((l for l in LESSONS if l["id"] == lesson_id), None)
    if lesson is None:
        return jsonify({"ok": False, "error": "Lesson not found."}), 404
    data = request.get_json(silent=True) or {}
    try:
        score = int(data.get("score"))
        total = int(data.get("total"))
    except (TypeError, ValueError):
        return jsonify({"ok": False, "error": "Invalid score."}), 400
    expected_total = len(lesson["quiz"])
    if total != expected_total or not (0 <= score <= total):
        return jsonify({"ok": False, "error": "Invalid score."}), 400

    row = QuizScore.query.filter_by(
        user_id=current_user.id, lesson_id=lesson_id
    ).first()
    if row:
        return jsonify(
            {"ok": False, "error": "You already took this quiz (1 attempt only)."}
        ), 400
    row = QuizScore(
        user_id=current_user.id,
        lesson_id=lesson_id,
        best_score=score,
        total_questions=total,
        attempts=1,
    )
    db.session.add(row)
    db.session.commit()
    return jsonify(
        {"ok": True, "best_score": row.best_score, "attempts": row.attempts}
    )


@app.route("/lesson/<int:lesson_id>/complete", methods=["POST"])
@login_required
def complete_lesson(lesson_id):
    if not any(l["id"] == lesson_id for l in LESSONS):
        flash("Lesson not found.", "danger")
        return redirect(url_for("dashboard"))
    exists = LessonProgress.query.filter_by(
        user_id=current_user.id, lesson_id=lesson_id
    ).first()
    if not exists:
        db.session.add(LessonProgress(user_id=current_user.id, lesson_id=lesson_id))
        db.session.commit()
        flash("Lesson marked as complete.", "success")
    else:
        flash("You already completed this lesson.", "info")
    return redirect(url_for("lesson", lesson_id=lesson_id))


@app.route("/sql-lab")
@login_required
def sql_lab():
    return render_template(
        "sql_lab.html",
        lab_completed=is_lab_completed(current_user, 19),
        lesson_id=19,
    )


@app.route("/sql-lab/complete", methods=["POST"])
@login_required
def sql_lab_complete():
    mark_lab_completed(current_user, 19)
    return jsonify({"ok": True})


@app.route("/sql-lab/reset", methods=["POST"])
@login_required
def sql_lab_reset():
    unmark_lab_completed(current_user, 19)
    return jsonify({"ok": True})


@app.route("/sql-lab-2")
@login_required
def sql_lab_2():
    return render_template(
        "sql_lab_2.html",
        lab_completed=is_lab_completed(current_user, 20),
        lesson_id=20,
    )


@app.route("/sql-lab-2/complete", methods=["POST"])
@login_required
def sql_lab_2_complete():
    mark_lab_completed(current_user, 20)
    return jsonify({"ok": True})


@app.route("/sql-lab-2/reset", methods=["POST"])
@login_required
def sql_lab_2_reset():
    unmark_lab_completed(current_user, 20)
    return jsonify({"ok": True})


@app.route("/section-quiz/<section>")
@login_required
def section_quiz(section):
    questions = LONG_QUIZZES.get(section)
    if not questions:
        flash("Long quiz not found.", "danger")
        return redirect(url_for("dashboard"))
    score = SectionQuizScore.query.filter_by(
        user_id=current_user.id, section=section
    ).first()
    last_answers = None
    if score and score.last_answers:
        try:
            last_answers = json.loads(score.last_answers)
        except (ValueError, TypeError):
            last_answers = None
    return render_template(
        "section_quiz.html",
        section=section,
        questions=questions,
        score=score,
        last_answers=last_answers,
    )


@app.route("/section-quiz/<section>/submit", methods=["POST"])
@login_required
def submit_section_quiz(section):
    questions = LONG_QUIZZES.get(section)
    if not questions:
        return jsonify({"ok": False, "error": "Long quiz not found."}), 404
    data = request.get_json(silent=True) or {}
    answers = data.get("answers")
    if not isinstance(answers, list) or len(answers) != len(questions):
        return jsonify({"ok": False, "error": "Invalid answers."}), 400
    score = 0
    for chosen, q in zip(answers, questions):
        if isinstance(chosen, int) and chosen == q["correct"]:
            score += 1
    row = SectionQuizScore.query.filter_by(
        user_id=current_user.id, section=section
    ).first()
    if row and row.attempts >= 2:
        return jsonify(
            {"ok": False, "error": "You already used your 2 attempts for this long quiz."}
        ), 400
    if row:
        row.best_score = max(row.best_score, score)
        row.attempts += 1
        row.last_answers = json.dumps(answers)
        db.session.commit()
    else:
        row = SectionQuizScore(
            user_id=current_user.id,
            section=section,
            best_score=score,
            total_questions=len(questions),
            attempts=1,
            last_answers=json.dumps(answers),
        )
        db.session.add(row)
        db.session.commit()
    return jsonify(
        {
            "ok": True,
            "best_score": row.best_score,
            "total_questions": row.total_questions,
            "attempts": row.attempts,
        }
    )


RUN_CONFIGS = {
    "python": {
        "source": "main.py",
    },
    "cpp": {
        "source": "main.cpp",
    },
    "java": {
        "source": "Main.java",
    },
}

COMPILER_FALLBACKS = {
    "g++": [r"C:\Users\chris\mingw64\bin\g++.exe"],
    "clang++": [r"C:\Program Files\LLVM\bin\clang++.exe"],
    "javac": [r"C:\Users\chris\jdk21\jdk-21.0.12+8\bin\javac.exe"],
    "java": [r"C:\Users\chris\jdk21\jdk-21.0.12+8\bin\java.exe"],
}

MINGW_BIN = r"C:\Users\chris\mingw64\bin"

# C++ online fallback: Compiler Explorer (free, keyless). Optional Judge0 backup
# via CODE_API_KEY env var: https://rapidapi.com/judge0-official/api/judge0-ce
CE_URL = "https://godbolt.org/api/compiler/g122/compile"
JUDGE0_URL = "https://judge0-ce.p.rapidapi.com/submissions?base64_encoded=false&wait=true"


def find_tool(name):
    found = shutil.which(name)
    if found:
        return found
    for path in COMPILER_FALLBACKS.get(name, []):
        if os.path.isfile(path):
            return path
    return None


def run_locally(cmd, workdir, timeout, extra_env=None, stdin=""):
    env = dict(os.environ)
    if extra_env:
        env["PATH"] = extra_env + os.pathsep + env.get("PATH", "")
    flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
    return subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=timeout,
        cwd=workdir,
        creationflags=flags,
        env=env,
        input=stdin,
    )


def judge0_submit(code, api_key, stdin=""):
    payload = json.dumps(
        {"source_code": code, "language_id": 54, "stdin": stdin}
    ).encode()
    req = urllib.request.Request(
        JUDGE0_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            result = json.loads(resp.read().decode())
    except (urllib.error.URLError, OSError):
        return None
    status = (result.get("status") or {}).get("description", "Unknown")
    output = result.get("stdout") or ""
    stderr = result.get("stderr") or ""
    compile_out = result.get("compile_output") or ""
    parts = [p for p in (compile_out, output, stderr) if p.strip()]
    text = "\n".join(parts)
    if not text.strip():
        text = "No output."
    if status == "Accepted":
        return jsonify({"ok": True, "output": text, "exit_code": result.get("exit_code", 0)})
    return jsonify(
        {"ok": True, "output": f"[{status}]\n{text}", "exit_code": result.get("exit_code", 1)}
    )


def run_cpp_ce(code, stdin=""):
    payload = json.dumps(
        {
            "source": code,
            "options": {
                "userArguments": "",
                "filters": {"execute": True},
                "executeParameters": {"args": [], "stdin": stdin},
            },
        }
    ).encode()
    req = urllib.request.Request(
        CE_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "CodeFundamentals/1.0",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode())
    except (urllib.error.URLError, OSError):
        return jsonify(
            {
                "ok": False,
                "error": "Could not reach the online C++ service (Compiler Explorer).",
            }
        )
    if data.get("code") != 0 or data.get("timedOut"):
        err = "\n".join(item.get("text", "") for item in data.get("stderr", []))
        err = re.sub(r"\x1b\[[0-9;]*m", "", err)
        return jsonify(
            {"ok": False, "compile_error": err or "Compilation failed."}
        )
    exec_result = data.get("execResult") or {}
    out_lines = [item.get("text", "") for item in exec_result.get("stdout", [])]
    err_lines = [item.get("text", "") for item in exec_result.get("stderr", [])]
    text = "\n".join([p for p in out_lines + err_lines if p.strip()])
    if exec_result.get("timedOut"):
        text = "Error: execution timed out.\n" + text
    if not text.strip():
        text = "No output."
    return jsonify(
        {"ok": True, "output": text, "exit_code": exec_result.get("code") or 0}
    )


def run_cpp_online(code, stdin=""):
    api_key = os.environ.get("CODE_API_KEY", "")
    if api_key:
        response = judge0_submit(code, api_key, stdin)
        if response is not None:
            return response
    return run_cpp_ce(code, stdin)


def compile_and_run_local(workdir, compile_cmd, stdin=""):
    try:
        compiled = run_locally(compile_cmd, workdir, 30)
    except subprocess.TimeoutExpired:
        return None
    if compiled.returncode != 0:
        return compiled.stderr
    try:
        result = run_locally(
            ["main.exe"], workdir, 10, extra_env=MINGW_BIN, stdin=stdin
        )
    except subprocess.TimeoutExpired:
        return jsonify(
            {
                "ok": True,
                "output": "Error: execution timed out (limit of 10 seconds).",
                "exit_code": -1,
            }
        )
    except (OSError, FileNotFoundError):
        return "BLOCKED"
    output = result.stdout
    if result.stderr.strip():
        output += ("\n" if output.strip() else "") + result.stderr
    return jsonify(
        {"ok": True, "output": output, "exit_code": result.returncode}
    )


def run_cpp(code, stdin=""):
    workdir = tempfile.mkdtemp(prefix="cf_run_")
    try:
        with open(os.path.join(workdir, "main.cpp"), "w", encoding="utf-8") as f:
            f.write(code)

        compile_errors = []
        toolchain_broken = False

        gpp = find_tool("g++")
        if gpp:
            outcome = compile_and_run_local(workdir, [gpp, "main.cpp", "-o", "main.exe"], stdin)
            if isinstance(outcome, dict):
                return outcome
            if outcome == "BLOCKED":
                toolchain_broken = True
            elif outcome is not None:
                if "cannot execute" in outcome or "blocked" in outcome.lower():
                    toolchain_broken = True
                compile_errors.append(outcome)

        clang = find_tool("clang++")
        if clang:
            outcome = compile_and_run_local(
                workdir,
                [
                    clang,
                    "--target=x86_64-w64-windows-gnu",
                    "--sysroot=" + os.path.dirname(MINGW_BIN),
                    "-std=c++17",
                    "main.cpp",
                    "-o",
                    "main.exe",
                ],
                stdin,
            )
            if isinstance(outcome, dict):
                return outcome
            if outcome == "BLOCKED":
                toolchain_broken = True
            elif outcome is not None:
                compile_errors.append(outcome)

        online = run_cpp_online(code, stdin)
        if online is not None:
            return online
        if toolchain_broken:
            return jsonify(
                {
                    "ok": False,
                    "error": (
                        "Local C++ execution is blocked by Windows Smart App Control "
                        "and the online service could not be reached."
                    ),
                }
            ), 501
        message = compile_errors[-1][:4000] if compile_errors else "Compilation failed."
        return jsonify({"ok": False, "compile_error": message})
    finally:
        shutil.rmtree(workdir, ignore_errors=True)


RUN_SESSIONS = {}
MAX_RUN_SECONDS = 120


def _start_local_process(lang, workdir):
    env = dict(os.environ)
    flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
    if lang == "python":
        env["PYTHONUNBUFFERED"] = "1"
        cmd = [sys.executable, "main.py"]
    elif lang == "java":
        cmd = [find_tool("java") or "java", "Main"]
    else:
        env["PATH"] = MINGW_BIN + os.pathsep + env.get("PATH", "")
        cmd = ["main.exe"]
    return subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd=workdir,
        creationflags=flags,
        env=env,
    )


def _pump_pipe(pipe, tag, session):
    try:
        while True:
            ch = pipe.read(1)
            if ch == "":
                break
            session["queue"].put({"type": tag, "data": ch})
    finally:
        session["queue"].put({"type": "done"})


@app.route("/run/start", methods=["POST"])
@login_required
def run_start():
    data = request.get_json(silent=True) or {}
    lang = data.get("language")
    code = data.get("code", "")
    stdin = data.get("stdin", "") or ""
    if lang not in RUN_CONFIGS or not code.strip():
        return jsonify({"ok": False, "error": "Invalid request."}), 400

    workdir = tempfile.mkdtemp(prefix="cf_run_")

    if lang == "cpp":
        stripped = re.sub(r"/\*.*?\*/", "", code, flags=re.S)
        stripped = re.sub(r"//[^\n]*", "", stripped)
        if re.search(r"\bcin\b", stripped) and not stdin.strip():
            shutil.rmtree(workdir, ignore_errors=True)
            return jsonify({
                "ok": False,
                "error": "This C++ program reads input with cin. "
                         "Type each value and press Enter."
            }), 400
        result = run_cpp(code, stdin)
        payload = result.get_json()
        session = {
            "queue": queue.Queue(),
            "proc": None,
            "workdir": workdir,
            "lang": "cpp",
        }
        if payload.get("ok"):
            session["queue"].put({"type": "out", "data": payload.get("output", "")})
            session["queue"].put({"type": "exit", "data": payload.get("exit_code", 0)})
        else:
            msg = payload.get("compile_error") or payload.get("error") or "Compilation failed."
            session["queue"].put({"type": "error", "data": msg})
            session["queue"].put({"type": "exit", "data": -1})
        sid = uuid.uuid4().hex
        RUN_SESSIONS[sid] = session
        return jsonify({"ok": True, "session_id": sid})

    source = RUN_CONFIGS[lang]["source"]
    with open(os.path.join(workdir, source), "w", encoding="utf-8") as f:
        f.write(code)

    if lang == "java":
        javac = find_tool("javac")
        if not javac:
            shutil.rmtree(workdir, ignore_errors=True)
            return jsonify(
                {"ok": False, "error": "Java compiler (javac) is not installed."}
            ), 500
        compiled = run_locally([javac, "Main.java"], workdir, 20)
        if compiled.returncode != 0:
            shutil.rmtree(workdir, ignore_errors=True)
            return jsonify({"ok": False, "compile_error": compiled.stderr[:4000]})

    try:
        proc = _start_local_process(lang, workdir)
    except (OSError, FileNotFoundError):
        shutil.rmtree(workdir, ignore_errors=True)
        return jsonify({"ok": False, "error": "Could not start the program."}), 500

    session = {
        "queue": queue.Queue(),
        "proc": proc,
        "workdir": workdir,
        "lang": lang,
        "started": time.time(),
    }
    sid = uuid.uuid4().hex
    RUN_SESSIONS[sid] = session
    threading.Thread(
        target=_pump_pipe, args=(proc.stdout, "out", session), daemon=True
    ).start()
    threading.Thread(
        target=_pump_pipe, args=(proc.stderr, "err", session), daemon=True
    ).start()
    return jsonify({"ok": True, "session_id": sid})


@app.route("/run/poll/<session_id>", methods=["POST"])
@login_required
def run_poll(session_id):
    session = RUN_SESSIONS.get(session_id)
    if not session:
        return jsonify({"ok": False, "error": "Session not found."}), 404
    proc = session.get("proc")
    events = []
    exit_code = None

    started = session.get("started")
    if started and time.time() - started > MAX_RUN_SECONDS:
        if proc and proc.poll() is None:
            proc.kill()
        session["queue"].put(
            {
                "type": "error",
                "data": "Program was stopped (time limit of %d seconds)."
                % MAX_RUN_SECONDS,
            }
        )
        session["queue"].put({"type": "exit", "data": -1})

    done_count = session.get("done_count", 0)
    text_buf = ""
    while True:
        try:
            item = session["queue"].get_nowait()
        except queue.Empty:
            break
        if item["type"] == "exit":
            exit_code = item["data"]
        elif item["type"] == "done":
            done_count += 1
        elif item["type"] == "error":
            if text_buf:
                events.append({"type": "out", "data": text_buf.rstrip("\r\n")})
                text_buf = ""
            events.append(item)
        else:
            text_buf += item["data"]
    if text_buf:
        events.append({"type": "out", "data": text_buf.rstrip("\r\n")})
    session["done_count"] = done_count

    if exit_code is None and proc is not None:
        if done_count >= 2 and proc.poll() is not None:
            exit_code = proc.returncode
        elif proc.poll() is not None:
            if session.get("drain_until") is None:
                session["drain_until"] = time.time() + 1.5
            elif time.time() > session["drain_until"]:
                exit_code = proc.returncode
        else:
            session.pop("drain_until", None)

    if exit_code is not None:
        if proc:
            try:
                proc.kill()
            except Exception:
                pass
        shutil.rmtree(session.get("workdir", ""), ignore_errors=True)
        RUN_SESSIONS.pop(session_id, None)
        return jsonify(
            {"ok": True, "events": events, "finished": True, "exit_code": exit_code}
        )
    return jsonify({"ok": True, "events": events, "finished": False})


@app.route("/run/input/<session_id>", methods=["POST"])
@login_required
def run_input(session_id):
    session = RUN_SESSIONS.get(session_id)
    if not session or not session.get("proc"):
        return jsonify({"ok": False, "error": "Session is not running."}), 404
    data = request.get_json(silent=True) or {}
    text = data.get("input", "")
    try:
        session["proc"].stdin.write(text + "\n")
        session["proc"].stdin.flush()
    except (BrokenPipeError, OSError, ValueError):
        return jsonify(
            {"ok": False, "error": "The program is no longer accepting input."}
        ), 400
    return jsonify({"ok": True})


@app.route("/run/stop/<session_id>", methods=["POST"])
@login_required
def run_stop(session_id):
    session = RUN_SESSIONS.get(session_id)
    if not session:
        return jsonify({"ok": True})
    proc = session.get("proc")
    if proc and proc.poll() is None:
        proc.kill()
    return jsonify({"ok": True})


def format_sql_table(cols, rows):
    if not rows:
        return f"-- {len(cols)} column(s), 0 rows returned"
    widths = [len(c) for c in cols]
    for row in rows:
        for i, value in enumerate(row):
            widths[i] = max(widths[i], len(str(value)))
    sep = "+" + "+".join("-" * (w + 2) for w in widths) + "+"

    def line(row):
        cells = []
        for i, value in enumerate(row):
            cells.append(" " + str(value).ljust(widths[i]) + " ")
        return "|" + "|".join(cells) + "|"

    lines = [sep, line(cols), sep]
    for row in rows:
        lines.append(line(row))
    lines.append(sep)
    label = f"({len(rows)} row returned)" if len(rows) == 1 else f"({len(rows)} rows returned)"
    lines.append(label)
    return "\n".join(lines)


@app.route("/run/sql", methods=["POST"])
@login_required
def run_sql():
    data = request.get_json(silent=True) or {}
    code = (data.get("code") or "").strip()
    if not code:
        return jsonify({"ok": False, "error": "No SQL provided."}), 400
    if len(code) > 50000:
        return jsonify({"ok": False, "error": "SQL is too long (50,000 characters max)."}), 400
    conn = sqlite3.connect(":memory:")
    output = []
    try:
        for statement in code.split(";"):
            statement = statement.strip()
            if not statement:
                continue
            cur = conn.execute(statement)
            if cur.description:
                output.append(format_sql_table([d[0] for d in cur.description], cur.fetchall()))
            elif cur.rowcount != -1:
                output.append(f"-- {cur.rowcount} row(s) affected")
            else:
                output.append("-- Statement executed")
        return jsonify({"ok": True, "output": output})
    except sqlite3.Error as e:
        return jsonify({"ok": False, "error": str(e)}), 400
    finally:
        conn.close()


PLAYGROUND_SCHEMA = [
    "CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, role TEXT)",
    "INSERT INTO users (id, username, password, role) VALUES "
    "(1, 'admin', 'admin123', 'admin'), "
    "(2, 'alice', 'wonderland', 'staff'), "
    "(3, 'bob', 'builder', 'staff'), "
    "(4, 'carol', 'carol123', 'guest')",
    "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price INTEGER)",
    "INSERT INTO products (id, name, price) VALUES "
    "(1, 'Laptop', 45000), "
    "(2, 'Mouse', 500), "
    "(3, 'Keyboard', 1200), "
    "(4, 'Monitor', 8000)",
]


@app.route("/sql-playground")
@login_required
def sql_playground():
    return render_template("sql_playground.html")


@app.route("/run/playground", methods=["POST"])
@login_required
def run_playground():
    data = request.get_json(silent=True) or {}
    code = (data.get("code") or "").strip()
    if not code:
        return jsonify({"ok": False, "error": "No SQL provided."}), 400
    if len(code) > 50000:
        return jsonify({"ok": False, "error": "SQL is too long (50,000 characters max)."}), 400
    conn = sqlite3.connect(":memory:")
    output = []
    try:
        for statement in PLAYGROUND_SCHEMA:
            conn.execute(statement)
        for statement in code.split(";"):
            statement = statement.strip()
            if not statement:
                continue
            cur = conn.execute(statement)
            if cur.description:
                output.append(format_sql_table([d[0] for d in cur.description], cur.fetchall()))
            elif cur.rowcount != -1:
                output.append(f"-- {cur.rowcount} row(s) affected")
            else:
                output.append("-- Statement executed")
        return jsonify({"ok": True, "output": output})
    except sqlite3.Error as e:
        return jsonify({"ok": False, "error": str(e)}), 400
    finally:
        conn.close()


with app.app_context():
    db.create_all()
    os.makedirs(AVATAR_DIR, exist_ok=True)
    is_sqlite = db.engine.dialect.name == "sqlite"
    if is_sqlite:
        for _ in range(10):
            try:
                with db.engine.begin() as conn:
                    conn.execute(sa_text("ALTER TABLE user ADD COLUMN avatar VARCHAR(200)"))
                break
            except Exception:
                time.sleep(0.5)
        for _ in range(10):
            try:
                with db.engine.begin() as conn:
                    conn.execute(sa_text("ALTER TABLE user ADD COLUMN lab_completed INTEGER DEFAULT 0"))
                break
            except Exception:
                time.sleep(0.5)
        for _ in range(10):
            try:
                with db.engine.begin() as conn:
                    conn.execute(sa_text("ALTER TABLE section_quiz_score ADD COLUMN last_answers TEXT"))
                break
            except Exception:
                time.sleep(0.5)
    try:
        has_lesson_10 = db.session.execute(
            sa_text("SELECT COUNT(*) FROM quiz_score WHERE lesson_id = 10")
        ).scalar()
        if not has_lesson_10:
            db.session.execute(
                sa_text("UPDATE quiz_score SET lesson_id = lesson_id + 1 WHERE lesson_id >= 5")
            )
            db.session.execute(
                sa_text("UPDATE lesson_progress SET lesson_id = lesson_id + 1 WHERE lesson_id >= 5")
            )
            db.session.commit()
    except Exception:
        pass
    try:
        legacy_users = db.session.execute(
            sa_text(
                "SELECT id FROM user WHERE lab_completed > 0 "
                "AND NOT EXISTS (SELECT 1 FROM lab_progress lp WHERE lp.user_id = user.id)"
            )
        ).fetchall()
        for (uid,) in legacy_users:
            db.session.add(LabProgress(user_id=uid, lesson_id=19))
        if legacy_users:
            db.session.commit()
    except Exception:
        pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, threaded=True, port=int(os.environ.get("PORT", 5001)))