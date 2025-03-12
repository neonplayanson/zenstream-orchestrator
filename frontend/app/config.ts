interface Environment {
  frontend: string;
  backend: string;
}

interface AppConfig {
  environment: {
    development: Environment;
    production: Environment;
  };
  isDev: boolean;
  apiUrl: string;
  frontendUrl: string;
}

const isDev = process.env.NODE_ENV !== "production";

const appConfig: AppConfig = {
  environment: {
    development: {
      frontend: "http://127.0.0.1:3000",
      backend: "http://127.0.0.1:9090",
    },
    production: {
      frontend: "https://google.com",
      backend: "https://google.com",
    },
  },
  isDev,
  get apiUrl() {
    return isDev
      ? this.environment.development.backend
      : this.environment.production.backend;
  },
  get frontendUrl() {
    return isDev
      ? this.environment.development.frontend
      : this.environment.production.frontend;
  },
};

export default appConfig;
