"use client";
import Link from "next/link";
import { useEffect, useState } from "react";
import { Button } from "@/components/ui/button";
import {jwtDecode} from "jwt-decode"; // Ensure this is correctly installed via npm/yarn

type TokenData = {
  user_id: string;
  role: string;
  exp: number;
};

export default function Navbar() {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  const [token, setToken] = useState<string | null>(null);
  const [role, setRole] = useState<string | null>(null);

  // Handle dropdown toggle
  const handleDropdownToggle = () => {
    setIsDropdownOpen(!isDropdownOpen);
  };

  // Handle logout
  const logoutBtn = () => {
    window.sessionStorage.removeItem("token");
    setToken(null); // Clear the state
    setRole(null); // Clear the role
  };

  // Listen for sessionStorage changes
  useEffect(() => {
    const handleStorageChange = () => {
      const tokenFromStorage = window.sessionStorage.getItem("token");
      if (tokenFromStorage) {
        setToken(tokenFromStorage);
        const decodedToken = jwtDecode<TokenData>(tokenFromStorage);
        setRole(decodedToken.role);
      } else {
        setToken(null);
        setRole(null);
      }
    };

    // Call the handler initially to set the initial state
    handleStorageChange();

    // Attach storage event listener
    window.addEventListener("storage", handleStorageChange);

    // Cleanup listener on component unmount
    return () => {
      window.removeEventListener("storage", handleStorageChange);
    };
  }, []);

  return (
    <nav className="bg-navBlue  text-primary-foreground shadow-md px-8 py-4">
      <div className="container mx-auto flex justify-between items-center">
        {/* Logo */}
        <Link href="/" className="text-2xl font-bold text-white">
          LawyersUp
        </Link>

        {/* Navigation Links */}
        <div className="flex space-x-6">
          <Link href="/" className="text-white">
            Home
          </Link>
          <Link href="/pages/Post-Services" className="text-white">
            Post Services
          </Link>
          <Link href="/pages/Login" className="text-white">
            Login
          </Link>
        </div>

        {/* Account Dropdown */}
        <div className="relative">
          {token ? (
            <>
              <Button
                onClick={handleDropdownToggle}
                className="bg-secondary text-secondary-foreground px-4 py-2 rounded-md hover:bg-muted hover:text-muted-foreground"
              >
                Account
              </Button>
              {isDropdownOpen && (
                <div className="absolute right-0 mt-2 w-40 bg-card text-card-foreground border border-border rounded-md shadow-lg">
                  <Link
                    href="/profile"
                    className="block px-4 py-2 hover:bg-muted"
                  >
                    Profile
                  </Link>
                  <div
                    onClick={logoutBtn}
                    className="block px-4 py-2 hover:bg-muted cursor-pointer"
                  >
                    Logout
                  </div>
                </div>
              )}
            </>
          ) : (
            <>
              <Link href="/pages/Register" className="text-white">
                Register
              </Link>
            </>
          )}
        </div>
      </div>
    </nav>
  );
}
