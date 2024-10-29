// components/lawyer/ReviewsSection.tsx

import React, { useMemo } from "react";
import { Card } from "@/components/ui/card";
import { FaUserTie, FaStar } from "react-icons/fa";
import ReviewComponent from "@/app/components/review";

interface Review {
  review_id: string;
  user_id: string;
  lawyer_id: string;
  comment: string;
  rating: number;
}

interface ReviewsSectionProps {
  reviews: Review[];
  averageRating: number;
  onRate: (rating: number) => void;
  userId?: number;
  lawyerId: string;
}

const ReviewsSection: React.FC<ReviewsSectionProps> = ({
  reviews,
  averageRating,
  onRate,
  userId,
  lawyerId,
}) => {
  // Function to render star ratings
  const renderStars = (rating: number) => {
    const stars = [];
    for (let i = 0; i < 5; i++) {
      stars.push(
        <FaStar
          key={i}
          className={`mr-1 ${i < rating ? "text-yellow-400" : "text-gray-300"}`}
        />
      );
    }
    return stars;
  };

  return (
    <div className="bg-white shadow-md rounded-lg p-6">
      <h2 className="text-2xl font-bold mb-4">Reviews</h2>
      <ul className="space-y-4">
        {reviews.map((review) => (
          <Card
            key={review.review_id}
            className="p-4 hover:shadow-lg transition-shadow rounded-lg border"
          >
            <div className="flex items-center">
              <FaUserTie className="mr-2 text-gray-500" />
              <p className="font-semibold">{`User ${review.user_id}`}</p>
            </div>
            <div className="flex items-center mt-2">
              {renderStars(review.rating)}
            </div>
            <p className="mt-2 text-gray-700">{review.comment}</p>
          </Card>
        ))}
      </ul>

      {/* Review Form */}
      <div className="mt-8">
        <h3 className="text-xl font-semibold mb-4">Leave a Review</h3>
        <ReviewComponent
          maxRating={5}
          onRate={onRate}
          lawyer_id={lawyerId}
          userId={userId}
        />
      </div>
    </div>
  );
};

export default ReviewsSection;
