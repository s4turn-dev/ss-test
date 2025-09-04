from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Length

from . import db
from models.user import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(message="Password can't be empty")])
    confirm_password = PasswordField('Confirm password', validators=[EqualTo('password', message='Passwords do not match')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('This username is already in use')


class RequisitesForm(FlaskForm):
    bank = StringField('Название банка', validators=[DataRequired(), Length(max=32)])
    bic = StringField('БИК', validators=[DataRequired(), Length(9, 9)])
    checking_account = StringField('Расчетный счет', validators=[DataRequired(), Length(max=32)])
    correspondent_account = StringField('Корреспондентский счет', validators=[DataRequired(), Length(0, 32)])
    swift = StringField('SWIFT', validators=[DataRequired(), Length(max=32)])
    iban = StringField('IBAN (Опциональное поле)', validators=[Length(max=32)])

    submit = SubmitField('Готово')
