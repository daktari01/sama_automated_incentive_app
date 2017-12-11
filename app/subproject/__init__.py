# app/subproject/__init__.py

from flask import Blueprint

subproject = Blueprint(subproject, __name__)

from . import views