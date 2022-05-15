from flask import Flask, render_template

#create flask instance
app = Flask(__name__)

#create the first route
@app.route('/')
def index():
    return "<h1>Hello Kimzy</h1>"