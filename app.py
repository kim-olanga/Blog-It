from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from .models import Users

#create flask instance
app = Flask(__name__)

#initialize database
db = SQLAlchemy(app)

#Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#Secret Key
app.config['SECRET_KEY'] = "kimzyy12345"


#create form class
class NamerForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    submit = SubmitField("submit")

#create form class
class UserForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
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

#create the route
@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = UserForm()
    #validate form
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        our_users = Users.querry.order_by(Users.date_added)
    return render_template("add_user.html", 
    name=name,
    form=form,
    our_users=our_users)
