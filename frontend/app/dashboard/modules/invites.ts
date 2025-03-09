const getCookie = (name: string) => {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop()?.split(";").shift();
};

async function generateInvite(): Promise<string | undefined> {
  try {
    const user = getCookie("Username");
    const token = getCookie("TOKEN");

    const response = await fetch(
      "http://127.0.0.1:5090/api/user/generate_invite",
      {
        method: "POST",
        headers: {
          Username: user || "",
          TOKEN: token || "",
        },
      },
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
