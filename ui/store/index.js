import { DEV_ENV } from "../env";
import { CURRENT_USER_ROLE } from "../src/constants";

export const state = () => ({
  user: null
});

export const getters = {};

export const actions = {
  switchPersistanceState({ commit }, payload) {
    switch (payload) {
      case "LOGIN":
        commit("LOGIN");
        break;
      case "LOGOUT":
        commit("LOGOUT");
        break;
    }
  }
};

export const mutations = {
  LOGIN(state) {
    if (
      DEV_ENV &&
      JSON.parse(localStorage.getItem("current-user")).user === null
    ) {
      localStorage.setItem(
        "current-user",
        JSON.stringify({
          uid: "Hq8GJM8enJM4lwyVbmKSnoKA4Ox2",
          firstname: "Joyce",
          lastname: "Rafflenbeul",
          role: CURRENT_USER_ROLE
        })
      );
    }
    state.user = JSON.parse(localStorage.getItem("current-user"));
  },
  LOGOUT(state) {
    state.user = null;
  }
};
