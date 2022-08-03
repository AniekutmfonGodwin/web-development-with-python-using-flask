from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from server import app
import os
from werkzeug.security import generate_password_hash,check_password_hash
import settings
from flask_login import UserMixin

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




