import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database
        # Validate submission
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")


        # Rememeber registrat
        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)

        # Confirm registration
        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        # Query for all birthdays
        birthdays = db.execute("SELECT * FROM birthdays")

        return render_template("index.html", birthdays=birthdays)





"""
TODO
1. In application.py, query for all birthdays and pass that data to index. html
2. In index. html, render each birthday aS a rowW in the table
3. In index.html, add a form to let users add a new birthday
4. In application.py, when the form submission Sreceived, insert the birthday into the database
"""