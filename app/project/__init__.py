# app/project/__init__.py

from flask import Blueprint

project = Blueprint(project, __name__)

from . import views