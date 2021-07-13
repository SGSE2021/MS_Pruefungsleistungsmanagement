<template>
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant="miniVariant"
      :clipped="clipped"
      fixed
      app
    >
      <v-layout column wrap align-items-center>
        <v-icon x-large>mdi-school</v-icon>
        <h3 class="logo__text">ILIAS 2.0</h3>
      </v-layout>
      <v-list>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :href="item.to"
          router
          exact
        >
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>

        <v-list-item
          @click="loginDev()"
          router
          exact
          v-if="!isLoggedIn() && isDev"
        >
          <v-list-item-content>
            <v-list-item-title v-text="`Einloggen`" />
          </v-list-item-content>
        </v-list-item>

        <v-list-item
          :href="getLoginURL()"
          router
          exact
          v-if="!isLoggedIn() && !isDev"
        >
          <v-list-item-content>
            <v-list-item-title v-text="`Einloggen`" />
          </v-list-item-content>
        </v-list-item>

        <v-list-item @click="logout()" router exact v-if="isLoggedIn()">
          <v-list-item-content>
            <v-list-item-title v-text="`Ausloggen`" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar :clipped-left="clipped" fixed app>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <h2>Prüfungen</h2>
      <v-spacer></v-spacer>
      <user-menu :user="user"></user-menu>
    </v-app-bar>
    <v-main>
      <v-container>
        <nuxt />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import UserMenu from "../components/layout/UserMenu.vue";
import { DEV_ENV } from "../env";
import { LOGIN_ROUTE, LOGOUT_ROUTE } from "../src/constants";
import { getUserFromLocalStorage, isDev } from "../src/helperFunctions";
export default {
  components: { UserMenu },
  data() {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      user: null,
      isDev: isDev(),
      items: [
        {
          title: "Startseite",
          to: "https://sgse2021-ilias.westeurope.cloudapp.azure.com/users/"
        },

        {
          title: "Nachrichten",
          to: "https://sgse2021-ilias.westeurope.cloudapp.azure.com/messages/"
        },
        {
          title: "Kurse",
          to: "https://sgse2021-ilias.westeurope.cloudapp.azure.com/courses/"
        },
        {
          title: "Termine",
          to:
            "https://sgse2021-ilias.westeurope.cloudapp.azure.com/courses/appointments"
        },
        {
          title: "Prüfungen",
          to: "https://sgse2021-ilias.westeurope.cloudapp.azure.com/exams/"
        },
        {
          title: "Studierende",
          to:
            "https://sgse2021-ilias.westeurope.cloudapp.azure.com/users/students"
        },
        {
          title: "Lehrende",
          to:
            "https://sgse2021-ilias.westeurope.cloudapp.azure.com/users/lecturers"
        },

        {
          title: "Raumbuchung",
          to: "https://sgse2021-ilias.westeurope.cloudapp.azure.com/booking/"
        }
      ],
      accountMenuItems: [
        {
          title: "Mein Account"
        }
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: "ILIAS 2.0"
    };
  },
  mounted() {
    this.initialize();
  },
  methods: {
    initialize() {
      if (getUserFromLocalStorage() !== null) {
        if (Object.keys(getUserFromLocalStorage()).length > 0) {
          this.user = getUserFromLocalStorage();
        }
      } else {
        this.user = null;
      }
    },
    getLogStatus() {
      return this.user ? "Ausloggen" : "Einloggen";
    },
    getLoginURL() {
      if (this.user === null && !DEV_ENV) {
        return LOGIN_ROUTE;
      } else {
        return "/";
      }
    },
    loginDev() {
      if (this.user === null && DEV_ENV) {
        localStorage.setItem(
          "current-user",
          JSON.stringify({
            uid: "Hq8GJM8enJM4lwyVbmKSnoKA4Ox2",
            firstname: "Joyce",
            lastname: "Rafflenbeul",
            role: 1
          })
        );
        this.user = getUserFromLocalStorage();
      }
    },
    logout() {
      window.location.href = LOGOUT_ROUTE;
    },
    isLoggedIn() {
      return this.user === null ? false : true;
    }
  }
};
</script>

<style>
.logo__text,
.user--name {
  text-align: center;
}
</style>
