from flask import Flask
from config import Configurations
from tasks.blueprint import tasks

app = Flask(__name__)
app.config.from_object(Configurations)

app.register_blueprint(tasks, url_prefix = '/tasks')