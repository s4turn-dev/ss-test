from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError

from . import db
from models.user import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class SignupForm(FlaskForm):
    username = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(message="Password can't be empty")])
    confirm_password = PasswordField('Confirm password', validators=[EqualTo('password', message='Passwords do not match')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        if User.query.filter_by(login=username.data).first():
            raise ValidationError('This username is already in use')
