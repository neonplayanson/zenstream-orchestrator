"use client";

import React from "react";

import { CiSearch } from "react-icons/ci";
import { RxHamburgerMenu } from "react-icons/rx";

/**
 * PageHeader component that provides the header for the dashboard pages.
 * @param title - The title of the page.
 * @returns A React element containing the page header.
 */
function PageHeader({
  title,
  icon,
}: {
  title: string;
  icon: React.ReactElement;
}) {
  return (
    <div className="flex flex-row ml-7 h-fit w-auto fixed bg-transparent items-center">
      {icon}
      <div className="text-white font-monterrat ml-2 text-md">{title}</div>
    </div>
  );
}

function SearchBar() {
  return (
    <div className="bg-neutral-950 drop-shadow-md shadow-white content-center rounded-full h-10 w-80 flex items-center ml-32">
      <CiSearch className="text-neutral-700 size-8 bg-transparent ml-5" />
      <input
        className="text-neutral-400 font-monterrat h-full w-full bg-transparent ml-2 rounded-full focus-within:outline-none"
        type="text"
        id="query"
        name="query"
        placeholder="Enter Search"
      />
    </div>
  );
}

function Header({ title, icon }: { title: string; icon: React.ReactElement }) {
  return (
    <div className="flex bg-black h-16 w-full items-center ml-24 fixed">
      <PageHeader title={title} icon={icon} />
      <div className="bg-transparent h-full w-7xl" />
      <SearchBar />
      <div className="bg-neutral-700 h-[1px] w-full mt-16 fixed" />
      <button className="bg-transparent size-9 cursor-pointer ml-7">
        <RxHamburgerMenu className="text-white bg-transparent size-full" />
      </button>
    </div>
  );
}

export default Header;
