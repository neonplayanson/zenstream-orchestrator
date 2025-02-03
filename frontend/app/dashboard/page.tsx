import React from "react";

function Greeting() {
  return (
    <h1 className="text-4xl text-schemes-dark-onBackground w-full pl-16 pt-16 font-mono font-normal">
      Welcome back, anson
    </h1>
  );
}

export default function Dashboard() {
  return (
    <div className="w-full h-screen bg-schemes-dark-surfaceContainerLowest items-start justify-start">
      <Greeting />
      <div className="grid grid-cols-1 md:grid-cols-2 items-start justify-center pt-16">
        <div className="flex flex-col items-start justify-start w-full h-full gap-9 singlecol-padding md:leftcol-padding">
          <div className="gadget-desktop h-[32rem]"></div>
          <div className="gadget-desktop h-96"></div>
        </div>
        <div className="flex flex-col items-start justify-start w-full h-full gap-9 singlecol-padding md:rightcol-padding">
          <div className="gadget-desktop h-64"></div>
          <div className="gadget-desktop h-96"></div>
        </div>
      </div>
    </div>
  );
}

//todo: single column layout
