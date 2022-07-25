from flask import Flask,request,redirect,render_template,abort,get_flashed_messages
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,EmailField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = EmailField('email')
    message = TextAreaField('message')


class ContactForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = TextAreaField('message')
    message = TextAreaField('message')



app = Flask(__name__)
app.config["SECRET_KEY"] = "xomlgwafgeodrmqiyetiwlsgzeyiteugktispbxhlzpbnspj"

bootstrap = Bootstrap(app)

# @app.route('/submit', methods=['GET', 'POST'])
# def test():
#     return render_template("bootstrap-example.html")

@app.route('/test', methods=['GET', 'POST'])
def submit():
    
    form = MyForm()
    if form.validate_on_submit():
        
        return redirect('/')
   
    return render_template('bootstrap-example.html', form=form)

@app.errorhandler(404)
def not_found(*args):
    print(args)
    return render_template("404.html")


@app.route('/')
def home():
    data = dict(
        name = "Anies",
        position = {
            "name":"position in class",
            "value":300
        },
        items = [1,2,3,4]
    )
    login = True
    
    return render_template("index.html",**data,login=login)



@app.route('/contact',methods=["GET","POST"])
def contact():
    form = ContactForm()
    
    if form.validate_on_submit():
        print("data",form.data)
        print('SELECT * FROM User WHERE username = {name}'.format(form.data["name"]))
        return redirect('/')
    
    print("errors",form.errors)
    return render_template("contact.html",form=form)

@app.route('/contact/<id>/')
def about(id):
    return "Contact pag "+id



if __name__ == "__main__":
    app.run(debug=True)
   