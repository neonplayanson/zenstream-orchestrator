import "../../globals.css";
import React from "react";

import Head from "next/head";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "ZenStream | Login",
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
      <body className="bg-schemes-dark-surface-container-lowest flex flex-row h-screen w-full">
        {children}
      </body>
    </html>
  );
}
