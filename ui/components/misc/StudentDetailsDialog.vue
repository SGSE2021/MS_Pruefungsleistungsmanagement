<template>
  <v-dialog v-model="detailsDialog" max-width="500px">
    <v-card>
      <v-card-title>
        <span class="text-h5">Details einsehen</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col cols="12" sm="6" md="4"> </v-col>
          </v-row>
        </v-container>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  props: { detailsDialog: { type: Boolean, required: true } },
  data: () => ({
      detailsDialog: true
  })
};
</script>
