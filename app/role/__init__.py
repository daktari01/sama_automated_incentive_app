# app/role/__init__.py

from flask import Blueprint

role = Blueprint('role', __name__)

from . import views

#.