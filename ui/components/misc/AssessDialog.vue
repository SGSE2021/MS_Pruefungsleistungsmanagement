<template>
  <div>
    <v-row justify="center">
      <v-dialog
        v-model="assessDialog"
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
              >Abgabe, Test oder Assessment bewerten</v-toolbar-title
            >
            <v-spacer></v-spacer>
            <v-toolbar-items>
              <v-btn dark text @click="save()">
                Speichern
              </v-btn>
            </v-toolbar-items>
          </v-toolbar>
          <v-container>
            <h3>
              Dokumente und Daten für Abgabe "{{ detailsItem.topic }}" (ID:
              {{ detailsItem.assessment_id }}) bewerten
            </h3>
            <h5>Eingereichte Dokumente</h5>
            <v-list v-for="(doc, i) in documents" :key="i">
              <v-list-item>
                <a :href="doc.doc_data" target="_blank">
                  <v-icon small>mdi-arrow-collapse-down</v-icon>{{ " " }}
                  {{ doc.doc_name }}</a
                >
              </v-list-item>
            </v-list>
            <v-divider></v-divider>
            <h5>Eingereichte Antworten</h5>
            <v-list v-for="(question, i) in questions" :key="i">
              <v-list-item>
                <v-col>
                  <h5>Aufgabe {{ i + 1 }}: {{ question.question }}</h5>
                  <div v-if="question.is_multiple_choice">
                    <v-list v-for="(answer, x) in answers" :key="x">
                      <v-list-item
                        v-if="
                          answer.question_question_id === question.question_id
                        "
                      >
                        <v-checkbox
                          :label="`${answer.answer_text}`"
                          v-model="answer.is_checked"
                          disabled
                        ></v-checkbox>
                        <v-spacer></v-spacer>
                        <v-alert
                          text
                          :type="
                            `${
                              answer.is_checked === answer.is_correct
                                ? `success`
                                : `error`
                            }`
                          "
                          >{{
                            answer.is_checked === answer.is_correct
                              ? "Diese Antwort ist korrekt"
                              : "Diese Antwort ist falsch"
                          }}</v-alert
                        >
                      </v-list-item>
                    </v-list>
                  </div>
                  <div v-else>
                    <v-textarea
                      outlined
                      :value="`${question.answer}`"
                      disabled
                    ></v-textarea>
                  </div>
                  <v-spacer></v-spacer>
                  <v-text-field
                    v-model="question.reached_score"
                    type="number"
                    :label="`Punktzahl (max. ${question.points})`"
                    min="0"
                    :max="`${question.points}`"
                    outlined
                    :rules="[v => v && v >= 0, v => v && v <= question.points]"
                  ></v-text-field>
                </v-col>
              </v-list-item>
            </v-list>
          </v-container>
        </v-card>
      </v-dialog>
    </v-row>
  </div>
</template>

<script>
import { API_URL } from "../../env";
import { IS_RATED } from "../../src/constants";
export default {
  components: {},
  props: ["assessDialog", "detailsItem", "questions", "answers", "documents"],
  data: () => ({
    file: null,
    questions: [],
    answers: []
  }),
  methods: {
    closeDialog() {
      const closedDialog = false;
      this.$emit("update-assess-dialog", closedDialog);
    },
    async save() {
      try {
        for await (const question of this.questions) {
          await this.$axios.$put(
            `${API_URL}/assessments/questions/question/${question.question_id}`,
            {
              points: question.points,
              answer: question.answer,
              reached_score: question.reached_score
            }
          );
        }
        for await (const answer of this.answers) {
          if (answer?.answer_id) {
            await this.$axios.$put(
              `${API_URL}/assessments/questions/answers/answer/${answer.answer_id}`,
              {
                is_checked: answer.is_checked
              }
            );
          }
        }

        let rating = 0;

        this.questions.forEach(question => {
          rating = rating + question.reached_score;
        });

        await this.$axios.$put(
          `${API_URL}/assessments/${this.detailsItem.assessment_id}`,
          {
            topic: this.detailsItem.topic,
            state: IS_RATED,
            is_rated: true,
            max_rating: this.detailsItem.max_rating,
            rating: rating
          }
        );
        this.closeDialog();
      } catch (error) {
        console.error(error);
      }
    }
  }
};
</script>
