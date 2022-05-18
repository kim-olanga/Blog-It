from email import message
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from ..models import User
from wtforms import ValidationError

#create Login Form
class LoginForm(FlaskForm):
        email = StringField('email', validators=[DataRequired(), Email()])
        password = PasswordField('Password', validators=[DataRequired()])
        remember = BooleanField('Remember me')
        submit = SubmitField('Submit')

# Create Registration Form
class RegistrationForm(FlaskForm):
        email = StringField('email', validators=[DataRequired(), Email()])
        username = StringField("Username", validators=[DataRequired()])
        password = PasswordField("Password", validators=[DataRequired(),EqualTo('password2',message = 'passwords must match')])
        password2 = PasswordField("confirm Passwords", validators= [DataRequired()])
        submit = SubmitField("Submit")

        #validating our email
        def validate_email(self,data_field):
           if User.query.filter_by(email = data_field.data).first():
             raise ValidationError('An account with that email exists')

        #validating our username
        def validate_username(self,data_field):
           if User.query.filter_by(username = data_field.data).first():
             raise ValidationError('Username is already taken')     