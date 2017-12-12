# app/auth/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Employee

class RegistrationForm(FlaskForm):
    emp_number = StringField('Employee Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    emp_name = StringField('Full Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
                                                DataRequired(), 
                                                EqualTo('confirm_password')
                                            ])