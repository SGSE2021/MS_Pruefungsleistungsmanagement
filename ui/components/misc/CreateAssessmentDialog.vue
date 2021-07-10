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
              <v-btn dark text @click="save()">
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
                <v-text-field
                  v-model="topic"
                  label="Thema/Bezeichnung"
                ></v-text-field>
              </v-list-item>
              <v-list-item>
                <v-text-field
                  v-model="maxRating"
                  type="number"
                  min="0"
                  label="Maximale Punktzahl"
                ></v-text-field>
              </v-list-item>
              <v-list-item>
                <v-select :items="courses" label="Kurs" outlined></v-select>
              </v-list-item>
              <client-only placeholder="Loading...">
                <v-list-item>
                  <v-datetime-picker
                    label="Startzeit wählen"
                    v-model="startTime"
                    :dateFormat="dateFormat"
                    :timeFormat="timeFormat"
                  >
                  </v-datetime-picker>
                </v-list-item>
                <v-list-item>
                  <v-datetime-picker
                    label="Endzeit wählen"
                    v-model="endTime"
                    :dateFormat="dateFormat"
                    :timeFormat="timeFormat"
                  >
                  </v-datetime-picker>
                </v-list-item>
              </client-only>
              <v-list-item>
                <v-btn
                  v-if="assessmentSwitch"
                  :createTasksDialog="createTasksDialog"
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
      :assessmentQuestions="assessmentQuestions"
      :assessmentAnswers="assessmentAnswers"
      @update-create-tasks-dialog="updateCreateTasksDialog"
      @update-assessment-questions="updateAssessmentQuestions"
      @update-assessment-answers="updateAssessmentAnswers"
    ></create-tasks-dialog>
    <v-snackbar v-model="missingSnackbar">
      Es fehlen verpflichtende Angaben
      <template v-slot:action="{ attrs }">
        <v-btn
          color="pink"
          text
          v-bind="attrs"
          @click="missingSnackbar = false"
        >
          Schließen
        </v-btn>
      </template>
    </v-snackbar>
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
import CreateTasksDialog from "./CreateTasksDialog.vue";
import { API_URL } from "../../env";
import {
  IS_CREATED,
  DATE_FORMAT,
  TIME_FORMAT,
  DATE_FORMAT_MOMENT
} from "../../src/constants";
export default {
  components: { CreateTasksDialog },
  props: ["createAssessmentDialog"],
  data: () => ({
    createTasksDialog: false,
    assessmentSwitch: true,
    assessmentQuestions: [],
    assessmentAnswers: [],
    topic: "",
    maxRating: 0,
    courses: [
      "Methoden des Maschinellen Lernens",
      "Software Engineering",
      "Data Mining"
    ],
    startTime: "",
    endTime: "",
    errorSnackbar: false,
    missingSnackbar: false,
    dateFormat: DATE_FORMAT,
    timeFormat: TIME_FORMAT
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
    },
    updateAssessmentQuestions(questions) {
      this.assessmentQuestions = questions;
    },
    updateAssessmentAnswers(answers) {
      this.assessmentAnswers = answers;
    },
    validateInput() {
      let valid = true;
      if (
        this.topic === undefined ||
        this.topic === "" ||
        this.startTime === undefined ||
        this.startTime === "" ||
        this.endTime === undefined ||
        this.endTime === ""
      ) {
        valid = false;
      } else {
        valid = valid && true;
      }
      return valid;
    },
    async save() {
      if (this.validateInput()) {
        try {
          const { assessment_id } = await this.$axios.$post(
            `${API_URL}/assessments`,
            {
              course_course_id: "1",
              topic: this.topic,
              start_date: this.$moment(this.startTime).format(
                `${DATE_FORMAT_MOMENT} ${TIME_FORMAT}`
              ),
              end_date: this.$moment(this.endTime).format(
                `${DATE_FORMAT_MOMENT} ${TIME_FORMAT}`
              ),
              state: IS_CREATED,
              is_rated: false,
              max_rating: this.maxRating
            }
          );

          if (this.assessmentSwitch) {
            const assessmentId = assessment_id[0].assessment_id;

            for await (const question of this.assessmentQuestions) {
              const questionCopy = Object.assign({}, question);
              delete questionCopy.question_id;
              const { question_id } = await this.$axios.$post(
                `${API_URL}/assessments/questions`,
                {
                  ...questionCopy,
                  assessment_assessment_id: assessmentId
                }
              );
              const questionId = question_id[0].question_id;
              for await (const answer of this.assessmentAnswers) {
                if (
                  answer.question_question_id === question.question_id &&
                  question.is_multiple_choice
                ) {
                  const answerCopy = Object.assign({}, answer);
                  delete answerCopy.answer_id;
                  console.log(answerCopy);
                  await this.$axios.$post(
                    `${API_URL}/assessments/questions/answers`,
                    {
                      ...answerCopy,
                      question_question_id: questionId
                    }
                  );
                }
              }
            }
          }
        } catch (error) {
          console.error(error);
          this.errorSnackbar = true;
        }
        this.closeDialog();
        this.$router.go(0);
      }
    }
  }
};
</script>
