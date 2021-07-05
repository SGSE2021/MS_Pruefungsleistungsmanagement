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
              <v-btn dark text @click="dialog = false">
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
                        ></v-checkbox>
                      </v-list-item>
                    </v-list>
                  </div>
                  <div v-if="!question.is_multiple_choice">
                    <v-textarea outlined placeholder="Antwort eingeben"></v-textarea></div
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
export default {
  components: {},
  props: ["submitDialog", "detailsItem"],
  data: () => ({
    file: null,
    // questions and answers for test purposes
    questions: [
      {
        question_id: 1,
        question: "Test Question 1",
        is_multiple_choice: true,
        points: 20,
        answer: ""
      },
      {
        question_id: 2,
        question: "Test Question 2",
        is_multiple_choice: false,
        points: 15,
        answer: "Test Answer"
      },
      {
        question_id: 3,
        question: "Test Question 3",
        is_multiple_choice: true,
        points: 30,
        answer: ""
      }
    ],
    answers: [
      {
        question_question_id: 1,
        answer_text: "Test answer 1",
        is_correct: true
      },
      {
        question_question_id: 1,
        answer_text: "Test answer 2",
        is_correct: false
      },
      {
        question_question_id: 3,
        answer_text: "Test answer 3",
        is_correct: true
      }
    ]
  }),
  methods: {
    closeDialog() {
      const closedDialog = false;
      this.$emit("update-submit-dialog", closedDialog);
    }
  }
};
</script>
