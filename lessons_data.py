LESSONS = [
    {
        "section": "Fundamentals",
        "id": 1,
        "minutes": 40,
        "title": "Introduction to Programming",
        "icon": "bi-code-slash",
        "description": "Programming is the process of writing instructions that a computer can follow. Every program, no matter how complex, is built from simple instructions. In this lesson you will learn how programs are structured in Python, C++, Java, and C.",
        "videos": {
            "python": [
                {"id": "9QKe2RvjG-A", "channel": "Doji Creates", "title": "Python Programming for Beginners Explained (Complete Introduction Guide)"},
            ],
            "cpp": [
                {"id": "LApkQYRUru8", "channel": "Doji Creates", "title": "C++ Coding for Beginners Introduction to Programming (Tagalog Tutorial)"},
            ],
            "java": [
                {"id": "Pyx9oLYpbi4", "channel": "Doji Creates", "title": "Java Programming Introduction Explained (What You Need to Know Before You Start)"},
            ],
            "c": [
                {"id": "aMpsKnf6DrQ", "channel": "mycodeschool", "title": "Writing and executing your first program: C Programming Tutorial 03"},
            ],
        },
        "key_points": [
            "A program is a sequence of instructions executed by a computer.",
            "Source code is written in a human-readable language, then translated or interpreted.",
            "Python is interpreted, while C++, Java, and C are compiled.",
            "C, C++, and Java use braces {} to group code, Python uses indentation.",
            "Java programs need a main method, C and C++ need a main function.",
        ],
        "code": {
            "python": "print(\"Hello, world!\")\nprint(\"Welcome to programming.\")",
            "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    cout << \"Hello, world!\" << endl;\n    cout << \"Welcome to programming.\" << endl;\n    return 0;\n}",
            "java": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, world!\");\n        System.out.println(\"Welcome to programming.\");\n    }\n}",
            "c": "#include <stdio.h>\n\nint main() {\n    printf(\"Hello, world!\\n\");\n    printf(\"Welcome to programming.\\n\");\n    return 0;\n}",
        },
        "quiz": [
            {
                "question": "Which language is interpreted rather than compiled?",
                "options": ["Python", "C++", "Java", "All of the above"],
                "correct": 0,
            },
            {
                "question": "What do C++ and Java use to group blocks of code?",
                "options": ["Indentation", "Braces {}", "Semicolons", "Parentheses ()"],
                "correct": 1,
            },
            {
                "question": "What must every Java program include to run?",
                "options": ["A print statement", "A main method", "A header file", "A loop"],
                "correct": 1,
            },
        ],
    },
    {
        "section": "Fundamentals",
        "id": 29,
        "minutes": 35,
        "title": "Programming History",
        "icon": "bi-clock-history",
        "description": "Every programming language has a creator and a story. In this lesson you will learn how C, C++, Java, and Python were invented — who built them, when, and why each language was designed.",
        "videos": {
            "general": [
                {"id": "RU1u-js7db8", "channel": "CrashCourse", "title": "The First Programming Languages: Crash Course Computer Science #11", "duration": 12},
            ],
            "python": [
                {"id": "GfH4QL4VqJ0", "channel": "CultRepo", "title": "The Story of Python and how it took over the world | Python: The Documentary", "duration": 84},
            ],
            "cpp": [
                {"id": "lI7tMxzSJ7w", "channel": "CultRepo", "title": "The Story of C++: The World's Most Consequential Programming Language", "duration": 72},
            ],
            "java": [
                {"id": "ZqGSg4b_cZA", "channel": "CultRepo", "title": "The Java Story | The Official Documentary", "duration": 74},
            ],
            "c": [
                {"id": "6VT8hDr2GhU", "channel": "LearningLad", "title": "Introduction to C Programming Language | What it is | History, Features | Beginners Video Tutorial", "duration": 13},
            ],
        },
        "key_points": [
            "C was created by Dennis Ritchie at Bell Labs in 1972 to build the UNIX operating system.",
            "C is the foundation of C++, Java, and Python; learning C helps you understand how the other languages work.",
            "C++ was created by Bjarne Stroustrup at Bell Labs in 1983, starting out as \"C with Classes\".",
            "C++ added object-oriented features on top of C while keeping C's speed and low-level control.",
            "Java was created by James Gosling at Sun Microsystems and released in 1995; its original name was Oak.",
            "Java runs on the Java Virtual Machine (JVM), which is why its motto is \"write once, run anywhere\".",
            "Python was created by Guido van Rossum and released in 1991; the name comes from the Monty Python comedy group, not the snake.",
            "Python was designed for readability, which is why it uses indentation instead of braces.",
        ],
        "code": {
            "python": "# A quick history lesson in code\n\nmilestones = [\n    (1983, \"C++\", \"Bjarne Stroustrup\"),\n    (1991, \"Python\", \"Guido van Rossum\"),\n    (1995, \"Java\", \"James Gosling\"),\n]\n\nfor year, name, creator in milestones:\n    print(str(year) + \": \" + name + \" was created by \" + creator)",
            "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    cout << \"1983: C++ was created by Bjarne Stroustrup\" << endl;\n    cout << \"1991: Python was created by Guido van Rossum\" << endl;\n    cout << \"1995: Java was created by James Gosling\" << endl;\n    return 0;\n}",
            "java": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"1983: C++ was created by Bjarne Stroustrup\");\n        System.out.println(\"1991: Python was created by Guido van Rossum\");\n        System.out.println(\"1995: Java was created by James Gosling\");\n    }\n}",
            "c": "#include <stdio.h>\n\nint main() {\n    printf(\"1972: C was created by Dennis Ritchie\\n\");\n    printf(\"1983: C++ was created by Bjarne Stroustrup\\n\");\n    printf(\"1991: Python was created by Guido van Rossum\\n\");\n    printf(\"1995: Java was created by James Gosling\\n\");\n    return 0;\n}",
        },
        "quiz": [
            {
                "question": "Who created the C++ programming language?",
                "options": ["James Gosling", "Bjarne Stroustrup", "Guido van Rossum", "Dennis Ritchie"],
                "correct": 1,
            },
            {
                "question": "What was Java originally called before it was renamed?",
                "options": ["Oak", "Pine", "Coffee", "Bean"],
                "correct": 0,
            },
            {
                "question": "Where does the name Python come from?",
                "options": ["The snake", "The Monty Python comedy group", "The inventor's surname", "A Greek myth"],
                "correct": 1,
            },
        ],
    },
    {
        "section": "Fundamentals",
        "id": 2,
        "minutes": 40,
        "title": "Variables and Data Types",
        "icon": "bi-box-seam",
        "description": "Variables store values in memory. Every variable has a name and a value. Python infers the type automatically, while C, C++, and Java require you to declare the type before the variable name.",
        "videos": {
            "python": [
                {"id": "2SG133xkpMQ", "channel": "Doji Creates", "title": "Python Variables Explained (How Data Storage Works in Code)"},
                {"id": "yp2xUIUjdIY", "channel": "Doji Creates", "title": "Python Data Types Explained (How Different Kinds of Data Work)"},
            ],
            "cpp": [
                {"id": "E4yj6QX-TW8", "channel": "Doji Creates", "title": "C++ Variables Explained (How Data Storage Works in Programming)"},
                {"id": "6yyOS7zeJJY", "channel": "Doji Creates", "title": "C++ Data Types Explained (How Different Data Categories Work)"},
            ],
            "java": [
                {"id": "cD-6C39RPKs", "channel": "Doji Creates", "title": "Java Variables Explained (How They Work for Beginners)"},
                {"id": "5Lxq9JJZRAg", "channel": "Doji Creates", "title": "Java Primitive Data Types Explained (Everything You Need to Know)"},
            ],
            "c": [
                {"id": "OSyjOvFbAGI", "channel": "mycodeschool", "title": "Data types, Constants and Variables - C Programming Tutorial 05"},
            ],
        },
        "key_points": [
            "Python is dynamically typed: the type is decided by the value.",
            "C, C++, and Java are statically typed: you must declare the type.",
            "Common types: int, double/float, char, boolean, and String.",
            "In Java a String is a class; in C++ it is std::string.",
            "C has no String type — text is stored in char arrays and printed with printf().",
            "In C, C++, and Java, every statement ends with a semicolon.",
        ],
        "code": {
            "python": "name = \"Alice\"\nage = 19\nheight = 1.68\nis_student = True\n\nprint(name, age, height, is_student)",
            "cpp": "#include <iostream>\n#include <string>\nusing namespace std;\n\nint main() {\n    string name = \"Alice\";\n    int age = 19;\n    double height = 1.68;\n    bool is_student = true;\n\n    cout << name << \" \" << age << \" \" << height << \" \" << is_student << endl;\n    return 0;\n}",
            "java": "public class Main {\n    public static void main(String[] args) {\n        String name = \"Alice\";\n        int age = 19;\n        double height = 1.68;\n        boolean isStudent = true;\n\n        System.out.println(name + \" \" + age + \" \" + height + \" \" + isStudent);\n    }\n}",
            "c": "#include <stdio.h>\n\nint main() {\n    char name[20] = \"Alice\";\n    int age = 19;\n    double height = 1.68;\n    int is_student = 1;  // 1 = true\n\n    printf(\"%s %d %.2f %d\\n\", name, age, height, is_student);\n    return 0;\n}",
        },
        "quiz": [
            {
                "question": "Which language decides the type of a variable automatically?",
                "options": ["C++", "Java", "Python", "All of the above"],
                "correct": 2,
            },
            {
                "question": "In C++ and Java, every statement must end with what?",
                "options": ["A period", "A semicolon ;", "A comma", "Nothing"],
                "correct": 1,
            },
            {
                "question": "Which is a valid Java declaration for a whole number?",
                "options": ["int age = 19;", "number age = 19;", "var age = 19;", "age = 19;"],
                "correct": 0,
            },
        ],
    },
    {
        "section": "Fundamentals",
        "id": 3,
        "minutes": 45,
        "title": "Input and Output",
        "icon": "bi-input-cursor-text",
        "description": "Programs communicate with the user through input and output. You read data from the keyboard and display results on the screen. Each language has its own functions for this.",
        "videos": {
            "python": [
                {"id": "7iZOEoGWnuU", "channel": "Doji Creates", "title": "Python User Input Explained (How Input Handling Works Step by Step)"},
            ],
            "cpp": [
                {"id": "vkALQRM5NNU", "channel": "Doji Creates", "title": "C++ User Input Explained (How Input Handling Works Step by Step)"},
            ],
            "java": [
                {"id": "sk_TzAjZ3zs", "channel": "Doji Creates", "title": "Java Scanner Input Explained (How to Get User Input)"},
            ],
            "c": [
                {"id": "xOIVXR35aI4", "channel": "mycodeschool", "title": "Input and Output: Printf and Scanf - C Programming Tutorial 06"},
            ],
        },
        "key_points": [
            "Python: input() returns a string, print() displays output.",
            "C++: cin reads, cout writes.",
            "Java: Scanner reads input, System.out.println prints.",
            "C: scanf() reads input, printf() writes output.",
            "Numeric input must be converted (int(), stoi, nextInt) or read with the right format specifier in C (scanf(\"%d\")).",
            "Always handle user input carefully; it comes in as text.",
        ],
        "code": {
            "python": "name = input(\"Enter your name: \")\nage = int(input(\"Enter your age: \"))\n\nprint(\"Hello, \" + name)\nprint(\"Next year you will be\", age + 1)",
            "cpp": "#include <iostream>\n#include <string>\nusing namespace std;\n\nint main() {\n    string name;\n    int age;\n\n    cout << \"Enter your name: \";\n    cin >> name;\n    cout << \"Enter your age: \";\n    cin >> age;\n\n    cout << \"Hello, \" << name << endl;\n    cout << \"Next year you will be \" << age + 1 << endl;\n    return 0;\n}",
            "java": "import java.util.Scanner;\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner scanner = new Scanner(System.in);\n\n        System.out.print(\"Enter your name: \");\n        String name = scanner.nextLine();\n        System.out.print(\"Enter your age: \");\n        int age = scanner.nextInt();\n\n        System.out.println(\"Hello, \" + name);\n        System.out.println(\"Next year you will be \" + (age + 1));\n        scanner.close();\n    }\n}",
            "c": "#include <stdio.h>\n\nint main() {\n    char name[50];\n    int age;\n\n    printf(\"Enter your name: \");\n    scanf(\"%s\", name);\n    printf(\"Enter your age: \");\n    scanf(\"%d\", &age);\n\n    printf(\"Hello, %s\\n\", name);\n    printf(\"Next year you will be %d\\n\", age + 1);\n    return 0;\n}",
        },
        "quiz": [
            {
                "question": "In Python, what does input() always return?",
                "options": ["An integer", "A string", "A float", "A boolean"],
                "correct": 1,
            },
            {
                "question": "Which C++ object reads input from the keyboard?",
                "options": ["cout", "cin", "Scanner", "printf"],
                "correct": 1,
            },
            {
                "question": "Which Java class is commonly used for keyboard input?",
                "options": ["Scanner", "InputStream", "Reader", "Console"],
                "correct": 0,
            },
        ],
    },
    {
        "section": "Fundamentals",
        "id": 4,
        "minutes": 45,
        "title": "Operators",
        "icon": "bi-plus-square",
        "description": "Operators perform calculations and comparisons. Arithmetic operators do math and relational operators compare values. Understanding these operators lets you write expressions that calculate results.",
        "videos": {
            "python": [
                {"id": "RYEDDygFNx8", "channel": "Doji Creates", "title": "Python Arithmetic Operators Explained (How Basic Math Operations Work)"},
                {"id": "x49Ez5QaqBQ", "channel": "Doji Creates", "title": "Python Comparison Operators Explained (How Values Are Compared Step by Step)"},
            ],
            "cpp": [
                {"id": "ib-Qfx7-iIQ", "channel": "Doji Creates", "title": "C++ Arithmetic Operators Explained (How Basic Math Operations Work)"},
                {"id": "e5_JYK1oYjA", "channel": "Doji Creates", "title": "C++ Comparison Operators Explained (How Value Comparison Works)"},
            ],
            "java": [
                {"id": "M0lnSma7qMw", "channel": "Doji Creates", "title": "Java Arithmetic Operators Explained (How Calculations Work)"},
                {"id": "yRwNhHubxc8", "channel": "Doji Creates", "title": "Java Relational Operators Explained (How Comparisons Work)"},
            ],
            "c": [
                {"id": "vvpDbhqPrww", "channel": "mycodeschool", "title": "Using Arithmetic Operators - C Programming Tutorial 07"},
            ],
        },
        "key_points": [
            "Arithmetic: + - * / % (modulo gives the remainder).",
            "Integer division differs: / in Python gives a float; int / int in C, C++, and Java gives an integer.",
            "Relational: == != < > <= >=. Comparison always produces true or false.",
            "The % operator (modulo) is common in all four languages.",
        ],
        "code": {
            "python": "a = 10\nb = 3\n\nprint(\"a + b =\", a + b)\nprint(\"a - b =\", a - b)\nprint(\"a * b =\", a * b)\nprint(\"a / b =\", a / b)\nprint(\"a % b =\", a % b)\nprint(\"a == b:\", a == b)\nprint(\"a > b:\", a > b)\nprint(\"b < a:\", b < a)",
            "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int a = 10;\n    int b = 3;\n\n    cout << \"a + b = \" << a + b << endl;\n    cout << \"a - b = \" << a - b << endl;\n    cout << \"a * b = \" << a * b << endl;\n    cout << \"a / b = \" << a / b << endl;  // integer division: 3\n    cout << \"a % b = \" << a % b << endl;\n    cout << \"a == b = \" << (a == b) << endl;\n    cout << \"a > b = \" << (a > b) << endl;\n    cout << \"b < a = \" << (b < a) << endl;\n    return 0;\n}",
            "java": "public class Main {\n    public static void main(String[] args) {\n        int a = 10;\n        int b = 3;\n\n        System.out.println(\"a + b = \" + (a + b));\n        System.out.println(\"a - b = \" + (a - b));\n        System.out.println(\"a * b = \" + (a * b));\n        System.out.println(\"a / b = \" + (a / b));  // integer division: 3\n        System.out.println(\"a % b = \" + (a % b));\n        System.out.println(\"a == b = \" + (a == b));\n        System.out.println(\"a > b = \" + (a > b));\n        System.out.println(\"b < a = \" + (b < a));\n    }\n}",
            "c": "#include <stdio.h>\n\nint main() {\n    int a = 10;\n    int b = 3;\n\n    printf(\"a + b = %d\\n\", a + b);\n    printf(\"a - b = %d\\n\", a - b);\n    printf(\"a * b = %d\\n\", a * b);\n    printf(\"a / b = %d\\n\", a / b);  // integer division: 3\n    printf(\"a %% b = %d\\n\", a % b);\n    printf(\"a == b = %d\\n\", a == b);\n    printf(\"a > b = %d\\n\", a > b);\n    printf(\"b < a = %d\\n\", b < a);\n    return 0;\n}",
        },
        "quiz": [
            {
                "question": "What does the % operator compute?",
                "options": ["The product", "The remainder", "The quotient", "The sum"],
                "correct": 1,
            },
            {
                "question": "In C++, int x = 10 / 3; stores what value in x?",
                "options": ["3.33", "4", "3", "0"],
                "correct": 2,
            },
            {
                "question": "Which operator checks if two values are equal?",
                "options": ["=", "==", "=>", "<>"],
                "correct": 1,
            },
        ],
    },
    {
        "section": "Fundamentals",
        "id": 5,
        "minutes": 50,
        "title": "Logical Operators",
        "icon": "bi-toggle-on",
        "description": "Logical operators combine true and false values to build bigger conditions. They let a program check several things at once. Python uses the words and, or, not; C, C++, and Java use &&, ||, and !.",
        "videos": {
            "python": [
                {"id": "srYNLwnEfeo", "channel": "Doji Creates", "title": "Python Logical Operators Explained (How AND OR NOT Logic Works)"},
            ],
            "cpp": [
                {"id": "JrcSEPKn6uI", "channel": "Doji Creates", "title": "C++ Logical Operators Explained (How AND OR NOT Logic Works)"},
            ],
            "java": [
                {"id": "h7pGky1QaJs", "channel": "Doji Creates", "title": "Java Logical Operators Explained (How They Work)"},
            ],
            "c": [
                {"id": "U19kiynYopE", "channel": "Portfolio Courses", "title": "Logical Operators | C Programming Tutorial"},
            ],
        },
        "key_points": [
            "and / && : the result is true only if both conditions are true.",
            "or / || : the result is true if at least one condition is true.",
            "not / ! : flips true to false and false to true.",
            "Relational operators (like age >= 18) produce true or false, which logical operators can combine.",
            "A truth table shows the result for every combination of inputs.",
        ],
        "code": {
            "python": "age = 20\nhas_id = True\n\nif age >= 18 and has_id:\n    print(\"You may enter.\")\n\nif age < 13 or age > 65:\n    print(\"Discount applies.\")\n\nif not has_id:\n    print(\"Show your ID first.\")\n\nprint(\"True and False:\", True and False)\nprint(\"True or False:\", True or False)\nprint(\"not True:\", not True)",
            "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int age = 20;\n    bool hasId = true;\n\n    if (age >= 18 && hasId) {\n        cout << \"You may enter.\" << endl;\n    }\n\n    if (age < 13 || age > 65) {\n        cout << \"Discount applies.\" << endl;\n    }\n\n    if (!hasId) {\n        cout << \"Show your ID first.\" << endl;\n    }\n\n    cout << \"True and False: \" << (true && false) << endl;\n    cout << \"True or False: \" << (true || false) << endl;\n    cout << \"not True: \" << (!true) << endl;\n    return 0;\n}",
            "java": "public class Main {\n    public static void main(String[] args) {\n        int age = 20;\n        boolean hasId = true;\n\n        if (age >= 18 && hasId) {\n            System.out.println(\"You may enter.\");\n        }\n\n        if (age < 13 || age > 65) {\n            System.out.println(\"Discount applies.\");\n        }\n\n        if (!hasId) {\n            System.out.println(\"Show your ID first.\");\n        }\n\n        System.out.println(\"True and False: \" + (true && false));\n        System.out.println(\"True or False: \" + (true || false));\n        System.out.println(\"not True: \" + (!true));\n    }\n}",
            "c": "#include <stdio.h>\n\nint main() {\n    int age = 20;\n    int has_id = 1;  // 1 = true\n\n    if (age >= 18 && has_id) {\n        printf(\"You may enter.\\n\");\n    }\n\n    if (age < 13 || age > 65) {\n        printf(\"Discount applies.\\n\");\n    }\n\n    if (!has_id) {\n        printf(\"Show your ID first.\\n\");\n    }\n\n    printf(\"True and False: %d\\n\", 1 && 0);\n    printf(\"True or False: %d\\n\", 1 || 0);\n    printf(\"not True: %d\\n\", !1);\n    return 0;\n}",
        },
        "quiz": [
            {
                "question": "What is the logical OR operator in Python?",
                "options": ["and", "or", "not", "||"],
                "correct": 1,
            },
            {
                "question": "In C++, which operator means \"not\"?",
                "options": ["!=", "!", "not", "~"],
                "correct": 1,
            },
            {
                "question": "What is the result of true and false?",
                "options": ["true", "false", "error", "0"],
                "correct": 1,
            },
        ],
    },
    {
        "section": "Fundamentals",
        "id": 6,
        "minutes": 45,
        "title": "Conditionals (if / else)",
        "icon": "bi-signpost-split",
        "description": "Conditionals let your program make decisions. Based on a condition, the program executes one block of code or another. The syntax differs slightly between languages.",
        "videos": {
            "python": [
                {"id": "aXWb4rDK8NE", "channel": "Doji Creates", "title": "Python If Else Statement Explained (How Basic Decision Making Works)"},
                {"id": "RHM8_z0tpHY", "channel": "Doji Creates", "title": "Python Elif Statement Explained (How Multiple Conditions Work)"},
            ],
            "cpp": [
                {"id": "ISLTa95qJJA", "channel": "Doji Creates", "title": "C++ If Else Statement Explained (How Decision Making Works)"},
            ],
            "java": [
                {"id": "GaAKcy9cEcU", "channel": "Doji Creates", "title": "Java If Else Statement Explained (How Decision Making Works)"},
            ],
            "c": [
                {"id": "q2LCT6gRZVY", "channel": "LearningLad", "title": "IF ELSE Conditional Statements in C Programming Video Tutorial"},
            ],
        },
        "key_points": [
            "Python uses if / elif / else with colons and indentation.",
            "C, C++, and Java use if / else if / else with braces and parentheses.",
            "In C, C++, and Java, the condition must be inside parentheses.",
            "You can nest conditionals inside other conditionals.",
            "Comparisons like >= and == are common in conditions.",
        ],
        "code": {
            "python": "score = 85\n\nif score >= 90:\n    print(\"Grade: A\")\nelif score >= 75:\n    print(\"Grade: B\")\nelif score >= 60:\n    print(\"Grade: C\")\nelse:\n    print(\"Grade: F\")\n\nif score >= 60 and score < 75:\n    print(\"Almost passing.\")",
            "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int score = 85;\n\n    if (score >= 90) {\n        cout << \"Grade: A\" << endl;\n    } else if (score >= 75) {\n        cout << \"Grade: B\" << endl;\n    } else if (score >= 60) {\n        cout << \"Grade: C\" << endl;\n    } else {\n        cout << \"Grade: F\" << endl;\n    }\n\n    return 0;\n}",
            "java": "public class Main {\n    public static void main(String[] args) {\n        int score = 85;\n\n        if (score >= 90) {\n            System.out.println(\"Grade: A\");\n        } else if (score >= 75) {\n            System.out.println(\"Grade: B\");\n        } else if (score >= 60) {\n            System.out.println(\"Grade: C\");\n        } else {\n            System.out.println(\"Grade: F\");\n        }\n    }\n}",
            "c": "#include <stdio.h>\n\nint main() {\n    int score = 85;\n\n    if (score >= 90) {\n        printf(\"Grade: A\\n\");\n    } else if (score >= 75) {\n        printf(\"Grade: B\\n\");\n    } else if (score >= 60) {\n        printf(\"Grade: C\\n\");\n    } else {\n        printf(\"Grade: F\\n\");\n    }\n\n    return 0;\n}",
        },
        "quiz": [
            {
                "question": "What keyword does Python use for \"else if\"?",
                "options": ["elseif", "elif", "else if", "el-if"],
                "correct": 1,
            },
            {
                "question": "In Java, what must the condition inside an if statement be wrapped in?",
                "options": ["Braces {}", "Parentheses ()", "Square brackets []", "Quotes"],
                "correct": 1,
            },
            {
                "question": "If a condition is false and there is an else block, what happens?",
                "options": ["The program crashes", "The else block runs", "Nothing runs", "The if block runs"],
                "correct": 1,
            },
        ],
    },
    {
        "section": "Fundamentals",
        "id": 7,
        "minutes": 45,
        "title": "Loops",
        "icon": "bi-arrow-repeat",
        "description": "Loops repeat a block of code. A for loop runs a fixed number of times, while a while loop repeats while a condition is true. Loops are used everywhere in real programs.",
        "videos": {
            "python": [
                {"id": "EX47v75YM1Y", "channel": "Doji Creates", "title": "Python For Loop Explained (How Iteration Works Step by Step)"},
                {"id": "Quuq2lC76iw", "channel": "Doji Creates", "title": "Python While Loop Explained (How Condition Based Repetition Works)"},
            ],
            "cpp": [
                {"id": "-Qev7T2a_Lc", "channel": "Doji Creates", "title": "C++ For Loop Explained (How Iteration Control Works Step by Step)"},
                {"id": "WKvTa-paPiM", "channel": "Doji Creates", "title": "C++ While Loop with Integer Explained (How Condition Based Loop Works)"},
            ],
            "java": [
                {"id": "Mt-gZKX3dq0", "channel": "Doji Creates", "title": "Java For Loop Explained (How It Works for Beginners)"},
                {"id": "LWLrbN4f0Fg", "channel": "Doji Creates", "title": "Java While Loop Explained (How It Works for Beginners)"},
            ],
            "c": [
                {"id": "b4DPj0XAfSg", "channel": "Bro Code", "title": "C for loops in 3 minutes!"},
                {"id": "GWS9Jm0d7Sw", "channel": "CodeWithBasha", "title": "While Loop in C Explained | C Programming Loops Tutorial for Beginners"},
            ],
        },
        "key_points": [
            "For loop: Python for x in range(n), C/C++/Java for (int i = 0; i < n; i++).",
            "While loop: repeats while the condition is true.",
            "Be careful: if the condition never becomes false, the loop runs forever.",
            "break stops the loop early, continue skips to the next iteration.",
            "Loops are useful for summing values, counting, and processing collections.",
        ],
        "code": {
            "python": "print(\"Counting from 1 to 5:\")\nfor i in range(1, 6):\n    print(i)\n\nsum_of_evens = 0\nnum = 2\nwhile num <= 10:\n    sum_of_evens += num\n    num += 2\nprint(\"Sum of evens up to 10:\", sum_of_evens)",
            "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    cout << \"Counting from 1 to 5:\" << endl;\n    for (int i = 1; i <= 5; i++) {\n        cout << i << endl;\n    }\n\n    int sum = 0;\n    int num = 2;\n    while (num <= 10) {\n        sum += num;\n        num += 2;\n    }\n    cout << \"Sum of evens up to 10: \" << sum << endl;\n    return 0;\n}",
            "java": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Counting from 1 to 5:\");\n        for (int i = 1; i <= 5; i++) {\n            System.out.println(i);\n        }\n\n        int sum = 0;\n        int num = 2;\n        while (num <= 10) {\n            sum += num;\n            num += 2;\n        }\n        System.out.println(\"Sum of evens up to 10: \" + sum);\n    }\n}",
            "c": "#include <stdio.h>\n\nint main() {\n    printf(\"Counting from 1 to 5:\\n\");\n    for (int i = 1; i <= 5; i++) {\n        printf(\"%d\\n\", i);\n    }\n\n    int sum = 0;\n    int num = 2;\n    while (num <= 10) {\n        sum += num;\n        num += 2;\n    }\n    printf(\"Sum of evens up to 10: %d\\n\", sum);\n    return 0;\n}",
        },
        "quiz": [
            {
                "question": "In Python, what values does range(1, 6) produce?",
                "options": ["1, 2, 3, 4, 5, 6", "1, 2, 3, 4, 5", "0, 1, 2, 3, 4, 5", "2, 3, 4, 5, 6"],
                "correct": 1,
            },
            {
                "question": "What does break do inside a loop?",
                "options": ["Skips one iteration", "Stops the loop", "Restarts the loop", "Ends the program"],
                "correct": 1,
            },
            {
                "question": "What happens if a while loop condition never becomes false?",
                "options": ["It runs forever", "It stops after 10 runs", "An error appears", "It skips the block"],
                "correct": 0,
            },
        ],
    },
    {
        "section": "Fundamentals",
        "id": 8,
        "minutes": 45,
        "title": "Functions",
        "icon": "bi-motherboard",
        "description": "A function is a reusable block of code that performs a specific task. You define it once and call it many times, which keeps your programs organized and shorter.",
        "videos": {
            "python": [
                {"id": "89cGQjB5R4M", "channel": "Bro Code", "title": "Functions in Python are easy"},
            ],
            "cpp": [
                {"id": "67I3ZEmyVKQ", "channel": "Doji Creates", "title": "C++ Functions Explained (How Code Reusability Works)"},
                {"id": "6zhISR9JQc8", "channel": "Doji Creates", "title": "C++ Parameters and Arguments Explained (How Function Inputs Work)"},
            ],
            "java": [
                {"id": "v5p_SUfi710", "channel": "Bro Code", "title": "Java methods explained in 10+ minutes"},
            ],
            "c": [
                {"id": "NGQoKF2Ggt8", "channel": "Portfolio Courses", "title": "Function Basics | C Programming Tutorial"},
            ],
        },
        "key_points": [
            "A function takes inputs (parameters) and returns a result.",
            "Python: def add(a, b): then return a + b.",
            "C and C++: specify the return type, e.g. int add(int a, int b).",
            "Java: methods live inside a class, e.g. static int add(...).",
            "Always give functions clear names that describe what they do.",
        ],
        "code": {
            "python": "def add(a, b):\n    return a + b\n\ndef greet(name):\n    print(\"Hello, \" + name + \"!\")\n\nresult = add(5, 7)\nprint(\"5 + 7 =\", result)\ngreet(\"Alice\")",
            "cpp": "#include <iostream>\n#include <string>\nusing namespace std;\n\nint add(int a, int b) {\n    return a + b;\n}\n\nvoid greet(string name) {\n    cout << \"Hello, \" << name << \"!\" << endl;\n}\n\nint main() {\n    int result = add(5, 7);\n    cout << \"5 + 7 = \" << result << endl;\n    greet(\"Alice\");\n    return 0;\n}",
            "java": "public class Main {\n    static int add(int a, int b) {\n        return a + b;\n    }\n\n    static void greet(String name) {\n        System.out.println(\"Hello, \" + name + \"!\");\n    }\n\n    public static void main(String[] args) {\n        int result = add(5, 7);\n        System.out.println(\"5 + 7 = \" + result);\n        greet(\"Alice\");\n    }\n}",
            "c": "#include <stdio.h>\n\nint add(int a, int b) {\n    return a + b;\n}\n\nvoid greet(char name[]) {\n    printf(\"Hello, %s!\\n\", name);\n}\n\nint main() {\n    int result = add(5, 7);\n    printf(\"5 + 7 = %d\\n\", result);\n    greet(\"Alice\");\n    return 0;\n}",
        },
        "quiz": [
            {
                "question": "Which keyword creates a function in Python?",
                "options": ["func", "def", "function", "define"],
                "correct": 1,
            },
            {
                "question": "In C++, which return type means the function returns nothing?",
                "options": ["int", "void", "null", "none"],
                "correct": 1,
            },
            {
                "question": "What keyword sends a value back from a function?",
                "options": ["send", "give", "return", "output"],
                "correct": 2,
            },
        ],
    },
    {
        "section": "Fundamentals",
        "id": 9,
        "minutes": 45,
        "title": "Arrays and Lists",
        "icon": "bi-collection",
        "description": "Collections store multiple values in one variable. In Python you use lists; in C and C++ you use arrays or vectors; in Java you use arrays or ArrayLists. Indexing starts at 0 in all four.",
        "videos": {
            "python": [
                {"id": "dpwp1NADaFU", "channel": "Doji Creates", "title": "Python Lists Explained (How Ordered Data Storage Works)"},
            ],
            "cpp": [
                {"id": "dRyf8cLyKgA", "channel": "Doji Creates", "title": "C++ Arrays Explained (How Indexed Data Storage Works)"},
            ],
            "java": [
                {"id": "9dr2mHYYoug", "channel": "Bro Code", "title": "Learn Java arrays in 9 minutes"},
            ],
            "c": [
                {"id": "MOeGnamlUP4", "channel": "Programiz", "title": "#19 C Arrays | [2025] C Programming For Beginners"},
            ],
        },
        "key_points": [
            "Indexing starts at 0: the first element is at position 0.",
            "Python lists: grades = [88, 92, 75] and can change size.",
            "C and C++ arrays have a fixed size; C++ std::vector grows dynamically.",
            "Java arrays have a fixed size; ArrayList grows dynamically.",
            "Loop over the collection to print or process every element.",
        ],
        "code": {
            "python": "grades = [88, 92, 75, 96, 81]\n\ntotal = 0\nfor g in grades:\n    total += g\n\naverage = total / len(grades)\nprint(\"Grades:\", grades)\nprint(\"Average:\", average)\nprint(\"First grade:\", grades[0])",
            "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int grades[] = {88, 92, 75, 96, 81};\n    int total = 0;\n    int count = 5;\n\n    for (int i = 0; i < count; i++) {\n        total += grades[i];\n    }\n\n    double average = (double)total / count;\n    cout << \"Average: \" << average << endl;\n    cout << \"First grade: \" << grades[0] << endl;\n    return 0;\n}",
            "java": "public class Main {\n    public static void main(String[] args) {\n        int[] grades = {88, 92, 75, 96, 81};\n        int total = 0;\n\n        for (int i = 0; i < grades.length; i++) {\n            total += grades[i];\n        }\n\n        double average = (double) total / grades.length;\n        System.out.println(\"Average: \" + average);\n        System.out.println(\"First grade: \" + grades[0]);\n    }\n}",
            "c": "#include <stdio.h>\n\nint main() {\n    int grades[] = {88, 92, 75, 96, 81};\n    int total = 0;\n    int count = 5;\n\n    for (int i = 0; i < count; i++) {\n        total += grades[i];\n    }\n\n    double average = (double)total / count;\n    printf(\"Average: %.1f\\n\", average);\n    printf(\"First grade: %d\\n\", grades[0]);\n    return 0;\n}",
        },
        "quiz": [
            {
                "question": "What is the index of the first element in all three languages?",
                "options": ["1", "0", "-1", "2"],
                "correct": 1,
            },
            {
                "question": "Which Python collection can grow and shrink in size?",
                "options": ["Tuple", "List", "Set of fixed size", "String"],
                "correct": 1,
            },
            {
                "question": "In Java, which of these grows dynamically?",
                "options": ["int[]", "String", "ArrayList", "double[]"],
                "correct": 2,
            },
        ],
    },
    {
        "section": "Fundamentals",
        "id": 10,
        "minutes": 50,
        "title": "Basic Problem Solving",
        "icon": "bi-lightbulb",
        "description": "Programming is really problem solving. The key is to break a problem into small steps, write them as a plan, then translate each step into code. Start with paper and pencil before typing.",
        "videos": [
            {"id": "6XJ8294lC0c", "channel": "Doji Creates", "title": "Flowchart Pseudocode and Algorithm Explained (How They Work Together)"},
        ],
        "key_points": [
            "Understand the problem first: what is the input, what is the output?",
            "Break the problem into smaller sub-problems.",
            "Write a plan or pseudocode before writing real code.",
            "Test your program with simple examples by hand first.",
            "Fix errors one at a time; use print statements to debug.",
        ],
        "code": {
            "python": "# Problem: sum of all even numbers from 1 to n\ndef sum_of_evens(n):\n    total = 0\n    for i in range(1, n + 1):\n        if i % 2 == 0:\n            total += i\n    return total\n\nn = 20\nprint(\"Sum of evens up to\", n, \"=\", sum_of_evens(n))",
            "cpp": "#include <iostream>\nusing namespace std;\n\nint sumOfEvens(int n) {\n    int total = 0;\n    for (int i = 1; i <= n; i++) {\n        if (i % 2 == 0) {\n            total += i;\n        }\n    }\n    return total;\n}\n\nint main() {\n    int n = 20;\n    cout << \"Sum of evens up to \" << n << \" = \" << sumOfEvens(n) << endl;\n    return 0;\n}",
            "java": "public class Main {\n    static int sumOfEvens(int n) {\n        int total = 0;\n        for (int i = 1; i <= n; i++) {\n            if (i % 2 == 0) {\n                total += i;\n            }\n        }\n        return total;\n    }\n\n    public static void main(String[] args) {\n        int n = 20;\n        System.out.println(\"Sum of evens up to \" + n + \" = \" + sumOfEvens(n));\n    }\n}",
            "c": "#include <stdio.h>\n\n// Problem: sum of all even numbers from 1 to n\nint sum_of_evens(int n) {\n    int total = 0;\n    for (int i = 1; i <= n; i++) {\n        if (i % 2 == 0) {\n            total += i;\n        }\n    }\n    return total;\n}\n\nint main() {\n    int n = 20;\n    printf(\"Sum of evens up to %d = %d\\n\", n, sum_of_evens(n));\n    return 0;\n}",
        },
        "quiz": [
            {
                "question": "What is the first step when solving a programming problem?",
                "options": ["Write code immediately", "Understand the problem", "Pick the hardest solution", "Ask for the answer"],
                "correct": 1,
            },
            {
                "question": "What is pseudocode?",
                "options": ["A compiled program", "A plain-language plan of the steps", "A type of loop", "A debugging tool"],
                "correct": 1,
            },
            {
                "question": "How should you fix errors in your program?",
                "options": ["All at once", "One at a time", "By rewriting everything", "By ignoring them"],
                "correct": 1,
            },
        ],
    },
    {
        "section": "Advanced Fundamentals",
        "id": 31,
        "minutes": 40,
        "title": "Introduction to GitHub",
        "icon": "bi-github",
        "description": "GitHub is the world's largest platform for hosting and collaborating on code. Learn what Git and GitHub are, how repositories work, and how to create, clone, commit, push, and manage branches — essential skills for any developer working on a capstone or team project.",
        "videos": {
            "general": [
                {"id": "tRZGeaHPoaw", "channel": "Kevin Stratvert", "title": "Git and GitHub Tutorial for Beginners"},
            ],
        },
        "key_points": [
            "Git is a version control system that tracks changes to your code over time; GitHub is a website that hosts Git repositories online.",
            "A repository (repo) is a project folder that Git tracks — it stores every version of your files.",
            "git init creates a new repo, git clone copies an existing one from GitHub to your computer.",
            "git add stages changes, git commit saves them with a message, and git push uploads them to GitHub.",
            "git pull downloads the latest changes from GitHub and merges them into your local copy.",
            "Branches let you work on features or fixes without affecting the main code; merge when ready.",
            "Pull requests let you propose changes, request code reviews, and merge safely with your team.",
            "A .gitignore file tells Git which files (like .env or node_modules) to never track.",
        ],
        "code": {
            "shell": "# Step 1: Install Git and configure your identity\ngit config --global user.name \"Your Name\"\ngit config --global user.email \"you@example.com\"\n\n# Step 2: Create a new repository\nmkdir my-project && cd my-project\ngit init\n\n# Step 3: Create a file and make your first commit\necho \"# My Project\" > README.md\ngit add README.md\ngit commit -m \"Initial commit: add README\"\n\n# Step 4: Connect to GitHub and push\ngit remote add origin https://github.com/yourname/my-project.git\ngit branch -M main\ngit push -u origin main\n\n# Step 5: Pull latest changes from GitHub\ngit pull origin main\n\n# Step 6: Create a branch for a new feature\ngit checkout -b feature-login\ngit add .\ngit commit -m \"Add login page\"\ngit push -u origin feature-login\n\n# Step 7: View your commit history\ngit log --oneline",
        },
        "quiz": [
            {
                "question": "What is Git?",
                "options": ["A website for hosting code", "A version control system that tracks code changes", "A programming language", "A database"],
                "correct": 1,
            },
            {
                "question": "What does git init do?",
                "options": ["Downloads a repo from GitHub", "Creates a new Git repository", "Deletes a file", "Connects to the internet"],
                "correct": 1,
            },
            {
                "question": "What command stages changes for commit?",
                "options": ["git commit", "git push", "git add", "git pull"],
                "correct": 2,
            },
            {
                "question": "What is a pull request?",
                "options": ["Downloading code from GitHub", "A proposal to merge your changes into another branch after code review", "A request to delete a repository", "A way to reset your code"],
                "correct": 1,
            },
            {
                "question": "What file tells Git which files to ignore?",
                "options": [".env", ".gitignore", "README.md", "package.json"],
                "correct": 1,
            },
        ],
    },
    {
        "section": "Advanced Fundamentals",
        "id": 30,
        "minutes": 45,
        "title": "Web Deployment Fundamentals",
        "icon": "bi-cloud-upload",
        "description": "Building a web app is only half the journey — deployment puts your project on the internet so anyone can use it. Learn the essentials of hosting, environment configuration, domain names, CI/CD, and how to deploy Laravel and React applications to production.",
        "videos": {
            "general": [
                {"id": "m-QO9Qp_wRQ", "channel": "Laravel Daily", "title": "Deploying a Laravel Application for the First Time"},
            ],
            "laravel": [
                {"id": "m-QO9Qp_wRQ", "channel": "Laravel Daily", "title": "Deploying a Laravel Application for the First Time"},
            ],
            "react": [
                {"id": "SuZBpX7Y7EA", "channel": "Coding with John", "title": "How to Deploy React Apps on Vercel"},
            ],
        },
        "key_points": [
            "Deployment means moving your app from your local machine to a server accessible on the internet.",
            "Static sites (HTML/CSS/JS) can be hosted on GitHub Pages, Netlify, or Vercel for free.",
            "Laravel apps need a server with PHP, a database, and a web server like Nginx or Apache.",
            "React apps are built into static files (npm run build) and can be deployed to Vercel, Netlify, or Cloudflare Pages.",
            "Environment variables (.env) keep secrets like API keys and database passwords out of your code.",
            "CI/CD pipelines (e.g., GitHub Actions) automate testing and deployment on every code push.",
            "Domain names translate human-readable URLs (example.com) to server IP addresses via DNS.",
            "Always set APP_DEBUG=false and APP_ENV=production when deploying Laravel to production.",
        ],
        "code": {
            "php": "// Laravel .env.production settings\nAPP_ENV=production\nAPP_DEBUG=false\nAPP_URL=https://yourdomain.com\n\nDB_CONNECTION=mysql\nDB_HOST=127.0.0.1\nDB_DATABASE=your_app\nDB_USERNAME=your_user\nDB_PASSWORD=your_strong_password\n\n// Terminal commands for Laravel deployment:\n// 1. Push code to GitHub\n//    git add . && git commit -m \"ready for deploy\" && git push\n// 2. SSH into your server\n//    ssh user@your-server-ip\n// 3. Clone and install\n//    git clone https://github.com/you/your-app.git\n//    cd your-app\n//    composer install --no-dev --optimize-autoloader\n//    cp .env.example .env\n//    php artisan key:generate\n//    php artisan migrate --force\n// 4. Optimize for production\n//    php artisan config:cache\n//    php artisan route:cache\n//    php artisan view:cache\n// 5. Set permissions\n//    chown -R www:www storage bootstrap/cache",
            "javascript": "// React — deploy to Vercel or Netlify\n\n// Step 1: Build for production\n// npm run build\n\n// Step 2: Push to GitHub\n// git init && git add .\n// git commit -m \"initial commit\"\n// git remote add origin https://github.com/you/my-react-app.git\n// git push -u origin main\n\n// Step 3: Import on Vercel (vercel.com)\n//   - Click \"New Project\" → Import GitHub repo\n//   - Build Command: npm run build\n//   - Output Directory: dist (Vite) or build (CRA)\n//   - Click Deploy\n\n// Step 4: Environment Variables on Vercel\n//   VITE_API_URL=https://api.yourdomain.com\n//   (Never commit .env files to Git!)\n\n// Example Vite config for production:\n// vite.config.js\nimport { defineConfig } from 'vite';\nimport react from '@vitejs/plugin-react';\n\nexport default defineConfig({\n  plugins: [react()],\n  base: '/',\n  build: {\n    outDir: 'dist',\n    sourcemap: false,\n  },\n});",
        },
        "quiz": [
            {
                "question": "What does deployment mean?",
                "options": ["Writing code on your laptop", "Moving your app to a server so anyone on the internet can use it", "Debugging your program", "Creating a database"],
                "correct": 1,
            },
            {
                "question": "Which of these is a free hosting platform for React apps?",
                "options": ["Vercel", "MySQL", "PHP", "Nginx"],
                "correct": 0,
            },
            {
                "question": "What is the purpose of a .env file in production?",
                "options": ["To store source code", "To keep secrets like API keys and passwords out of your code", "To style your website", "To run tests"],
                "correct": 1,
            },
            {
                "question": "What command builds a React app for production?",
                "options": ["npm start", "npm run build", "npm install", "npm test"],
                "correct": 1,
            },
            {
                "question": "What should APP_DEBUG be set to in Laravel production?",
                "options": ["true", "false", "null", "1"],
                "correct": 1,
            },
        ],
    },
    {
        "section": "Advanced Fundamentals",
        "id": 32,
        "minutes": 40,
        "title": "Deploying with Render",
        "icon": "bi-cloud-arrow-up",
        "description": "Render is a cloud platform that makes deploying web apps, APIs, and databases effortless. Connect your GitHub repo, set your build and start commands, and Render handles the rest — SSL certificates, auto-deploys, scaling, and more. Learn how to deploy Laravel, React, and Node.js apps to Render.",
        "videos": {
            "general": [
                {"id": "srudWEWKPv0", "channel": "Tech With Tim", "title": "How to Deploy Laravel Project on Render in 2025 (FULL Tutorial)"},
            ],
        },
        "key_points": [
            "Render is a PaaS (Platform as a Service) that hosts web services, static sites, databases, and background workers.",
            "Connect your GitHub or GitLab repo and Render auto-deploys on every push to the linked branch.",
            "Free tier is available for hobby projects — web services spin down after inactivity to save resources.",
            "A render.yaml file lets you define your infrastructure as code (web services, databases, env vars).",
            "Environment variables store secrets (API keys, database URLs) — never commit .env files to Git.",
            "Render provides free managed PostgreSQL databases with automatic backups.",
            "Static sites (React, Vue, HTML/CSS/JS) deploy in seconds with zero configuration.",
            "Custom domains with free automatic SSL certificates are supported on all plans.",
            "Setting up a Render account: Sign up at render.com, connect your GitHub account, and authorize Render to access your repositories.",
            "Creating a Web Service: Click 'New' > 'Web Service', select your repository, choose the branch, and configure build/start commands.",
            "Laravel deployment on Render: Use PHP environment, set buildCommand to run composer install and artisan commands, startCommand to serve the app.",
            "React deployment on Render: Use Static Site type, set buildCommand to npm run build, publish path to dist or build folder.",
            "Environment variables in Render dashboard: Go to your service > Environment tab, add KEY=VALUE pairs for secrets like APP_KEY, DB_URL, API tokens.",
            "Render automatically detects your project type and suggests optimal settings for popular frameworks.",
            "Deploy hooks: Trigger manual deploys from the Render dashboard or use webhook URLs to deploy from CI/CD pipelines.",
            "Logs and monitoring: View real-time logs in the Render dashboard to debug deployment issues and monitor app performance.",
            "Background workers: Run queue workers, cron jobs, or any background process using Render's Background Worker service type.",
            "Database management: Render PostgreSQL includes automatic backups, connection pooling, and dashboard for direct SQL queries.",
            "Scaling: Upgrade from free to paid plans for more RAM, CPU, custom domains, and to prevent service spin-down.",
            "Common issues: Missing environment variables, incorrect build commands, and not setting the correct PORT environment variable.",
        ],
        "code": {
            "shell": "# ========================================\n# DEPLOYING WITH RENDER - STEP BY STEP\n# ========================================\n\n# --- STEP 1: Create render.yaml in project root ---\n# This file defines your entire infrastructure\n\n# --- Laravel Example ---\nservices:\n  - type: web\n    name: my-laravel-app\n    env: php\n    buildCommand: |\n      composer install --no-dev --optimize-autoloader\n      php artisan key:generate\n      php artisan migrate --force\n      php artisan config:cache\n      php artisan route:cache\n    startCommand: php artisan serve --host=0.0.0.0 --port=$PORT\n    envVars:\n      - key: APP_ENV\n        value: production\n      - key: APP_DEBUG\n        value: \"false\"\n      - key: APP_URL\n        sync: false\n      - key: DB_URL\n        fromDatabase:\n          name: my-postgres-db\n          property: connectionString\n\n# --- React / Static Site Example ---\nservices:\n  - type: static_site\n    name: my-react-app\n    buildCommand: npm run build\n    staticPublishPath: dist\n    routes:\n      - type: rewrite\n        source: /*\n        destination: /index.html\n\n# --- PostgreSQL Database ---\ndatabases:\n  - name: my-postgres-db\n    plan: free\n    databaseName: myapp\n    ipAllowList: []\n\n# ========================================\n# STEP 2: Setting up environment variables\n# ========================================\n\n# In your Laravel .env file (NEVER commit this to Git):\nAPP_ENV=production\nAPP_KEY=base64:your-generated-key-here\nAPP_DEBUG=false\nAPP_URL=https://your-app.onrender.com\nDB_CONNECTION=pgsql\nDB_URL=your-database-url-from-render\nCACHE_DRIVER=file\nSESSION_DRIVER=file\n\n# In Render Dashboard:\n# Go to Service > Environment > Add Environment Variable\n# Key: APP_KEY  Value: base64:your-generated-key\n# Key: DB_URL   Value: (copy from Render database connection)\n\n# ========================================\n# STEP 3: Deploying - Manual steps on Render\n# ========================================\n\n# 1. Go to render.com and sign up / log in\n# 2. Click 'New' button (top right)\n# 3. Select 'Web Service' for backend, 'Static Site' for frontend\n# 4. Connect your GitHub account\n# 5. Select your repository\n# 6. Configure:\n#    - Name: my-laravel-app\n#    - Region: Singapore (closest to PH)\n#    - Branch: main\n#    - Runtime: PHP\n#    - Build Command: composer install --no-dev --optimize-autoloader\n#    - Start Command: php artisan serve --host=0.0.0.0 --port=$PORT\n# 7. Add environment variables from your .env\n# 8. Click 'Create Web Service'\n\n# ========================================\n# STEP 4: Deploy React frontend separately\n# ========================================\n\n# 1. Click 'New' > 'Static Site'\n# 2. Connect same repo or separate frontend repo\n# 3. Configure:\n#    - Name: my-react-app\n#    - Build Command: npm run build\n#    - Publish Directory: dist\n# 4. Add environment variable:\n#    Key: VITE_API_URL  Value: https://my-laravel-app.onrender.com\n# 5. After deploy, update Laravel CORS to allow your React domain\n\n# ========================================\n# STEP 5: Database setup\n# ========================================\n\n# 1. Click 'New' > 'PostgreSQL'\n# 2. Configure:\n#    - Name: my-postgres-db\n#    - Database: myapp\n#    - Plan: Free (or Paid for production)\n# 3. Copy the Internal Database URL\n# 4. Add as environment variable DB_URL in your web service\n# 5. Run migrations: add 'php artisan migrate --force' to buildCommand\n\n# ========================================\n# STEP 6: Custom domain (optional)\n# ========================================\n\n# 1. Go to your service > Settings\n# 2. Scroll to 'Custom Domains'\n# 3. Click 'Add Custom Domain'\n# 4. Enter your domain: www.yourdomain.com\n# 5. Add DNS records at your domain registrar:\n#    Type: CNAME  Name: www  Value: your-app.onrender.com\n#    Type: A      Name: @    Value: 216.24.57.1 (Render's IP)\n# 6. SSL certificate is auto-provisioned by Render\n\n# ========================================\n# STEP 7: Monitoring and logs\n# ========================================\n\n# - View logs: Service > Logs tab (real-time)\n# - Check events: Service > Events tab (deploy history)\n# - Set up alerts: Service > Notifications\n# - Monitor metrics: Service > Metrics (CPU, RAM usage)\n\n# ========================================\n# Common troubleshooting\n# ========================================\n\n# Issue: App not starting\n# Fix: Check logs, ensure PORT env var is used in startCommand\n\n# Issue: Database connection failed\n# Fix: Use Internal Database URL, not External\n\n# Issue: Build fails\n# Fix: Check buildCommand, ensure all dependencies in composer.json/package.json\n\n# Issue: CORS errors\n# Fix: Add your frontend domain to Laravel's config/cors.php allowed_origins",
        },
        "quiz": [
            {
                "question": "What type of platform is Render?",
                "options": ["A text editor", "A PaaS (Platform as a Service) for hosting apps", "A programming language", "A database only"],
                "correct": 1,
            },
            {
                "question": "How does Render deploy your code?",
                "options": ["You upload ZIP files manually", "It connects to your GitHub/GitLab repo and auto-deploys on push", "You FTP files to a server", "You email the code to Render support"],
                "correct": 1,
            },
            {
                "question": "What file defines your Render infrastructure as code?",
                "options": [".env", "render.yaml", "package.json", "Dockerfile"],
                "correct": 1,
            },
            {
                "question": "What does the free tier do to inactive web services?",
                "options": ["Deletes them", "Spins them down (sleeps) to save resources", "Charges you extra", "Nothing"],
                "correct": 1,
            },
            {
                "question": "Which of these can Render host?",
                "options": ["Only React apps", "Only Laravel apps", "Web services, static sites, databases, and workers", "Only HTML pages"],
                "correct": 2,
            },
            {
                "question": "What should you use in Laravel's startCommand on Render?",
                "options": ["php artisan serve", "php artisan serve --host=0.0.0.0 --port=$PORT", "php -S localhost:8000", "apache start"],
                "correct": 1,
            },
            {
                "question": "Where should you store environment variables like APP_KEY and DB_URL?",
                "options": ["In render.yaml file", "In .env file committed to Git", "In Render Dashboard > Environment tab", "In index.php"],
                "correct": 2,
            },
            {
                "question": "How do you deploy a React app on Render?",
                "options": ["As a Web Service with npm start", "As a Static Site with buildCommand npm run build", "As a Background Worker", "As a PostgreSQL database"],
                "correct": 1,
            },
            {
                "question": "What type of DNS record do you add for a custom domain on Render?",
                "options": ["A record only", "CNAME for www and A record for @", "MX record", "TXT record"],
                "correct": 1,
            },
            {
                "question": "Why should you use Internal Database URL instead of External?",
                "options": ["It's faster and avoids egress charges", "External doesn't work", "Internal has more storage", "No reason, both are the same"],
                "correct": 0,
            },
            {
                "question": "What command should be in your Laravel buildCommand to set up the database?",
                "options": ["php artisan db:seed", "php artisan migrate --force", "php artisan db:create", "mysql -u root"],
                "correct": 1,
            },
            {
                "question": "How can you debug deployment issues on Render?",
                "options": ["Check the Logs tab in your service dashboard", "Email Render support", "Look at your local terminal", "Check GitHub Actions"],
                "correct": 0,
            },
        ],
    },
    {
        "section": "Advanced Fundamentals",
        "id": 33,
        "minutes": 35,
        "title": "Deploying with Netlify",
        "icon": "bi-globe",
        "description": "Netlify is a web platform for building, deploying, and managing modern web projects. Deploy static sites, SPAs, and JAMstack apps instantly from Git. Learn how to deploy React, Vue, and HTML/CSS/JS projects to Netlify with automatic deploys, form handling, and serverless functions.",
        "videos": {
            "general": [
                {"id": "IH95RG9Y6L4", "channel": "Netlify", "title": "Netlify Deployment: The ULTIMATE Guide to Going Live (FAST)"},
                {"id": "YUtNzwxOVYY", "channel": "Tech With Tim", "title": "How To Deploy Project On Netlify 2025"},
            ],
        },
        "key_points": [
            "Netlify is a web platform for building, deploying, and managing modern web projects.",
            "Connect your GitHub/GitLab/Bitbucket repo and Netlify auto-deploys on every push.",
            "Free tier includes 100GB bandwidth/month, 300 build minutes, and unlimited sites.",
            "A netlify.toml file lets you define build settings, redirects, headers, and plugins.",
            "Drag-and-drop deployment: just drop your build folder to Netlify Drop for instant deployment.",
            "Netlify automatically provisions SSL certificates for custom domains.",
            "Deploy Previews: every pull request gets its own unique preview URL for testing.",
            "Netlify Forms: add a contact form to your HTML without any backend code.",
            "Netlify Functions: run serverless Node.js/Go functions without managing servers.",
            "Netlify Identity: add user authentication to your site without a backend.",
            "Environment variables store secrets (API keys, tokens) — configure them in the Netlify dashboard.",
            "Netlify CLI lets you deploy, test, and manage sites from the command line.",
            "Redirects and proxy rules in netlify.toml handle SPA routing and API proxying.",
            "Netlify Edge: run code at the edge for personalization and A/B testing.",
            "Branch deploys: test different features on separate deploy URLs before merging.",
            "Setting up a Netlify account: Sign up at netlify.com, connect your Git provider, and authorize access.",
            "Creating a new site: Click 'Add new site' > 'Import an existing project', select your repo, and configure build settings.",
            "React deployment on Netlify: Set build command to 'npm run build' and publish directory to 'dist' or 'build'.",
            "Vue deployment on Netlify: Set build command to 'npm run build' and publish directory to 'dist'.",
            "Common issues: Missing _redirects file for SPA, incorrect publish directory, and build command errors.",
        ],
        "code": {
            "shell": "# ========================================\n# DEPLOYING WITH NETLIFY - STEP BY STEP\n# ========================================\n\n# --- STEP 1: Create netlify.toml in project root ---\n# This file defines your build settings and behavior\n\n[build]\n  command = \"npm run build\"\n  publish = \"dist\"\n\n# Environment variables\n[build.environment]\n  NODE_VERSION = \"18\"\n  VITE_API_URL = \"https://api.yoursite.com\"\n\n# Redirects for SPA routing\n[[redirects]]\n  from = \"/*\"\n  to = \"/index.html\"\n  status = 200\n\n# Headers for caching\n[[headers]]\n  for = \"/static/*\"\n  [headers.values]\n    Cache-Control = \"public, max-age=31536000, immutable\"\n\n# --- STEP 2: React project setup ---\n# In your React project's package.json:\n{\n  \"name\": \"my-react-app\",\n  \"scripts\": {\n    \"dev\": \"vite\",\n    \"build\": \"vite build\",\n    \"preview\": \"vite preview\"\n  }\n}\n\n# --- STEP 3: Deploy via Netlify CLI ---\n# Install Netlify CLI globally\nnpm install -g netlify-cli\n\n# Login to your Netlify account\nnetlify login\n\n# Initialize a new Netlify site\nnetlify init\n\n# Deploy to production\nnetlify deploy --prod\n\n# --- STEP 4: Deploy via Git (Recommended) ---\n# 1. Push your code to GitHub/GitLab\n# 2. Go to app.netlify.com\n# 3. Click 'Add new site' > 'Import an existing project'\n# 4. Select your Git provider and repository\n# 5. Configure:\n#    - Branch: main\n#    - Build command: npm run build\n#    - Publish directory: dist\n# 6. Click 'Deploy site'\n# 7. Netlify auto-deploys on every push to main\n\n# --- STEP 5: Drag and drop deployment ---\n# 1. Build your project locally: npm run build\n# 2. Go to app.netlify.com\n# 3. Scroll to 'Want to deploy a project manually?'\n# 4. Drag your 'dist' or 'build' folder to the drop zone\n# 5. Site is live instantly!\n\n# --- STEP 6: Custom domain setup ---\n# 1. Go to Site settings > Domain management\n# 2. Click 'Add custom domain'\n# 3. Enter your domain: www.yourdomain.com\n# 4. Add DNS records at your domain registrar:\n#    Type: CNAME  Name: www  Value: your-site.netlify.app\n#    Type: A      Name: @    Value: 75.2.60.5\n# 5. SSL certificate is auto-provisioned\n\n# --- STEP 7: Environment variables ---\n# 1. Go to Site settings > Build & deploy > Environment\n# 2. Click 'Edit variables'\n# 3. Add key-value pairs:\n#    VITE_API_URL = https://api.yoursite.com\n#    DATABASE_URL = postgres://...\n# 4. Variables are available during build and at runtime\n\n# --- STEP 8: Netlify Forms (no backend needed) ---\n# Add to your HTML:\n<form name=\"contact\" method=\"POST\" data-netlify=\"true\">\n  <input type=\"hidden\" name=\"form-name\" value=\"contact\">\n  <p>\n    <label>Your Name: <input type=\"text\" name=\"name\"></label>\n  </p>\n  <p>\n    <label>Your Email: <input type=\"email\" name=\"email\"></label>\n  </p>\n  <p>\n    <label>Message: <textarea name=\"message\"></textarea></label>\n  </p>\n  <p><button type=\"submit\">Send</button></p>\n</form>\n\n# --- STEP 9: Netlify Functions ---\n# Create a file: netlify/functions/hello.js\nexports.handler = async (event, context) => {\n  return {\n    statusCode: 200,\n    body: JSON.stringify({ message: \"Hello from Netlify Functions!\" }),\n  };\n};\n\n# Call from your frontend:\nfetch(\"/.netlify/functions/hello\")\n  .then(res => res.json())\n  .then(data => console.log(data));\n\n# --- STEP 10: Branch deploys and deploy previews ---\n# - Every push to main = production deploy\n# - Every push to other branches = branch deploy (your-branch--your-site.netlify.app)\n# - Every pull request = deploy preview (deploy-preview-123--your-site.netlify.app)\n# - Configure in Site settings > Build & deploy > Branches\n\n# --- Common troubleshooting ---\n\n# Issue: SPA routes return 404\n# Fix: Add _redirects file in public/ folder:\n# /* /index.html 200\n\n# Issue: Build fails with 'command not found'\n# Fix: Ensure build command matches package.json scripts\n\n# Issue: Environment variables not available\n# Fix: Prefix with VITE_ for Vite, REACT_APP_ for CRA, NEXT_PUBLIC_ for Next.js\n\n# Issue: Custom domain not working\n# Fix: Wait for DNS propagation (up to 48 hours), verify DNS records",
        },
        "quiz": [
            {
                "question": "What type of platform is Netlify?",
                "options": ["A database service", "A web platform for building and deploying web projects", "A code editor", "A CDN only"],
                "correct": 1,
            },
            {
                "question": "How does Netlify deploy your code?",
                "options": ["You upload ZIP files manually", "It connects to your Git repo and auto-deploys on push", "You FTP files to a server", "You email the code to Netlify support"],
                "correct": 1,
            },
            {
                "question": "What file defines your Netlify build settings and behavior?",
                "options": [".env", "netlify.toml", "package.json", "Dockerfile"],
                "correct": 1,
            },
            {
                "question": "What is Netlify Drop?",
                "options": ["A music streaming service", "A drag-and-drop deployment tool", "A database backup tool", "A code editor"],
                "correct": 1,
            },
            {
                "question": "What does Netlify provide for free with every custom domain?",
                "options": ["A database", "SSL certificates", "Email hosting", "CDN only"],
                "correct": 1,
            },
            {
                "question": "How do you deploy a React app on Netlify?",
                "options": ["As a Web Service with npm start", "With build command 'npm run build' and publish directory 'dist'", "As a Background Worker", "As a PostgreSQL database"],
                "correct": 1,
            },
            {
                "question": "What is a Deploy Preview?",
                "options": ["A paid feature", "A unique URL for testing pull requests before merging", "A backup of your site", "A local development server"],
                "correct": 1,
            },
            {
                "question": "How do you handle SPA routing on Netlify?",
                "options": ["Add a _redirects file with '/* /index.html 200'", "Use Apache .htaccess", "Configure nginx", "It works automatically"],
                "correct": 0,
            },
            {
                "question": "What is Netlify Functions?",
                "options": ["A math library", "Serverless functions that run without managing servers", "A debugging tool", "A CSS framework"],
                "correct": 1,
            },
            {
                "question": "How do you add a contact form without a backend?",
                "options": ["Use Netlify Forms with data-netlify=\"true\"", "Install a plugin", "Write PHP code", "Use a third-party service"],
                "correct": 0,
            },
            {
                "question": "What prefix is needed for environment variables in Vite?",
                "options": ["REACT_APP_", "VITE_", "NEXT_PUBLIC_", "No prefix needed"],
                "correct": 1,
            },
            {
                "question": "How do you deploy from the command line?",
                "options": ["netlify deploy --prod", "npm run deploy", "git push netlify", "netlify upload"],
                "correct": 0,
            },
        ],
    },
    {
        "section": "Advanced Fundamentals",
        "id": 34,
        "minutes": 40,
        "title": "Building Websites with WordPress",
        "icon": "bi-wordpress",
        "description": "WordPress powers over 40% of all websites on the internet — and you do not need to be a professional programmer to use it. Learn the difference between WordPress.com and WordPress.org, how themes and plugins work, how to create posts and pages, and how to install, customize, and secure a WordPress site with its own domain and hosting.",
        "videos": {
            "general": [
                {"id": "UT3No6nswz8", "channel": "Kevin Stratvert", "title": "WordPress Tutorial for Beginners"},
            ],
        },
        "key_points": [
            "WordPress is a free, open-source Content Management System (CMS) written in PHP that lets anyone build a website without coding.",
            "WordPress.com is a hosted service where WordPress handles the hosting; WordPress.org is the open-source software you install on your own hosting.",
            "WordPress.org (self-hosted) gives you full control: your own domain, plugins, themes, and ad-free site.",
            "A theme controls your site's look and layout; thousands of free and paid themes are available.",
            "A plugin adds features like contact forms, SEO, security, and e-commerce without writing code.",
            "Posts are for blog entries (shown newest-first); Pages are for static content like About and Contact.",
            "The admin dashboard (/wp-admin) is where you manage posts, pages, media, themes, plugins, and settings.",
            "The block editor (Gutenberg) lets you build pages by dragging and dropping blocks for text, images, videos, buttons, and more.",
            "You can install WordPress with one-click installers from most hosting providers, or manually with a local tool like XAMPP or Local.",
            "WP-CLI is a command-line tool that lets you install and manage WordPress from the terminal.",
            "A .htaccess file (Apache) or nginx config handles pretty permalinks and security rules.",
            "Plugins must stay updated — outdated plugins are the #1 cause of WordPress sites being hacked.",
            "Keep WordPress core, themes, and plugins updated, use strong passwords, and enable two-factor authentication to stay secure.",
            "Backups (via plugins or hosting) protect your content and database if something goes wrong.",
            "A typical WordPress stack needs a web server (Apache/Nginx), PHP, and MySQL/MariaDB — similar to any PHP web app.",
        ],
        "code": {
            "shell": "# ========================================\n# WORDPRESS - INSTALL & MANAGE VIA WP-CLI\n# ========================================\n\n# --- STEP 1: Download WordPress (self-hosted / WordPress.org) ---\ncurl -O https://wordpress.org/latest.tar.gz\ntar -xzf latest.tar.gz\ncd wordpress\n\n# --- STEP 2: Create a database in MySQL ---\nmysql -u root -p -e \"CREATE DATABASE wordpress_db CHARACTER SET utf8mb4;\"\nmysql -u root -p -e \"CREATE USER 'wpuser'@'localhost' IDENTIFIED BY 'strong_password';\"\nmysql -u root -p -e \"GRANT ALL ON wordpress_db.* TO 'wpuser'@'localhost';\"\nmysql -u root -p -e \"FLUSH PRIVILEGES;\"\n\n# --- STEP 3: Configure wp-config.php ---\ncp wp-config-sample.php wp-config.php\n# Edit wp-config.php and set:\n#   define('DB_NAME', 'wordpress_db');\n#   define('DB_USER', 'wpuser');\n#   define('DB_PASSWORD', 'strong_password');\n#   define('DB_HOST', 'localhost');\n\n# --- STEP 4: Install WordPress using WP-CLI (if installed) ---\nwp core install \\\n  --url=https://yoursite.com \\\n  --title=\"My WordPress Site\" \\\n  --admin_user=admin \\\n  --admin_password=strong-admin-pass \\\n  --admin_email=you@example.com\n\n# --- STEP 5: Common WP-CLI commands ---\nwp plugin list                # list installed plugins\nwp plugin install woocommerce # install a plugin\nwp theme activate twentytwentyfive  # activate a theme\nwp post create --post_title=\"Hello World\" --post_status=publish\nwp user create juan juan@example.com --role=author\nwp search-replace 'http://localhost' 'https://yoursite.com' --all-tables\nwp cache flush               # clear the cache\nwp core update               # update WordPress core\nwp plugin update --all       # update all plugins\n\n# --- STEP 6: Useful folders ---\n# wp-content/themes/   -> your themes\n# wp-content/plugins/  -> your plugins\n# wp-content/uploads/  -> your media files\n\n# --- STEP 7: Secure it ---\n# 1. Always keep core, themes, and plugins updated\n# 2. Use a strong admin password and 2FA\n# 3. Limit login attempts (plugin like Limit Login Attempts)\n# 4. Enable HTTPS with a free SSL certificate\n# 5. Schedule regular backups",
        },
        "quiz": [
            {
                "question": "What is WordPress?",
                "options": ["A programming language", "A free, open-source Content Management System (CMS)", "A web hosting provider", "A social media platform"],
                "correct": 1,
            },
            {
                "question": "What is the difference between WordPress.com and WordPress.org?",
                "options": ["They are the same thing", "WordPress.com hosts your site; WordPress.org is the self-hosted open-source software", "WordPress.org is paid only", "WordPress.com requires coding"],
                "correct": 1,
            },
            {
                "question": "What controls the look and layout of a WordPress site?",
                "options": ["A plugin", "A theme", "The database", "PHP settings"],
                "correct": 1,
            },
            {
                "question": "What adds features like contact forms and SEO without writing code?",
                "options": ["A theme", "A plugin", "A post", "A tag"],
                "correct": 1,
            },
            {
                "question": "In WordPress, what is a Page?",
                "options": ["A blog entry", "Static content like About or Contact", "A theme file", "A plugin setting"],
                "correct": 1,
            },
            {
                "question": "What does a CMS like WordPress let you do?",
                "options": ["Write machine code", "Build and manage a website without coding", "Compile programs", "Design microchips"],
                "correct": 1,
            },
            {
                "question": "What is the #1 cause of WordPress sites being hacked?",
                "options": ["Using too many pages", "Outdated plugins", "Dark themes", "Too many posts"],
                "correct": 1,
            },
            {
                "question": "Which components make up a typical WordPress hosting stack?",
                "options": ["Node.js, MongoDB, Express", "Apache/Nginx, PHP, and MySQL/MariaDB", "Java, Tomcat, Oracle", "HTML, CSS, JavaScript only"],
                "correct": 1,
            },
            {
                "question": "What command-line tool manages WordPress from the terminal?",
                "options": ["npm", "WP-CLI", "pip", "composer"],
                "correct": 1,
            },
            {
                "question": "Where is the WordPress admin area usually located?",
                "options": ["/admin", "/wp-admin", "/dashboard", "/login"],
                "correct": 1,
            },
        ],
    },
    {
        "section": "Advanced Fundamentals",
        "id": 35,
        "minutes": 45,
        "title": "TypeScript Fundamentals",
        "icon": "bi-filetype-tsx",
        "description": "TypeScript is JavaScript with superpowers — it adds static types that catch bugs before your code ever runs. This lesson revisits every core programming fundamental you learned earlier — variables and constants, primitive types, arrays and tuples, functions, objects, interfaces, classes, conditionals, loops, and more — this time in TypeScript. Learn how to annotate types, design object shapes with interfaces, and run .ts files directly with Node.js.",
        "videos": {
            "general": [
                {"id": "d56mG7DezGs", "channel": "Programming with Mosh", "title": "TypeScript Tutorial for Beginners"},
            ],
        },
        "key_points": [
            "TypeScript is a superset of JavaScript — everything from JavaScript still works, plus you get static types.",
            "Static types let the compiler catch bugs like passing a number where a string is expected — before the code ever runs.",
            "Node.js can run TypeScript directly with node --experimental-strip-types; real projects also use tsc to type-check and build.",
            "let declares a changeable variable; const declares a constant that cannot be reassigned.",
            "Annotate types with a colon — name: string, age: number, isDone: boolean.",
            "TypeScript infers types automatically, but explicit annotations document your intent and catch mistakes early.",
            "Arrays are written string[] or Array<string>; tuples are fixed-length arrays with a type per position, like [string, number].",
            "Union types (number | string) let a value be one of several types; literal unions like \"Easy\" | \"Hard\" restrict it to exact choices.",
            "Interfaces describe the shape of an object; classes add implementation with private, public, and static members.",
            "Functions declare parameter and return types; arrow functions, default parameters, and template literals keep code concise.",
            "Control flow (if/else, ternary, switch) and loops (for, for...of, while) work exactly like JavaScript.",
            "The TypeScript compiler catches bugs at compile time, which is why big teams adopt it — this lesson maps every fundamental you already know in Python, C++, and Java.",
        ],
        "code": {
            "typescript": "// ==============================================\n// TYPESCRIPT FUNDAMENTALS - EVERYTHING IN ONE FILE\n// Run with: node --experimental-strip-types main.ts\n// ==============================================\n\n// ---------- 1. VARIABLES & CONSTANTS ----------\nlet topic: string = \"TypeScript Fundamentals\";\nconst version: number = 5.4;\ntopic = \"Advanced TypeScript\";      // let can change\n// version = 6;                     // ERROR - const cannot be reassigned\n\n// ---------- 2. PRIMITIVES & TYPE INFERENCE ----------\nconst teacher = \"Mosh\";             // string (inferred)\nconst students = 2500000;           // number (inferred)\nconst isBeginner = true;            // boolean (inferred)\nlet maybe: string | null = null;    // union type: string OR null\n\n// ---------- 3. ARRAYS, TUPLES & LITERAL UNIONS ----------\nconst skills: string[] = [\"typing\", \"logic\", \"testing\"];\nconst scores: number[] = [98, 87, 91];\nconst pair: [string, number] = [\"Alice\", 92];     // tuple: fixed length + types\nlet difficulty: \"Easy\" | \"Medium\" | \"Hard\" = \"Easy\"; // literal union\n\n// ---------- 4. FUNCTIONS ----------\nfunction average(nums: number[]): number {\n  let total = 0;\n  for (const n of nums) {          // for...of loop\n    total += n;\n  }\n  return total / nums.length;\n}\n\nconst greet = (name: string, emoji = \"!\"): string =>\n  `Hello, ${name}${emoji}`;        // arrow fn + default param + template literal\n\n// ---------- 5. OBJECTS & INTERFACES ----------\ninterface Student {\n  name: string;\n  score: number;\n  passed: boolean;\n}\n\nconst alice: Student = { name: \"Alice\", score: 92, passed: true };\n\n// ---------- 6. CLASSES ----------\nclass Course {\n  title: string;\n  private lessons: number;\n  static platform = \"CodeFundamentals\";\n\n  constructor(title: string, lessons: number) {\n    this.title = title;\n    this.lessons = lessons;\n  }\n\n  summary(): string {\n    const status = this.lessons > 10 ? \"advanced\" : \"starter\"; // ternary\n    return `${Course.platform} - ${this.title} (${status})`;\n  }\n}\n\n// ---------- 7. CONTROL FLOW ----------\nfunction grade(score: number): string {\n  if (score >= 90) return \"A\";\n  else if (score >= 75) return \"B\";\n  else if (score >= 60) return \"C\";\n  else return \"Fail\";\n}\n\n// ---------- RUN EVERYTHING ----------\nconsole.log(\"=== TypeScript Fundamentals ===\");\nconsole.log(`${topic} (v${version}) - taught by ${teacher}`);\nconsole.log(\"Skills:\", skills.join(\", \"));\nconsole.log(\"Average score:\", average(scores));\nconsole.log(\"Grade for 88:\", grade(88));\nconsole.log(greet(\"Student\", \"!\"));\nconsole.log(`${alice.name} passed:`, alice.passed);\n\nswitch (difficulty) {              // switch statement\n  case \"Easy\":\n    console.log(\"Difficulty: perfect for beginners\");\n    break;\n  default:\n    console.log(\"Difficulty:\", difficulty);\n}\n\nconst course = new Course(\"TypeScript\", 12);\nconsole.log(course.summary());\n\nlet total = 0;\nfor (let i = 1; i <= 5; i++) {     // classic for loop\n  total += i;\n}\nconsole.log(\"Sum 1..5 =\", total);\n",
        },
        "quiz": [
            {
                "question": "What is TypeScript?",
                "options": ["A superset of JavaScript that adds static types", "A Python library for web apps", "A database query language", "A CSS framework"],
                "correct": 0,
            },
            {
                "question": "Which keyword declares a constant that cannot be reassigned?",
                "options": ["let", "const", "var", "static"],
                "correct": 1,
            },
            {
                "question": "What type does TypeScript infer for `let x = 5;`?",
                "options": ["string", "boolean", "number", "any"],
                "correct": 2,
            },
            {
                "question": "How do you declare an array that only holds numbers?",
                "options": ["let nums = numbers[]", "let nums: number[]", "let nums: int[]", "let nums: array<numbers>"],
                "correct": 1,
            },
            {
                "question": "Which syntax creates a union type?",
                "options": ["number & string", "number or string", "number | string", "number : string"],
                "correct": 2,
            },
            {
                "question": "What is a tuple in TypeScript?",
                "options": ["A function that never returns", "An array with a fixed length and a fixed type for each position", "A type that can hold any value", "A constant object"],
                "correct": 1,
            },
            {
                "question": "Which command runs a TypeScript file directly in Node.js 22+?",
                "options": ["node main.ts", "node --experimental-strip-types main.ts", "tsc main.ts", "npm run ts"],
                "correct": 1,
            },
            {
                "question": "What does an interface describe in TypeScript?",
                "options": ["The shape of an object", "How loops work", "A database table", "The browser's DOM"],
                "correct": 0,
            },
        ],
    },
    {
        "section": "Advanced Fundamentals",
        "id": 36,
        "minutes": 60,
        "title": "Angular",
        "icon": "bi-bezier2",
        "description": "Angular is one of the world's most popular frameworks for building large-scale web applications. Watch the official origin story documentary to learn how AngularJS was born inside Google, how a complete rewrite divided the community, and how the modern Angular framework rose again with TypeScript, components, and Ivy. After the video, download the essay activity and answer the questions.",
        "videos": {
            "general": [
                {"id": "cRC9DlH45lA", "channel": "CultRepo", "title": "Angular: The Documentary | An origin story", "duration": 60},
            ],
        },
        "key_points": [
            "AngularJS was created by Miško Hevery in 2009 as an internal Google experiment, initially brushed off by Gmail and Google Maps before becoming a JavaScript sensation.",
            "AngularJS made two-way data binding and dependency injection mainstream, which made building single-page applications dramatically easier.",
            "Angular 2 (released 2016) was a complete rewrite of AngularJS, not a version bump — the team decided a clean break was the only way forward.",
            "The rewrite split the community, but TypeScript — a superset of JavaScript with static types — became the foundation of modern Angular.",
            "Modern Angular is built around components, templates, dependency injection, and modules; components combine an HTML template with a class that controls it.",
            "Ivy is the modern Angular compiler and runtime: faster builds, smaller bundles, and better debugging.",
            "Signals are Angular's newer reactivity system, making state changes faster and more predictable.",
            "Angular is designed for large-scale, enterprise applications: strict structure, built-in router, forms, HTTP client, and tooling like the Angular CLI.",
            "The documentary highlights how open-source communities, internal pressure at Google, and years of iteration shaped the framework we use today.",
        ],
        "code": {
            "typescript": "// ==============================================\n// ANGULAR - A BASIC COMPONENT (app.component.ts)\n// Angular apps are built from components:\n// a class that controls a template.\n// ==============================================\n\nimport { Component } from '@angular/core';\n\n@Component({\n  selector: 'app-root',              // used as <app-root> in HTML\n  template: `\n    <h1>{{ title }}</h1>\n    <p>Count: {{ count }}</p>\n    <button (click)=\"increase()\">+1</button>\n    <button (click)=\"reset()\">Reset</button>\n  `,\n})\nexport class AppComponent {\n  title = 'My Angular App';          // data binding: {{ title }}\n  count = 0;\n\n  increase(): void {\n    this.count += 1;                 // event binding: (click)\n  }\n\n  reset(): void {\n    this.count = 0;\n  }\n}\n\n// Run with the Angular CLI:\n//   ng new my-app        -> create a new project\n//   cd my-app            -> go inside it\n//   ng serve             -> start the dev server\n//   ng generate component hello  -> generate a new component",
        },
        "activity": {
            "title": "Activity: Angular - An Origin Story",
            "docx": "Activity - Angular Origin Story.docx",
            "description": "Answer the essay questions based on the documentary and your own understanding of Angular. Download the document, type your answers, and submit it to your instructor.",
        },
        "quiz": [
            {
                "question": "Who created AngularJS?",
                "options": ["Brad Green", "Miško Hevery", "Guido van Rossum", "Addy Osmani"],
                "correct": 1,
            },
            {
                "question": "What happened when Angular 2 was released?",
                "options": ["It was a small update to AngularJS", "It was a complete rewrite of the framework", "It added Python support", "It renamed to TypeScript"],
                "correct": 1,
            },
            {
                "question": "Which language became the foundation of modern Angular?",
                "options": ["JavaScript", "Java", "TypeScript", "C#"],
                "correct": 2,
            },
            {
                "question": "What is a component in Angular?",
                "options": ["A database table", "A class combined with a template that controls part of the page", "A CSS file", "A type of loop"],
                "correct": 1,
            },
            {
                "question": "What is Ivy?",
                "options": ["A new version of AngularJS", "The modern Angular compiler and runtime", "A CSS framework", "A JavaScript library for animations"],
                "correct": 1,
            },
        ],
    },
    {
        "section": "Advanced Database System",
        "id": 11,
        "minutes": 35,
        "title": "Database Systems Overview",
        "icon": "bi-database",
        "description": "A database is an organized collection of related data, and a DBMS (Database Management System) is the software that stores, retrieves, and manages that data. In this lesson you will see why modern systems use the database approach instead of plain files.",
        "videos": [
            {"id": "wR0jg0eQsZA", "channel": "Lucid Software", "title": "Database Tutorial for Beginners"},
        ],
        "key_points": [
            "Data are raw facts; information is data that has been given meaning.",
            "A database is an organized collection of related data.",
            "A DBMS is software that stores, retrieves, updates, and secures data.",
            "Traditional file processing suffers from redundancy and inconsistency; the database approach solves them.",
            "SQL is the standard language for talking to relational DBMSs.",
        ],
        "code": {
            "sql": "-- A small taste of what a database can do\nCREATE TABLE students (\n    id INTEGER PRIMARY KEY,\n    name TEXT,\n    grade REAL\n);\n\nINSERT INTO students (name, grade) VALUES ('Alice', 92.5);\nINSERT INTO students (name, grade) VALUES ('Bob', 88.0);\n\nSELECT * FROM students;",
        },
        "quiz": [
            {
                "question": "What is a DBMS?",
                "options": ["A programming language", "Software that manages and stores data", "A type of computer network", "A spreadsheet"],
                "correct": 1,
            },
            {
                "question": "Which best describes data?",
                "options": ["Raw facts", "A formatted report", "A database", "Software"],
                "correct": 0,
            },
            {
                "question": "What is SQL?",
                "options": ["A web framework", "A hardware component", "The standard language for relational databases", "A file format"],
                "correct": 2,
            },
        ],
    },
    {
        "section": "Advanced Database System",
        "id": 12,
        "minutes": 40,
        "title": "Entity Relationship Model and Keys",
        "icon": "bi-diagram-3",
        "diagram": "erd-sample.svg",
        "diagram_caption": "Sample ERD: STUDENTS 1:N ENROLLMENTS N:1 COURSES. A student can enroll in many courses, and a course can be taken by many students. The ENROLLMENTS table holds the foreign keys that link both sides. Primary keys are underlined; foreign keys are marked FK.",
        "description": "Before writing SQL you design the database. The Entity Relationship (ER) model describes entities, attributes, and relationships, and keys make every row unique and link tables together.",
        "videos": [
            {"id": "xsg9BDiwiJE", "channel": "Lucid Software", "title": "Entity Relationship Diagram (ERD) Tutorial - Part 1"},
        ],
        "key_points": [
            "An entity is a thing stored in the database (student, course); an attribute is a property of it (name, age).",
            "A relationship connects entities, e.g. a student enrolls in a course.",
            "A primary key uniquely identifies every row of a table.",
            "A foreign key links a table to the primary key of another table.",
            "Referential integrity means a foreign key value must exist in the referenced table.",
        ],
        "code": {
            "sql": "CREATE TABLE students (\n    student_id INTEGER PRIMARY KEY,\n    name TEXT NOT NULL,\n    email TEXT UNIQUE\n);\n\nCREATE TABLE courses (\n    course_code TEXT PRIMARY KEY,\n    title TEXT NOT NULL\n);\n\nCREATE TABLE enrollments (\n    enrollment_id INTEGER PRIMARY KEY,\n    student_id INTEGER,\n    course_code TEXT,\n    FOREIGN KEY (student_id) REFERENCES students(student_id),\n    FOREIGN KEY (course_code) REFERENCES courses(course_code)\n);\n\nSELECT name FROM sqlite_master WHERE type = 'table';",
        },
        "quiz": [
            {
                "question": "What uniquely identifies every row of a table?",
                "options": ["Foreign key", "Primary key", "Index", "Attribute"],
                "correct": 1,
            },
            {
                "question": "Which key links two tables together?",
                "options": ["Foreign key", "Candidate key", "Composite key", "Alternate key"],
                "correct": 0,
            },
            {
                "question": "What does an attribute describe?",
                "options": ["A relationship between tables", "A property of an entity", "A query result", "A backup"],
                "correct": 1,
            },
        ],
    },
    {
        "section": "Advanced Database System",
        "id": 13,
        "minutes": 45,
        "title": "Normalization",
        "icon": "bi-layers",
        "description": "Normalization organizes tables to remove redundant data and prevent update problems. You will learn the first three normal forms (1NF, 2NF, 3NF), the most important ones for real database design.",
        "videos": [
            {"id": "GFQaEYEc8_8", "channel": "Decomplexify", "title": "Learn Database Normalization - 1NF, 2NF, 3NF, 4NF, 5NF"},
        ],
        "key_points": [
            "Normalization removes redundancy so the same fact is not stored in many places.",
            "1NF: every cell holds one value and there are no repeating groups.",
            "2NF: satisfies 1NF and has no partial dependency on part of a composite key.",
            "3NF: satisfies 2NF and has no transitive dependency through non-key attributes.",
            "Denormalization (merging tables on purpose) is sometimes done to speed up reads.",
        ],
        "diagram": "normalization-sample.svg",
        "diagram_title": "Normalization Sample Design: 1NF to 3NF",
        "diagram_caption": "One big ORDERS table is split step by step. 1NF removes repeating groups so every cell holds one value. 2NF removes partial dependencies by splitting order items into their own table. 3NF removes transitive dependencies by moving customer details into a separate CUSTOMERS table.",
        "code": {
            "sql": "-- Normalized design in 3NF\nCREATE TABLE students (\n    student_id INTEGER PRIMARY KEY,\n    name TEXT\n);\n\nCREATE TABLE courses (\n    course_id INTEGER PRIMARY KEY,\n    title TEXT\n);\n\nCREATE TABLE enrollments (\n    student_id INTEGER,\n    course_id INTEGER,\n    grade TEXT,\n    PRIMARY KEY (student_id, course_id),\n    FOREIGN KEY (student_id) REFERENCES students(student_id),\n    FOREIGN KEY (course_id) REFERENCES courses(course_id)\n);\n\nINSERT INTO students VALUES (1, 'Alice');\nINSERT INTO courses VALUES (101, 'Advanced Database Systems');\nINSERT INTO enrollments VALUES (1, 101, 'A');\n\nSELECT * FROM enrollments;",
        },
        "quiz": [
            {
                "question": "What problem does normalization fix?",
                "options": ["Slow internet", "Data redundancy and update problems", "Too many queries", "Table colors"],
                "correct": 1,
            },
            {
                "question": "Which normal form requires every cell to hold a single value?",
                "options": ["1NF", "2NF", "3NF", "None"],
                "correct": 0,
            },
            {
                "question": "3NF removes dependencies on which attributes?",
                "options": ["Primary key attributes", "Non-key attributes", "Foreign keys only", "Text attributes"],
                "correct": 1,
            },
        ],
    },
    {
        "section": "Advanced Database System",
        "id": 14,
        "minutes": 35,
        "title": "SQL Basics and DDL",
        "icon": "bi-table",
        "description": "SQL has several command groups. DDL (Data Definition Language) defines the structure of your database: creating, altering, and dropping tables, with proper data types for each column.",
        "videos": [
            {"id": "3Qbq61A_sNs", "channel": "Data with Baraa", "title": "SQL DDL Commands (Visually Explained) | CREATE, ALTER, DROP"},
        ],
        "key_points": [
            "DDL (Data Definition Language): CREATE, ALTER, DROP.",
            "DML (Data Modification Language): INSERT, UPDATE, DELETE.",
            "DQL (Data Query Language): SELECT.",
            "Common data types: INTEGER, TEXT, REAL, and DATE/TIME.",
            "DROP TABLE removes the table and all of its data permanently.",
        ],
        "code": {
            "sql": "CREATE TABLE students (\n    id INTEGER PRIMARY KEY,\n    name TEXT NOT NULL,\n    age INTEGER\n);\n\nALTER TABLE students ADD COLUMN email TEXT;\nALTER TABLE students DROP COLUMN age;\n\nINSERT INTO students (name, email) VALUES ('Alice', 'alice@example.com');\n\nSELECT * FROM students;\n\nDROP TABLE students;",
        },
        "quiz": [
            {
                "question": "Which command creates a new table?",
                "options": ["INSERT TABLE", "CREATE TABLE", "NEW TABLE", "MAKE TABLE"],
                "correct": 1,
            },
            {
                "question": "Which SQL category does SELECT belong to?",
                "options": ["DDL", "DML", "DQL", "TCL"],
                "correct": 2,
            },
            {
                "question": "What does ALTER TABLE do?",
                "options": ["Deletes the whole database", "Changes the structure of an existing table", "Renames the database", "Adds rows to a table"],
                "correct": 1,
            },
        ],
    },
    {
        "section": "Advanced Database System",
        "id": 15,
        "minutes": 35,
        "title": "Data Modification Language (DML)",
        "icon": "bi-pencil-square",
        "description": "DML changes the data inside tables. INSERT adds new rows, UPDATE changes existing rows, and DELETE removes rows. These are the CRUD operations behind almost every application.",
        "videos": [
            {"id": "ku3vMAP0h0s", "channel": "Data with Baraa", "title": "SQL DML Commands (Visually Explained) | INSERT, UPDATE, DELETE"},
        ],
        "key_points": [
            "INSERT adds one row or many rows at once.",
            "UPDATE modifies existing rows; the WHERE clause decides which ones.",
            "DELETE removes rows; without a WHERE clause it removes every row.",
            "Always double-check the WHERE clause before UPDATE or DELETE.",
            "After changes, run a SELECT to verify the data.",
        ],
        "code": {
            "sql": "CREATE TABLE students (\n    id INTEGER PRIMARY KEY,\n    name TEXT,\n    grade REAL\n);\n\nINSERT INTO students (name, grade) VALUES ('Alice', 85.0);\nINSERT INTO students (name, grade) VALUES ('Bob', 91.5);\nINSERT INTO students (name, grade) VALUES ('Cara', 78.0);\n\nUPDATE students SET grade = 92.0 WHERE name = 'Alice';\nDELETE FROM students WHERE name = 'Cara';\n\nSELECT * FROM students;",
        },
        "quiz": [
            {
                "question": "Which command adds a new row to a table?",
                "options": ["INSERT", "UPDATE", "DELETE", "ADD"],
                "correct": 0,
            },
            {
                "question": "What happens if DELETE has no WHERE clause?",
                "options": ["Nothing happens", "All rows are removed", "Only the first row is removed", "An error always appears"],
                "correct": 1,
            },
            {
                "question": "Which command changes existing rows?",
                "options": ["INSERT", "UPDATE", "DELETE", "SELECT"],
                "correct": 1,
            },
        ],
    },
    {
        "section": "Advanced Database System",
        "id": 16,
        "minutes": 40,
        "title": "Data Query Language (SELECT and Filtering)",
        "icon": "bi-search",
        "description": "SELECT is how you read data. You choose which columns to show, which rows to filter with WHERE, and how to sort with ORDER BY. Filtering uses comparison, logical, and pattern operators.",
        "videos": [
            {"id": "4Uv0o8IBqw0", "channel": "Becoming a Data Scientist", "title": "How to Filter with the WHERE clause in SQL"},
        ],
        "key_points": [
            "SELECT chooses columns; WHERE filters rows.",
            "Comparison operators: =, <>, <, >, <=, >=.",
            "IN checks a list, BETWEEN checks a range, LIKE matches patterns with % and _.",
            "AND, OR, NOT combine conditions into bigger filters.",
            "ORDER BY sorts results; LIMIT limits how many rows are returned.",
        ],
        "code": {
            "sql": "CREATE TABLE students (\n    id INTEGER PRIMARY KEY,\n    name TEXT,\n    age INTEGER,\n    course TEXT\n);\n\nINSERT INTO students (name, age, course) VALUES\n    ('Alice', 19, 'BSIT'),\n    ('Bob', 21, 'BSCS'),\n    ('Cara', 18, 'BSIT'),\n    ('Dan', 22, 'BSCS');\n\nSELECT name, age FROM students WHERE age >= 20;\nSELECT name FROM students WHERE course = 'BSIT' AND age < 20;\nSELECT name FROM students WHERE name LIKE 'A%';\nSELECT * FROM students ORDER BY age DESC LIMIT 2;",
        },
        "quiz": [
            {
                "question": "Which clause filters which rows are returned?",
                "options": ["SELECT", "WHERE", "FROM", "LIMIT"],
                "correct": 1,
            },
            {
                "question": "Which operator matches text patterns?",
                "options": ["LIKE", "IN", "BETWEEN", "="],
                "correct": 0,
            },
            {
                "question": "What does ORDER BY age DESC do?",
                "options": ["Sorts by name", "Sorts oldest to youngest", "Sorts youngest to oldest", "Removes duplicates"],
                "correct": 1,
            },
        ],
    },
    {
        "section": "Advanced Database System",
        "id": 17,
        "minutes": 45,
        "title": "SQL JOINs",
        "icon": "bi-link-45deg",
        "description": "Real databases split data across many tables, so you need JOIN to combine them. INNER JOIN returns only matching rows, while LEFT and RIGHT JOIN keep all rows from one side.",
        "videos": [
            {"id": "Yh4CrPHVBdE", "channel": "Anton Putra", "title": "6 SQL Joins you MUST know! (Animated + Practice)"},
        ],
        "key_points": [
            "INNER JOIN returns only rows that match in both tables.",
            "LEFT JOIN keeps every row of the left table even without a match.",
            "RIGHT JOIN keeps every row of the right table.",
            "You usually join on the foreign key that links the two tables.",
            "Forgetting the ON condition creates a Cartesian product (every pair of rows).",
        ],
        "code": {
            "sql": "CREATE TABLE students (\n    student_id INTEGER PRIMARY KEY,\n    name TEXT\n);\n\nCREATE TABLE enrollments (\n    enrollment_id INTEGER PRIMARY KEY,\n    student_id INTEGER,\n    course TEXT,\n    FOREIGN KEY (student_id) REFERENCES students(student_id)\n);\n\nINSERT INTO students VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Cara');\nINSERT INTO enrollments VALUES (10, 1, 'Databases'), (11, 2, 'Networking');\n\nSELECT students.name, enrollments.course\nFROM students\nINNER JOIN enrollments ON students.student_id = enrollments.student_id;\n\nSELECT students.name, enrollments.course\nFROM students\nLEFT JOIN enrollments ON students.student_id = enrollments.student_id;",
        },
        "quiz": [
            {
                "question": "Which join returns only the matching rows from both tables?",
                "options": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "CROSS JOIN"],
                "correct": 0,
            },
            {
                "question": "A LEFT JOIN keeps...",
                "options": ["Only matching rows", "All rows from the left table", "All rows from both tables", "No rows"],
                "correct": 1,
            },
            {
                "question": "What do you usually join two tables on?",
                "options": ["A random column", "The foreign key", "The first column", "The table name"],
                "correct": 1,
            },
        ],
    },
    {
        "section": "Advanced Database System",
        "id": 18,
        "minutes": 45,
        "title": "Subqueries, Aggregates, and Grouping",
        "icon": "bi-bar-chart",
        "description": "Aggregate functions summarize whole columns, GROUP BY groups rows for per-group totals, and HAVING filters those groups. Subqueries let you use the result of one query inside another.",
        "videos": [
            {"id": "GpC0XyiJPEo", "channel": "Becoming a Data Scientist", "title": "How to do Subqueries in SQL with Examples"},
            {"id": "nNrgRVIzeHg", "channel": "Becoming a Data Scientist", "title": "Advanced Aggregate Functions in SQL (GROUP BY, HAVING vs. WHERE)"},
        ],
        "key_points": [
            "Aggregates: COUNT, SUM, AVG, MIN, MAX.",
            "GROUP BY groups rows that share a value; HAVING filters the groups.",
            "A subquery is a SELECT nested inside another query.",
            "IN and EXISTS check a value against a subquery result.",
            "UNION combines the results of two queries into one list.",
        ],
        "code": {
            "sql": "CREATE TABLE scores (\n    student_id INTEGER,\n    name TEXT,\n    subject TEXT,\n    score INTEGER\n);\n\nINSERT INTO scores VALUES\n    (1, 'Alice', 'SQL', 92),\n    (1, 'Alice', 'ERD', 88),\n    (2, 'Bob', 'SQL', 85),\n    (2, 'Bob', 'ERD', 90),\n    (3, 'Cara', 'SQL', 78);\n\nSELECT COUNT(*) AS total_students FROM scores;\nSELECT AVG(score) AS average FROM scores;\nSELECT name, SUM(score) AS total FROM scores GROUP BY name;\nSELECT name FROM scores GROUP BY name HAVING AVG(score) > 85;\nSELECT name FROM scores WHERE subject = 'SQL' AND score > (\n    SELECT AVG(score) FROM scores WHERE subject = 'SQL'\n);",
        },
        "quiz": [
            {
                "question": "Which function counts the number of rows?",
                "options": ["SUM", "AVG", "COUNT", "MIN"],
                "correct": 2,
            },
            {
                "question": "Which clause filters groups after GROUP BY?",
                "options": ["WHERE", "HAVING", "ORDER BY", "LIMIT"],
                "correct": 1,
            },
            {
                "question": "A subquery is...",
                "options": ["A SELECT inside another query", "A backup copy", "A type of table", "A foreign key"],
                "correct": 0,
            },
        ],
    },
    {
        "section": "SQL Injection",
        "id": 19,
        "minutes": 45,
        "title": "Introduction to SQL Injection",
        "icon": "bi-shield-exclamation",
        "description": "SQL injection is one of the most dangerous web attacks: attackers insert malicious SQL into user input to steal, change, or delete database data. Learn how the attack works and how the right defense stops it.",
        "videos": [
            {"id": "wcaiKgQU6VE", "channel": "Hacksplaining", "title": "What Is SQL Injection?"},
        ],
        "key_points": [
            "SQL injection happens when user input is directly concatenated into a SQL query.",
            "The most common target is the login form: typing ' OR '1'='1 -- can bypass authentication.",
            "Because '1'='1' is always true, the injected condition makes the query return a valid user.",
            "Damages range from stolen data to deleted tables and full database takeover.",
            "The best defense is parameterized queries (prepared statements), never string concatenation.",
        ],
        "code": {
            "sql": "-- VULNERABLE: user input is pasted straight into the query\n-- Login form: username = ' OR '1'='1 --  and password = anything\n\nSELECT * FROM users WHERE username = '' OR '1'='1' -- ' AND password = 'x';\n\n-- Because '1'='1' is always true, the query returns the first user\n-- and the attacker logs in without knowing any password.",
            "python": "# VULNERABLE: input is concatenated into the query string\nusername = input(\"Username: \")\npassword = input(\"Password: \")\n\nquery = \"SELECT * FROM users WHERE username = '\" + username + \\\n        \"' AND password = '\" + password + \"'\"\n\n# Attacker types:  ' OR '1'='1 --\n# query becomes:\n# SELECT * FROM users WHERE username = '' OR '1'='1' -- ' AND password = 'x'\n# The comment -- hides the password check, and '1'='1' matches a user.",
        },
        "quiz": [
            {
                "question": "What is SQL injection?",
                "options": ["A way to speed up database queries", "Inserting malicious SQL into user input that the database executes", "A database backup technique", "A type of database index"],
                "correct": 1,
            },
            {
                "question": "Which input is a classic login-bypass payload?",
                "options": ["' OR '1'='1' --", "SELECT * FROM users", "WHERE id = 1", "ORDER BY name"],
                "correct": 0,
            },
            {
                "question": "What is the best defense against SQL injection?",
                "options": ["Longer passwords", "Parameterized queries", "More database tables", "Disabling the database"],
                "correct": 1,
            },
        ],
    },
    {
        "section": "SQL Injection",
        "id": 20,
        "minutes": 40,
        "title": "How SQL Injection Works",
        "icon": "bi-terminal",
        "description": "Understand injection points, how queries are built from user input, and why string concatenation lets attackers rewrite the SQL statement.",
        "videos": [
            {"id": "FwIUkAwKzG8", "channel": "Christian Linares", "title": "SQL Injection - Simply Explained"},
        ],
        "key_points": [
            "An injection point is any place where user input is placed directly into a SQL query.",
            "Classic injection points: login forms, search boxes, URL parameters (id=), and profile fields.",
            "String concatenation is the root cause: the program builds the query by pasting raw input into the SQL text.",
            "Because the DB cannot tell code from data, an injected quote can close the string and rewrite the rest of the query.",
            "The comment sequence -- hides everything after it, which lets attackers disable password checks.",
            "The fix is always parameterized queries: user input becomes data (a ? or %s placeholder), never part of the SQL text.",
        ],
        "code": {
            "sql": "-- VULNERABLE: the search box concatenates input\n-- Attacker types:  x' OR '1'='1 --\n\nSELECT * FROM products WHERE name LIKE '%x' OR '1'='1' --%';\n\n-- The OR '1'='1' is always true, and -- comments out the rest,\n-- so the query returns EVERY product. The attacker just filtered\n-- every row out of your database for free.",
            "python": "# VULNERABLE: raw input is pasted into the SQL string\nproduct = input(\"Search: \")            # attacker: x' OR '1'='1 --\n\nquery = \"SELECT * FROM products \" \\\n        \"WHERE name LIKE '%' + product + \"%'\"\n\n# The query suddenly becomes:\n# SELECT * FROM products WHERE name LIKE '%x' OR '1'='1' --%'\n# The OR makes the condition always true, so every row is returned.\n\n# SAFE VERSION: the input is bound as data, never merged into the SQL text.\n# (Python with SQLite uses a ? placeholder)\nquery_safe = \"SELECT * FROM products WHERE name LIKE ?\"\ncursor.execute(query_safe, (\"%\" + product + \"%\",))",
        },
        "quiz": [
            {
                "question": "What is an injection point?",
                "options": ["The server that hosts the database", "Any place where user input is placed directly into a SQL query", "The password hashing algorithm", "The network cable connecting the web server to the database"],
                "correct": 1,
            },
            {
                "question": "Which of these is a common injection point?",
                "options": ["A search box", "A login form", "A URL parameter like ?id=5", "All of the above"],
                "correct": 3,
            },
            {
                "question": "What does the -- sequence do in a SQL injection payload?",
                "options": ["Splits the query into two", "Comments out the rest of the query", "Errors on purpose", "Encrypts the input"],
                "correct": 1,
            },
            {
                "question": "What is the correct fix for string concatenation SQL queries?",
                "options": ["Replace single quotes with double quotes", "Add more WHERE conditions", "Use parameterized queries (prepared statements)", "Disable the search feature"],
                "correct": 2,
            },
        ],
    },
    {
        "section": "SQL Injection",
        "id": 21,
        "minutes": 40,
        "title": "Types of SQL Injection",
        "icon": "bi-diagram-3",
        "description": "Learn the three families of SQL injection: in-band (error-based and UNION), blind (boolean and time-based), and out-of-band attacks.",
        "key_points": [
            "In-band injection sends the attack and receives the result through the same channel: the web page itself.",
            "Error-based injection abuses database error messages that are printed to the page, which can reveal table names and structure.",
            "UNION-based injection adds a UNION SELECT to the original query so you can read data from other tables.",
            "Blind injection happens when the page shows no error or data: the attacker asks yes/no questions (boolean-based) or measures delays (time-based).",
            "Out-of-band injection uses a second channel such as DNS or HTTP to receive stolen data when no output path exists.",
            "The first step in any attack is detecting the injection point and learning how the query is built around your input.",
        ],
        "code": {
            "sql": "-- IN-BAND (UNION): the result is shown on the page\n-- Original query: SELECT name, price FROM products WHERE id = 1\n-- Payload in the id parameter:\n\n1 UNION SELECT username, password FROM users --\n\n-- The UNION merges the attacker's SELECT into the page's result set.\n\n-- BLIND (boolean-based): no output, so ask yes/no questions\n-- 1 AND 1=1   -> page behaves normally  (true)\n-- 1 AND 1=2   -> page looks different   (false)\n-- Each true/false answer reveals one bit of information.\n\n-- BLIND (time-based): when the page never changes visibly\n-- 1; IF(1=1, SLEEP(5), 0)   -> slow response = true\n-- 1; IF(1=2, SLEEP(5), 0)   -> fast response  = false",
            "python": "# IN-BAND attack against a vulnerable login (UNION data theft)\npayload = \"1 UNION SELECT username, password FROM users --\"\n\n# The vulnerable Python builds the query by pasting the input in:\nquery = \"SELECT name, price FROM products WHERE id = \" + payload\nprint(\"EXECUTED:\", query)\n\n# BLIND: the page never prints query results, so the attacker\n# guesses the admin password one character at a time:\n#  1 AND SUBSTRING((SELECT password FROM users LIMIT 1), 1, 1) = 'a'\n# The page either looks normal (true) or different (false).",
        },
        "quiz": [
            {
                "question": "Which type of SQL injection receives the stolen data directly on the same web page?",
                "options": ["Blind", "In-band", "Out-of-band", "Boolean-based"],
                "correct": 1,
            },
            {
                "question": "What does error-based SQL injection abuse?",
                "options": ["Database error messages printed to the page", "The website logo", "The database password file", "Browser cookies"],
                "correct": 0,
            },
            {
                "question": "A page shows no error and no stolen data, but responds faster or slower based on the payload. What is this?",
                "options": ["Error-based injection", "UNION-based injection", "Time-based blind injection", "Out-of-band injection"],
                "correct": 2,
            },
            {
                "question": "Which attack family sends stolen data through a second channel like DNS?",
                "options": ["In-band", "Blind", "Out-of-band", "UNION-based"],
                "correct": 2,
            },
        ],
    },
    {
        "section": "SQL Injection",
        "id": 22,
        "minutes": 45,
        "title": "UNION-Based SQL Injection",
        "icon": "bi-collection",
        "description": "Use UNION SELECT to pull data from other columns and tables, and learn how attackers count columns and find database versions.",
        "key_points": [
            "UNION merges the result set of two SELECTs: the original query plus your injected query.",
            "Two strict rules for UNION: both SELECTs must return the same number of columns, and the data types must be compatible.",
            "Attackers count columns by appending ORDER BY n -- and raising n until the query errors, or by UNION SELECT NULL,NULL,... and adding NULLs until it works.",
            "Once the column count matches, place strings in each column position to find which ones are shown on the page.",
            "The injected SELECT reads from other tables: UNION SELECT username, password FROM users -- is the classic data-theft payload.",
            "Different databases expose metadata differently: MySQL has information_schema, while SQLite uses sqlite_master.",
        ],
        "code": {
            "sql": "-- Step 1: find the number of columns (bump n until it errors)\n-- SELECT name, price FROM products WHERE id = 1 ORDER BY 1  -- ok\n-- SELECT name, price FROM products WHERE id = 1 ORDER BY 2  -- ok\n-- SELECT name, price FROM products WHERE id = 1 ORDER BY 3  -- error! 2 columns\n\n-- Step 2: UNION with the same column count, using NULLs as probes\n-- SELECT name, price FROM products WHERE id = 1 UNION SELECT NULL, NULL --\n\n-- Step 3: find a text column so data is displayed\n-- SELECT name, price FROM products WHERE id = 1 UNION SELECT username, 'x' FROM users --\n\n-- Step 4: steal the data\n-- SELECT name, price FROM products WHERE id = 1 UNION SELECT username, password FROM users --",
            "python": "# Attacker sends the payload in the id URL parameter:\nid_param = \"1 UNION SELECT username, password FROM users --\"\n\n# Vulnerable code pastes it straight into the query:\nquery = \"SELECT name, price FROM products WHERE id = \" + id_param\nprint(\"EXECUTED:\", query)\n\n# The UNION adds the users table rows to the result set.\n# The app only expects name + price, so it prints the password\n# wherever a price was expected - no extra code needed.",
        },
        "quiz": [
            {
                "question": "What two rules must a UNION SELECT payload follow?",
                "options": ["Same table name and same password", "Same number of columns and compatible data types", "Same column names and same row count", "Same database and same server"],
                "correct": 1,
            },
            {
                "question": "How do attackers find the number of columns in the original query?",
                "options": ["By adding ORDER BY n -- and raising n until it errors", "By deleting columns one by one", "By reading the source code", "By guessing the table name"],
                "correct": 0,
            },
            {
                "question": "Why are NULLs used as UNION probes at first?",
                "options": ["NULL is faster to type", "NULL matches any data type", "NULL makes the query valid SQL", "NULL is the only legal column"],
                "correct": 1,
            },
            {
                "question": "Which payload steals usernames and passwords?",
                "options": ["SELECT * FROM products", "1 UNION SELECT username, password FROM users --", "1; DROP TABLE users --", "admin'--"],
                "correct": 1,
            },
        ],
    },
    {
        "section": "SQL Injection",
        "id": 23,
        "minutes": 45,
        "title": "Blind SQL Injection",
        "icon": "bi-eye-slash",
        "description": "When errors are hidden, attackers ask yes/no questions with boolean conditions or measure delays with time-based payloads.",
        "key_points": [
            "Blind injection happens when the application shows no database errors and no stolen data.",
            "Boolean-based blind injection turns the page into a yes/no oracle: 1 AND 1=1 looks normal, 1 AND 1=2 looks different.",
            "Each true/false answer reveals one fact, so attackers extract data character by character with SUBSTRING and ASCII.",
            "Time-based blind injection uses SLEEP(5) or WAITFOR DELAY so a slow response means 'true' and a fast response means 'false'.",
            "A binary-search approach halves the guessing: instead of 26 letters, each character is found in about 5 true/false questions.",
            "Blind attacks are slower than in-band but just as dangerous — a tool like sqlmap automates the whole extraction.",
        ],
        "code": {
            "sql": "-- The page never prints results, only TRUE (normal) or FALSE (different)\n-- 1 AND 1=1        -> normal page   (TRUE)\n-- 1 AND 1=2        -> different     (FALSE)\n\n-- Extract the admin password's first character (guess letter by letter)\n-- 1 AND ASCII(SUBSTRING((SELECT password FROM users LIMIT 1),1,1)) = 97\n-- 1 AND ASCII(SUBSTRING((SELECT password FROM users LIMIT 1),1,1)) = 98\n-- ... keep guessing until the page behaves normally again.\n\n-- Time-based version when the page NEVER changes:\n-- 1; IF(ASCII(SUBSTRING((SELECT password FROM users LIMIT 1),1,1)) = 97, SLEEP(5), 0)\n-- Slow response = character is 'a'. Fast = wrong guess.",
            "python": "# Boolean blind: the request simply returns 'OK' or 'NOT FOUND'\nimport requests\n\nurl = \"http://target/page?id=\"\npassword = \"\"\nfor pos in range(1, 9):\n    for ascii_code in range(32, 127):\n        payload = f\"1 AND ASCII(SUBSTRING((SELECT password FROM users LIMIT 1),{pos},1))={ascii_code}\"\n        r = requests.get(url + payload)\n        if \"normal content\" in r.text:   # TRUE answer\n            password += chr(ascii_code)\n            break\nprint(\"Extracted password:\", password)",
        },
        "quiz": [
            {
                "question": "When is SQL injection considered 'blind'?",
                "options": ["When the attacker wears a blindfold", "When the page shows no database errors or stolen data", "When the database is encrypted", "When the password is hashed"],
                "correct": 1,
            },
            {
                "question": "What does boolean-based blind injection use as its signal?",
                "options": ["A visible error message", "The difference between true and false conditions in the page", "The database log file", "The HTTP status code alone"],
                "correct": 1,
            },
            {
                "question": "What does the SLEEP(5) in a time-based payload do?",
                "options": ["It pauses the database 5 seconds so a slow page means 'true'", "It encrypts the page", "It deletes the session", "It speeds up the query"],
                "correct": 0,
            },
            {
                "question": "Why is binary search useful in blind injection?",
                "options": ["It avoids triggering alarms", "It finds each character in about 5 yes/no questions instead of 26", "It makes the payload shorter", "It hides the attack from logs"],
                "correct": 1,
            },
        ],
    },
    {
        "section": "SQL Injection",
        "id": 24,
        "minutes": 40,
        "title": "SQL Injection in Real-World Queries",
        "icon": "bi-database",
        "description": "Injection does not only happen in SELECT: see how INSERT, UPDATE, DELETE, JOINs, and second-order injection are exploited.",
        "key_points": [
            "Any SQL statement that pastes user input in is injectable: SELECT, INSERT, UPDATE, DELETE, and even ORDER BY clauses.",
            "INSERT injection can add extra rows or values: ' , 'x')-- changes which columns receive the data.",
            "UPDATE injection can rewrite whole tables: setting every password or role to a value the attacker chooses.",
            "DELETE injection can wipe data, and stacking statements (; DROP TABLE users --) can destroy a schema when the driver allows it.",
            "Second-order injection stores a payload in the database first, then a later query pastes the stored value into SQL.",
            "JOINs multiply the risk: a payload in a WHERE clause can expose joined columns from unrelated tables.",
        ],
        "code": {
            "sql": "-- UPDATE injection: change every password to 'owned'\n-- Original:  UPDATE users SET password = '<input>' WHERE username = 'admin'\n-- Payload:   x', role='admin' WHERE '1'='1' --\n\n-- Becomes:  UPDATE users SET password = 'x', role='admin' WHERE '1'='1' --'\n--            WHERE username = 'admin'\n-- Every row gets password 'x' and role 'admin'.\n\n-- Stacked queries (only on some drivers): add a second statement\n-- 1; DROP TABLE users --\n\n-- Second-order injection:\n-- Step 1: register with username  admin'--   (stored, no error yet)\n-- Step 2: the app later runs  SELECT * FROM users WHERE username = 'admin'--'\n--         The stored quote breaks out and comments the rest.",
            "python": "# VULNERABLE UPDATE (string concatenation)\nnew_password = input(\"New password: \")  # attacker: x', role='admin' WHERE '1'='1' --\nquery = \"UPDATE users SET password = '\" + new_password + \"' WHERE username = 'admin'\"\nprint(\"EXECUTED:\", query)\n\n# SAFE: parameterized - input is data, never SQL text\nquery = \"UPDATE users SET password = ? WHERE username = ?\"\ncursor.execute(query, (new_password, \"admin\"))",
        },
        "quiz": [
            {
                "question": "Which of these SQL statements can be injectable?",
                "options": ["Only SELECT", "Only INSERT", "Only DELETE", "SELECT, INSERT, UPDATE, DELETE, and even ORDER BY"],
                "correct": 3,
            },
            {
                "question": "What is second-order SQL injection?",
                "options": ["Attacking a database a second time", "A payload stored in the database first, then executed by a later query", "Using two databases at once", "Encrypting the payload twice"],
                "correct": 1,
            },
            {
                "question": "What do stacked queries allow an attacker to do?",
                "options": ["Run multiple statements in one go, e.g. ; DROP TABLE users --", "Sort the results", "Join two tables", "Speed up the database"],
                "correct": 0,
            },
            {
                "question": "A user registers with the username admin'-- and it works. What is the danger?",
                "options": ["The username is too long", "The stored quote will break out of a later query (second-order attack)", "The username has special characters only", "Nothing - registration is harmless"],
                "correct": 1,
            },
        ],
    },
    {
        "section": "SQL Injection",
        "id": 25,
        "minutes": 45,
        "title": "Preventing SQL Injection: Parameterized Queries",
        "icon": "bi-shield-check",
        "description": "Prepared statements separate SQL code from data in Python, Java, and SQL so user input can never become executable SQL.",
        "key_points": [
            "A parameterized query (prepared statement) uses a placeholder like ? or %s; the input is sent as data, never merged into the SQL text.",
            "The database parses the statement once with the placeholder, then binds the value — so a quote in the input can never close the string.",
            "Even a payload like ' OR '1'='1' -- becomes an ordinary string when parameterized; it matches nothing and the attack fails.",
            "SQLite uses ? placeholders, Python's psycopg uses %s, and Java uses PreparedStatement with setString() and setInt().",
            "Parameterize every query that touches user input: SELECT, INSERT, UPDATE, DELETE, and stored procedure calls.",
            "Parameterization is not an excuse to skip validation — layer it with input validation and the principle of least privilege.",
        ],
        "code": {
            "sql": "-- VULNERABLE: input is pasted into the SQL text\n-- SELECT * FROM users WHERE username = '<input>' AND password = '<input>'\n\n-- SAFE: the same query with a placeholder\n-- SELECT * FROM users WHERE username = ? AND password = ?\n-- Values are bound separately, so ' OR '1'='1' -- stays plain data.\n\n-- Java (JDBC)\n-- PreparedStatement ps = conn.prepareStatement(\n--     \"SELECT * FROM users WHERE username = ? AND password = ?\");\n-- ps.setString(1, username);\n-- ps.setString(2, password);",
            "python": "# VULNERABLE\nusername = input(\"Username: \")\nquery = \"SELECT * FROM users WHERE username = '\" + username + \"'\"\n\n# SAFE - SQLite with a ? placeholder\ncursor.execute(\n    \"SELECT * FROM users WHERE username = ?\",\n    (username,),\n)\n\n# SAFE - PostgreSQL / psycopg with %s placeholder\ncursor.execute(\n    \"SELECT * FROM users WHERE username = %s\",\n    (username,),\n)",
        },
        "quiz": [
            {
                "question": "What does a parameterized query do with user input?",
                "options": ["It quotes it twice", "It treats it as data bound to a placeholder, never as SQL code", "It encrypts it before sending", "It blocks inputs with quotes"],
                "correct": 1,
            },
            {
                "question": "Why does ' OR '1'='1' -- fail against a prepared statement?",
                "options": ["The database blocks the OR keyword", "The payload is too long", "The quote is passed as part of one data value and cannot break the SQL", "Prepared statements only run SELECTs"],
                "correct": 2,
            },
            {
                "question": "Which is the Java way to write a parameterized query?",
                "options": ["Connection.query(\"SELECT * FROM users\")", "PreparedStatement with setString() and setInt()", "String.format with the input", "Runtime.exec with SQL"],
                "correct": 1,
            },
            {
                "question": "A safe SQLite query in Python uses which placeholder?",
                "options": ["%s", ":name", "?", "{0}"],
                "correct": 2,
            },
        ],
    },
    {
        "section": "SQL Injection",
        "id": 26,
        "minutes": 40,
        "title": "Defense in Depth",
        "icon": "bi-shield-lock",
        "description": "Input validation, output escaping, least privilege accounts, stored procedures, and web application firewalls layered together.",
        "key_points": [
            "No single control is perfect: real protection layers several defenses so one failure does not expose the database.",
            "Input validation (whitelists, type checks) rejects suspicious values before they reach a query — but never rely on it alone.",
            "Output escaping and encoding make stored payloads print as harmless text instead of executing.",
            "Least privilege: the app's database account should only be able to run the queries it needs, never DROP or admin actions.",
            "Stored procedures can still be injectable — parameterize inside them too.",
            "A Web Application Firewall (WAF) blocks known payloads, but attackers bypass signatures, so it is a net, not a wall.",
            "Secure the whole chain: HTTPS, updated frameworks, strong hashed passwords, error pages that leak nothing, and audit logs.",
        ],
        "code": {
            "sql": "-- Layered defenses for a login feature:\n\n-- Layer 1 (app): validate input before SQL\n-- if not re.match(r'^[A-Za-z0-9_]{3,20}$', username): reject\n\n-- Layer 2 (query): always parameterize\n-- SELECT * FROM users WHERE username = ? AND password = ?\n\n-- Layer 3 (database): least privilege account\n-- CREATE USER 'app_user' IDENTIFIED BY 'strong-password';\n-- GRANT SELECT, INSERT, UPDATE ON shop.* TO 'app_user';\n-- The app account cannot DROP or ALTER anything.\n\n-- Layer 4 (errors): never print DB exceptions to the page\n-- Layer 5 (edge): WAF rules block known injection payloads",
            "python": "# Layered defenses in the app layer\nimport re\n\nusername = input(\"Username: \")\n\n# Layer 1 - input validation (whitelist, reject payload characters)\nif not re.fullmatch(r\"[A-Za-z0-9_]+\", username):\n    raise ValueError(\"Invalid username\")\n\n# Layer 2 - parameterized query (the real defense)\nrow = cursor.execute(\n    \"SELECT * FROM users WHERE username = ?\", (username,)\n).fetchone()\n\n# Layer 3 - the database account has only the grants it needs",
        },
        "quiz": [
            {
                "question": "What is the core idea of defense in depth?",
                "options": ["Use the strongest single password", "Layer multiple defenses so one failure does not expose the data", "Hide the database server IP", "Disable all error messages"],
                "correct": 1,
            },
            {
                "question": "What does the principle of least privilege require?",
                "options": ["The app account can run only the queries it needs", "Admins get the strongest passwords", "Users can see the schema", "Queries run with root privileges"],
                "correct": 0,
            },
            {
                "question": "Why is a WAF alone not enough?",
                "options": ["WAFs are always offline", "Attackers can craft payloads that bypass signatures", "WAFs slow the site too much", "WAFs only protect SELECTs"],
                "correct": 1,
            },
            {
                "question": "A stored procedure call is always safe. True or false?",
                "options": ["True - procedures are compiled", "False - a procedure can still be injectable if it concatenates input", "True - procedures reject quotes", "False - procedures run on a separate server"],
                "correct": 1,
            },
        ],
    },
    {
        "section": "SQL Injection",
        "id": 27,
        "minutes": 40,
        "title": "SQL Injection Testing and Detection",
        "icon": "bi-search",
        "description": "How to test applications safely with manual payloads and tools, and how to spot vulnerable code during code review.",
        "key_points": [
            "The manual test starts simple: inject a single quote ' and watch for an error, then compare AND 1=1 with AND 1=2.",
            "Always test against a copy of the database first — never run destructive payloads against production data.",
            "Fuzz common injection points: search boxes, logins, URL parameters, headers, and cookies.",
            "Automated tools like sqlmap, Burp Suite, and OWASP ZAP probe many payloads quickly, but results still need manual review.",
            "SAST (static analysis) scans source code for dangerous string concatenation in queries; DAST tests the running app from outside.",
            "During code review, search for query strings built with + or % and user input, and for .format or f-strings inside SQL.",
            "A safe test bed: parameterize, use a dedicated test database, and get written permission before testing any system.",
        ],
        "code": {
            "sql": "-- Manual testing checklist on a safe test database:\n\n-- 1. Single quote probe: does the page error?\n--     id=1'          -> error? suspicious!\n\n-- 2. Always-true vs always-false comparison:\n--     id=1 AND 1=1   -> normal page\n--     id=1 AND 1=2   -> different page?  boolean-based blind!\n\n-- 3. Comment probe: does -- change the behavior?\n--     id=1--         -> works normally? input may be injectable\n\n-- 4. Column count (UNION prep):\n--     id=1 ORDER BY 10 --   -> error when n exceeds columns\n\n-- 5. Time probe (safe, no data damage):\n--     id=1; IF(1=1, SLEEP(3), 0)   -> slow? time-based blind!",
            "python": "# Code-review red flags - the exact patterns to search for:\n\n# BAD: string concatenation with user input\nquery = \"SELECT * FROM users WHERE id = \" + request.args.get(\"id\")\n\n# BAD: f-strings or .format() inside SQL\nquery = f\"SELECT * FROM users WHERE name = '{name}'\"\n\n# BAD: % formatting with user input\nquery = \"SELECT * FROM users WHERE name = '%s'\" % user_input\n\n# GOOD: parameterized - input stays data\nquery = \"SELECT * FROM users WHERE id = ?\"\ncursor.execute(query, (user_id,))",
        },
        "quiz": [
            {
                "question": "What is the first manual probe in a SQL injection test?",
                "options": ["A DROP TABLE statement", "A single quote ' to see if the page errors", "A UNION with 50 columns", "A parameterized query"],
                "correct": 1,
            },
            {
                "question": "Where should destructive injection tests be run?",
                "options": ["On the production database", "On a copy of the database", "On your own laptop only", "On the database of the web host"],
                "correct": 1,
            },
            {
                "question": "Which of these is a code-review red flag?",
                "options": ["cursor.execute(query, (user_id,))", "query = f\"SELECT * FROM users WHERE id = {id}\"", "CREATE TABLE users (id INT)", "SELECT * FROM users ORDER BY id"],
                "correct": 1,
            },
            {
                "question": "What does sqlmap do?",
                "options": ["It creates SQL tables", "It automates probing and exploiting SQL injection", "It encrypts the database", "It parameterizes all queries automatically"],
                "correct": 1,
            },
        ],
    },
    {
        "section": "SQL Injection",
        "id": 28,
        "minutes": 45,
        "title": "Real-World Attack Scenarios",
        "icon": "bi-exclamation-triangle",
        "description": "Famous real-world breaches caused by SQL injection and the lessons they teach about securing database-driven applications.",
        "key_points": [
            "In 2008, Heartland Payment Systems was breached through SQL injection, exposing over 130 million credit cards — one of the largest data breaches in history.",
            "In 2011, attackers used SQL injection on a Sony subsidiary to steal millions of user accounts and even delete entire databases.",
            "In 2015, TalkTalk suffered a SQL injection attack on its website that leaked the personal details of over 150,000 customers.",
            "In 2016, the Adult FriendFinder breach exposed over 400 million accounts, largely through a SQL injection flaw.",
            "The common thread is the same: user input concatenated into SQL queries, combined with weak passwords and unpatched software.",
            "The lessons: parameterize every query, keep software patched, encrypt and hash stored data, and limit database privileges.",
            "Regulations now punish this: GDPR and other laws impose heavy fines on companies that fail to protect customer data.",
        ],
        "code": {
            "sql": "-- The vulnerable pattern behind most historic breaches:\n\n-- VULNERABLE (the pattern from the 2008-2016 era breaches)\n-- SELECT * FROM accounts WHERE username = '<input>' AND password = '<input>'\n\n-- A single login form using string concatenation was enough.\n\n-- The modern, mandatory replacement:\n-- SELECT * FROM accounts WHERE username = ? AND password = ?\n\n-- Plus: hashed passwords (never plain text), least privilege,\n-- patched servers, and a tested incident-response plan.",
            "python": "# The historical vulnerable login (concatenation) vs the fix\n\n# VULNERABLE - this exact pattern powered the big breaches\nusername = input(\"Username: \")\npassword = input(\"Password: \")\nquery = (\n    \"SELECT * FROM accounts WHERE username = '\" + username\n    + \"' AND password = '\" + password + \"'\"\n)\n\n# FIXED - parameterized and hashed\nquery = \"SELECT * FROM accounts WHERE username = ? AND password_hash = ?\"\ncursor.execute(query, (username, hash_password(password)))",
        },
        "quiz": [
            {
                "question": "Which 2008 breach exposed over 130 million credit cards via SQL injection?",
                "options": ["Sony", "TalkTalk", "Heartland Payment Systems", "Equifax"],
                "correct": 2,
            },
            {
                "question": "What was the common vulnerability across the historic SQL injection breaches?",
                "options": ["Weak Wi-Fi passwords", "User input concatenated straight into SQL queries", "Faulty hard drives", "Too many database tables"],
                "correct": 1,
            },
            {
                "question": "Besides parameterized queries, what should companies do?",
                "options": ["Hash stored passwords and limit database privileges", "Delete their databases", "Use only HTTPS", "Turn off error pages"],
                "correct": 0,
            },
            {
                "question": "Why do modern laws like GDPR matter for security?",
                "options": ["They require faster internet", "They impose heavy fines for failing to protect customer data", "They ban SQL entirely", "They force companies to publish code"],
                "correct": 1,
            },
        ],
    },
    {
        "section": "Fundamentals",
        "id": 37,
        "minutes": 30,
        "title": "Flowcharts",
        "icon": "bi-diagram-3",
        "description": "A flowchart is a diagram that shows the steps of a process or algorithm using standard shapes. Before writing code, drawing a flowchart helps you plan the logic clearly and catch mistakes early. In this lesson you will learn the common flowchart symbols and how to read and draw a flowchart, then build your own in the interactive Flowchart Builder.",
        "key_points": [
            "An oval (terminator) shows the Start or End of a flowchart.",
            "A rectangle (process) shows a single action or calculation, like x = x + 1.",
            "A diamond (decision) shows a yes/no question; it has two exits (usually Yes and No).",
            "A parallelogram (input/output) shows reading input or printing output.",
            "Arrows show the flow of control from one step to the next.",
            "Draw the flowchart first, then translate each shape into code.",
        ],
        "code": {
            "python": "# Flowchart for: is a number even?\n# (parallelogram: input n)\n# (diamond: n % 2 == 0 ?)\n#   Yes -> rectangle: print 'Even'\n#   No  -> rectangle: print 'Odd'\n\nn = int(input('Enter a number: '))\nif n % 2 == 0:\n    print('Even')\nelse:\n    print('Odd')",
            "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int n;\n    cout << \"Enter a number: \";   // parallelogram: output\n    cin >> n;                      // parallelogram: input\n    if (n % 2 == 0) {              // diamond: decision\n        cout << \"Even\";            // rectangle: process\n    } else {\n        cout << \"Odd\";\n    }\n    return 0;\n}",
            "java": "import java.util.Scanner;\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        System.out.print(\"Enter a number: \");  // parallelogram: output\n        int n = sc.nextInt();                   // parallelogram: input\n        if (n % 2 == 0) {                      // diamond: decision\n            System.out.println(\"Even\");         // rectangle: process\n        } else {\n            System.out.println(\"Odd\");\n        }\n    }\n}",
            "c": "#include <stdio.h>\n\nint main() {\n    int n;\n    printf(\"Enter a number: \");   // parallelogram: output\n    scanf(\"%d\", &n);               // parallelogram: input\n    if (n % 2 == 0) {              // diamond: decision\n        printf(\"Even\");            // rectangle: process\n    } else {\n        printf(\"Odd\");\n    }\n    return 0;\n}",
        },
        "quiz": [
            {
                "question": "Which shape shows the Start or End of a flowchart?",
                "options": ["Rectangle", "Oval (terminator)", "Diamond", "Parallelogram"],
                "correct": 1,
            },
            {
                "question": "A diamond is used for a ...",
                "options": ["Process step", "Input/output", "Decision (yes/no question)", "Start point"],
                "correct": 2,
            },
            {
                "question": "What do the arrows in a flowchart represent?",
                "options": ["Time", "Flow of control", "Memory", "Code comments"],
                "correct": 1,
            },
            {
                "question": "Which shape is used for input or output?",
                "options": ["Parallelogram", "Oval", "Rectangle", "Hexagon"],
                "correct": 0,
            },
            {
                "question": "Why should you draw a flowchart before coding?",
                "options": ["It makes the program run faster", "It helps plan logic and catch mistakes early", "It replaces the need for a language", "It is required by the compiler"],
                "correct": 1,
            },
        ],
        "builder": "flowchart",
    },
]

