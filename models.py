from flask import Flask, render_template
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#initialize flask
app = Flask(__name__)

#initialize database
db = SQLAlchemy(app)

#create Model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    data_added = db.Column(db.DateTime, default=datetime.utcnow)

    #create string
    def __repr__(self):
        return '<Name %r>' % self.name

# #create form class
# class UserForm(FlaskForm):
#     name = StringField("name", validators=[DataRequired()])
#     email = StringField("email", validators=[DataRequired()])
#     submit = SubmitField("submit")