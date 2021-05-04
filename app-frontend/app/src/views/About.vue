<template>
  <div class="about">
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

