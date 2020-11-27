from flask import render_template
from code.app_config import *

@app.route('/')
def hello_world():
    return render_template('index.html')