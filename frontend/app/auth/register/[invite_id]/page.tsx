"use client";
import React, { useCallback, useState } from "react";
import Image from "next/image";
import { useRouter, usePathname } from "next/navigation";

/**
 * Register page component that displays the register form.
 * @returns A React element containing the register page.
 */
export default function Register() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const router = useRouter();
  const curpath = usePathname();
  const inviteId = curpath.split("/").pop() || "";

  const handleUsernameChange = useCallback(
    (e: React.ChangeEvent<HTMLInputElement>) => {
      setUsername(e.target.value);
    },
    []
  );

  const handlePasswordChange = useCallback(
    (e: React.ChangeEvent<HTMLInputElement>) => {
      setPassword(e.target.value);
    },
    []
  );

  const handleSubmit = useCallback(
    async (event: React.FormEvent<HTMLFormElement>) => {
      event.preventDefault();

      const response = await fetch("http://127.0.0.1:5090/api/user/register", {
        method: "POST",
        credentials: "include",
        headers: {
          Username: username,
          Password: password,
        },
      });

      if (response.status === 201) {
        document.cookie = `Username=${username}; path=/; SameSite=Lax`;
        const deletion = await fetch(
          "http://127.0.0.1:5090/api/user/delete_invite",
          {
            method: "DELETE",
            credentials: "include",
            headers: {
              url: inviteId,
            },
          }
        );
        if (deletion.status === 200) {
          router.push("/auth/login");
        } else {
          alert("An error occurred, please try again later.");
        }
      } else {
        alert("An error occurred, please try again later.");
      }
    },
    [username, password, inviteId, router]
  );

  return (
    <div className="flex w-full h-screen bg-linear-to-br from-schemes-dark-surface-container-lowest to-schemes-dark-medium-contrast-inverse-primary items-center justify-center">
      <div className="h-[292px] w-[388px] bg-clip-border bg-schemes-dark-surface-container-low rounded-xl flex flex-col items-center justify-center overflow-hidden relative shadow-md shadow-schemes-dark-surface-container-lowest">
        <div className="flex h-[600px] w-96 bg-conic rounded-xl from-transparent to-schemes-dark-on-background from-85% items-center justify-center absolute animate-spin-slow" />
        <form
          className="flex flex-col items-center justify-start h-auto w-96 bg-schemes-dark-surface-container-low rounded-xl relative gap-4 p-6"
          onSubmit={handleSubmit}
        >
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
            onChange={handleUsernameChange}
            required
          />
          <input
            type="password"
            placeholder="Password"
            className="appearance-none focus:outline-none bg-schemes-dark-surface-dim shadow-inner shadow-schemes-dark-surface-container-lowest rounded-xl text-schemes-dark-on-background bg-opacity-0 font-sans font-medium text-md whitespace-nowrap h-12 w-full pl-4"
            onChange={handlePasswordChange}
            required
          />
          <input
            type="submit"
            value="Register"
            className="cursor-pointer flex items-center justify-center h-12 w-full bg-schemes-dark-medium-contrast-inverse-primary shadow-md hover:shadow-sm shadow-schemes-dark-surface-container-lowest rounded-xl text-schemes-dark-on-background font-sans font-medium text-lg transition-all"
          />
        </form>
      </div>
    </div>
  );
}
