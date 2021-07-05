<template>
  <v-data-table
    :headers="headers"
    :items="[detailsItem]"
    :items-per-page="1"
    :hide-default-footer="true"
    class="elevation-1"
  >
  </v-data-table>
</template>

<script>
export default {
  props: ["detailsItem"],
  data: () => ({
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
      { text: "Status", value: "state" }
    ]
  }),
  methods: {}
};
</script>