LONG_QUIZZES = {
    "Fundamentals": [
        {
            "question": "Which language is interpreted line by line?",
            "options": ["Python", "C++", "Java", "Assembly"],
            "correct": 0,
        },
        {
            "question": "What does a compiler do?",
            "options": ["Runs code line by line", "Translates the whole source code into machine code before running", "Formats the code", "Debugs the code"],
            "correct": 1,
        },
        {
            "question": "In Python, what is the type of 3.14?",
            "options": ["int", "double", "float", "decimal"],
            "correct": 2,
        },
        {
            "question": "In C++ and Java, what must you write before a variable name?",
            "options": ["A semicolon", "The data type", "A print statement", "The main method"],
            "correct": 1,
        },
        {
            "question": "What does int(input()) do in Python?",
            "options": ["Reads text and converts it to an integer", "Prints an integer", "Creates an integer variable", "Converts an integer to text"],
            "correct": 0,
        },
        {
            "question": "Which operator gives the remainder of a division?",
            "options": ["/", "//", "%", "&"],
            "correct": 2,
        },
        {
            "question": "In Java, int x = 10 / 3; stores what value in x?",
            "options": ["3.33", "4", "3", "0"],
            "correct": 2,
        },
        {
            "question": "What is the C++/Java equivalent of the Python keyword and?",
            "options": ["&", "||", "&&", "!"],
            "correct": 2,
        },
        {
            "question": "What is the result of true and false?",
            "options": ["true", "false", "error", "0"],
            "correct": 1,
        },
        {
            "question": "Which keyword does Python use for \"else if\"?",
            "options": ["elseif", "elif", "else if", "elsif"],
            "correct": 1,
        },
        {
            "question": "If a condition is false and there is an else block, what happens?",
            "options": ["The program crashes", "Nothing runs", "The else block runs", "The if block runs"],
            "correct": 2,
        },
        {
            "question": "In Python, what values does range(1, 6) produce?",
            "options": ["1, 2, 3, 4, 5, 6", "1, 2, 3, 4, 5", "0, 1, 2, 3, 4", "2, 3, 4, 5, 6"],
            "correct": 1,
        },
        {
            "question": "Which loop repeats while a condition is true?",
            "options": ["for loop", "while loop", "do loop", "repeat loop"],
            "correct": 1,
        },
        {
            "question": "What does return do inside a function?",
            "options": ["Stops the program", "Sends a value back to the caller", "Prints a value", "Repeats the function"],
            "correct": 1,
        },
        {
            "question": "What is the index of the first element in an array or list?",
            "options": ["1", "0", "-1", "2"],
            "correct": 1,
        },
    ],
    "Advanced Database System": [
        {
            "question": "What is a DBMS?",
            "options": ["A programming language", "Software that manages and stores data", "A type of network", "A spreadsheet"],
            "correct": 1,
        },
        {
            "question": "Which best describes data?",
            "options": ["Raw facts", "A formatted report", "A database", "Software"],
            "correct": 0,
        },
        {
            "question": "What uniquely identifies every row of a table?",
            "options": ["Foreign key", "Primary key", "Index", "Attribute"],
            "correct": 1,
        },
        {
            "question": "What is the purpose of a foreign key?",
            "options": ["To sort rows", "To link a table to another table's primary key", "To speed up backups", "To delete data"],
            "correct": 1,
        },
        {
            "question": "Which normal form requires every cell to hold a single value?",
            "options": ["1NF", "2NF", "3NF", "BCNF"],
            "correct": 0,
        },
        {
            "question": "What problem does normalization fix?",
            "options": ["Slow internet", "Data redundancy and update problems", "Too many queries", "Table colors"],
            "correct": 1,
        },
        {
            "question": "Which of these is a DDL command?",
            "options": ["SELECT", "CREATE TABLE", "INSERT", "UPDATE"],
            "correct": 1,
        },
        {
            "question": "What does ALTER TABLE do?",
            "options": ["Deletes the whole database", "Changes the structure of an existing table", "Renames the database", "Adds rows"],
            "correct": 1,
        },
        {
            "question": "Which command adds a new row to a table?",
            "options": ["INSERT", "UPDATE", "DELETE", "SELECT"],
            "correct": 0,
        },
        {
            "question": "What happens if DELETE has no WHERE clause?",
            "options": ["Nothing happens", "All rows are removed", "Only the first row is removed", "An error appears"],
            "correct": 1,
        },
        {
            "question": "Which clause filters which rows are returned?",
            "options": ["SELECT", "WHERE", "FROM", "ORDER BY"],
            "correct": 1,
        },
        {
            "question": "Which query returns names that start with A?",
            "options": ["WHERE name = 'A'", "WHERE name LIKE 'A%'", "WHERE name IN 'A'", "WHERE name > 'A'"],
            "correct": 1,
        },
        {
            "question": "Which join returns only the matching rows from both tables?",
            "options": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "CROSS JOIN"],
            "correct": 0,
        },
        {
            "question": "A LEFT JOIN keeps...",
            "options": ["Only matching rows", "All rows from the left table", "All rows from both tables", "No rows"],
            "correct": 1,
        },
        {
            "question": "Which clause filters groups after GROUP BY?",
            "options": ["WHERE", "HAVING", "ORDER BY", "LIMIT"],
            "correct": 1,
        },
    ],
    "SQL Injection": [
        {
            "question": "What is SQL injection?",
            "options": ["A way to speed up queries", "An attack that runs your SQL statements inside the app's query", "A backup technique", "A type of firewall"],
            "correct": 1,
        },
        {
            "question": "How does the web app normally build a query?",
            "options": ["It concatenates the user's input directly into the SQL string", "It only uses stored procedures", "It encodes every query in binary", "It never touches the database"],
            "correct": 0,
        },
        {
            "question": "What does the comment -- do in an injected payload?",
            "options": ["Deletes the table", "Comments out the rest of the original query", "Encrypts the input", "Sorts the results"],
            "correct": 1,
        },
        {
            "question": "Which payload commonly bypasses a login?",
            "options": ["' OR '1'='1 --", "DROP TABLE users", "SELECT @@version", "1=2"],
            "correct": 0,
        },
        {
            "question": "Why can a stacked-query 'OR 1=1' row dump be dangerous in SELECT?",
            "options": ["It prints a syntax error", "It can return every row, exposing all accounts", "It locks the table", "It has no effect"],
            "correct": 1,
        },
        {
            "question": "What does a UNION-based attack do?",
            "options": ["Joins two tables", "Combines the results of the injected SELECT with the original query", "Drops a database", "Adds a column"],
            "correct": 1,
        },
        {
            "question": "Which statement runs a second query in the same connection?",
            "options": ["UNION SELECT", "DROP", "SLEEP", "ORDER BY"],
            "correct": 0,
        },
        {
            "question": "What does a blind SQL injection rely on?",
            "options": ["Error messages", "True/false or time-based answers to questions about the database", "UNION columns", "Direct output of rows"],
            "correct": 1,
        },
        {
            "question": "In boolean-based blind injection, what changes between a TRUE and FALSE probe?",
            "options": ["The database password", "The page content", "The server IP", "Nothing"],
            "correct": 1,
        },
        {
            "question": "In a time-based blind attack, what is the marker?",
            "options": ["A login success", "A delay in the response", "An error code", "A redirect"],
            "correct": 1,
        },
        {
            "question": "Which is the real fix for SQL injection?",
            "options": ["Filtering out the word SELECT", "Parameterized queries", "Disabling error pages", "Using GET instead of POST"],
            "correct": 1,
        },
        {
            "question": "Which parameterized query is correct?",
            "options": ["SELECT * FROM users WHERE id = ? with (id,) as a parameter", "SELECT * FROM users WHERE id = $id with string concat", "SELECT * FROM users WHERE id = '?'", "SELECT * FROM users WHERE id = ? with ? as a raw string"],
            "correct": 0,
        },
        {
            "question": "Which is a defense-in-depth layer?",
            "options": ["Input validation", "Least privilege", "Logging and monitoring", "All of the above"],
            "correct": 3,
        },
        {
            "question": "What is the principle of least privilege?",
            "options": ["Everyone gets admin access", "The database account can run only the queries it needs", "Passwords are short", "Queries run as root"],
            "correct": 1,
        },
        {
            "question": "What is the safest way to test for SQL injection?",
            "options": ["On the production database with DROP payloads", "On a copy of the database with harmless payloads and permission", "On a random website", "Only with automated tools and no review"],
            "correct": 1,
        },
    ],
}
