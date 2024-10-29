// components/ui/badge.tsx

import React from "react";
import classNames from "classnames";

interface BadgeProps {
  variant?: "success" | "warning" | "danger" | "info";
  className?: string;
  children: React.ReactNode;
}

export const Badge: React.FC<BadgeProps> = ({
  variant = "info",
  className,
  children,
}) => {
  const baseClasses = "px-2 py-1 rounded-full text-sm font-medium";
  const variantClasses = {
    success: "bg-green-100 text-green-800",
    warning: "bg-yellow-100 text-yellow-800",
    danger: "bg-red-100 text-red-800",
    info: "bg-blue-100 text-blue-800",
  };
  return (
    <span
      className={classNames(baseClasses, variantClasses[variant], className)}
    >
      {children}
    </span>
  );
};
