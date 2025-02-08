"use client";

import React, { ReactElement } from "react";
import { FaCopy } from "react-icons/fa";

function Greeting({ user }: { user: string }) {
  return (
    <h1 className="text-4xl text-schemes-dark-on-background w-full pl-16 pt-16 font-sans font-semibold">
      Welcome back, {user}
    </h1>
  );
}

function Gadget({
  title,
  icon,
  content,
}: {
  title: string;
  icon: ReactElement;
  content: React.ReactElement;
}) {
  return (
    <div className="flex gadget-desktop w-full h-auto flex-col">
      <div className="flex w-full h-auto flex-row justify-start items-center gap-3">
        <div className="pt-6 pl-8">{icon}</div>
        <div className="text-xl w-auto pt-6 font-sans font-medium text-schemes-dark-on-background">
          {title}
        </div>
      </div>
      <div className="h-auto w-full flex flex-col items-start justify-start gap-4 px-6">
        {content}
      </div>
    </div>
  );
}

//todo: support for syntax highlighting
function Codeblock({ code }: { code: string }) {
  return (
    <div className="flex flex-row h-12 w-full bg-schemes-dark-surface-dim shadow-inner shadow-schemes-dark-surface-container-lowest rounded-xl">
      <pre className="flex grow items-center px-4 overflow-x-scroll">
        <code className="text-schemes-dark-on-background bg-opacity-0 font-mono font-normal text-md whitespace-nowrap pt-1">
          {code}
        </code>
      </pre>
      <button
        type="button"
        className="flex items-center justify-center size-12 cursor-pointer"
      >
        <FaCopy className="size-5 text-schemes-dark-on-background bg-opacity-0" />
      </button>
    </div>
  );
}

function Checkbox({ label }: { label: string }) {
  return (
    <div className="flex flex-row items-center justify-start gap-2 mr-6 mb-4">
      <input
        type="checkbox"
        className="appearance-none w-6 h-6 border-2 border-transparent hover:border-opacity-100 hover:border-schemes-dark-primary shadow-inner shadow-schemes-dark-surface-container-lowest bg-schemes-dark-surface-dim rounded-md checked:shadow-none checked:bg-schemes-dark-primary transition-all duration-100"
      />
      <label className="text-schemes-dark-on-background font-sans font-medium text-lg w-28">
        {label}
      </label>
    </div>
  );
}

function Button({
  label,
  buttontype,
}: {
  label: string;
  buttontype: "button" | "submit" | "reset" | undefined;
}) {
  const handleClick = (event: React.MouseEvent<HTMLButtonElement>) => {
    event.preventDefault();
    //todo: generate api key
  };

  return (
    <button
      type={buttontype}
      className="px-4 w-auto h-12 bg-schemes-dark-primary text-schemes-dark-on-primary font-sans font-medium text-lg rounded-lg shadow-schemes-dark-surface-container-lowest hover:shadow-none hover:bg-schemes-dark-primary-hover transition-all duration-100 cursor-pointer"
      onClick={handleClick}
    >
      {label}
    </button>
  );
}

export { Greeting, Gadget, Codeblock, Checkbox, Button };
