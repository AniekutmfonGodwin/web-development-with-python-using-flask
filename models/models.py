from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from hello import app
import os

basedir = os.path.abspath(os.path.dirname(__file__))
path_to_db = os.path.join(basedir,"data.sqlite")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path_to_db
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username





