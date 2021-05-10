<template>
  <div class="home">
    <div>
      <p>This is the Home page</p>
    </div>
    <v-container fluid>
      <v-row align="center">
        <v-col class="d-flex" cols="12" sm="6">
          <v-select
            :items="items"
            label="Faites votre choix"
            v-model="choice"
          ></v-select>
        </v-col>
      </v-row>
    </v-container>

    <v-simple-table
    fixed-header
    height="300px">
      <thead v-html="renderTableHeader"></thead>
      <tbody v-html="renderTableData"></tbody>
    </v-simple-table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "home",
  props: {},

  data: () => ({
    bills: [],
    selectedItem: 1,
    items: [
      { text: "Products", icon: "mdi-clock", value: "PRODUCTS" },
      { text: "Clients", icon: "mdi-account", value: "CLIENTS" },
      { text: "Bills", icon: "mdi-flag", value: "BILLS" },
    ],

    choice: null,
  }),
  computed: {
    renderTableData() {
      if (!this.bills.length) {
        return;
      }

      let objectKeys = Object.keys(this.bills[0]);

      return this.bills
        .map((bill) => {
          const body = [];

          for (const key of objectKeys) {
            const html = `<td>${bill[key]}</td>`;
            body.push(html);
          }

          return `<tr>${body}</tr>`;
        })
        .join()
        .replace(/,/g, "");
    },

    renderTableHeader() {
      if (!this.bills.length) {
        return;
      }
      console.log(this.bills[0]);
      let header = Object.keys(this.bills[0]);
      return header
        .map((key, index) => {
          return `<th key=${index}>${key.toUpperCase()}</th>`;
        })
        .join()
        .replace(/,/g, "");
    },
  },

  watch: {
    choice: function (value) {
      if (value === "PRODUCTS") {
        this.apiCall("product");
      }
      if (value === "CLIENTS") {
        this.apiCall("client");
      }
      if (value === "BILLS") {
        this.apiCall("bill");
      }
    },
  },

  methods: {
    async apiCall(resource) {
      try {
        const url = `http://127.0.0.1:8000/${resource}/`;
        const { data } = await axios.get(url);

        this.bills = data;
      } catch (e) {
        console.error(e);
      }
    },
  },
};
</script>


<style lang="scss">
.container {
  flex-direction: column;
  margin: auto;
  margin-top: 5%;
}
</style>
