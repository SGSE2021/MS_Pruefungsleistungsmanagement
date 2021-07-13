<template>
  <v-data-table
    :headers="headers"
    :items="[detailsItem]"
    :items-per-page="1"
    :hide-default-footer="true"
    class="elevation-1"
  >
    <template v-slot:item.course="{ item }">
      {{ getCourseName() }}
    </template>
  </v-data-table>
</template>

<script>
export default {
  props: ["detailsItem", "courses"],
  data() {
    return {
      headers: [
        {
          text: "ID",
          align: "start",
          sortable: false,
          value: "assessment_id"
        },
        { text: "Thema/Bezeichnung", value: "topic" },
        { text: "Kurs", value: "course" },
        { text: "Startdatum", value: "start_date" },
        { text: "Enddatum", value: "end_date" },
        { text: "Status", value: "state" }
      ]
    };
  },
  methods: {
    getCourseName() {
      return this.courses.find(
        course => course.id === this.detailsItem.course_course_id
      ).name;
    }
  }
};
</script>
