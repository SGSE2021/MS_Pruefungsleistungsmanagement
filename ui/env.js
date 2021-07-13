export const DEVELOPMENT = "development";

export const DEV_ENV = process.env.NODE_ENV === DEVELOPMENT;

export const API_URL = DEV_ENV
  ? "http://localhost:8000"
  : "https://sgse2021-ilias.westeurope.cloudapp.azure.com/exams-api/";
