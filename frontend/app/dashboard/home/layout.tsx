import "../../globals.css";
import React from "react";
import type { Metadata } from "next";

/**
 * Metadata for the home layout.
 */
export const metadata: Metadata = {
  title: "ZenStream | Dashboard",
};

export default function HomeLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="bg-black min-h-full w-full pl-24 pt-16">{children}</div>
  );
}
