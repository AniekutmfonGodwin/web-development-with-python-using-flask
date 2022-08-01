from flask import render_template,Request,Response
from hello import app
from wtforms.validators import InputRequired

@app.route("/")
def home():
    request = Request()
    request.user
    
    return render_template("index.html")


@app.route("/<name>/")
def name(name):
    
    return render_template("index.html",name=name)
