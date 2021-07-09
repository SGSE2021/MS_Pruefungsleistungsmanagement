<template>
  <div>
    <v-row justify="center">
      <v-dialog
        v-model="submitDialog"
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
              >Abgabe, Test oder Assessment einreichen</v-toolbar-title
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
              {{ detailsItem.assessment_id }}) einreichen
            </h3>
            <v-file-input
              label="Dokument (.pdf) hochladen"
              accept=".pdf"
              v-model="file"
            ></v-file-input>
            <v-divider></v-divider>
            <h3>Zu beantwortende Fragen</h3>
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
                        ></v-checkbox>
                      </v-list-item>
                    </v-list>
                  </div>
                  <div v-else>
                    <v-textarea
                      outlined
                      placeholder="Antwort eingeben"
                      v-model="question.answer"
                    ></v-textarea></div
                ></v-col>
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
import { IS_SUBMITTED } from "../../src/constants";
export default {
  components: {},
  props: ["submitDialog", "detailsItem", "questions", "answers"],
  data: () => ({
    file: null
  }),
  methods: {
    closeDialog() {
      const closedDialog = false;
      this.$emit("update-submit-dialog", closedDialog);
    },
    convertToBase64(file) {
      return new Promise(resolve => {
        var fileReader = new FileReader();
        var base64;
        fileReader.onload = function(fileLoadedEvent) {
          base64 = fileLoadedEvent.target.result;
          resolve(base64);
        };
        fileReader.readAsDataURL(file);
      });
    },
    async save() {
      try {
        if (this.file) {
          const base64 = await this.convertToBase64(this.file);
          await this.$axios.$post(`${API_URL}/assessments/documents`, {
            assessment_assessment_id: this.detailsItem.assessment_id,
            doc_name: this.file.name,
            doc_data: base64
          });
        }
        console.log(this.detailsItem, IS_SUBMITTED);
        await this.$axios.$put(
          `${API_URL}/assessments/${this.detailsItem.assessment_id}`,
          {
            topic: this.detailsItem.topics,
            state: IS_SUBMITTED,
            is_rated: this.detailsItem.is_rated,
            max_rating: this.detailsItem.max_rating,
            rating: this.detailsItem.rating
          }
        );
        for await (const question of this.questions) {
          await this.$axios.$put(
            `${API_URL}/assessments/questions/question/${question.question_id}`,
            {
              points: question.points,
              answer: question.answer,
              reached_score: 0
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
        this.closeDialog();
        this.$router.go(0);
      } catch (error) {
        console.error(error);
      }
    }
  }
};
</script>
