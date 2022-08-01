from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from hello import app
import os
from werkzeug.security import generate_password_hash,check_password_hash
import settings

basedir = os.path.abspath(os.path.dirname(__file__))
path_to_db = os.path.join(basedir,"data.sqlite")



mysql_db_string_temlate = "mysql://{username}:{password}@{host}:{port}/sql_hr"

db_string = None

if all([
    settings.DB_HOST,
    settings.DB_PASSWORD,
    settings.DB_PORT,
    settings.DB_USERNAME,
]):
    db_string = mysql_db_string_temlate.format(
        username = settings.DB_USERNAME,
        password = settings.DB_PASSWORD,
        host = settings.DB_HOST,
        port = settings.DB_PORT,
    )
    print("connecting with mysql")
else:
    db_string = 'sqlite:///' + path_to_db 
    print('connecting with sqlite')


app.config['SQLALCHEMY_DATABASE_URI'] = db_string

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{username}:{password}@127.0.0.1:3306/sql_hr'

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

"""
mysql://{username}:{password}@127.0.0.1:3306/sql_hr
"""

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))



    @property
    def password(self):
        raise AttributeError("password is not readable")

    @password.setter
    def password(self,value):
        self.password_hash = generate_password_hash(value)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)


    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def fullname(self):
        ...


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username





