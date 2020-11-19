from app import app
from flask import render_template, flash, request, url_for, redirect, session
#from dbmodels import connection, insert_user
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from passlib.hash import sha256_crypt
from dbmodels import login_password, login_username, db, reg_user, delete_task, select_tasks
import log
from flask import jsonify


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
            reg_user(name, email, secure_password)
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
        namedata = login_username(name)
        passworddata = login_password(password)

        if namedata is None:
            flash("No name", "danger")
            return render_template("login.html")
        else:
            for password_data in passworddata:
                if sha256_crypt.verify(password, password_data):
                    session["log"] = True
                    session["username"] = name
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