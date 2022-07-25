import os
from models.models import db
basedir = os.path.abspath(os.path.dirname(__file__))
print("full path to where i want my database to be created \n",'sqlite:////' + os.path.join(basedir,"data.sqlite"))



if __name__ == "__main__":
    db.create_all()