from flask import Flask, render_template, request
import re

app = Flask(__name__)

COMMON_PASSWORDS = [
    "password", "admin", "123456", "qwerty",
    "welcome", "letmein", "iloveyou", "password123"
]

def estimate_crack_time(password):
    pool = 0
    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(c in "!@#$%^&*()_+=-" for c in password):
        pool += 10

    if pool == 0:
        return 0

    combinations = pool ** len(password)
    guesses_per_second = 1_000_000_000
    return combinations / guesses_per_second


def format_time(seconds):
    if seconds < 60:
        return f"{seconds:.1f} seconds"
    elif seconds < 3600:
        return f"{seconds/60:.1f} minutes"
    elif seconds < 86400:
        return f"{seconds/3600:.1f} hours"
    elif seconds < 31536000:
        return f"{seconds/86400:.1f} days"
    else:
        return f"{seconds/31536000:.1f} years"


def password_strength(pw):
    if pw.lower() in COMMON_PASSWORDS:
        return "VERY WEAK", 0, ["Common password found in leaked databases"]

    score = 0
    tips = []

    checks = [
        (len(pw) >= 8, "Use at least 8 characters"),
        (re.search(r"[A-Z]", pw), "Add an uppercase letter"),
        (re.search(r"[a-z]", pw), "Add a lowercase letter"),
        (re.search(r"[0-9]", pw), "Add a number"),
        (re.search(r"[!@#$%^&*()_+=-]", pw), "Add a special character")
    ]

    for passed, tip in checks:
        if passed:
            score += 1
        else:
            tips.append(tip)

    percentage = (score / 5) * 100
    strength = "WEAK" if score <= 2 else "MEDIUM" if score <= 4 else "STRONG"

    return strength, percentage, tips


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        password = request.form["password"]

        strength, percent, tips = password_strength(password)
        crack_time = format_time(estimate_crack_time(password))

        result = {
            "strength": strength,
            "percent": percent,
            "tips": tips,
            "crack_time": crack_time
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

