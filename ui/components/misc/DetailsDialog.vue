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
                    :courses="courses"
                  ></single-assessment-table>
                </v-col>
                <v-col cols="12" xs="12" v-if="detailsItem.is_rated">
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
                <v-col cols="12" xs="12" v-if="detailsItem.is_rated">
                  <h3>Eingereichte Dokumente</h3>
                  <v-list v-for="(doc, i) in documents" :key="i">
                    <v-list-item>
                      <a :href="doc.doc_data" target="_blank">
                        <v-icon small>mdi-arrow-collapse-down</v-icon>{{ " " }}
                        {{ doc.doc_name }}</a
                      >
                    </v-list-item>
                  </v-list>
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

export default {
  components: { SingleAssessmentTable },
  props: [
    "detailsDialog",
    "detailsItem",
    "questions",
    "answers",
    "documents",
    "courses"
  ],
  data: () => ({}),
  methods: {
    closeDialog() {
      const closedDialog = false;
      this.$emit("update-details-dialog", closedDialog);
    }
  }
};
</script>
