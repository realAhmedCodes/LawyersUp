"use client";
import { useState, useEffect } from "react";
import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
} from "@/components/ui/dialog";
import { jwtDecode } from "jwt-decode";
import { useToast } from "@/hooks/use-toast";

type FormData = {
  startTime: string;
  endTime: string;
  userId: number;
  lawyerId: number;
};

type TokenData = {
  user_id: number;
};

export default function BookingPage({
  isOpen,
  onClose,
  lawyerId,
}: {
  isOpen: boolean;
  onClose: () => void;
  lawyerId: number;
}) {
  const { toast } = useToast();
  const [token, setToken] = useState<string | null>(null);
  const [userId, setUserId] = useState<number>(0);
  const [formData, setFormData] = useState<FormData>({
    startTime: "",
    endTime: "",
    userId: 0,
    lawyerId: lawyerId,
  });

  useEffect(() => {
    const tokenFromStorage = window.sessionStorage.getItem("token");
    if (tokenFromStorage) {
      setToken(tokenFromStorage);
      const decodedToken = jwtDecode<TokenData>(tokenFromStorage);
      setUserId(decodedToken.user_id);
      setFormData((prevData) => ({
        ...prevData,
        userId: decodedToken.user_id,
      }));
    }
  }, [lawyerId]);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const response = await fetch("http://localhost:5000/api/book", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    });

    if (response.ok) {
      toast({
        title: "Success",
        description: "Booking successful!",
      });
      onClose(); // Close modal on success
    } else {
      toast({
        title: "Error",
        description: "Booking didn't work!",
        variant: "destructive",
      });
    }
  };

  return (
    <Dialog open={isOpen} onOpenChange={onClose}>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Book Your Appointment</DialogTitle>
          <DialogDescription>
            Select a time to book an appointment with the lawyer.
          </DialogDescription>
        </DialogHeader>

        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="flex flex-col space-y-2">
            <Label htmlFor="startTime">Start Time</Label>
            <Input
              id="startTime"
              name="startTime"
              type="datetime-local" // Use datetime-local for better UX
              value={formData.startTime}
              onChange={handleInputChange}
            />
          </div>

          <div className="flex flex-col space-y-2">
            <Label htmlFor="endTime">End Time</Label>
            <Input
              id="endTime"
              name="endTime"
              type="datetime-local"
              value={formData.endTime}
              onChange={handleInputChange}
            />
          </div>

          <Button type="submit" className="w-full">
            Confirm Booking
          </Button>
        </form>
      </DialogContent>
    </Dialog>
  );
}
