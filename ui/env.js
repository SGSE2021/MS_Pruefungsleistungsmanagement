export const DEVELOPMENT = "development";
export const PRODUCTION = "production";

export const ENV = process.env.NODE_ENV || DEVELOPMENT;

export const API_URL = ENV === DEVELOPMENT ? "http://localhost:8000" : "";
