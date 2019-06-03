<template>
  <div>
    <order-form-dialog></order-form-dialog>
    <ul v-if="orders && orders.results && orders.results.length">
      <li v-bind:key="order.id" v-for="order of orders.results">
        <v-container fluid grid-list-md>
          <v-data-iterator
            :items="order.items"
            :rows-per-page-items="rowsPerPageItems"
            :pagination.sync="pagination"
            content-tag="v-layout"
            hide-actions
            row
            wrap
          >
            <template v-slot:header>
              <v-toolbar
                class="mb-2"
                color="indigo darken-5"
                dark
                flat
              >
                <v-toolbar-title>{{order.id}}. {{order.client.name}}  - ${{ order.total_price }}</v-toolbar-title>
              </v-toolbar>
            </template>
            <template v-slot:item="order">
              <v-flex
                xs12
                sm6
                md4
                lg3
              >
                <v-card>
                  <v-card-title class="subheading font-weight-bold">{{ order.item.product.name }}
                    {{ order.item.product.multiplier ? '(M' + order.item.product.multiplier + ')' : '' }}</v-card-title>

                  <v-divider></v-divider>

                  <v-list dense>
                    <v-list-tile>
                      <v-list-tile-content>Quantity:</v-list-tile-content>
                      <v-list-tile-content class="align-end">{{ order.item.quantity }}</v-list-tile-content>
                    </v-list-tile>
                  </v-list>
                  <v-list dense>
                    <v-list-tile>
                      <v-list-tile-content>Unit Price:</v-list-tile-content>
                      <v-list-tile-content class="align-end">{{ order.item.unit_price }}</v-list-tile-content>
                    </v-list-tile>
                  </v-list>
                  <v-list dense>
                    <v-divider/>
                  </v-list>
                  <v-list dense>
                    <v-list-tile>
                      <v-list-tile-content>Total:</v-list-tile-content>
                      <v-list-tile-content class="align-end">{{ (order.item.unit_price * order.item.quantity).toFixed(2) }}</v-list-tile-content>
                    </v-list-tile>
                  </v-list>
                </v-card>
              </v-flex>
            </template>
          </v-data-iterator>
        </v-container>
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
import {buildUrl} from '@/config'
import OrderFormDialog from '@/components/OrderFormDialog'

export default {
  name: 'Main',
  components: {OrderFormDialog},
  data () {
    return {
      rowsPerPageItems: [4, 8, 12],
      pagination: {
        rowsPerPage: 4
      },
      orders: [],
      errors: []
    }
  },

  created () {
    this.reloadOrders()
  },

  methods: {
    reloadOrders () {
      axios.get(buildUrl('orders/'))
        .then(response => {
          // JSON responses are automatically parsed.
          this.orders = response.data
        })
        .catch(e => {
          this.errors.push(e)
        })
    }
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  ul {
    list-style-type: none;
  }
</style>
