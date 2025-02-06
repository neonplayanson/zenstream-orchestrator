import React from "react";
import Image from "next/image";
import { MdSpaceDashboard } from "react-icons/md";

type TabParams = {
  icon: React.ReactElement;
  path: string;
};

function Logo({ icon }: { icon: string }) {
  return (
    <div className="items-center bg-opacity-0 p-3 order-first m-1">
      <Image
        src={icon}
        alt="icon"
        height={48}
        width={48}
        unoptimized={true}
        priority
      />
    </div>
  );
}

function Seperator() {
  return <div className="w-20 h-6 bg-opacity-0" />;
}

function Tab({ icon, path }: TabParams) {
  return (
    <div className="flex items-center justify-center relative size-12 hover:size-14 ease-out transition-all duration-150 group">
      <div className="absolute size-9 blur-none rounded-full group-hover:blur-md group-hover:bg-schemes-dark-onSurfaceVariant ease-out transition-all duration-150" />
      <a
        href={path}
        className="relative bg-schemes-dark-surfaceContainerLowest rounded-full size-12 flex items-center justify-center ease-out group-hover:size-14 group-hover:bg-schemes-dark-surfaceVariant transition-all duration-150"
      >
        {icon}
      </a>
    </div>
  );
}

export default function Navbar() {
  return (
    <div className="fixed flex flex-col bg-schemes-dark-background h-full w-20 items-center justify-start border-r-[1px] border-schemes-dark-surfaceContainerLow ">
      <Logo icon="/icons/icon.png" />
      <Seperator />
      <Tab
        icon={
          <MdSpaceDashboard className="size-8 text-schemes-dark-onBackground" />
        }
        path="/dashboard"
      />
    </div>
  );
}
