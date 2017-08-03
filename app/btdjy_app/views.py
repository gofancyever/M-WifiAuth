from . import btdjy
from flask import render_template


@btdjy.route('/')
def index():
    return render_template('index.html'),200



