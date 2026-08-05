CHANGELOG = [
    {
        "version": "1.46",
        "date": "2026-08-05",
        "type": "feature",
        "title": "Update Popup Notifications",
        "changes": [
            "Added a popup that announces new updates whenever a new version is released",
            "The popup shows only once per session - refreshing the page will not show it again",
            "The popup reappears in a new session only when a newer version is available",
            "Added a link to the full Updates page from the popup",
        ],
    },
    {
        "version": "1.45",
        "date": "2026-08-05",
        "type": "feature",
        "title": "Database Fixed Popup & Version Badge",
        "changes": [
            "Added \"Database Fixed!\" popup modal on the landing page announcing the PostgreSQL migration",
            "Added app version badge (v1.45) to the footer",
            "Turned off maintenance mode and restored the live site",
        ],
    },
    {
        "version": "1.44",
        "date": "2026-08-05",
        "type": "fix",
        "title": "Maintenance Popup Fix",
        "changes": [
            "Fixed the maintenance page popup modal not showing by adding the Bootstrap JS bundle",
        ],
    },
    {
        "version": "1.43",
        "date": "2026-08-05",
        "type": "feature",
        "title": "Under Maintenance Mode",
        "changes": [
            "Added an Under Maintenance page with an Important Notice popup modal",
            "Disabled all buttons and links while maintenance is active",
            "Maintenance mode is on by default and can be toggled via the MAINTENANCE_MODE environment variable",
        ],
    },
    {
        "version": "1.42",
        "date": "2026-08-05",
        "type": "fix",
        "title": "PostgreSQL Data Persistence",
        "changes": [
            "Added a PostgreSQL database service to render.yaml so user accounts and progress are no longer lost when the Render service sleeps",
        ],
    },
    {
        "version": "1.41",
        "date": "2026-08-05",
        "type": "notice",
        "title": "Account Information Notice",
        "changes": [
            "Added and later removed an account information loss notice while the database issue was being resolved",
        ],
    },
    {
        "version": "1.40",
        "date": "2026-08-04",
        "type": "fix",
        "title": "Database Auto-Recovery",
        "changes": [
            "Automatically recreate corrupted database tables on startup",
            "Wrap admin account creation in try-except to handle corrupted databases",
            "Wrap table inspection in try-except for fresh databases",
        ],
    },
    {
        "version": "1.39",
        "date": "2026-08-04",
        "type": "feature",
        "title": "Public Feedback Page",
        "changes": [
            "Made the feedback page public and show user avatars",
            "Added a feedback page with category selection",
        ],
    },
    {
        "version": "1.38",
        "date": "2026-08-04",
        "type": "feature",
        "title": "Landing Page Update",
        "changes": [
            "Updated the landing page with new features and an Advanced Fundamentals section",
        ],
    },
    {
        "version": "1.37",
        "date": "2026-08-04",
        "type": "feature",
        "title": "Advanced Fundamentals Lessons",
        "changes": [
            "Added GitHub, Web Deployment, Render, and Netlify lessons",
            "Added admin online/offline tracking",
            "Added admin user progress management",
            "Added auto-migration for the last_seen column on startup",
        ],
    },
    {
        "version": "1.36",
        "date": "2026-08-04",
        "type": "feature",
        "title": "E.R.E.N AI Assistant Enhancements",
        "changes": [
            "Added full-page /aiassist view with history and new-chat buttons",
            "Added conversation history persisted in localStorage",
            "Added general knowledge, runnable code blocks, and textarea input",
            "Replies in English and Tagalog only",
        ],
    },
    {
        "version": "1.35",
        "date": "2026-08-04",
        "type": "feature",
        "title": "Google Gemini Integration",
        "changes": [
            "Integrated the Google Gemini API into the E.R.E.N assistant with a rule-engine fallback",
            "Load GEMINI_API_KEY from .env and read it at request time",
            "Default to gemini-3.5-flash-lite model",
        ],
    },
    {
        "version": "1.34",
        "date": "2026-08-04",
        "type": "feature",
        "title": "Persistent Avatars",
        "changes": [
            "Store profile avatars in the database as base64 data URIs so they survive Render redeploys",
        ],
    },
    {
        "version": "1.33",
        "date": "2026-08-04",
        "type": "fix",
        "title": "Philippine Timezone",
        "changes": [
            "Show admin timestamps in Philippine local time (UTC+8) instead of UTC",
        ],
    },
    {
        "version": "1.32",
        "date": "2026-08-04",
        "type": "feature",
        "title": "Video Lessons & Estimates",
        "changes": [
            "Added video lesson tabs with per-language YouTube embeds",
            "Added footer credits marquee for video creators",
            "Compute lesson estimates including embedded video durations",
            "Added official Python/C++/Java history documentaries",
        ],
    },
    {
        "version": "1.31",
        "date": "2026-08-04",
        "type": "feature",
        "title": "Admin Dashboard",
        "changes": [
            "Added admin dashboard with activity logs, recent registrations, and user overview",
            "Added a dedicated admin account and route admins to the admin dashboard on login",
        ],
    },
    {
        "version": "1.30",
        "date": "2026-08-03",
        "type": "feature",
        "title": "Programming History Lesson",
        "changes": [
            "Added a Programming History lesson with badge and updated lesson counts",
            "Moved Programming History to lesson 2 position in Fundamentals",
        ],
    },
    {
        "version": "1.29",
        "date": "2026-08-03",
        "type": "feature",
        "title": "Synchronous Compiler",
        "changes": [
            "Made the lesson compiler fully synchronous - no polling",
            "Unified stdin input flow in the compiler UI",
            "Added Java online compiler via Compiler Explorer",
            "Added no-cache headers for HTML to prevent stale compiler JS",
        ],
    },
    {
        "version": "1.28",
        "date": "2026-08-03",
        "type": "fix",
        "title": "Compiler Session Fixes",
        "changes": [
            "Fixed C++ compiler to return results synchronously without a polling session",
            "Use a single gunicorn worker with threads for in-memory run sessions",
        ],
    },
    {
        "version": "1.27",
        "date": "2026-08-03",
        "type": "fix",
        "title": "Render PostgreSQL Fixes",
        "changes": [
            "Require SSL for Render Postgres connections",
            "Added pool pre-ping and connection recycling",
        ],
    },
    {
        "version": "1.26",
        "date": "2026-08-03",
        "type": "feature",
        "title": "Render Deployment",
        "changes": [
            "Deployed to Render with PostgreSQL support, gunicorn, dark mode, and SQL labs",
        ],
    },
    {
        "version": "1.0",
        "date": "2026-08-03",
        "type": "launch",
        "title": "Initial Launch",
        "changes": [
            "CodeFundamentals launched with 19 lessons, long quizzes, certificates, badges, and the SQL Injection Lab",
            "Lessons in Python, C++, Java, and SQL for first-year programming students",
        ],
    },
]
