# app/attendance/__init__.py

from flask import Blueprint

attendance = Blueprint(attendance, __name__)

from . import views

