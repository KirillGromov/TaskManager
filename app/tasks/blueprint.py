from flask import Blueprint
from flask import render_template, flash, request, redirect, url_for, session
from dbmodels import db

tasks = Blueprint('tasks', __name__, template_folder='templates')

@tasks.route('/')
def index():
    name = session["username"]
    query = "SELECT * FROM task WHERE name like '{0}'".format(name)
    tasks = db.execute(query).fetchall()
    return render_template('tasks/index.html', tasks = tasks)

@tasks.route("/add_task", methods=["POST", "GET"])
def AddTask():
    if request.method =="POST":
        title = request.form.get("title")
        description = request.form.get("description")
        name = session["username"]

        if title is None:
            return render_template("tasks/add_task.html")
        else:
            db.execute("INSERT INTO task(name, title, description) VALUES(:name,:title,:description)",
                        {"name":name,"title":title,"description": description})
            db.commit()
            return redirect(url_for('tasks.index'))
    return render_template("tasks/add_task.html")





