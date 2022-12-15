from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField, validators, EmailField, ValidationError
import email_validator
from market.models import User

MIN_PASSWORD = 6
MIN_USERNAME = 3
MAX_USERNAME = 30


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a new username.')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email address already in use, try a different email.')

    username = StringField('Username', [validators.Length(min=MIN_USERNAME, max=MAX_USERNAME),
                                        validators.DataRequired()])
    email_address = EmailField('Email Address', [validators.Email(), validators.DataRequired()])
    password1 = PasswordField('Password', [validators.Length(min=MIN_PASSWORD), validators.DataRequired()])
    password2 = PasswordField('Confirm Password', [validators.EqualTo('password1'), validators.DataRequired()])
    submit = SubmitField('Create Account')


class LoginForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Sign in')


class PurchaseItemForm(FlaskForm):
    submit = SubmitField('Purchase Item')


class SellItemForm(FlaskForm):
    submit = SubmitField('Sell Item')
