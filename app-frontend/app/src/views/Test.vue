<template>
  <div class="test">
    <!-- ////////////// TODO LIST ////////////////////////    -->
    <div>
    <input
    placeholder="nom"
    v-model="toDoThing.newTaskName"
    @keyup.enter="addInTodoArray">

    <input
    placeholder="prénom"
    v-model="toDoThing.newTaskFirstname"
    @keyup.enter="addInTodoArray">
    <button v-on:click="addInTodoArray">Ajouter</button>

    <table  >
        <tr v-for="(item, index) in toDoThing.tasks" :key="index" >
            <td> {{item.name}} || {{item.firstname}} </td>
            <button v-on:click="deleteTodo(index)">Supprimer</button>
        </tr>
    </table>
    </div>
  </div>

</template>

<script>
export default {
  name: 'Test',
  component: {},
  data: () => ({
    toDoThing: {
      newTaskName: '',
      newTaskFirstname: '',
      tasks: [
        { name: 'Gilou', firstname: 'Gilla' },
        { name: 'Biche', firstname: 'Ette' },
        { name: 'Bryan', firstname: 'third' }
      ]
    }
  }),
  methods: {

    erase () {
      this.name = ' '
      return name
    },

    eraseInput () {
      this.toDoThing.newTaskName = ''
      this.toDoThing.newTaskFirstname = ''
    },
    addInTodoArray () {
      var newItem = { name: this.toDoThing.newTaskName, firstname: this.toDoThing.newTaskFirstname }
      if (this.toDoThing.newTaskName && this.toDoThing.newTaskFirstname) {
        this.toDoThing.tasks.push(newItem)
        this.eraseInput()
      } else {
        alert('BOUHHHHH!! T\'es nulle !!')
      }
    },
    deleteTodo (index) {
      this.toDoThing.tasks.splice(index, 1)
    },
    even (numbers) {
      return numbers.filter(function (number) {
        return number % 2 === 0
      })
    },

    showAll () {
      console.log(this.toDoThing.tasks)
    }

  }
}
</script>

<style scoped>
    h1{
        color: red
    }
</style>
