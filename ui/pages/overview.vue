<template>
  <v-container>
    <h1>Abgaben, Tests & Assessments</h1>
    <v-divider class="divider"></v-divider>
    <v-row>
      <v-col cols="12" xs="12" sm="12" md="6">
        <h3>Übersicht für Studierende/Lehrende</h3>
      </v-col>
      <v-col cols="12" xs="12" sm="12" md="6">
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
export default {
  components: { OverviewTable, CreateAssessmentDialog },
  data: () => ({
    createAssessmentDialog: false
  }),
  methods: {
    viewCreateAssessmentDialog() {
      this.createAssessmentDialog = true;
    },
    updateCreateAssessmentDialog(dialog) {
      this.createAssessmentDialog = dialog;
    }
  }
};
</script>

<style>
.divider {
  margin: 1em 0 1em 0;
}
</style>
