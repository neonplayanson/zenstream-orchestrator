import React from "react";
import Image from "next/image";
import { MdSpaceDashboard } from "react-icons/md";

type TabParams = {
  icon: React.ReactElement;
  path: string;
};

/**
 * Logo component that displays a logo image.
 * @param icon - The path to the logo image.
 * @returns A React element containing the logo image.
 */
function Logo({ icon }: { icon: string }) {
  return (
    <div className="items-center bg-opacity-0 p-3 order-first m-1">
      <Image
        src={icon}
        alt="icon"
        height={48}
        width={48}
        unoptimized
        priority
      />
    </div>
  );
}

/**
 * Seperator component that displays a separator.
 * @returns A React element containing the separator.
 */
function Seperator() {
  return <div className="w-20 h-6 bg-opacity-0" />;
}

/**
 * Tab component that displays a tab with an icon and a link.
 * @param icon - The icon to display inside the tab.
 * @param path - The path to navigate to when the tab is clicked.
 * @returns A React element containing the tab.
 */
function Tab({ icon, path }: TabParams) {
  return (
    <div className="flex items-center justify-center relative size-12 hover:size-14 ease-out transition-all duration-150 group">
      <div className="absolute size-9 blur-none rounded-full group-hover:blur-md group-hover:bg-schemes-dark-on-surface-variant ease-out transition-all duration-150" />
      <a
        href={path}
        className="relative bg-schemes-dark-surface-container-lowest rounded-full size-12 flex items-center justify-center ease-out group-hover:size-14 group-hover:bg-schemes-dark-surface-variant transition-all duration-150"
      >
        {icon}
      </a>
    </div>
  );
}

/**
 * Navbar component that displays the navigation bar.
 * @returns A React element containing the navigation bar.
 */
export default function Navbar() {
  return (
    <div className="fixed flex flex-col bg-schemes-dark-background h-full w-20 items-center justify-start border-r-[1px] border-schemes-dark-surface-container-low">
      <Logo icon="/icons/icon.png" />
      <Seperator />
      <Tab
        icon={
          <MdSpaceDashboard className="size-8 text-schemes-dark-on-background" />
        }
        path="/dashboard"
      />
    </div>
  );
}
