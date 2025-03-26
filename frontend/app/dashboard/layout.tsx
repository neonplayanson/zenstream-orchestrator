import "../globals.css";
import React from "react";
import Head from "next/head";
import type { Metadata } from "next";
import Header from "./components/header";
import Sidebar from "./components/sidebar";

import { GoHome, GoGear } from "react-icons/go";

/**
 * Metadata for the home layout.
 */
export const metadata: Metadata = {
  title: "ZenStream | Why are you here?",
};

/**
 * HomeLayout component that provides the layout for the home pages.
 * @param children - The child components to render inside the layout.
 * @returns A React element containing the home layout.
 */
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  //Tabs for the sidebar
  const tabs = [
    <GoHome key="home" className="text-white bg-transparent size-9" />,
    <GoGear key="settings" className="text-white bg-transparent size-9" />,
  ];

  return (
    <html lang="en">
      <Head>
        <link rel="icon" href="../../public/favicon.ico" />
      </Head>
      <body className="bg-transparent h-screen w-screen relative overflow-x-hidden">
        <Sidebar tabs={tabs} />
        <Header title="Home" icon={<GoHome className="page-icon" />} />
        {children}
      </body>
    </html>
  );
}
