import { saveConfig } from "./actions";

interface AppConfig {
  environment: {
    development: string;
    production: string;
  };
  isDev: boolean;
  apiUrl: string;
  updateApiUrl(url: string): Promise<void>;
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
  async updateApiUrl(url: string): Promise<void> {
    this.environment.development = url;
    await saveConfig(this.environment);
    return Promise.resolve();
  },
};

export default appConfig;
