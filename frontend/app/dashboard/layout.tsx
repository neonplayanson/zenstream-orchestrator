import "./globals.css";
import React from "react";
import Navbar from "./components/sidebar";
import Head from "next/head";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "ZenStream | Dashboard",
};

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <Head>
        <link rel="icon" href="../../public/favicon.ico" />
      </Head>
      <body className="bg-schemes-dark-surfaceContainerLowest flex flex-row h-screen w-full">
        <Navbar />
        <div className="flex-grow ml-20">{children}</div>
      </body>
    </html>
  );
}
