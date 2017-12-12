# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# local imports
from config import app_config

# db_variable initialization
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page"
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)

    from app import models

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .attendance import attendance as attendance_blueprint
    app.register_blueprint(attendance_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .employee import employee as employee_blueprint
    app.register_blueprint(employee_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .incentive import incentive as incentive_blueprint
    app.register_blueprint(incentive_blueprint)

    from .project import project as project_blueprint
    app.register_blueprint(project_blueprint)

    from .role import role as role_blueprint
    app.register_blueprint(role_blueprint)

    from .subproject import subproject as subproject_blueprint
    app.register_blueprint(subproject_blueprint)



    return app