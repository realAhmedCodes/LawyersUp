from flask import Blueprint, request, jsonify
from models import db, User, Lawyer, Review

reviews_bp = Blueprint('reviews', __name__)

@reviews_bp.route('/reviewSubmit', methods=['POST', 'OPTIONS'])
def review_post():
    if request.method=='OPTIONS':
        return jsonify({"message": "Preflight OK"}),200
    data= request.get_json()

    user_id= data.get('user_id')
    lawyer_id= data.get('lawyer_id')
    comment=data.get('review')
    rating=data.get('rating')

    print(f"Received start_time: {comment}")
    print(f"Received end_time: {rating}")
    print(f"Received user_id: {user_id}")
    print(f"Received lawyer_id: {lawyer_id}")


    if not comment or not rating or not user_id or not lawyer_id:
        return jsonify({"error": "Missing required fields"}), 400

    existing_review = Review.query.filter_by(Review.user_id==user_id , Review.lawyer_id ==lawyer_id).first()
    if not existing_review:
        return jsonify({"error": "Review Already Exist"}), 404
    

    new_review=Review(
        user_id=user_id,
        lawyer_id=lawyer_id,
        comment=comment,
        rating=rating
    )

    db.session.add(new_review)
    db.session.commit()

    return jsonify({"message": "Booking successful", "review_id": new_review.review_id}),



    


    
@reviews_bp.route('/getReviews/<int:lawyer_id>', methods=['GET'])
def get_lawyer_booking(lawyer_id):
    # Query all bookings for the given lawyer
    reviews = Review.query.filter_by(lawyer_id=lawyer_id).all()

    # If no bookings are found, return an empty array
    if not reviews:
        return jsonify({"reviews": []}), 200

    # Prepare a list of booking details to return
    reviews_data = []
    for review in reviews:
        # Manually query the User model using the user_id from the booking
        review = Review.query.get(review.review_id)

        reviews_data.append({
            "review_id": review.review_id,
            "user_id": review.user_id,
           
            "lawyer_id": review.lawyer_id,
           
            "comment": review.comment,
             "rating": review.rating 
        })

    return jsonify({"reviews": reviews_data}), 200
