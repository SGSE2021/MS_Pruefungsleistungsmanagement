import { DEV_ENV } from "../env";

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
      (JSON.parse(localStorage.getItem("current-user")).user === null ||
        Object.keys(JSON.parse(localStorage.getItem("current-user")).user)
          .length === 0)
    ) {
      localStorage.setItem(
        "current-user",
        JSON.stringify({
          user: {
            uid: "Hq8GJM8enJM4lwyVbmKSnoKA4Ox2",
            firstname: "Joyce",
            lastname: "Rafflenbeul",
            role: 1
          }
        })
      );
    }
    state.user = JSON.parse(localStorage.getItem("current-user")).user;
  },
  LOGOUT(state) {
    state.user = null;
  }
};
