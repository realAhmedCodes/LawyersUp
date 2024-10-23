
# In your api/lawyers.py
from flask import Blueprint, jsonify
from models import db, Lawyer

lawyers_bp = Blueprint('lawyers', __name__)

@lawyers_bp.route('/lawyers', methods=['GET'])
def get_lawyers():
    lawyers = Lawyer.query.all()
    lawyer_data = []
    for lawyer in lawyers:
        lawyer_data.append({
            "lawyer_id": lawyer.lawyer_id,
            "name": lawyer.user.name,  # Accessing user's name through relationship
            "specialization": lawyer.specialization,
            "experience": lawyer.experience,
            "hourly_rate": lawyer.hourly_rate,
            "availability": lawyer.availability,
        })
    return jsonify({"lawyers": lawyer_data}), 200



@lawyers_bp.route('/lawyers/<int:lawyer_id>', methods=['GET'])
def get_lawyer(lawyer_id):
    lawyer = Lawyer.query.filter_by(lawyer_id=lawyer_id).first()
    if not lawyer:
        return jsonify({"error": "Lawyer not found"}), 404

    # Fetch associated services
    services = [
        {
            "service_id": service.service_id,
            "title": service.title,
            "description": service.description,
            "price": service.price
        } for service in lawyer.services
    ]

    lawyer_data = {
        "lawyer_id": lawyer.lawyer_id,
        "specialization": lawyer.specialization,
        "experience": lawyer.experience,
        "hourly_rate": lawyer.hourly_rate,
        "availability": lawyer.availability,
        "education": lawyer.education,
        "location":lawyer.location,
        "bio": lawyer.bio,
        "services": services,  # Include the services in the response
        "user": {
            "name": lawyer.user.name,
            "email": lawyer.user.email,
            "role": lawyer.user.role
        }
    }
    return jsonify({"lawyer": lawyer_data}), 200
