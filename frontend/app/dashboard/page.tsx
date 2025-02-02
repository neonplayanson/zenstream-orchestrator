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
      <div className="flex flex-row flex-wrap items-start justify-center gap-9 p-12">
        <div className="gadget-small"></div>
        <div className="gadget-small"></div>
        <div className="gadget-small"></div>
        <div className="gadget-small"></div>
        <div className="gadget-big"></div>
        <div className="gadget-big"></div>
      </div>
    </div>
  );
}
