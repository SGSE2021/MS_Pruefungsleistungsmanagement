<template>
  <v-row justify="center">
    <v-dialog
      v-model="createTasksDialog"
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
          <v-toolbar-title>Aufgaben anlegen</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-toolbar-items>
            <v-btn dark text @click="save()">
              Speichern
            </v-btn>
          </v-toolbar-items>
        </v-toolbar>
        <v-container>
          <v-list v-for="(question, i) in questions" :key="i">
            <v-list-item>
              <v-card width="100%">
                <v-card-text>
                  <v-text-field
                    label="Frage"
                    v-model="question.question"
                  ></v-text-field>
                  <v-text-field
                    label="Punktzahl"
                    v-model="question.points"
                  ></v-text-field>
                  <v-row>
                    <v-switch
                      v-model="question.is_multiple_choice"
                      :label="`Multiple Choice`"
                    ></v-switch
                    ><v-spacer></v-spacer>
                    <v-btn @click="removeTask(i)"
                      ><v-icon>
                        mdi-delete
                      </v-icon></v-btn
                    ></v-row
                  >
                  <v-divider v-if="question.is_multiple_choice"></v-divider>
                  <div v-if="question.is_multiple_choice">
                    <v-list v-for="(answer, x) in answers" :key="x">
                      <!-- List of answers-->
                      <v-list-item
                        v-if="
                          answer.question_question_id === question.question_id
                        "
                      >
                        <v-row align="center">
                          <v-text-field
                            label="Multiple Choice Antwort eingeben"
                            v-model="answer.answer_text"
                          ></v-text-field>
                          <v-spacer></v-spacer>
                          <v-switch
                            v-model="answer.is_correct"
                            :label="`Richtige Antwort?`"
                          ></v-switch>
                          <v-spacer></v-spacer>
                          <v-btn @click="removeAnswer(x)"
                            ><v-icon>
                              mdi-delete
                            </v-icon></v-btn
                          >
                        </v-row>
                      </v-list-item>
                    </v-list>
                    <v-btn @click="addAnswer(question.question_id)"
                      >Antwort hinzufügen</v-btn
                    >
                  </div>
                </v-card-text>
              </v-card>
            </v-list-item>
          </v-list>
          <v-btn @click="addTask()">Aufgabe hinzufügen</v-btn>
        </v-container>
      </v-card>
    </v-dialog>
    <v-snackbar v-model="errorSnackbar">
      Es fehlen verpflichtende Angaben
      <template v-slot:action="{ attrs }">
        <v-btn color="pink" text v-bind="attrs" @click="errorSnackbar = false">
          Schließen
        </v-btn>
      </template>
    </v-snackbar>
  </v-row>
</template>

<script>
export default {
  props: ["createTasksDialog", "assessmentQuestions", "assessmentAnswers"],
  data: () => ({
    errorSnackbar: false,
    questions: [
      {
        is_multiple_choice: false,
        question: "Test Question",
        points: 0,
        question_id: 1
      }
    ],
    answers: [
      {
        answer_text: "Test answer",
        is_correct: true,
        is_checked: false,
        question_question_id: 1
      }
    ]
  }),
  methods: {
    closeDialog() {
      const closedDialog = false;
      this.$emit("update-create-tasks-dialog", closedDialog);
    },
    addTask() {
      let questionsCopy = this.questions;
      questionsCopy.push({
        is_multiple_choice: false,
        question: "",
        points: 0,
        answer: "",
        question_id: this.questions[this.questions.length - 1]?.question_id
          ? this.questions[this.questions.length - 1].question_id + 1
          : 1
      });
      this.questions = questionsCopy;
    },
    addAnswer(question_id) {
      let answersCopy = this.answers;
      answersCopy.push({
        answer_text: "",
        is_correct: false,
        is_checked: false,
        question_question_id: question_id
      });
      this.answers = answersCopy;
    },
    removeTask(i) {
      const questionId = this.questions[i].question_id;

      let questionsCopy = this.questions;
      questionsCopy.splice(i, 1);
      this.questions = questionsCopy;

      let answersCopy = this.answers;
      this.answers.forEach(
        (answer, x) =>
          answer.question_question_id === questionId && answersCopy.splice(x, 1)
      );
      this.answers = answersCopy;
    },
    removeAnswer(x) {
      let answersCopy = this.answers;
      answersCopy.splice(x, 1);
      this.answers = answersCopy;
    },
    validateQuestionsAndAnswer() {
      let valid = true;
      for (const question of this.questions) {
        if (question.question === "" || question.question === undefined) {
          valid = false;
        } else {
          valid = valid && true;
        }
      }

      for (const answer of this.answers) {
        const relatedQuestion = this.questions.find(
          question => question.question_id === answer.question_question_id
        );
        if (
          (answer.answer_text === "" || answer.answer_text === undefined) &&
          relatedQuestion?.is_multiple_choice
        ) {
          valid = false;
        } else {
          valid = valid && true;
        }
      }
      return valid;
    },
    save() {
      if (this.validateQuestionsAndAnswer()) {
        const assessmentQuestions = this.questions;
        this.$emit("update-assessment-questions", assessmentQuestions);
        const assessmentAnswers = this.answers;
        this.$emit("update-assessment-answers", assessmentAnswers);
        this.closeDialog();
      } else {
        this.errorSnackbar = true;
      }
    }
  }
};
</script>
