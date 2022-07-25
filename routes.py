from flask import render_template
from hello import app


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<name>/")
def name(name):
    return render_template("index.html",name=name)
