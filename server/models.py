from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)  # Changed to user_id
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # Increased to 255
    role = db.Column(db.String(10), nullable=False)

    # Relationships
    lawyer = db.relationship('Lawyer', backref='user', uselist=False)
    
class Lawyer(db.Model):
    __tablename__ = 'lawyer'
    lawyer_id = db.Column(db.Integer, primary_key=True)  # Changed to lawyer_id
    education=db.Column(db.String(55), nullable=True)
    specialization = db.Column(db.String(120), nullable=False)
    experience = db.Column(db.Integer, nullable=False)
    hourly_rate = db.Column(db.Float, nullable=False)
    availability = db.Column(db.JSON)
    location=db.Column(db.String(55), nullable=True)
    bio = db.Column(db.Text, nullable=True)  # Adding bio field

    # Foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))  # Refers to user_id in User

    # Relationships
    services = db.relationship('Service', backref='lawyer')
    bookings = db.relationship('Booking', backref='lawyer')


class Service(db.Model):
    __tablename__ = 'service'
    service_id = db.Column(db.Integer, primary_key=True)  # Changed to service_id
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

    # Foreign key
    lawyer_id = db.Column(db.Integer, db.ForeignKey('lawyer.lawyer_id'))  # Refers to lawyer_id in Lawyer

class Booking(db.Model):
    __tablename__ = 'booking'
    booking_id = db.Column(db.Integer, primary_key=True)  # Changed to booking_id
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))  # Refers to user_id in User
    lawyer_id = db.Column(db.Integer, db.ForeignKey('lawyer.lawyer_id'))  # Refers to lawyer_id in Lawyer
    caseType = db.Column(db.String(20), nullable=False)  # Nullable should be outside of db.String
    description = db.Column(db.String(255), nullable=False)  # Nullable should be outside of db.String
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False)

class Review(db.Model):
    __tablename__ = 'review'
    review_id = db.Column(db.Integer, primary_key=True)  # Changed to review_id
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))  # Refers to user_id in User
    lawyer_id = db.Column(db.Integer, db.ForeignKey('lawyer.lawyer_id'))  # Refers to lawyer_id in Lawyer
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)
