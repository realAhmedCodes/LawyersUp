"use client";

import { useEffect, useState } from "react";
import { useRouter, useParams } from "next/navigation";
import { Card } from "@/components/ui/card";
import { useToast } from "@/hooks/use-toast";
import Navbar from "@/app/components/navbar";
import {
  FaUserTie,
  FaBriefcase,
  FaClock,
  FaMoneyBillWave,
  FaTasks,
  FaEnvelope,
  FaMapMarkerAlt,
} from "react-icons/fa"; // Icons
import BookingPage from "@/app/components/bookingCom";

interface Service {
  service_id: number;
  title: string;
  description: string;
  price: number;
}

interface Review {
  reviewer: string;
  rating: number;
  comment: string;
  date: string;
}

interface Lawyer {
  name: string;
  bio: string;
  specialization: string;
  experience: number;
  hourly_rate: number;
  location: string;
  reviews: Review[];
  services: Service[];
}

const LawyerProfilePage = () => {
  const router = useRouter();
  const { lawyerId } = useParams<{ lawyerId: string }>();
  const [lawyer, setLawyer] = useState<Lawyer | null>(null);
  const [isBookingOpen, setIsBookingOpen] = useState<boolean>(false);
  const { toast } = useToast();

  useEffect(() => {
    if (lawyerId) {
      fetchLawyerData();
    }
  }, [lawyerId]);

  const fetchLawyerData = async () => {
    try {
      const response = await fetch(
        `http://localhost:5000/api/lawyers/${lawyerId}`
      );
      if (!response.ok) {
        throw new Error("Failed to fetch lawyer data");
      }
      const data = await response.json();
      setLawyer(data.lawyer);
    } catch (error) {
      toast({
        title: "Error",
        description: "Failed to load lawyer profile",
        variant: "destructive",
      });
    }
  };

  if (!lawyer) return <div>Loading...</div>;

  return (
    <div>
      <Navbar />

      {/* Gradient Header */}
      <div className="bg-gradient-to-r from-purple-400 to-indigo-600 h-56 flex items-center justify-center">
        <div className="flex items-center space-x-6">
          <div className="rounded-full bg-white p-2 shadow-lg">
            <img
              src="/path/to/lawyer-profile-image.jpg" // Replace with actual lawyer image
              alt={lawyer.name}
              className="rounded-full w-28 h-28 object-cover"
            />
          </div>
          <div className="text-white">
            <h1 className="text-4xl font-bold">{lawyer.name}</h1>
            <p className="text-lg flex items-center">
              <FaMapMarkerAlt className="mr-2" />{" "}
              {lawyer.location || "Location not available"}
            </p>
          </div>
        </div>
      </div>

      <div className="container mx-auto px-4 py-8">
        {/* Services Section */}
        <div className="mb-12">
          <h2 className="text-2xl font-bold mb-4">Services</h2>
          <ul className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {lawyer.services.map((service) => (
              <li
                key={service.service_id}
                className="border p-4 rounded-lg shadow-sm hover:shadow-md transition bg-gray-50"
              >
                <h3 className="text-xl font-semibold text-blue-600">
                  <FaTasks className="mr-2" />
                  {service.title}
                </h3>
                <p className="text-gray-600 mt-2">{service.description}</p>
                <p className="text-gray-700 mt-2 font-semibold">
                  Price: ${service.price}
                </p>
              </li>
            ))}
          </ul>
        </div>

        {/* Contact and Book Buttons */}
        <div className="flex justify-center space-x-4">
          <button className="flex items-center space-x-2 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition">
            <FaEnvelope className="inline-block" />
            <span>Contact</span>
          </button>
          <button
            className="flex items-center space-x-2 bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 transition"
            onClick={() => setIsBookingOpen(true)}
          >
            <FaTasks className="inline-block" />
            <span>Book a Session</span>
          </button>
        </div>

        {/* Booking Modal */}
        {isBookingOpen && (
          <BookingPage
            isOpen={isBookingOpen}
            onClose={() => setIsBookingOpen(false)}
            lawyerId={parseInt(lawyerId)}
          />
        )}
      </div>
    </div>
  );
};

export default LawyerProfilePage;
