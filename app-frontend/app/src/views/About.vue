<template>
  <div class="about">
    <v-container fluid>
      <v-row align="center">
        <v-col
          class="d-flex"
          cols="12"
          sm="6"
        >
          <v-select
            :items="items"
            label="Faites votre choix"
          ></v-select>
        </v-col>
      </v-row>
    </v-container>
    <template v-if="!showFormUpdate">
      <Data :data="data" v-for="data in datas" :key="data.id" />
      <v-fab-transition>
        <v-btn
          v-show="!hidden"
          color="pink"
          dark
          right
          fab
          absolute
          @click="showFormUpdate = true"
        >
          <v-icon>mdi-plus</v-icon>
        </v-btn>
      </v-fab-transition>
    </template>
  </div>
</template>

<script>
// @ is an alias to /src
import { mapState } from "vuex";
import Data from "@/components/Data.vue";

export default {
  name: "about",
  props: {},

  components: {
    Data,
  },
  data: () => ({
    showFormUpdate: false,
    selectedItem: 1,
    items: [
      { text: "Products", icon: "mdi-clock" },
      { text: "Clients", icon: "mdi-account" },
      { text: "Bills", icon: "mdi-flag" },
    ],
  }),
  computed: {
    ...mapState({
      datas: (state) => state.datas,
    }),
  },
  methods: {},
};
</script>

<style lang="scss" scoped>
</style>

