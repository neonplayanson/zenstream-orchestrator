"use client";

import React, { useState } from "react";
import { FaKey } from "react-icons/fa";
import {
  Gadget,
  Greeting,
  Codeblock,
  Checkbox,
  Button,
} from "./components/page_util";
import generateInvite from "./modules/invites";

/**
 * Dashboard component that displays the main dashboard page.
 * @returns A React element containing the dashboard page.
 */
export default function Dashboard() {
  const [invite, setInvite] = useState<string>("ur mother");

  /**
   * Handles the generation of a new invite link.
   * Makes an asynchronous call to generate a unique invite code and
   * updates the invite state with a formatted registration URL.
   */
  const handleGenerateInvite = async () => {
    try {
      const newInvite = await generateInvite.generateInvite();
      setInvite(`http://127.0.0.1:3000/auth/register/${newInvite}`);
    } catch (error) {
      console.error("Error generating invite:", error);
    }
  };

  return (
    <div className="w-full h-screen bg-schemes-dark-surface-container-lowest items-start justify-start">
      <Greeting user="user" />
      <div className="grid grid-cols-1 md:grid-cols-2 items-start justify-center pt-16">
        <div className="flex flex-col items-start justify-start w-full h-full gap-9 singlecol-padding md:leftcol-padding">
          <Gadget
            title="Generate Orchestrator Invite"
            icon={<FaKey className="size-5 text-schemes-dark-on-background" />}
            content={
              <form
                method="POST"
                className="h-full w-full flex flex-col items-start justify-start gap-4 py-6"
              >
                <Codeblock code={invite} />
                <Button
                  label="Generate"
                  buttontype="submit"
                  onClick={handleGenerateInvite}
                />
              </form>
            }
          />
        </div>
        <div className="flex flex-col items-start justify-start w-full h-full gap-9 singlecol-padding md:rightcol-padding">
          <div className="gadget-desktop h-64" />
          <div className="gadget-desktop h-96" />
          <div className="gadget-desktop h-96" />
        </div>
      </div>
    </div>
  );
}
