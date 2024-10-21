from flask import Blueprint, request, jsonify
from models import db, Service, Lawyer
import jwt
import os

services_bp = Blueprint('services', __name__)

# Load secret key from environment
SECRET_KEY = os.getenv("ACCESS_TOKEN_SECRET")

@services_bp.route('/servicesPost', methods=['POST', 'OPTIONS'])
def servicePost():
    if request.method == 'OPTIONS':
        return jsonify({"message": "Preflight OK"}), 200

    data = request.get_json()
    services = data.get('services', [])
    lawyer_id = data.get('lawyer_id')

    if not lawyer_id:
        return jsonify({"error": "Missing lawyer_id"}), 400

    # Find the lawyer by lawyer_id
    lawyer = Lawyer.query.filter_by(lawyer_id=lawyer_id).first()

    if not lawyer:
        return jsonify({"error": "Lawyer not found"}), 404

    # Validate and add each service
    for service in services:
        title = service.get('title')
        description = service.get('description')
        price = service.get('price')

        if not title or not description or not price:
            return jsonify({"error": "Missing required fields"}), 400

        new_service = Service(title=title, description=description, price=price, lawyer_id=lawyer.lawyer_id)
        db.session.add(new_service)

    db.session.commit()

    return jsonify({"message": "Services entered successfully"}), 201
