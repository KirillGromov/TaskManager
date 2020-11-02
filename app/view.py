from app import app
from flask import render_template, flash, request, url_for, redirect, session
#from dbmodels import connection, insert_user
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from passlib.hash import sha256_crypt
from dbmodels import db
import gc
import log
#from models import RegistrationForm


@app.route("/")
def index():
    return render_template("index.html")

# registration form

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method =='POST':
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm = request.form.get("confirm")
        secure_password = sha256_crypt.encrypt(str(password))

        if password == confirm:
            db.execute("INSERT INTO user(name, email, password) VALUES(:name,:email,:password)",
                        {"name":name,"email":email,"password": secure_password})
            db.commit()
            return redirect(url_for('login'))
        else:
            flash("password does not match", "danger")
            return render_template('registration.html.')

    return render_template('registration.html')

# login form

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")

        namedata = db.execute("SELECT name FROM user WHERE name=name",{"name":name}).fetchone()
        passworddata = db.execute("SELECT password FROM user WHERE password=password",{"password":password}).fetchone()

        if namedata is None:
            flash("No name", "danger")
            return render_template("login.html")
        else:
            for password_data in passworddata:
                if sha256_crypt.verify(password, password_data):
                    session["log"] = True
                    flash("You are now login", "success")
                    return redirect(url_for('tasks.index'))
                else:
                    flash("incorrect password", "danger")
                    return render_template("login.html")
    
    return render_template('login.html')

#logout
@app.route("/logout")
def logout():
    session.clear()
    flash("You are logout", "success")
    return redirect(url_for("login"))