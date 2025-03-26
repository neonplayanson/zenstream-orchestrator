"use client";

import React from "react";
import Image from "next/image";

function Tab({ icon }: { icon: React.ReactElement }) {
  return (
    <div className="flex h-16 w-16 items-center justify-center bg-transparent flex-col">
      {icon}
      <div className="bg-white h-0.5 w-3 rounded-full mt-1" />
    </div>
  );
}

/**
 * Sidebar component that provides the sidebar for the dashboard pages.
 * @returns A React element containing the sidebar.
 */
function Sidebar({ tabs }: { tabs: React.ReactElement[] }) {
  return (
    <div className="bg-black min-h-full w-24 justify-start items-center fixed flex flex-col">
      <Image
        src="/icons/icon.png"
        alt="icon"
        height={100}
        width={100}
        unoptimized
        priority
        className="mt-5 size-12"
      />
      <div className="flex flex-col h-12 w-24 bg-transparent" />
      <div className="flex flex-col h-full w-24 items-center justify-start bg-transparent">
        {tabs.map((tab, index) => (
          <Tab key={index} icon={tab} />
        ))}
      </div>
      <div className="bg-neutral-700 h-full w-[1px] ml-[95px] absolute" />
    </div>
  );
}

export default Sidebar;
