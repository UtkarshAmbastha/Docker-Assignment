from flask import Flask,render_template
p1 = Flask(__name__)

@p1.route('/')
def hello_world():
    return render_template('main.html')