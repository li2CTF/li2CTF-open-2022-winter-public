from flask import Flask, redirect
import time

app = Flask(__name__)


@app.route("/")
def index():
    time.sleep(10)
    return "lol"

app.run(port=8082)
