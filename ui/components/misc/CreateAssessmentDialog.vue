<template>
  <div>
    <v-row justify="center">
      <v-dialog
        v-model="createAssessmentDialog"
        fullscreen
        hide-overlay
        transition="dialog-bottom-transition"
        @input="closeDialog()"
      >
        <v-card>
          <v-toolbar dark color="primary">
            <v-btn icon dark @click="closeDialog()">
              <v-icon>mdi-close</v-icon>
            </v-btn>
            <v-toolbar-title
              >Abgabe, Test oder Assessment anlegen</v-toolbar-title
            >
            <v-spacer></v-spacer>
            <v-toolbar-items>
              <v-btn dark text @click="dialog = false">
                Speichern
              </v-btn>
            </v-toolbar-items>
          </v-toolbar>
          <v-container>
            <v-list three-line subheader>
              <v-list-item>
                <template>
                  <v-container class="px-0" fluid>
                    <v-switch
                      v-model="assessmentSwitch"
                      :label="`Assessment/Test`"
                    ></v-switch>
                  </v-container>
                </template>
              </v-list-item>
              <v-list-item>
                <v-text-field label="Thema/Bezeichnung"></v-text-field>
              </v-list-item>
              <v-list-item>
                <v-select :items="courses" label="Kurs" outlined></v-select>
              </v-list-item>
              <client-only placeholder="Loading...">
                <v-list-item>
                  <v-datetime-picker
                    label="Startzeit wählen"
                    v-model="startTime"
                  >
                  </v-datetime-picker>
                </v-list-item>
                <v-list-item>
                  <v-datetime-picker label="Endzeit wählen" v-model="endTime">
                  </v-datetime-picker>
                </v-list-item>
              </client-only>
              <v-list-item>
                <v-btn
                  v-if="assessmentSwitch"
                  @click.stop="viewCreateTasksDialog()"
                  >Aufgaben anlegen</v-btn
                >
              </v-list-item>
            </v-list>
          </v-container>
        </v-card>
      </v-dialog>
    </v-row>
    <create-tasks-dialog
      :createTasksDialog="createTasksDialog"
      @update-create-tasks-dialog="updateCreateTasksDialog"
    ></create-tasks-dialog>
  </div>
</template>

<script>
import CreateTasksDialog from "./CreateTasksDialog.vue";

export default {
  components: { CreateTasksDialog },
  props: ["createAssessmentDialog"],
  data: () => ({
    createTasksDialog: false,
    assessmentSwitch: true,
    courses: [
      "Methoden des Maschinellen Lernens",
      "Software Engineering",
      "Data Mining"
    ],
    startTime: "",
    endTime: ""
  }),
  methods: {
    closeDialog() {
      const closedDialog = false;
      this.$emit("update-create-assessment-dialog", closedDialog);
    },
    viewCreateTasksDialog() {
      this.createTasksDialog = true;
    },
    updateCreateTasksDialog(dialog) {
      this.createTasksDialog = dialog;
    }
  }
};
</script>
