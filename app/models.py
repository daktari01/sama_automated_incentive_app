# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship

from app import db, login_manager

class Employee(UserMixin, db.Model):
    """
    Create Employee table
    """

    # Ensures table will be named in plural and not in singular 
    # as in the name of the model
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    emp_number = db.Column(db.String(10), index=True, nullable=False, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    emp_name = db.Column(db.String(100), index=True)
    password_hash = db.Column(db.String(128))
    emp_project_id = db.Column(db.Integer, nullable=False, db.ForeignKey('projects.id'))
    emp_subproject_id = db.Column(db.Integer, nullable=False, db.ForeignKey('subprojects.id'))
    emp_role_id = db.Column(db.Integer, nullable=False, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)
    emp_attendances = db.relationship('Attendance', backref='att_employee', 
                                    lazy='dynamic', foreign_keys="[attendances.id]")
    emp_incentives = db.relationship('Incentive', backref='inc_employee', 
                                    lazy='dynamic', foreign_keys="[incentives.id]")
    

    @property
    def password(self):
        """
        Prevent password from being accessed
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

class Role(db.Model):
    """
    Create a Role table
    """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=False)
    rol_employees = db.relationship('Employee', backref='role', 
                                    lazy='dynamic', foreign_keys="[employees.id]")

    def __repr__(self):
        return '<Role: {}>'.format(self.name)
        
class Project(db.Model):
    """
    Create a Project table
    """

    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False, unique=True)
    pro_employee_id = db.Column(db.Integer, nullable=False, db.ForeignKey('employees.id'))
    description = db.Column(db.String(200), nullable=False)
    pro_subprojects = db.relationship('Subproject', backref='sp_project', 
                                    lazy='dynamic', foreign_keys="[subprojects.id]")
    pro_employees = db.relationship('Employee', backref='emp_project', 
                                    lazy='dynamic', foreign_keys="[employees.id]")
                                    
class Subproject(db.Model):
    """
    Create a Subproject class
    """

    __tablename__ = 'subprojects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=False)
    sp_project_id = db.Column(db.Integer, nullable=False, db.ForeignKey('projects.id'))
    sp_employees = db.relationship('Employee', backref='emp_subproject', 
                                    lazy='dynamic', foreign_keys="[employees.id]")
    sp_incentives = db.relationship('Incentive', backref='inc_subproject', 
                                    lazy='dynamic', foreign_keys="[incentives.id]")

    def __repr__(self):
        return '<Subproject: {}>'.format(self.name)

class Attendance(db.Model):
    """
    Create an Attendance class
    """

    __tablename__ = 'attendances'

    id = db.Column(db.Integer, primary_key=True)
    att_employee_id = db.Column(db.Integer, nullable=False, db.ForeignKey('employees.id'))
    leave_days = db.Column(db.Integer, nullable=False)
    days_present = db.Column(db.Integer, nullable=False)
    percentage_attendance = db.Column(db.Integer, nullable=False)
    att_incentives = db.relationship('Incentive', backref='attendance', 
                                    lazy='dynamic', foreign_keys="[incentives.id]")
        
class Incentive(db.Model):
    """
    Create an Incentive table
    """

    __tablename__ = 'incentives'

    id = db.Column(db.Integer, primary_key=True)
    inc_employee_id = db.Column(db.Integer, nullable=False, db.ForeignKey('employees.id'))
    inc_subproject_id = db.Column(db.Integer, nullable=False, db.ForeignKey('subprojects.id'))
    inc_attendances_id = db.Column(db.Integer, nullable=False, db.ForeignKey('attendances.id'))
    production = db.Column(db.Integer, nullable=False)
    av_qa_score = db.Column(db.Integer, nullable=False)
    total_points = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)