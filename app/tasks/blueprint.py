from flask import Blueprint
from flask import render_template

tasks = Blueprint('tasks', __name__, template_folder='templates')

@tasks.route('/')
def index():
    return render_template('tasks/index.html')