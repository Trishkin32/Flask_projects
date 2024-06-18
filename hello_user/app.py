from flask import Flask, render_template
import datetime


app = Flask(__name__)


@app.route('')
def index():
    now = datetime.datetime.now()
    if now.hour >= 6 and now.hour < 12:
        return "Доброе утро!"


