// components/lawyer/ServicesSection.tsx

import React from "react";
import { FaTasks } from "react-icons/fa";
import { Card } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

interface Service {
  service_id: number;
  title: string;
  description: string;
  price: number;
}

interface ServicesSectionProps {
  services: Service[];
  onBook: () => void;
}

const ServicesSection: React.FC<ServicesSectionProps> = ({
  services,
  onBook,
}) => {
  return (
    <div className="bg-white shadow-md rounded-lg p-6">
      <h2 className="text-3xl font-bold mb-6">Services</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {services.map((service) => (
          <Card
            key={service.service_id}
            className="hover:shadow-xl transition-shadow p-4 rounded-lg border"
          >
            <h3 className="text-2xl font-semibold text-gray-800 flex items-center">
              <FaTasks className="mr-2 text-blue-500" />
              {service.title}
            </h3>
            <p className="mt-2 text-gray-600">{service.description}</p>
            <p className="mt-4 font-semibold text-lg text-green-600">
              ${service.price.toLocaleString()}
            </p>
            <Button
              variant="outline"
              className="mt-6 w-full"
              onClick={onBook}
              aria-label={`Book ${service.title}`}
            >
              Book Service
            </Button>
          </Card>
        ))}
      </div>
    </div>
  );
};

export default ServicesSection;
