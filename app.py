from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#create flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "kimzyy12345"

#create form class
class NamerForm(FlaskForm):
    name = StringField("What's Your Name", Validators=[DataRequired()])
    submit = SubmitField("submit")

#create the first route
@app.route('/')
def index():
    return render_template("index.html")

#localhost:500/user/john
# @app.route('/user/<name>')
# def user(name):
#     return render_template("user.html",name='john')


#create custom error pages
# invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

#internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

#create name page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    #validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template("form.html", 
        name=name, 
        form=form)