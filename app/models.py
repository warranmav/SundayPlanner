from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Speaker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    topic = db.Column(db.String(200), nullable=False)
    # Add other fields as needed

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
