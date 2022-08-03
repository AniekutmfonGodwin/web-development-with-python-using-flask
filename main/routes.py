from flask import render_template,Request,Response, url_for
from wtforms.validators import InputRequired
from flask_mail import Mail,Message
from settings import EMAIL,PASSWORD

from flask import Blueprint


main = Blueprint("main",__name__,static_folder="static",template_folder="template")






@main.route("/")
def home():
    # form = dict(username="anies",email="myemail@gmail.com")
    # db.session.add(User(**form))
    # db.session.commit()
    # # return render_template("index.html")
    # result =  render_template("index.html",username = 'Anies')
    print(url_for("main.home"))
    return "home"


@main.route("/<name>/")
def name(name):
    
    return render_template("index.html",name=name)


# @main.route("/sendmail/<email>/")
# def send_mail(email):
#     msg = Message("Hello",
#                   sender=EMAIL,
#                   recipients=[email])

#     mail.send(msg)
#     return "done"

