from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    is_approved = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.String(30), unique=True)
    name = db.Column(db.String(100), nullable=False)
    external_id = db.Column(db.String(50))
    hourly_rate = db.Column(db.Float, nullable=False, default=0.0)
    piece_rate = db.Column(db.Float, nullable=False, default=0.0)
    is_active = db.Column(db.Boolean, default=True)
    entries = db.relationship('Entry', backref='employee', lazy=True, cascade="all, delete-orphan")
    harvests = db.relationship('DailyHarvest', backref='employee', lazy=True, cascade="all, delete-orphan")

class Field(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class BerryVariety(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    piece_rate_modifier = db.Column(db.Float, nullable=False, default=1.0)

class WorkType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    is_piece_rate = db.Column(db.Boolean, default=False)
    unit = db.Column(db.String(20), nullable=True)

class DailyHarvest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    quantity_kg = db.Column(db.Float, nullable=False)
    variety_id = db.Column(db.Integer, db.ForeignKey('berry_variety.id'), nullable=False)
    field_id = db.Column(db.Integer, db.ForeignKey('field.id'), nullable=False)
    comment = db.Column(db.Text, nullable=True)
    variety = db.relationship('BerryVariety')
    field = db.relationship('Field')

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    work_type_id = db.Column(db.Integer, db.ForeignKey('work_type.id'), nullable=False)
    hours = db.Column(db.Float, nullable=True, default=0.0)
    quantity = db.Column(db.Float, nullable=True, default=0.0)
    piece_rate = db.Column(db.Float, nullable=True)   # <--- DODAJ TO
    variety_id = db.Column(db.Integer, db.ForeignKey('berry_variety.id'), nullable=True)
    field_id = db.Column(db.Integer, db.ForeignKey('field.id'), nullable=True)
    comment = db.Column(db.Text, nullable=True)
    work_type = db.relationship('WorkType')
    variety = db.relationship('BerryVariety')
    field = db.relationship('Field')

class Presence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    time_in = db.Column(db.Time, nullable=False)
    time_out = db.Column(db.Time, nullable=True)
    break_minutes = db.Column(db.Integer, nullable=True, default=0)
    comment = db.Column(db.Text, nullable=True)