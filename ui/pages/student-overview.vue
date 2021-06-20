<template>
  <v-container>
    <h1>Abgaben, Tests & Assessments</h1>
    <v-divider class="divider"></v-divider>
    <h3>Übersicht für Studierende</h3>
    <student-overview-table></student-overview-table>
  </v-container>
</template>

<script>
import StudentOverviewTable from "../components/layout/StudentOverviewTable.vue";
export default {
  components: { StudentOverviewTable }
};
</script>

<style>
.divider {
  margin: 1em 0 1em 0;
}
</style>
