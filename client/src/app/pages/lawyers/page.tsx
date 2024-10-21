// /pages/lawyers/index.tsx
"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { Card } from "@/components/ui/card";
import { useToast } from "@/hooks/use-toast";
import Navbar from "@/app/components/navbar";
import { FaUserTie, FaBriefcase, FaClock } from "react-icons/fa"; // Icons from react-icons

interface Lawyer {
  lawyer_id: number;
  name: string;
  specialization: string;
  experience: number;
  hourly_rate: number;
}

const LawyersListPage = () => {
  const [lawyers, setLawyers] = useState<Lawyer[]>([]);
  const { toast } = useToast();

  useEffect(() => {
    fetchLawyers();
  }, []);

  const fetchLawyers = async () => {
    try {
      const response = await fetch("http://localhost:5000/api/lawyers");
      if (!response.ok) {
        throw new Error("Failed to fetch lawyers");
      }
      const data = await response.json();
      setLawyers(data.lawyers);
    } catch (error) {
      toast({
        title: "Error",
        description: "Failed to load lawyers",
        variant: "destructive",
      });
    }
  };

  return (
    <div>
      <Navbar />
      <div className="bg-gray-100 min-h-screen py-10">
        <div className="container mx-auto px-4">
          <h1 className="text-4xl font-bold text-center text-gray-800 mb-10">
            Find the Right Lawyer
          </h1>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {lawyers.map((lawyer) => (
              <Card
                key={lawyer.lawyer_id}
                className="p-6 bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300"
              >
                <div className="flex items-center space-x-4">
                  <FaUserTie className="text-blue-500 text-3xl" />
                  <h2 className="text-2xl font-semibold text-gray-800">
                    {lawyer.name}
                  </h2>
                </div>
                <div className="mt-4">
                  <div className="flex items-center space-x-2">
                    <FaBriefcase className="text-gray-500" />
                    <p className="text-gray-600">
                      <strong>Specialization:</strong> {lawyer.specialization}
                    </p>
                  </div>
                  <div className="flex items-center space-x-2 mt-2">
                    <FaClock className="text-gray-500" />
                    <p className="text-gray-600">
                      <strong>Experience:</strong> {lawyer.experience} years
                    </p>
                  </div>
                </div>
                <Link
                  href={`/pages/lawyers/${lawyer.lawyer_id}`}
                  className="inline-block mt-4 text-blue-500 hover:text-blue-600 font-medium transition-colors"
                >
                  View Profile
                </Link>
              </Card>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default LawyersListPage;
