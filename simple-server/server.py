import time
import datetime

from flask import Flask

app = Flask(__name__)

# Run with
# FLASK_APP=hello.py flask run

@app.route("/")
def hello():
    current_time = time.time()
    formatted_time = datetime.datetime.fromtimestamp(current_time).strftime('%Y-%m-%d %H:%M:%S')
    return "Hello World! The time is " + formatted_time