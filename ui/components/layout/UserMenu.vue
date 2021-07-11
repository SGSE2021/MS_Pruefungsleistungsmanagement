<template>
  <div class="text-center">
    <v-menu offset-y>
      <template v-slot:activator="{ on, attrs }">
        <div>
          <v-icon v-bind="attrs" v-on="on" x-large>mdi-account-circle</v-icon
          ><br />
          {{ getFirstname() }} {{ getLastname() }}
        </div>
      </template>
    </v-menu>
  </div>
</template>

<script>
export default {
  props: ["user"],
  data: () => ({}),
  methods: {
    getFirstname() {
      if (this.user) {
        return this.user.firstname && this.user.firstname;
      }
    },
    getLastname() {
      if (this.user) {
        return this.user.lastname && this.user.lastname;
      }
    }
  }
};
</script>
