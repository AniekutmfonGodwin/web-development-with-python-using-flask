from flask import Blueprint

dashboard = Blueprint("dashboard",__name__,static_folder="static",template_folder="template")

@dashboard.route("/home")
def home():
    return "dashboard home"