from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(10), nullable=False)

    # Relationships
    lawyer = db.relationship('Lawyer', backref='user', uselist=False)

class Lawyer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    specialization = db.Column(db.String(120), nullable=False)
    experience = db.Column(db.Integer, nullable=False)
    hourly_rate = db.Column(db.Float, nullable=False)
    availability = db.Column(db.JSON)

    # Foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Relationships
    services = db.relationship('Service', backref='lawyer')
    bookings = db.relationship('Booking', backref='lawyer')

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

    # Foreign key
    lawyer_id = db.Column(db.Integer, db.ForeignKey('lawyer.id'))

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    lawyer_id = db.Column(db.Integer, db.ForeignKey('lawyer.id'))
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    lawyer_id = db.Column(db.Integer, db.ForeignKey('lawyer.id'))
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)
