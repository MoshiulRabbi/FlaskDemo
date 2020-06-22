import random

from flask import Flask, render_template


app = Flask(__name__)



@app.route("/")
def inex():
    number=random.randint(0,1)
    return render_template("index.html",Number=number)
