__author__ = 'will'

from flask import Blueprint, render_template


home = Blueprint('home', __name__)


@home.route('/')
@home.route('/home')
def index():
    return render_template('home/home.html')

