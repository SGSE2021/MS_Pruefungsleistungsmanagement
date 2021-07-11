<template>
  <v-container>
    <h1>Abgaben, Tests & Assessments</h1>
    <v-divider class="divider"></v-divider>
    <v-row>
      <v-col cols="12" xs="12" sm="12" md="6">
        <h3>Übersicht für {{ getCurrentRole() }}</h3>
      </v-col>
      <v-col cols="12" xs="12" sm="12" md="6" v-if="user.role === lecturerRole">
        <v-layout align-end justify-end>
          <v-btn @click.stop="viewCreateAssessmentDialog()"
            >Abgabe, Test oder Assessment erstellen</v-btn
          >
        </v-layout>
      </v-col>
    </v-row>
    <overview-table></overview-table>
    <create-assessment-dialog
      :createAssessmentDialog="createAssessmentDialog"
      @update-create-assessment-dialog="updateCreateAssessmentDialog"
    ></create-assessment-dialog>
  </v-container>
</template>

<script>
import OverviewTable from "../components/layout/OverviewTable.vue";
import CreateAssessmentDialog from "../components/misc/CreateAssessmentDialog.vue";
import { STUDENT, LECTURER, ADMINISTRATIVE } from "../src/constants";
export default {
  components: { OverviewTable, CreateAssessmentDialog },
  data() {
    return {
      createAssessmentDialog: false,
      user: this.$store.state.user ?? { role: -1 }
    };
  },
  mounted() {
    if (this.user.role === -1) {
      this.$router.push("/");
    }
  },
  methods: {
    viewCreateAssessmentDialog() {
      this.createAssessmentDialog = true;
    },
    updateCreateAssessmentDialog(dialog) {
      this.createAssessmentDialog = dialog;
    },
    getCurrentRole() {
      switch (this.user.role) {
        case STUDENT:
          return "Studierende";
        case LECTURER:
          return "Lehrende";
        case ADMINISTRATIVE:
          return "Administrative";
      }
    }
  }
};
</script>

<style>
.divider {
  margin: 1em 0 1em 0;
}
</style>
