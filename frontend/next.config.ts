import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  redirects() {
    return Promise.resolve([
      {
        source: "/",
        destination: "/dashboard",
        permanent: false,
      },
    ]);
  },
};

export default nextConfig;
