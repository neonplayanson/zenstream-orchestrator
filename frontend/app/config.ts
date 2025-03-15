import { saveConfig } from "./actions";

interface AppConfig {
  environment: {
    development: string;
    production: string;
  };
  isDev: boolean;
  apiUrl: string;
  updateApiUrl(url: string): void;
}

const isDev = process.env.NODE_ENV !== "production";

const appConfig: AppConfig = {
  environment: {
    development: "http://127.0.0.1:9090",
    production: "https://google.com",
  },
  isDev,
  get apiUrl() {
    return isDev ? this.environment.development : this.environment.production;
  },
  async updateApiUrl(url: string) {
    this.environment.development = url;
    await saveConfig(this.environment);
  },
};

export default appConfig;
