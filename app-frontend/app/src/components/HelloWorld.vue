<template>
  <div class="hello">
    <p> {{pays}}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HelloWorld',

  data: () => ({
    pays: null
  }),
  mounted () {
    axios
      .get('http://127.0.0.1:8000/client/')
      .then(response => (this.pays = response))
  }
}
</script>

<style scoped lang="scss">

</style>
