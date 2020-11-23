from flask import Blueprint
from flask import render_template, flash, request, redirect, url_for, session, request
from dbmodels import db, delete_task, select_tasks
from flask import jsonify

tasks = Blueprint('tasks', __name__, template_folder='templates')

@tasks.route('/')
def index():
    name = session["username"]
    tasks = select_tasks(name)
    

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

@tasks.route('/del_task', methods=['POST'])
def delete_item():
    tasks = select_tasks(session["username"])
    item_id = int(request.get_json()['id'])

    for i in range(len(tasks)):
        if tasks[i][0] == item_id:
            delete_task(item_id)
            break

    return jsonify(removed_item=item_id)

@tasks.route('/task')
def task():
    return render_template("tasks/task.html")












