// components/FilterForm.tsx

"use client";

import React, { useState } from "react";
import { useRouter } from "next/navigation";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";

interface FilterFormProps {
  initialFilters: {
    specialization: string;
    minExperience: number;
    maxHourlyRate: number;
    location: string;
  };
}

const FilterForm: React.FC<FilterFormProps> = ({ initialFilters }) => {
  const [inputFilters, setInputFilters] = useState(initialFilters);
  const router = useRouter();

  const handleInputFilterChange = (name: string, value: any) => {
    setInputFilters((prevFilters) => ({
      ...prevFilters,
      [name]: value,
    }));
  };

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();

    const queryParams: Record<string, string> = {};

    if (inputFilters.specialization) {
      queryParams.specialization = inputFilters.specialization;
    }
    if (inputFilters.minExperience > 0) {
      queryParams.minExperience = inputFilters.minExperience.toString();
    }
    if (inputFilters.maxHourlyRate > 0) {
      queryParams.maxHourlyRate = inputFilters.maxHourlyRate.toString();
    }
    if (inputFilters.location) {
      queryParams.location = inputFilters.location;
    }

    // Reset to first page on new search
    queryParams.page = "1";

    const queryString = new URLSearchParams(queryParams).toString();

    router.push(`/pages/lawyers?${queryString}`);
  };

  return (
    <div className="bg-white p-8 rounded-xl shadow-md mb-16">
      <form
        onSubmit={handleSearch}
        className="grid grid-cols-1 md:grid-cols-8 gap-6"
      >
        <div className="md:col-span-2">
          <Label
            htmlFor="specialization"
            className="block text-lg font-medium text-gray-700 mb-2"
          >
            Specialization
          </Label>
          <select
            id="specialization"
            value={inputFilters.specialization}
            onChange={(e) =>
              handleInputFilterChange("specialization", e.target.value)
            }
            className="block w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-gray-500 focus:border-gray-500 bg-gray-50"
          >
            <option value="">All Specializations</option>
            <option value="Criminal Law">Criminal Law</option>
            <option value="Family Law">Family Law</option>
            <option value="Corporate Law">Corporate Law</option>
          </select>
        </div>

        <div className="md:col-span-2">
          <Label
            htmlFor="minExperience"
            className="block text-lg font-medium text-gray-700 mb-2"
          >
            Minimum Experience (Years)
          </Label>
          <Input
            id="minExperience"
            type="number"
            placeholder="e.g., 5"
            value={inputFilters.minExperience}
            onChange={(e) =>
              handleInputFilterChange(
                "minExperience",
                parseInt(e.target.value) || 0
              )
            }
            className="block w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-gray-500 focus:border-gray-500 bg-gray-50"
            min={0}
          />
        </div>

        <div className="md:col-span-2">
          <Label
            htmlFor="maxHourlyRate"
            className="block text-lg font-medium text-gray-700 mb-2"
          >
            Maximum Hourly Rate ($)
          </Label>
          <Input
            id="maxHourlyRate"
            type="number"
            placeholder="e.g., 200"
            value={inputFilters.maxHourlyRate}
            onChange={(e) =>
              handleInputFilterChange(
                "maxHourlyRate",
                parseFloat(e.target.value) || 0
              )
            }
            className="block w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-gray-500 focus:border-gray-500 bg-gray-50"
            min={0}
          />
        </div>

        <div className="md:col-span-2">
          <Label
            htmlFor="location"
            className="block text-lg font-medium text-gray-700 mb-2"
          >
            Location
          </Label>
          <Input
            id="location"
            type="text"
            placeholder="e.g., New York"
            value={inputFilters.location}
            onChange={(e) =>
              handleInputFilterChange("location", e.target.value)
            }
            className="block w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-gray-500 focus:border-gray-500 bg-gray-50"
          />
        </div>

        <div className="md:col-span-2 flex items-end">
          <Button
            type="submit"
            className="w-full bg-green-600 hover:bg-green-700 text-white py-3 rounded-lg shadow-md transition duration-300"
          >
            Search
          </Button>
        </div>
      </form>
    </div>
  );
};

export default FilterForm;
