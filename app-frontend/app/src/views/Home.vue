<template>
  <div class="home" @click="getHeaderApiRequest">
    <div>
      <p>This is the Home page</p>
    </div>

    <!-- ---------------------------------------- -->
    <!--  ---------------MODAL------------------- -->
    <!-- ---------------------------------------- -->

    <v-dialog v-model="dialog" max-width="500px">
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
          <span class="headline">Add new {{ renderModalTitle }}</span>
        </v-card-title>

        <v-card-text>
          <v-container>
            <v-row>
              <v-col
                cols="12"
                sm="6"
                md="4"
                v-for="(field, i) in fields"
                :key="i"
              >
                <v-text-field
                  hide-details="auto"
                  :label="field.label"
                  v-model="form[i]"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog = false">
            Cancel
          </v-btn>
          <v-btn color="blue darken-1" text> Save </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- ---------------------------------------- -->
    <!--  ---------------SELECTOR---------------- -->
    <!-- ---------------------------------------- -->
    <v-container fluid>
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

    <table v-if="requestAPI.length">
      <thead>
        <tr>
          <th v-for="(data, index) in requestAPI[0]" :key="index">
            {{ index }}
          </th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(data, index) in requestAPI" :key="index">
          <td v-for="(prop, i) in data" :key="i">{{ prop }}</td>

          <td>
            <button>Update</button> |
            <button @click="deleteItem(resource, data['id'])">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "home",
  props: {},

  data: () => ({
    // ---------------MODAL-------------------
    dialog: false,
    rules: [
      (value) => !!value || "Required.",
      (value) => (value && value.length >= 3) || "Min 3 characters",
    ],

    fields: [],
    form: {},

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

    theadName: ["Update", "Delete"],
    resource: "",
  }),

  computed: {
    // ---------------MODAL-------------------

    renderModalTitle() {
      if (this.requestAPI) {
        if (this.choice == "PRODUCTS") {
          return "product";
        }
        if (this.choice == "CLIENTS") {
          return "client";
        }
        if (this.choice == "BILLS") {
          return "bill";
        } else {
          return "";
        }
      } else {
        return " ";
      }
    },
  },

  watch: {
    choice: async function (value) {
      if (value === "PRODUCTS") {
        await this.apiCall("product");
        await this.formRequest("product");
        // const fields = Object.keys(data[0]);
        this.resource = "product";
      }
      if (value === "CLIENTS") {
        this.apiCall("client");

        this.resource = "client";
        await this.formRequest("client");
      }
      if (value === "BILLS") {
        this.apiCall("bill");

        this.resource = "bill";
        await this.formRequest("bill");
      }
    },
  },

  methods: {
    async apiCall(resource) {
      try {
        const url = `http://127.0.0.1:8000/${resource}/`;
        const { data } = await axios.get(url);

        this.requestAPI = data;

        return data;
      } catch (e) {
        console.error(e);
      }
    },

    async deleteItem(resource, id) {
      try {
        const url = `http://127.0.0.1:8000/${resource}/${id}`;
        const { data } = await axios.delete(url, { data: { id } });

        await this.apiCall(resource);

        return data;
      } catch (e) {
        console.error(e);
      }
    },

    async formRequest(resource) {
      try {
        const url = `http://127.0.0.1:8000/${resource}/`;

        const { data } = await axios.options(url);

        const fields = data.actions.POST;
        delete fields.id;

        this.fields = fields;

        return data;
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
