<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <v-card>
        <v-card-title class="headline">
          ILIAS 2.0 Prüfungsleistungsmanagement
        </v-card-title>
        <v-card-text>
          <p>
            Das Prüfungsleistungsmanagement ermöglicht Studierenden die
            Teilnahme an Prüfungsleistungen in Form von Assessments, welche von
            Lehrenden angelegt und verwalted sowie von Verwaltenden eingesehen
            werden können.
          </p>
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn
            v-if="isLoggedIn"
            color="primary"
            nuxt
            @click="redirectToOverview()"
          >
            Zu der Übersicht
          </v-btn>
          <v-btn v-if="!isLoggedIn" color="primary" nuxt disabled>
            Bitte melden Sie sich an
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import Logo from "~/components/Logo.vue";
import VuetifyLogo from "~/components/VuetifyLogo.vue";
export default {
  components: {
    Logo,
    VuetifyLogo
  },
  data() {
    return {
      isLoggedIn: false
    };
  },
  mounted() {
    this.isLoggedIn = this.checkLogStatus();
  },
  methods: {
    checkLogStatus() {
      return this.$store.state.user !== null;
    },

    redirectToOverview() {
      this.$router.push("/overview");
    }
  }
};
</script>
