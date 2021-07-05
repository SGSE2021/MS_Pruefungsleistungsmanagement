<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="assessments"
      :items-per-page="5"
      class="elevation-1"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Abgaben</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
        </v-toolbar>
      </template>

      <template v-slot:item.details="{ item }">
        <v-btn @click.stop="viewDetails(item)">einsehen</v-btn>
      </template>
      <template v-slot:item.submit="{ item }">
        <v-btn @click="submitAssessment(item)">
          einreichen
        </v-btn>
      </template>
      <template v-slot:item.assess="{ item }">
        <v-btn @click.stop="assessAssessment(item)">bewerten</v-btn>
      </template>
    </v-data-table>
    <details-dialog
      :detailsDialog="detailsDialog"
      :detailsItem="detailsItem"
      @update-details-dialog="updateDetailsDialog"
    ></details-dialog>
    <submit-dialog
      :submitDialog="submitDialog"
      :detailsItem="detailsItem"
      @update-submit-dialog="updateSubmitDialog"
    ></submit-dialog>
    <assess-dialog
      :assessDialog="assessDialog"
      :detailsItem="detailsItem"
      @update-assess-dialog="updateAssessDialog"
    ></assess-dialog>
    <v-snackbar v-model="errorSnackbar">
      Es ist ein Fehler aufgetreten
      <template v-slot:action="{ attrs }">
        <v-btn color="pink" text v-bind="attrs" @click="errorSnackbar = false">
          Schließen
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script>
import DetailsDialog from "../misc/DetailsDialog.vue";
import SubmitDialog from "../misc/SubmitDialog.vue";
import AssessDialog from "../misc/AssessDialog.vue";
import { API_URL } from "../../env";
export default {
  components: { DetailsDialog, SubmitDialog, AssessDialog },
  data: () => ({
    detailsDialog: false,
    submitDialog: false,
    assessDialog: false,
    errorSnackbar: false,
    headers: [
      {
        text: "ID",
        align: "start",
        sortable: false,
        value: "assessment_id"
      },
      { text: "Thema/Bezeichnung", value: "topic" },
      { text: "Kurs", value: "course_course_id" },
      { text: "Startdatum", value: "start_date" },
      { text: "Enddatum", value: "end_date" },
      { text: "Status", value: "state" },
      { text: "Details", value: "details" },
      { text: "Abgabe", value: "submit" },
      { text: "Assessment", value: "assess" }
    ],
    assessments: [],
    detailsIndex: -1,
    detailsItem: {
      assessment_id: "",
      topic: "",
      course: "",
      start_date: "",
      end_date: "",
      state: ""
    }
  }),
  created() {
    this.initialize();
  },
  methods: {
    async initialize() {
      try {
        const { assessments } = await this.$axios.$get(
          `${API_URL}/assessments`
        );
        this.assessments = assessments;
      } catch (error) {
        console.error(error);
        this.errorSnackbar = true;
      }
    },

    viewDetails(item) {
      this.detailsIndex = this.assessments.indexOf(item);
      this.detailsItem = Object.assign({}, item);
      this.detailsDialog = true;
    },

    submitAssessment(item) {
      this.detailsIndex = this.assessments.indexOf(item);
      this.detailsItem = Object.assign({}, item);
      this.submitDialog = true;
    },

    assessAssessment(item) {
      this.detailsIndex = this.assessments.indexOf(item);
      this.detailsItem = Object.assign({}, item);
      this.assessDialog = true;
    },

    updateDetailsDialog(dialog) {
      this.detailsDialog = dialog;
    },
    updateSubmitDialog(dialog) {
      this.submitDialog = dialog;
    },
    updateAssessDialog(dialog) {
      this.assessDialog = dialog;
    }
  }
};
</script>
