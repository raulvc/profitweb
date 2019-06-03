<template>
  <v-layout row justify-center>
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on }">
        <v-btn id="add_button" color="primary" dark v-on="on">add a new order</v-btn>
      </template>
      <v-card>
        <v-card-title class="header">
          <span class="headline">New Order</span>
        </v-card-title>
        <v-card-text>
          <v-container class="container" grid-list-md>
            <v-layout wrap>
              <v-flex xs12>
                <v-combobox
                  v-model="order.client"
                  :items="clients"
                  label="Select a client"
                  item-text="name"
                >
                </v-combobox>
              </v-flex>
              <v-flex xs12>
                <ul>
                  <li v-bind:key="index" v-for="(item, index) in order.items">
                    <v-divider v-if="index !== 0"></v-divider>

                    <order-item-form :products="products" :index="index" @changed="updateItem"></order-item-form>

                    <v-btn color="red" dark v-if="index !== 0" @click="removeItem(index)">
                      <span>Remove</span>
                    </v-btn>
                  </li>
                </ul>
              </v-flex>
              <v-flex xs12 sm6>
                <v-btn id="add_item_button" color="primary" @click="addItem">add item</v-btn>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red darken-1" flat @click="cancel">Cancel</v-btn>
          <v-btn color="blue darken-1" flat @click="save">Save</v-btn>
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

    this.addItem()
  },

  methods: {
    addItem () {
      this.order.items.push({})
    },

    removeItem (index) {
      this.order.items.splice(index, 1)
    },

    updateItem (payload) {
      const index = payload.index
      this.order.items[index] = payload.item
    },

    cancel () {
      this.dialog = false
      this.resetItems()
    },

    resetItems () {
      this.order.items = []
      this.addItem()
    },

    save () {
      this.$emit('added_order') // letting parent know order was successfully added
      this.cancel()
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
  .header {
    padding-bottom: 0;
  }
  .container {
    padding-top: 0;
  }
</style>
