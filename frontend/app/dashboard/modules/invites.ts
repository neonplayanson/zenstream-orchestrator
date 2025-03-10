import cookieManager from "../cookie_manager";

async function generateInvite(): Promise<string | undefined> {
  try {
    const user = await cookieManager.getCookie("Username");
    const token = await cookieManager.getCookie("TOKEN");

    const response = await fetch(
      "http://127.0.0.1:5090/api/user/generate_invite",
      {
        method: "POST",
        headers: {
          Username: String(user) || "",
          TOKEN: String(token) || "",
        },
      }
    );

    if (response.ok) {
      const data = await response.json();
      return data.inviteid;
    }
  } catch (error) {
    console.error(error);
  }
}

const invitesModule = { generateInvite };

export default invitesModule;
