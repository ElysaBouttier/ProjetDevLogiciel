<template>
  <div class="about">
    
    <h3> Logiciel adaptatif de gestion de facture de supermarché.</h3>
    <p>Crée par Elysa Bouttier et Loup Bruneau dans le cadre de la formation Bachelore 3 Informatique développement logiciel </p>
    <p>Langue : Anglais </p>
    <p>derniere modification 23/05/2021</p>
    <p>Django version 3.2</p>
    <p>Vue.js version 3.0.11</p>
    
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

