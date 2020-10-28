from flask import Flask
from config import Configurations

app = Flask(__name__)
app.config.from_object(Configurations)