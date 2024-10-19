"use client";
import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";

type FormData = {
  name: string;
  email: string;
  password: string;
  confirmPassword: string;
  role: "user" | "lawyer";
};

export default function RegisterPage() {
  const [formData, setFormData] = useState<FormData>({
    name: "",
    email: "",
    password: "",
    confirmPassword: "",
    role: "user", 
  });

  const handleInputChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>
  ) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    // Example: Basic form validation
    if (formData.password !== formData.confirmPassword) {
      alert("Passwords don't match!");
      return;
    }

    // Send form data to Flask backend
    const response = await fetch("http://localhost:5000/api/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    });

    const result = await response.json();
    console.log(result);
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100 p-4">
      <div className="bg-white shadow-lg rounded-lg p-8 max-w-lg w-full space-y-6">
        <h1 className="text-3xl font-semibold text-gray-800 text-center">
          Register
        </h1>
        <p className="text-gray-500 text-center">
          Create your account as a User or Lawyer.
        </p>

        <form onSubmit={handleSubmit} className="space-y-6">
          <div>
            <Label htmlFor="name" className="text-gray-600">
              Full Name
            </Label>
            <Input
              id="name"
              name="name"
              type="text"
              value={formData.name}
              onChange={handleInputChange}
              required
              className="mt-2"
            />
          </div>

          <div>
            <Label htmlFor="email" className="text-gray-600">
              Email
            </Label>
            <Input
              id="email"
              name="email"
              type="email"
              value={formData.email}
              onChange={handleInputChange}
              required
              className="mt-2"
            />
          </div>

          <div>
            <Label htmlFor="password" className="text-gray-600">
              Password
            </Label>
            <Input
              id="password"
              name="password"
              type="password"
              value={formData.password}
              onChange={handleInputChange}
              required
              className="mt-2"
            />
          </div>

          <div>
            <Label htmlFor="confirmPassword" className="text-gray-600">
              Confirm Password
            </Label>
            <Input
              id="confirmPassword"
              name="confirmPassword"
              type="password"
              value={formData.confirmPassword}
              onChange={handleInputChange}
              required
              className="mt-2"
            />
          </div>

          <div>
            <Label htmlFor="role" className="text-gray-600">
              Register as:
            </Label>
            <select
              id="role"
              name="role"
              value={formData.role}
              onChange={handleInputChange}
              className="mt-2 w-full p-2 border border-gray-300 rounded-lg"
            >
              <option value="user">User</option>
              <option value="lawyer">Lawyer</option>
            </select>
          </div>

          <Button type="submit" className="w-full py-3">
            Register
          </Button>
        </form>

        <p className="text-sm text-gray-500 text-center">
          Already have an account?{" "}
          <a href="/login" className="text-blue-500 hover:underline">
            Login here
          </a>
        </p>
      </div>
    </div>
  );
}
