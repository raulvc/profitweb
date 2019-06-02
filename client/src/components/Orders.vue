<template>
  <div>
    <ul v-if="orders && orders.results.length">
      <li v-bind:key="order.id" v-for="order of orders.results">
        <p><strong>{{order.id}}</strong></p>
        <p>{{order.client.name}}</p>
      </li>
    </ul>

    <ul v-if="errors && errors.length">
      <li v-bind:key="error.message" v-for="error of errors">
        {{error.message}}
      </li>
    </ul>
  </div>
</template>

<script>

import axios from 'axios'

const APIBaseURL = 'http://localhost:8000/'

function buildUrl (url) {
  return APIBaseURL + url
}

export default {
  name: 'Orders',
  data () {
    return {
      orders: [],
      errors: []
    }
  },

  created () {
    axios.get(buildUrl('orders/'), {
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(response => {
        // JSON responses are automatically parsed.
        this.orders = response.data
      })
      .catch(e => {
        this.errors.push(e)
      })
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
