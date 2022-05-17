from flask import Flask, render_template, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# from models import User

#create flask instance
app = Flask(__name__)
#Add Database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#New database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://kimberly:kim12345@localhost/test'
#Secret Key
app.config['SECRET_KEY'] = "kimzyy12345"
#initialize database
db = SQLAlchemy(app)
migrate = Migrate(app, db)


#create Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    data_added = db.Column(db.DateTime, default=datetime.utcnow)

    #create string
    def __repr__(self):
        return '<Name %r>' % self.name

#create form class
class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Submit")

#Update database record
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = UserForm()
    name_to_update = User.querry.get_or_404(id)
    if request.method =="POST":
        name_to_update.name = request.form['name']
        name_to_update.email = request.form['email']
        try:
            db.session.commit()
            flash("User updated successfully!")
            return render_template("update.html", 
            form=form,
            name_to_update = name_to_update)
        except:
           flash("Looks like there was a problem updating try again")
           return render_template("update.html", 
           form=form,
           name_to_update = name_to_update) 
    else:
        return render_template("update.html", 
           form=form,
           name_to_update = name_to_update) 


#create form class
class NamerForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Submit")


#create the route
@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = UserForm()
    #validate form
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            user = User(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        our_user = User.querry.order_by(User.date_added)
    return render_template("add_user.html", 
    form=form,
    name=name,
    our_user=our_user)

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

# #create the route
# @app.route('/user/add', methods=['GET', 'POST'])
# def add_user():
#     name = None
#     form = UserForm()
#     #validate form
#     if form.validate_on_submit():
#         user = UserForm.query.filter_by(email=form.email.data).first()
#         if user is None:
#             user = UserForm(name=form.name.data, email=form.email.data)
#             db.session.add(user)
#             db.session.commit()
#         name = form.name.data
#         form.name.data = ''
#         form.email.data = ''
#         our_users = User.querry.order_by(User.date_added)
#     return render_template("add_user.html", 
#     name=name,
#     form=form,
#     our_users=our_users)
