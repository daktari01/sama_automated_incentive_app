# app/auth/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from ..models import Employee, Project, Subproject, Role

class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    emp_project_name = QuerySelectField(query_factory=lambda: Project.query.all(), 
                                                        get_label="name")
    emp_subproject_name = QuerySelectField(query_factory=lambda: Subproject.query.all(), 
                                                        get_label="name")
    emp_role_name = QuerySelectField(query_factory=lambda: Role.query.all(), 
                                                        get_label="name")
    emp_number = StringField('Employee Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    emp_name = StringField('Full Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
                                                DataRequired(), 
                                                EqualTo('confirm_password')
                                            ])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    def validate_email(self, field):
        if Employee.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_username(self, field):
        if Employee.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')

class LoginForm(FlaskForm):
    """
    Form for users to log in
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')