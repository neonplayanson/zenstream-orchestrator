import { cookies } from "next/headers";

/**
 * Sets the cookies for the given username and token.
 *
 * @param {string} username - The username to set in the cookie.
 * @param {string} token - The token to set in the cookie.
 */
const setCookies = async (username: string, token: string) => {
  const cookieStore = await cookies();
  cookieStore.set("Username", username, {
    path: "/",
    sameSite: "lax",
    secure: process.env.NODE_ENV === "production",
  });
  cookieStore.set("TOKEN", token, {
    path: "/",
    sameSite: "lax",
    secure: process.env.NODE_ENV === "production",
  });
};

/**
 * Sets a cookie with the specified name and value, and optional path.
 *
 * @param {string} name - The name of the cookie.
 * @param {string} value - The value of the cookie.
 * @param {string} [path] - The path where the cookie is accessible.
 */
const setCookie = async (
  name: string,
  value: string,
  path?: string,
  sameSite?: boolean | "lax" | "strict" | "none",
  secure?: boolean,
) => {
  const cookieStore = await cookies();
  cookieStore.set(name, value, {
    path: path || "/",
    sameSite: (sameSite as "lax" | "strict" | "none") || "lax",
    secure: secure || process.env.NODE_ENV === "production",
  });
};

/**
 * Retrieves a cookie value by name.
 *
 * @param {string} name - The name of the cookie to retrieve.
 * @returns {Promise<string>} A promise that resolves to the cookie value.
 */
const getCookie = async (name: string) => {
  const cookieStore = await cookies();
  return cookieStore.get(name);
};

const cookieManager = { setCookies, getCookie, setCookie };

export default cookieManager;
