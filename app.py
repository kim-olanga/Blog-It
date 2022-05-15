from flask import Flask, render_template, render_template_string

#create flask instance
app = Flask(__name__)

#create the first route
@app.route('/')
def index():
    return render_template("index.html")

#localhost:5000/user/James
@app.route('/user/<name>')
def user(name):
    return "<h1>Hello {}??!!</h1>".format(name)