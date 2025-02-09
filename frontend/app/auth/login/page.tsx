"use client";
import React from "react";
import Image from "next/image";

/**
 * Login page component that displays the login form.
 * @returns A React element containing the login page.
 */
export default function Dashboard() {
  return (
    <div className="flex w-full h-screen bg-linear-to-br from-schemes-dark-surface-container-lowest to-schemes-dark-medium-contrast-inverse-primary items-center justify-center">
      <div className="h-[292px] w-[388px] bg-clip-border bg-schemes-dark-surface-container-low rounded-xl flex flex-col items-center justify-center overflow-hidden relative shadow-md shadow-schemes-dark-surface-container-lowest">
        <div className="flex h-[600px] w-96 bg-conic rounded-xl from-transparent to-schemes-dark-on-background from-85% items-center justify-center absolute animate-spin-slow"></div>
        <form className="flex flex-col items-center justify-start h-auto w-96 bg-schemes-dark-surface-container-low rounded-xl relative gap-4 p-6">
          <Image
            src="/icons/icon.png"
            alt="icon"
            height={48}
            width={48}
            unoptimized
            priority
          />
          <input
            type="text"
            placeholder="Username"
            className="appearance-none focus:outline-none bg-schemes-dark-surface-dim shadow-inner shadow-schemes-dark-surface-container-lowest rounded-xl text-schemes-dark-on-background bg-opacity-0 font-sans font-medium text-md whitespace-nowrap h-12 w-full pl-4"
            required
          />
          <input
            type="password"
            placeholder="Password"
            className="appearance-none focus:outline-none bg-schemes-dark-surface-dim shadow-inner shadow-schemes-dark-surface-container-lowest rounded-xl text-schemes-dark-on-background bg-opacity-0 font-sans font-medium text-md whitespace-nowrap h-12 w-full pl-4"
            required
          />
          <button
            type="submit"
            className="flex items-center justify-center h-12 w-full bg-schemes-dark-medium-contrast-inverse-primary shadow-md hover:shadow-sm shadow-schemes-dark-surface-container-lowest rounded-xl text-schemes-dark-on-background font-sans font-medium text-lg transition-all"
          >
            Login
          </button>
        </form>
      </div>
    </div>
  );
}
