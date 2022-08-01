from flask import Flask
from settings import EMAIL, PASSWORD


app = Flask(__name__)


app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = EMAIL
app.config["MAIL_PASSWORD"] = PASSWORD
app.config["MAIL_DEFAULT_SENDER"] = EMAIL

from routes import *
from models.models import *



if __name__ == "__main__":
    app.run(debug=True)
