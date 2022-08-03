from flask import Blueprint, redirect, render_template, request, url_for,request
from auth.forms import LoginForm,RegistrationForm
from auth.models import User
from config.db_setup import db


auth = Blueprint("auth",__name__)




@auth.route("/login",methods=["get","post"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        password = data.pop("password",None)
        user = User(**data)
        user.password = password
        db.session.add(user)
        db.session.commit()
        return redirect(request.args.get("next") or url_for("main.home"))
    return render_template("login.html",form=form)


@auth.route("/register",methods=["get","post"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        data = form.data
        password = data.pop("password",None)
        user = User(**data)
        user.password = password
        db.session.add(user)
        db.session.commit()
        return redirect(request.args.get("next") or url_for("main.home"))
    return render_template("login.html",form=form)
