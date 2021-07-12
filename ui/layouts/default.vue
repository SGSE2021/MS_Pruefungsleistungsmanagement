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

        <v-list-item @click="refresh()" router exact>
          <v-list-item-content>
            <v-list-item-title v-text="`Aktualisieren`" />
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
import { getUserFromLocalStorage, isDev } from "../src/helperFunctions";
import { mapActions } from "vuex";
export default {
  components: { UserMenu },
  data() {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      user: this.$store.state.user,
      isDev: isDev(),
      items: [
        {
          title: "Startseite",
          to: "/"
        },
        {
          title: "Mail",
          to: "/"
        },
        {
          title: "Kurse",
          to: "/"
        },
        {
          title: "Stundenplan",
          to: "/"
        },
        {
          title: "Prüfungen",
          to: "/"
        },
        {
          title: "Raumbuchung",
          to: "/"
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
    ...mapActions({
      switchPersistanceState: "switchPersistanceState"
    }),
    initialize() {
      if (getUserFromLocalStorage() !== null) {
        this.switchPersistanceState("LOGIN");
      }
    },
    getLogStatus() {
      return this.$store.state.user ? "Ausloggen" : "Einloggen";
    },
    getLoginURL() {
      if (this.$store.state.user === null && !DEV_ENV) {
        return "https://sgse2021-ilias.westeurope.cloudapp.azure.com/users/login?returnUrl=%2Fsettings";
      } else {
        return "/";
      }
    },
    loginDev() {
      if (this.$store.state.user === null && DEV_ENV) {
        this.switchPersistanceState("LOGIN");
        this.$router.go(0);
      }
    },
    logout() {
      if (this.$store.state.user !== null) {
        this.switchPersistanceState("LOGOUT");
        this.$router.go(0);
      }
    },
    isLoggedIn() {
      return this.$store.state.user === null ? false : true;
    },
    refresh() {
      this.$router.go(0);
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
