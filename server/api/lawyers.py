from flask import Blueprint, jsonify, request
from models import db, Lawyer

# Create a Blueprint for Lawyer routes
lawyers_bp = Blueprint('lawyers', __name__)

@lawyers_bp.route('/lawyers', methods=['GET'])
def get_lawyers():
    lawyers = Lawyer.query.all()
    return jsonify([{"id": lawyer.id, "specialization": lawyer.specialization, "experience": lawyer.experience} for lawyer in lawyers])

@lawyers_bp.route('/lawyers', methods=['POST'])
def create_lawyer():
    data = request.get_json()
    new_lawyer = Lawyer(specialization=data['specialization'], experience=data['experience'], hourly_rate=data['hourly_rate'], user_id=data['user_id'])
    db.session.add(new_lawyer)
    db.session.commit()
    return jsonify({"message": "Lawyer created successfully"}), 201
