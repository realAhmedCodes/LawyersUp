"use client"
import React from 'react'
import { useState, useEffect } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Label } from "@/components/ui/label";
import { useToast } from "@/hooks/use-toast";
import Navbar from '@/app/components/navbar';
import {jwtDecode} from "jwt-decode"
type ServiceData={
title: string;
description: string;
price: number;
}

const getLawyerId=()=>
{
    const token = sessionStorage.getItem('token')
    if(token){
        const decodedToken: any= jwtDecode(token)
        return decodedToken.lawyer_id;
    }
    return null;
}




export default function page() {
  const { toast } = useToast();
  const [services, setServices] = useState<ServiceData[]>([
    { title: "", description: "", price: 0 },
  ]);


const handleInputChange= (index: number, e:React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>)=>{
    const{name, value}= e.target;
    const updatedServices=[...services]
    updatedServices[index] ={...updatedServices[index], [name]: value}
    setServices(updatedServices)
}

const addServiceField=()=>{
    setServices([...services, {title: "", description: "", price: 0}])
}
 const handleSubmit = async () => {
  const lawyerId= getLawyerId()
  if(!lawyerId){
    toast({
      title: "Error",
      description: "Unauthorized",
      variant: "destructive",
    });
    return
  }

   // Submit service data to the backend
   const response = await fetch("http://localhost:5000/api/servicesPost", {
     method: "POST",
     headers: {
       "Content-Type": "application/json",
     },
     body: JSON.stringify({ services, lawyer_id: lawyerId }),
   });

   if (response.ok) {
     toast({
       title: "Success",
       description: "Services added successfully!",
     });
   } else {
     toast({
       title: "Error",
       description: "Failed to add services",
       variant: "destructive",
     });
   }
 };

  return (
    <div>
        <Navbar></Navbar>
      <div className="container mx-auto p-4">
        <h1 className="text-2xl font-bold mb-4">Add Your Services</h1>

        {/* Services Input */}
        {services.map((service, index) => (
          <div key={index} className="mb-6">
            <Label htmlFor={`title-${index}`}>Service Title</Label>
            <Input
              id={`title-${index}`}
              name="title"
              type="text"
              placeholder="Service Title"
              value={service.title}
              onChange={(e) => handleInputChange(index, e)}
              required
            />
            <Label htmlFor={`description-${index}`} className="mt-2">
              Service Description
            </Label>
            <Textarea
              id={`description-${index}`}
              name="description"
              placeholder="Describe your service"
              value={service.description}
              onChange={(e) => handleInputChange(index, e)}
              required
            />
            <Label htmlFor={`price-${index}`} className="mt-2">
              Price
            </Label>
            <Input
              id={`price-${index}`}
              name="price"
              type="number"
              placeholder="Service Price"
              value={service.price}
              onChange={(e) => handleInputChange(index, e)}
              required
            />
          </div>
        ))}

        {/* Add Another Service */}
        <Button onClick={addServiceField} className="mr-4">
          Add Another Service
        </Button>

        {/* Submit Services */}
        <Button
          onClick={handleSubmit}
          className="bg-primary text-primary-foreground"
        >
          Submit Services
        </Button>
      </div>
    </div>
  );
}