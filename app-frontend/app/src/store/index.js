import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    datas: [
      { id: 1, name: "Bich",  lastname: "Ette", mail: "mail@valide.fr" },
      { id: 2, name: "Bi",  lastname: "Dulle", mail: "mail@valide.fr" },
      { id: 3, name: "Flan",  lastname: "By", mail: "mail@valide.fr" },
    ],
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
