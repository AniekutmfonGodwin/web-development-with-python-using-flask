from flask import render_template,Request,Response
from hello import app
from wtforms.validators import InputRequired


from models.models import User,db
from flask_mail import Mail,Message
from settings import EMAIL,PASSWORD

mail = Mail(app)
    

@app.route("/")
def home():
    # form = dict(username="anies",email="myemail@gmail.com")
    # db.session.add(User(**form))
    # db.session.commit()
    # # return render_template("index.html")
    # result =  render_template("index.html",username = 'Anies')
    return "home"


@app.route("/<name>/")
def name(name):
    
    return render_template("index.html",name=name)


@app.route("/sendmail/<email>/")
def send_mail(email):
    msg = Message("Hello",
                  sender=EMAIL,
                  recipients=[email])

    mail.send(msg)
    return "done"
