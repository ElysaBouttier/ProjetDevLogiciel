<template>
  <div class="home">
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
            <v-row v-for="(field, i) in fields" :key="i">
                
              <v-col cols="12" >
                <p>{{field.label}}</p>

                  <v-text-field v-if="field.type == 'string'"
                   :label="field.label" @change="ev => inputChanged(ev, field)"></v-text-field>
                   
                   <v-checkbox v-else-if="field.type == 'boolean'"
                   :label="field.label" @change="ev => inputChanged(ev, field)"></v-checkbox>

                   <v-text-field v-else-if="field.type == 'datetime'"
                   :label="field.label" type="date" @change="ev => inputChanged(ev, field)"></v-text-field>

                   <v-text-field v-else-if="field.type == 'integer'"
                   :label="field.label" @change="ev => inputChanged(ev, field)"></v-text-field>
                   <v-text-field v-else-if="field.type == 'decimal'"
                   :label="field.label" @change="ev => inputChanged(ev, field)"></v-text-field>

                   <v-select v-else-if="field.type == 'field'"
                   :label="field.label" @change="ev => inputChanged(ev, field)"></v-select>
                
                <!-- <component :is="getFieldFormType(field.type)" :label="field.label" >
                </component> -->

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

    <v-simple-table class="table-api">
      <thead>
        <tr>
          <th>
            Id
          </th>
          <th v-for="(data, index) in fields" :key="index">
            {{ data.label }}
          </th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(data, index) in requestAPI" :key="index">
          
          <td v-for="(prop, key) in data" :key="key">
            <span v-if="getFieldType(key) == 'datetime'">
              {{prop | formatDate}}
            </span>
            <span v-else>
              {{prop}}
            </span>
            
          </td>

          <td>
            <button>Update</button> |
            <button @click="deleteItem(resource, data['id'])">Delete</button>
          </td>
        </tr>
      </tbody>
    </v-simple-table>
  </div>
</template>

<script>
import axios from "axios";

import { VTextField, VCheckbox } from "vuetify/lib";

export default {
  name: "home",
  props: {},

  components: {
    VTextField,
    VCheckbox,
    // VDatePicker,
  },

  data: () => ({
    // ---------------MODAL-------------------
    // to open or close modal windows
    dialog: false,
    // array contain objects from request api data.action.POST
    fields: [],

    //
    userImput:{

    },
    

    // ---------------SELECTOR----------------
    choice: null,

    // ----------------TABLE------------------
    requestAPI: [],
    // end of api request
    resource: "",
    items: [
      { text: "Products", icon: "mdi-clock", value: "PRODUCTS" },
      { text: "Clients", icon: "mdi-account", value: "CLIENTS" },
      { text: "Bills", icon: "mdi-flag", value: "BILLS" },
    ],
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

  filters: {
  formatDate: function (value) {
    if (value) {
      let data = value.replace('T', ' ').substr(0,19)
      return data;
    }
    return ''
  }
  },


  methods: {

    inputChanged(ev, field){
      console.log("ev" , ev);
      console.log("field" , field);
      let apiField = field.label[0].toLowerCase() + field.label.substring(1);
      this.userImput[apiField]= ev;

      // au clic sur save faire requete axios pour save userInput. Attention si 
      // datetime => trsf en iso
    },  
    // getFieldFormType(type) {
    //   if (type === "string") {
    //     return "v-text-field";
    //   }
    //   if (type === "boolean") {
    //     return "v-checkbox";
    //   }
    //   if (type === "datetime") {
    //     return "v-date-picker";
    //   }
    //   if (type === "integer" || type === "decimal") {
    //     return "v-text-field";
    //   }
    //   if (type === "field") {
    //     return "v-select";
    //   }

    //   return null;
    // },

    getFieldType(label) {
      // example : label = "IssuingDate"
      // from a label get field type from fields
      
      const found = this.fields.find(element => label.toLowerCase() == element.label.toLowerCase());
      if (found == undefined){
        return;
      }
      return found.type;
    },

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
        this.fields = [];

        Object.entries(fields).map((item) => {
          const field = {
            type: item[1].type,
            label: item[1].label,
          };

          this.fields.push(field);
        });

        this.userImput={};
        

        // return data;
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
.table-api{
  thead {
    background-color: rgb(206, 206, 206);
  }
}
</style>
