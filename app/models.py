# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class Employee(UserMixin, db.Model):
    """
    Create Employee table
    """

    # Ensures table will be named in plural and not in singular 
    # as in the name of the model
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    emp_number = db.Column(db.String(10), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    emp_name = db.Column(db.String(100), index=True)
    password_hash = db.Column(db.String(128))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)
    subprojects = db.relationship('Subproject', backref='employee', 
                                    lazy='dynamic')
    attendances = db.relationship('Attendance', backref='employee', 
                                    lazy='dynamic')
    incentives = db.relationship('Incentive', backref='employee', 
                                    lazy='dynamic')

    @property
    def password(self):
        """
        Prevent password frombeing accessed
        """
        raise AttributeError('Password is not readable.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Employee: {}>'.format(self.username)

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))

class Incentive(db.Model):
    """
    Create an Incentive table
    """

    __tablename__ = 'incentives'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    subproject_id = db.Column(db.Integer, db.ForeignKey('subprojects.id'))
    production = db.Column(db.Integer)
    av_qa_score = db.Column(db.Integer)
    total_points = db.Column(db.Integer)
    amount = db.Column(db.Float)

    def __repr__(self):
        return '<Incentive: {}>'.format(self.id)


class Project(db.Model):
    """
    Create a Project table
    """

    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    team_lead = db.Column(db.String(100), db.ForeignKey('employees.id'))
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='project',
                                 lazy='dynamic')
    subprojects = db.relationship('Subproject', backref='project', 
                                    lazy='dynamic')

    def __repr__(self):
        return '<Project: {}>'.format(self.name)

class Subproject(db.Model):
    """
    Create a Subproject class
    """

    __tablename__ = 'subprojects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    incentives = db.relationship('Incentive', backref='subproject', 
                                    lazy='dynamic')

    def __repr__(self):
        return '<Subproject: {}>'.format(self.name)

class Attendance(db.Model):
    """
    Create an Attendance class
    """

    __tablename__ = 'attendances'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    leave_days = db.Column(db.Integer)
    days_present = db.Column(db.Integer)
    percentage_attendance = db.Column(db.Integer)

    def __repr__(self):
        return '<Attendance: {}>'.format(self.id)

class Role(db.Model):
    """
    Create a Role table
    """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role: {}>'.format(self.name)
    
