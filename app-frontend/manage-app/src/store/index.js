import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    datas: [
      { id: 5, name: 'Lala', lastname: 'teletobie', mail: 'lalal@valide.fr' },
      { id: 1, name: 'Bid', lastname: 'Ul', mail: 'Bidul@valide.fr' },
      { id: 2, name: 'Eve', lastname: 'A', mail: 'Eva@valide.fr' },
      { id: 3, name: 'Flan', lastname: 'By', mail: 'mail@valide.fr' }
    ]
  },
  mutations: {
    ADD_ALERT (state, alert) {
      state.alerts.push(alert)
    },

    UPDATE_IS_CONNECTED (state, isConnected) {
      // mutate state
      state.isConnected = isConnected
    }
  },
  actions: {
  },
  modules: {
  }
})
