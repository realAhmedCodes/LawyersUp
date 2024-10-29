
import React from "react";
import {
  FaGraduationCap,
  FaBriefcase,
  FaMoneyCheckAlt,
  FaCalendarAlt,
} from "react-icons/fa";

interface AboutSectionProps {
  bio: string;
  education?: string;
  experience: number;
  hourlyRate: number;
  availability: { [key: string]: string };
}

const AboutSection: React.FC<AboutSectionProps> = ({
  bio,
  education,
  experience,
  hourlyRate,
  availability,
}) => {
  return (
    <div className="bg-white shadow-md rounded-lg p-6">
      <h2 className="text-3xl font-bold mb-6">About</h2>
      <p className="text-gray-700 mb-6">{bio || "No bio available."}</p>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="flex items-center">
          <FaGraduationCap className="mr-2 text-gray-600" />
          <span>
            <strong>Education:</strong> {education || "Not specified"}
          </span>
        </div>
        <div className="flex items-center">
          <FaBriefcase className="mr-2 text-gray-600" />
          <span>
            <strong>Experience:</strong> {experience} years
          </span>
        </div>
        <div className="flex items-center">
          <FaMoneyCheckAlt className="mr-2 text-gray-600" />
          <span>
            <strong>Hourly Rate:</strong> ${hourlyRate}/hr
          </span>
        </div>
        <div className="flex items-center">
          <FaCalendarAlt className="mr-2 text-gray-600" />
          <span>
            <strong>Availability:</strong>{" "}
            {availability
              ? Object.entries(availability)
                  .map(([day, time]) => `${day}: ${time}`)
                  .join(", ")
              : "Not specified"}
          </span>
        </div>
      </div>
    </div>
  );
};

export default AboutSection;
