__author__ = 'will'

from flask import Flask
from .views.home import home

app = Flask(__name__)
app.register_blueprint(home)
