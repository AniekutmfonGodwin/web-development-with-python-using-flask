from flask import Flask,render_template
app = Flask(__name__)

from routes import *
from _models import *

if __name__ == "__main__":
    app.run(debug=True)
