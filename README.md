# Web development with python using flask framework
web development with python using flask and flask-sqlalchemy orm for database integration



## steps to setup the app
* install virtualenv if you do not have it in your pc

        pip install virtualenv
* create a folder and create a virtual enviroment with

        virtualenv env

* activate the virtualenv using 

        # for windows
        env/Scripts/activate

        # for linux or mac
        source env/bin/activate

* install requirements with 

        pip install -r requirements.txt

* run server with 

        python hello.py




## Assignment
* Push your code to github
* create a route that accept an email and send a mail with and html template using flask mailer.



# Session 10

packages to install:
https://werkzeug.palletsprojects.com/en/2.2.x/utils/



#### Note to use flask-sqlachemy with mysql you must installl mysqlclient

        pip3 install mysqlclient


### To create table from models run
        db.create_all()

## To delete all table run 
        db.drop_all()
