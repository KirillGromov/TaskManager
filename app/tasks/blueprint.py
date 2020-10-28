from flask import Blueprint
from flask import render_template

tasks = Blueprint('tasks', __name__, template_folder='templates')

@tasks.route('/')
def index():
    tasks = [
        {'task': 'Work', 'details': 'do work in office'},
        {'task': 'Work2', 'details': 'do work in office2'}
    ]
    return render_template('tasks/index.html', tasks = tasks)

