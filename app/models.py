from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Speaker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    exceptions = db.relationship('SpeakerException', backref='speaker', lazy=True)  # Updated to 'SpeakerException'

class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    speaker_id = db.Column(db.Integer, db.ForeignKey('speaker.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Enum('3 Min', '5 Min', '10 Min', '15 Min', '20 Min'), nullable=False)
    order = db.Column(db.Integer, nullable=False)
    speaker = db.relationship('Speaker', backref=db.backref('assignments', lazy=True))

class Prayer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)  # e.g., 'Opening', 'Closing'
    name = db.Column(db.String(100), nullable=False)

class Announcement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

class Hymn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    number = db.Column(db.Integer, nullable=False)

# Renamed to SpeakerException
class SpeakerException(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    speaker_id = db.Column(db.Integer, db.ForeignKey('speaker.id'), nullable=False)
    reason = db.Column(db.Enum('Health Reasons', 'Refusal', 'Vacation'), nullable=False)
    expiry_date = db.Column(db.Date, nullable=True)  # Only for vacation or time-bound exceptions
