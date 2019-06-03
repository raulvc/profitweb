<template>
  <v-layout row justify-center>
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on }">
        <v-btn id="add_button" color="primary" dark v-on="on">add a new order</v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">New Order</span>
        </v-card-title>
        <v-card-text>
          <v-container grid-list-md>
            <v-layout wrap>
              <v-flex xs12>
                <v-combobox
                  v-model="selected_client"
                  :items="clients"
                  label="Select a client"
                  item-text="name"
                >
                </v-combobox>
              </v-flex>
              <v-flex xs12>
                <ul>
                  <li v-bind:key="item.product" v-for="item of order.items">
                    <order-item-form :products="products" :item="item"></order-item-form>
                  </li>
                </ul>
              </v-flex>
              <v-flex xs12 sm6>
                <v-btn id="add_item_button" color="primary" @click="add_item">add item</v-btn>
              </v-flex>
            </v-layout>
          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" flat @click="dialog = false">Close</v-btn>
          <v-btn color="blue darken-1" flat @click="dialog = false">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
</template>

<script>
import axios from 'axios'
import {buildUrl} from '@/config'
import OrderItemForm from '@/components/OrderItemForm'

export default {
  name: 'OrderFormDialog',
  components: {OrderItemForm},
  data () {
    return {
      clients: [],
      products: [],
      errors: [],
      dialog: false,

      // form data
      order: {
        client: null,
        items: []
      }
    }
  },

  created () {
    axios.get(buildUrl('clients/'))
      .then(response => { this.clients = response.data.results })
      .catch(e => { this.errors.push(e) })

    axios.get(buildUrl('products/'))
      .then(response => { this.products = response.data.results })
      .catch(e => { this.errors.push(e) })

    this.add_item()
  },

  methods: {
    add_item () {
      this.order.items.push({})
    }
  }
}
</script>

<style scoped>
  #add_button {
    margin-top: 20px;
    margin-left: 50px;
  }
  ul {
    list-style-type: none;
  }
</style>
