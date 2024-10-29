// components/lawyer/BookingsSection.tsx

import React from "react";
import { Card } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { FaUserTie, FaClock } from "react-icons/fa";

interface Booking {
  booking_id: number;
  start_time: string;
  end_time: string;
  status: string;
  user_name: string;
  caseType: string;
}

interface BookingsSectionProps {
  bookings: Booking[];
  onUpdateStatus: (
    message: string,
    variant?: "success" | "destructive"
  ) => void;
  updateStatus: (booking_id: number, status: string) => void;
}

const BookingsSection: React.FC<BookingsSectionProps> = ({
  bookings,
  onUpdateStatus,
  updateStatus,
}) => {
  return (
    <div className="bg-white shadow-md rounded-lg p-6">
      <h2 className="text-3xl font-bold mb-6">Bookings</h2>
      <ul className="space-y-6">
        {bookings.map((booking) => (
          <Card
            key={booking.booking_id}
            className="p-4 hover:shadow-lg transition-all rounded-lg border"
          >
            <div className="flex justify-between items-center">
              <div>
                <h3 className="text-xl font-semibold text-gray-800 flex items-center">
                  <FaUserTie className="mr-2" />
                  {booking.user_name}
                </h3>
                <p className="mt-1 text-gray-600 flex items-center">
                  <FaClock className="mr-2" />
                  {new Date(booking.start_time).toLocaleString()} -{" "}
                  {new Date(booking.end_time).toLocaleString()}
                </p>
                <p className="mt-1 text-gray-600">
                  <strong>Case Type:</strong> {booking.caseType}
                </p>
              </div>
              <div className="text-right">
                <Badge
                  variant={
                    booking.status === "accepted"
                      ? "success"
                      : booking.status === "declined"
                      ? "destructive"
                      : "warning"
                  }
                >
                  {booking.status}
                </Badge>
                <div className="flex space-x-2 mt-2">
                  <Button
                    size="sm"
                    onClick={() => updateStatus(booking.booking_id, "accepted")}
                    aria-label={`Accept booking ${booking.booking_id}`}
                  >
                    Accept
                  </Button>
                  <Button
                    size="sm"
                    variant="destructive"
                    onClick={() => updateStatus(booking.booking_id, "declined")}
                    aria-label={`Decline booking ${booking.booking_id}`}
                  >
                    Decline
                  </Button>
                </div>
              </div>
            </div>
          </Card>
        ))}
      </ul>
    </div>
  );
};

export default BookingsSection;
