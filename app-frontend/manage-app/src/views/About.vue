<template>
  <div class='about'>
    <template v-if='!showFormAddData'>
      <Data :data='data' v-for='data in datas' :key='data.id' />
    </template>
  </div>
</template>

<script>
// @ is an alias to /src
import { mapState } from 'vuex'
import Data from '@/components/Data.vue'

export default {
  name: 'about',
  props: {},

  components: {
    Data
  },
  data: () => ({
    showFormAddData: false
  }),
  computed: {
    ...mapState({
      alerts: (state) => state.alerts,
      datas: (state) => state.datas
    })
  },
  methods: {}
}
</script>

<style lang='scss' scoped>

</style>
