<template>
  <div class="home"
   @click="getHeaderApiRequest">
    <div>
      <p>This is the Home page</p>
    </div>

    <!-- ---------------------------------------- -->
    <!--  ---------------MODAL------------------- -->
    <!-- ---------------------------------------- -->

    <v-dialog
      v-model="dialog"
      max-width="500px"
    >
      <template v-slot:activator="{ attrs }">
        <v-btn
          color="primary"
          dark
          class="mb-2"
          v-bind="attrs"
          @click="dialog = true"
        >
          New Item
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">Add new {{renderModalTitle}}</span>
        </v-card-title>

        <v-card-text
        >
          <v-container>
            <v-row>
              <v-col
                cols="12"
                sm="6"
                md="4"
                v-for="element in imputName"
                  v-bind:key="element"
              >
              <v-text-field
                :rules="rules"
                hide-details="auto"
                
                  :label="element"
              ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="dialog = false"
          >
            Cancel
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>


    <!-- ---------------------------------------- -->
    <!--  ---------------SELECTOR---------------- -->
    <!-- ---------------------------------------- -->
    <v-container fluid
    >
      <v-row align="center">
        <v-col class="d-flex" cols="12" sm="6">
          <v-select
            :items="items"
            label="Make a choice"
            v-model="choice"
          ></v-select>
        </v-col>
      </v-row>
    </v-container>


    <!-- ---------------------------------------- -->
    <!-- ----------------TABLE------------------- -->
    <!-- ---------------------------------------- -->
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
    // ---------------MODAL-------------------
    editedItem: {name: 'nom', calories: 'calorie'},
    dialog: false,
    rules: [
        value => !!value || 'Required.',
        value => (value && value.length >= 3) || 'Min 3 characters',
      ],
    imputName: [],

    // ---------------SELECTOR----------------
    selectedItem: 1,
    choice: null,

    // ----------------TABLE------------------
    requestAPI: [],
    items: [
      { text: "Products", icon: "mdi-clock", value: "PRODUCTS" },
      { text: "Clients", icon: "mdi-account", value: "CLIENTS" },
      { text: "Bills", icon: "mdi-flag", value: "BILLS" },
    ],
    updateWord: 'Update',
    deleteWord: 'Delete',
    theadName: [],
  }),

  computed: {
    // ---------------MODAL-------------------

    renderModalTitle(){
      if(this.requestAPI){
        if(this.choice == "PRODUCTS"){
          return "product"
        }
        if(this.choice == "CLIENTS"){
          return "client"
        }
        if(this.choice == "BILLS"){
          return "bill"
        }
        else{
          return ""
        }
      }
      else{
        return ' ';
      }
    },

    // ---------------SELECTOR----------------
    
    // ----------------TABLE------------------
    // Show data inside the table  READ of CRUD
    renderTableData() {
      if (!this.requestAPI.length) {
        return;
      }

      let objectKeys = Object.keys(this.requestAPI[0]);

      return this.requestAPI
        .map((bill) => {
          const body = [];

          for (const key of objectKeys) {
            const html = `<td>${bill[key]}</td>`;
            body.push(html);
          }

          return `<tr>
          
          ${body}
          <td> <button type="button" @click="updateItem()"> Update </button> </td>
          <td> <button type="button" @click="deleteItem()"> Delete </button></td>
          </tr>`;
        })
        .join()
        .replace(/,/g, "");
    },

    // renderTableHeader() {
    //   if (!this.requestAPI.length) {
    //     return;
    //   }
    //   let header = Object.keys(this.requestAPI[0]);
    //   // this.imputName = header;
    //   return header
    //     .map((key, index) => {
    //       return `<th key=${index}>${key.toUpperCase()}</th>`;
    //     })
    //     .join()
    //     .replace(/,/g, "");
    // },


    renderTableHeader(){
      if (!this.requestAPI.length) {
        return;
      }
      let header = this.theadName
      // this.imputName = header;
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
  mounted:
    function() {
      if (!this.requestAPI.length) {
        return;
      }
      let header = Object.keys(this.requestAPI[0]);
      this.imputName = header;
            console.log("this.imputName", this.imputName);
    }
  ,

  methods: {
    async apiCall(resource) {
      try {
        const url = `http://127.0.0.1:8000/${resource}/`;
        const { data } = await axios.get(url);

        this.requestAPI = data;
      } catch (e) {
        console.error(e);
      }
    },
    
    getHeaderApiRequest() {
      if (!this.requestAPI.length) {
        return;
      }
      let header = Object.keys(this.requestAPI[0]);
      this.imputName = header;
      let headerTable = header;
      headerTable.push(this.updateWord, this.deleteWord)
      this.theadName=headerTable;
      console.log("headerTable", headerTable);
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
