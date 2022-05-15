from flask import Flask, render_template, render_template_string

#create flask instance
app = Flask(__name__)

#create the first route
@app.route('/')
def index():
    return render_template("index.html")

#create custom error pages
# invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

#internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
