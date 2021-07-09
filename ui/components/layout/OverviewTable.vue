<template>
  <div>
    <v-data-table
      v-if="assessments.length > 0"
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
        <v-btn
          @click="submitAssessment(item)"
          :disabled="item.state === isRated || item.state === isSubmitted"
        >
          einreichen
        </v-btn>
      </template>
      <template v-slot:item.assess="{ item }">
        <v-btn
          @click.stop="assessAssessment(item)"
          :disabled="item.state === isRated"
          >bewerten</v-btn
        >
      </template>
    </v-data-table>
    <details-dialog
      v-if="detailsItem.assessment_id"
      :detailsDialog="detailsDialog"
      :detailsItem="detailsItem"
      :questions="questions"
      :answers="answers"
      :documents="documents"
      @update-details-dialog="updateDetailsDialog"
    ></details-dialog>
    <submit-dialog
      :submitDialog="submitDialog"
      :detailsItem="detailsItem"
      :questions="questions"
      :answers="answers"
      @update-submit-dialog="updateSubmitDialog"
    ></submit-dialog>
    <assess-dialog
      :assessDialog="assessDialog"
      :detailsItem="detailsItem"
      :questions="questions"
      :answers="answers"
      :documents="documents"
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
import {
  ASSESS_DIALOG,
  DETAILS_DIALOG,
  SUBMIT_DIALOG,
  IS_CREATED,
  IS_SUBMITTED,
  IS_RATED
} from "../../src/constants";
export default {
  components: { DetailsDialog, SubmitDialog, AssessDialog },
  data: () => ({
    detailsDialog: false,
    submitDialog: false,
    assessDialog: false,
    errorSnackbar: false,
    isCreated: IS_CREATED,
    isSubmitted: IS_SUBMITTED,
    isRated: IS_RATED,
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
    questions: [],
    answers: [],
    documents: [],
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

    async fetchData(dialogType) {
      try {
        const { questions } = await this.$axios.$get(
          `${API_URL}/assessments/questions/${this.detailsItem.assessment_id}`
        );
        this.questions = questions;

        let answersCopy = [];
        for await (const q of this.questions) {
          const { answers } = await this.$axios.$get(
            `${API_URL}/assessments/questions/answers/${q.question_id}`
          );
          answersCopy = answersCopy.concat(answers);
        }
        this.answers = answersCopy;

        const { documents } = await this.$axios.$get(
          `${API_URL}/assessments/documents/${this.detailsItem.assessment_id}`
        );
        this.documents = documents;
        switch (dialogType) {
          case DETAILS_DIALOG:
            this.detailsDialog = true;
            break;
          case SUBMIT_DIALOG:
            this.submitDialog = true;
            break;
          case ASSESS_DIALOG:
            this.assessDialog = true;
            break;
          default:
            break;
        }
      } catch (error) {
        console.error(error);
        this.errorSnackbar = true;
      }
    },
    async viewDetails(item) {
      this.detailsIndex = this.assessments.indexOf(item);
      this.detailsItem = Object.assign({}, item);
      this.fetchData(DETAILS_DIALOG);
    },

    async submitAssessment(item) {
      this.detailsIndex = this.assessments.indexOf(item);
      this.detailsItem = Object.assign({}, item);
      this.fetchData(SUBMIT_DIALOG);
    },

    async assessAssessment(item) {
      this.detailsIndex = this.assessments.indexOf(item);
      this.detailsItem = Object.assign({}, item);
      this.fetchData(ASSESS_DIALOG);
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
