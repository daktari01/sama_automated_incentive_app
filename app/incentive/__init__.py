# app/incentive/__init__.py

from flask import Blueprint

incentive = Blueprint(incentive, __name__)

from . import views