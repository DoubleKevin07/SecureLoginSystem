import os
import json
from flask import Flask, session, render_template, request, redirect, url_for
import hashlib, binascii # For pw encrpytion
from models import *

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "<DATABASE KEY HERE>"
db.init_app(app)



# This creates spots in the data base if they don't exist.
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template("home.html")

# Account stuff
@app.route("/account")
def account():
    # If we don't have a user id stored in our cookie ...
    if "userid" not in session:
        # ... make them log in!
        return redirect(url_for("login"))
    # Othewrise, if we do ...
    else:
        # ... take them to their profile!
        return redirect(url_for("profile"))

# Profile page
@app.route("/profile")
def profile():
    # Same thing here. If we don't have a user id stored in our cookie ...
    if "userid" not in session:
        # ... return them to the login screen!
        return redirect(url_for("login"))
    # Otherwise ...
    else:
        # ... display the profile!
        id = session["userid"]
        user = Account.get_user_by_id(id)
        return render_template("profile.html", user=user)

# Signup page.
@app.route("/signup")
def signup():
    return render_template("signup.html")

# Login page.
@app.route("/login")
def login():
    return render_template("login.html")

# Logout page.
@app.route("/logout")
def logout():
    session.pop("userid", None)
    return redirect(url_for("login"))

# This is the page we use for attempting to log in. I called it "Gate" because it's like you're trying to enter.
@app.route("/gate", methods=["POST"])
def gate():

    # Gets the user's input data.
    username = request.form.get("name")
    pw = request.form.get("password")

    # Attempts to find the account associated with the username.
    user = Account.get_user(username)

    # If there is no user ...
    if(not user): 
        # ... return the error page, with a generic error message.
        # The reason the message is generic is, we don't want people to know specifically what error they made, 
        # because that would give an attack more data.
        return render_template("error.html", message="ERROR: Invalid username or password!")

    # Hash the password the user entered.
    salt = user.salt
    attempt_hash = binascii.hexlify(hashlib.pbkdf2_hmac('sha256', pw.encode(), salt, 100000)).decode("utf-8")

    # Check for login success.

    # If the password re-hashed is the same as the hash in the account database ...
    if(attempt_hash == user.pw_hash):

        # ... then we're successful!
        session["userid"] = user.id
        return redirect(url_for("profile")) 

    # Otherwise ...
    else: 
        # Return generic error, like before.
        return render_template("error.html", message="ERROR: Invalid username or password!")

# This is the page for creating an account.
@app.route("/create_account", methods=["POST"])
def create_account():

    # Get user input.
    username = request.form.get("name")
    pw = request.form.get("password")
    pwc = request.form.get("confirm-password")

    # Password confirmation.
    if(pw != pwc):
        return render_template("error.html", message="ERROR: Confirmed password does not match!")
    
    # See if the account already exists.
    if(Account.get_user(username)):
        print("returned from does_account_exist()");
        return render_template("error.html", message="ERROR: Account already exists! Please choose a different username.")

    # Otherwise create a new account.
    # https://docs.python.org/2/library/hashlib.html

    # Compute salt
    # Salts are nice because they make sure two accounts with the same password have unique password hashes.
    salt = os.urandom(16)

    # Compute hash
    dk = hashlib.pbkdf2_hmac('sha256', pw.encode(), salt, 100000)
    pw_hash = binascii.hexlify(dk).decode("utf-8")

    # Add account to database.
    user = Account(username, pw_hash, salt)
    db.session.add(user)
    db.session.commit()

    return render_template("error.html", message="Not actually an error, this means it worked!")


