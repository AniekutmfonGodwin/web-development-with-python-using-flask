from flask import Flask
from settings import EMAIL, PASSWORD
from flask_login import LoginManager
from flask_mail import Mail
import os

login_manager = LoginManager()

app = Flask(__name__)

mail = Mail(app)

@login_manager.user_loader
def load_user(user_id):
    from auth.models import User
    return User.query.get(user_id)


app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = EMAIL
app.config["MAIL_PASSWORD"] = PASSWORD
app.config["MAIL_DEFAULT_SENDER"] = EMAIL
app.config["SECRET_KEY"] = "SGGHTggafsg45562987"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False






def create_app():
    from dashboard.routes import dashboard
    from auth.routes import auth
    from main.routes import main
    from api.routes import api
    login_manager.init_app(app)
    app.register_blueprint(dashboard,url_prefix="/dashboard")
    app.register_blueprint(auth,url_prefix="/auth")
    app.register_blueprint(api,url_prefix="/api")
    app.register_blueprint(main,url_prefix="/")

    return app

DEBUG = os.getenv("DEBUG","False").lower() in ["true",'1',1]

app = create_app()

if __name__ == "__main__":
    app = create_app()
    app.run(debug=DEBUG,port = 5002)
