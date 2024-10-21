from flask import Blueprint, request, jsonify
from models import db, User, Lawyer
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import os
import datetime

users_bp = Blueprint('users', __name__)

# Registration endpoint
@users_bp.route('/register', methods=['POST', 'OPTIONS'])
def register():
    if request.method == 'OPTIONS':
        return jsonify({"message": "Preflight OK"}), 200

    data = request.get_json()

    # Extract fields
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role')

    # Lawyer-specific fields
    specialization = data.get('specialization', None)
    experience = data.get('experience', None)
    hourly_rate = data.get('hourly_rate', None)
    availability = data.get('availability', None)
    bio = data.get('bio', None)

    # Basic validation
    if not name or not email or not password or not role:
        return jsonify({"error": "Missing required fields"}), 400

    # Check if user already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"error": "User already exists"}), 400

    # Hash the password for security
    hashed_password = generate_password_hash(password)

    # Create the user
    new_user = User(name=name, email=email, password=hashed_password, role=role)
    db.session.add(new_user)
    db.session.commit()

    # If the user is a lawyer, create a Lawyer profile
    if role == "lawyer":
        # Check for missing fields
        if not specialization or not experience or not hourly_rate or availability is None or bio is None:
            return jsonify({"error": "Missing lawyer-specific fields"}), 400

        # Create lawyer profile
        new_lawyer = Lawyer(
            specialization=specialization,
            experience=experience,
            hourly_rate=hourly_rate,
            availability=availability,
            bio=bio,
            user_id=new_user.user_id  # Link to the User using user_id
        )
        db.session.add(new_lawyer)
        db.session.commit()

    return jsonify({"message": "Registration successful"}), 201


@users_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Extract email and password
    email = data.get('email')
    password = data.get('password')

    # Basic validation
    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400

    # Check if user exists
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Verify password
    if not check_password_hash(user.password, password):
        return jsonify({"error": "Incorrect password"}), 401

    # Check if user is a lawyer
    if user.role == 'lawyer':
        lawyer = Lawyer.query.filter_by(user_id=user.user_id).first()  # Get the lawyer profile using user_id
        if not lawyer:
            return jsonify({"error": "Lawyer profile not found"}), 404

        # Create a JWT token with lawyer_id
        token = jwt.encode({
            'user_id': user.user_id,  # Use user_id instead of id
            'lawyer_id': lawyer.lawyer_id,  # Include the lawyer_id
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, os.getenv("ACCESS_TOKEN_SECRET"), algorithm="HS256")

        return jsonify({
            "message": "Login successful",
            "token": token,
            "user": {
                "user_id": user.user_id,  # Use user_id in the response
                "name": user.name,
                "email": user.email,
                "role": user.role,
                "lawyer_id": lawyer.lawyer_id  # Return lawyer_id in the response
            }
        }), 200
    else:
        # For regular users, create a JWT token without lawyer_id
        token = jwt.encode({
            'user_id': user.user_id,  # Use user_id instead of id
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, os.getenv("ACCESS_TOKEN_SECRET"), algorithm="HS256")

        return jsonify({
            "message": "Login successful",
            "token": token,
            "user": {
                "user_id": user.user_id,  # Use user_id in the response
                "name": user.name,
                "email": user.email,
                "role": user.role
            }
        }), 200