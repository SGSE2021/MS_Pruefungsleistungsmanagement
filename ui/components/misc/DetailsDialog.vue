<template>
  <v-row justify="center">
    <v-dialog v-model="detailsDialog" max-width="1000px" @input="closeDialog()">
      <v-card>
        <v-container>
          <v-card-title>
            <span class="text-h5">Details einsehen</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col cols="12" xs="12">
                  <single-assessment-table
                    :detailsItem="detailsItem"
                  ></single-assessment-table>
                </v-col>
                <v-col cols="12" xs="12">
                  <h3>Eingereichte Antworten</h3>
                  <v-list v-for="(question, i) in questions" :key="i">
                    <v-list-item>
                      <v-col>
                        <h5>Aufgabe {{ i + 1 }}: {{ question.question }}</h5>
                        <div v-if="question.is_multiple_choice">
                          <v-list v-for="(answer, x) in answers" :key="x">
                            <v-list-item
                              v-if="
                                answer.question_question_id ===
                                  question.question_id
                              "
                            >
                              <v-checkbox
                                :label="`${answer.answer_text}`"
                                v-model="answer.is_checked"
                                disabled
                              ></v-checkbox>
                            </v-list-item>
                          </v-list>
                        </div>
                        <div v-if="!question.is_multiple_choice">
                          <v-textarea
                            outlined
                            :value="`${question.answer}`"
                            disabled
                          ></v-textarea>
                        </div>
                      </v-col>
                    </v-list-item>
                  </v-list>
                </v-col>
                <v-col cols="12" xs="12">
                  <h3>Eingereichte Dokumente</h3>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-container>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import SingleAssessmentTable from "../layout/SingleAssessmentTable.vue";
import { API_URL } from "../../env";

export default {
  components: { SingleAssessmentTable },
  props: ["detailsDialog", "detailsItem"],
  data: () => ({
    // questions and answers for test purposes
    questions: [
      // {
      //   question_id: 1,
      //   question: "Test Question 1",
      //   is_multiple_choice: true,
      //   points: 20,
      //   answer: ""
      // },
      // {
      //   question_id: 2,
      //   question: "Test Question 2",
      //   is_multiple_choice: false,
      //   points: 15,
      //   answer: "Test Answer"
      // },
      // {
      //   question_id: 3,
      //   question: "Test Question 3",
      //   is_multiple_choice: true,
      //   points: 30,
      //   answer: ""
      // }
    ],
    answers: [
      // {
      //   question_question_id: 1,
      //   answer_text: "Test answer 1",
      //   is_correct: true,
      //   is_checked: false
      // },
      // {
      //   question_question_id: 1,
      //   answer_text: "Test answer 2",
      //   is_correct: false,
      //   is_checked: false
      // },
      // {
      //   question_question_id: 3,
      //   answer_text: "Test answer 3",
      //   is_correct: true,
      //   is_checked: true
      // }
    ]
  }),
  created() {
    this.initialize();
  },
  methods: {
    async initialize() {
      try {
        const { questions } = await this.$axios.$get(
          `${API_URL}/assessments/questions`
        );
        this.questions = questions;
      } catch (error) {
        console.error(error);
        this.errorSnackbar = true;
      }
    },
    closeDialog() {
      const closedDialog = false;
      this.$emit("update-details-dialog", closedDialog);
    }
  }
};
</script>
