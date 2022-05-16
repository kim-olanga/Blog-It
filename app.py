from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#create flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "kimzyy12345"

#create form class
class NamerForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    submit = SubmitField("submit")

#create the first route
@app.route('/')
def index():
    return render_template("index.html", user_name=name)

# localhost:500/user/john
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)


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
        flash("Form submitted successfully.!!")
    return render_template("name.html", 
        name=name, 
        form=form)