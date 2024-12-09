from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock user data
users = {"zira": {"password": "password123", "tasks": []}}

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username]["password"] == password:
            session["user"] = username
            return redirect(url_for("dashboard"))
        return "Invalid Credentials!"
    return render_template("login.html")

# Dashboard
@app.route("/dashboard")
def dashboard():
    if "user" in session:
        user = session["user"]
        tasks = users[user]["tasks"]
        return render_template("dashboard.html", user=user, tasks=tasks)
    return redirect(url_for("login"))

# Add Task
@app.route("/add_task", methods=["POST"])
def add_task():
    if "user" in session:
        task = request.form["task"]
        user = session["user"]
        users[user]["tasks"].append({"task": task, "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

# Logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
