from flask import Blueprint, request, jsonify
from models import db, User, Lawyer, Booking
from datetime import datetime

bookings_bp = Blueprint('bookings', __name__)

@bookings_bp.route('/booking', methods=['POST', 'OPTIONS'])
def booking_post():
    # Handle CORS preflight request
    if request.method == 'OPTIONS':
        return jsonify({"message": "Preflight OK"}), 200

    # Get data from request
    data = request.get_json()

    # Extract data from the request
    start_time = data.get('startTime')
    end_time = data.get('endTime')
    user_id = data.get('user_id')
    lawyer_id = data.get('lawyer_id')
    caseType=data.get('caseType')
    description=data.get('description')
    status=data.get('status')

    # Debugging: print the values to see what is being sent from the frontend
    print(f"Received start_time: {start_time}")
    print(f"Received end_time: {end_time}")
    print(f"Received user_id: {user_id}")
    print(f"Received lawyer_id: {lawyer_id}")
    print(f"Received user_id: {caseType}")
    print(f"Received lawyer_id: {description}")
    print(f"Received lawyer_id: {status}")

    # Basic validation for missing fields
    if not start_time or not end_time or not user_id or not lawyer_id or not description or not caseType or not status:
        return jsonify({"error": "Missing required fields"}), 400

    # Convert startTime and endTime to datetime objects
    try:
        start_time = datetime.strptime(start_time, '%Y-%m-%dT%H:%M')  # Assuming ISO format from datetime-local input
        end_time = datetime.strptime(end_time, '%Y-%m-%dT%H:%M')
    except ValueError:
        print("Invalid date format")
        return jsonify({"error": "Invalid date format"}), 400

    # Check for overlapping bookings (optional but recommended)
    existing_booking = Booking.query.filter(
        Booking.lawyer_id == lawyer_id,
        Booking.start_time < end_time,
        Booking.end_time > start_time
    ).first()

    if existing_booking:
        return jsonify({"error": "The lawyer is not available at the selected time"}), 409

    # Create a new Booking object
    new_booking = Booking(
        start_time=start_time,
        end_time=end_time,
        user_id=user_id,
        lawyer_id=lawyer_id,
        caseType=caseType,
        description=description,
        status=status
    )

    # Add and commit the booking to the database
    db.session.add(new_booking)
    db.session.commit()

    return jsonify({"message": "Booking successful", "booking_id": new_booking.booking_id}), 201



@bookings_bp.route('/getLawyersBookings/<int:lawyer_id>', methods=['GET'])
def get_lawyer_booking(lawyer_id):
    # Query all bookings for the given lawyer
    bookings = Booking.query.filter_by(lawyer_id=lawyer_id).all()

    # If no bookings are found, return an empty array
    if not bookings:
        return jsonify({"bookings": []}), 200

    # Prepare a list of booking details to return
    bookings_data = []
    for booking in bookings:
        # Manually query the User model using the user_id from the booking
        user = User.query.get(booking.user_id)

        bookings_data.append({
            "booking_id": booking.booking_id,
            "user_id": booking.user_id,
            "user_name": user.name if user else "Unknown",  # Safeguard in case the user is not found
            "lawyer_id": booking.lawyer_id,
            "start_time": booking.start_time.strftime('%Y-%m-%d %H:%M:%S'),
            "end_time": booking.end_time.strftime('%Y-%m-%d %H:%M:%S'),
            "status": booking.status  # Assuming 'status' is a column in your model
        })

    return jsonify({"bookings": bookings_data}), 200



@bookings_bp.route('/getUsersBookings/<int:user_id>', methods=['GET'])
def get_user_booking(user_id):
    # Query all bookings for the given user
    bookings = Booking.query.filter_by(user_id=user_id).all()

    # If no bookings are found, return an empty array
    if not bookings:
        return jsonify({"bookings": []}), 200

    # Prepare a list of booking details to return
    bookings_data = []
    for booking in bookings:
        # Query the Lawyer model using the lawyer_id from the booking
        lawyer = Lawyer.query.get(booking.lawyer_id)

        # Access the lawyer's name through the associated user
        lawyer_name = lawyer.user.name if lawyer and lawyer.user else "Unknown"

        bookings_data.append({
            "booking_id": booking.booking_id,
            "user_id": booking.user_id,
            "lawyer_name": lawyer_name,  # Safeguard in case the lawyer or user is not found
            "lawyer_id": booking.lawyer_id,
            "start_time": booking.start_time.strftime('%Y-%m-%d %H:%M:%S'),
            "end_time": booking.end_time.strftime('%Y-%m-%d %H:%M:%S'),
            "status": booking.status  # Assuming 'status' is a column in your model
        })

    return jsonify({"bookings": bookings_data}), 200



@bookings_bp.route('/updateBookingStatus/<int:booking_id>', methods=['PUT'])
def update_booking_status(booking_id):
    data = request.get_json()
    status = data.get('status')

    print(f"Received status: {status}")
   

    # Find the booking by booking_id
    booking = Booking.query.get(booking_id)

    if not booking:
        return jsonify({"error": "Booking not found"}), 404

    # Update the status
    booking.status = status

    try:
        db.session.commit()
        return jsonify({"message": "Booking status updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500