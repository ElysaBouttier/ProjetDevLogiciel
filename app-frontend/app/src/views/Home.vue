<template>
  <div class="home">
    <div>
      <p>This is the Home page</p>
    </div>
    <table>
      <thead v-html="renderTableHeader"></thead>
      <tbody v-html="renderTableData"></tbody>
    </table>
  </div>
</template>

<script>
// @ is an alias to /src

import axios from "axios";

export default {
  name: "home",
  props: {},

  //   components: {},
  data: () => ({
    bills: [],
  }),
  computed: {
    renderTableData() {
      return this.bills
        .map((bill) => {
          const {
            id,
            issuingDate,
            isPaid,
            payementDate,
            price,
            idClient,
          } = bill;

          return `<tr key=${id}><td>${id}</td><td>${issuingDate}</td><td>${isPaid}</td><td>${payementDate}</td><td>${price}</td><td>${idClient}</td></tr>`;
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

  methods: {
    // renderTableData() {
    //   return this.bills.map((bill) => {
    //     const { id, issuingDate, isPaid, payementDate, price, idClient } = bill;
    //     return (
    //       <tr key={id}>
    //         <td>{issuingDate}</td>
    //         <td>{isPaid}</td>
    //         <td>{payementDate}</td>
    //         <td>{price}</td>
    //         <td>{idClient}</td>
    //       </tr>
    //     );
    //   });
    // },
  },
  mounted() {
    axios.get("http://127.0.0.1:8000/bill/").then((response) => {
      this.bills = response.data;
    });
  },
  beforeMount() {},
};
</script>


<style lang="scss">
.container {
  flex-direction: column;
  margin: auto;
  margin-top: 21%;
}
</style>
