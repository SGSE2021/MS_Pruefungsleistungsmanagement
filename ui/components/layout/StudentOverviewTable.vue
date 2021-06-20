<template>
  <v-data-table
    :headers="headers"
    :items="assessments"
    :items-per-page="5"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title>Meine Abgaben</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
      </v-toolbar>
    </template>
    <student-details-dialog
      v-bind="detailsDialog"
    ></student-details-dialog>
    <template v-slot:activator="{ on, attrs }">
      <v-btn color="red lighten-2" dark v-bind="attrs" v-on="on">
        Click Me
      </v-btn>
    </template>
    <template v-slot:item.details="{ item }">
      <v-btn @click="viewDetails(item)">
        einsehen
      </v-btn>
    </template>
    <template v-slot:item.submit="{ item }">
      <v-btn @click="submitAssessment(item)">
        einreichen
      </v-btn>
    </template>
  </v-data-table>
</template>

<script>
import StudentDetailsDialog from "../misc/StudentDetailsDialog.vue";
export default {
  components: { StudentDetailsDialog },
  data: () => ({
    detailsDialog: false,
    headers: [
      {
        text: "ID",
        align: "start",
        sortable: false,
        value: "id"
      },
      { text: "Thema/Bezeichnung", value: "topic" },
      { text: "Kurs", value: "course" },
      { text: "Startdatum", value: "start_date" },
      { text: "Enddatum", value: "end_date" },
      { text: "Status", value: "state" },
      { text: "Details", value: "details" },
      { text: "Abgaben", value: "submit" }
    ],
    assessments: [],
    detailsIndex: -1,
    detailsItem: {
      id: "",
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
    initialize() {
      this.assessments = [
        {
          id: "1",
          topic: "Praktikum 04",
          course: "Methoden des maschinellen Lernens",
          start_date: "01.06.2021 12:00 Uhr",
          end_date: "07.06.2021 13:00 Uhr",
          state: "abgeschlossen"
        }
      ];
    },

    viewDetails(item) {
      this.detailsIndex = this.assessments.indexOf(item);
      this.detailsItem = Object.assign({}, item);
      this.detailsDialog = true;
    },

    submitAssessment(item) {}
  }
};
</script>
