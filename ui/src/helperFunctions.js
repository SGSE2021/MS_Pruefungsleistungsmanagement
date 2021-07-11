import { DEV_ENV } from "../env";

export const getUserFromLocalStorage = () => {
  return JSON.parse(localStorage.getItem("current-user"));
};

export const isDev = () => {
  return DEV_ENV;
};
