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
          <v-form ref="order_form" persistent max-width="600px">
            <v-container class="container" grid-list-md>
              <v-layout wrap>
                <v-flex xs12>
                  <v-combobox
                    v-model="order.client"
                    :items="clients"
                    label="Select a client"
                    item-text="name"
                    :rules="[v => !!v || 'Item is required']"
                  >
                  </v-combobox>
                </v-flex>
                <v-flex xs12>
                  <ul>
                    <li v-bind:key="index" v-for="(item, index) in order.items">
                      <v-divider v-if="index !== 0"></v-divider>

                      <order-item-form :products="products" :index="index" @changed="updateItem"></order-item-form>

                      <v-btn color="red" dark flat v-if="index !== 0" @click="removeItem(index)">
                        <span>Remove</span>
                      </v-btn>
                    </li>
                  </ul>
                </v-flex>
                <v-btn id="add_item_button" color="primary" flat @click="addItem">add item</v-btn>
              </v-layout>
            </v-container>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red" dark @click="close">Cancel</v-btn>
          <v-btn color="blue" dark @click="save">Save</v-btn>
        </v-card-actions>
      </v-card>
      <ul v-if="errors.length">
        <b>Error(s) detected:</b>
        <li v-bind:key="index" v-for="(error, index) in errors">
          {{ error }}
        </li>
      </ul>
    </v-dialog>
  </v-layout>
</template>

<script>
import axios from 'axios'
import {buildUrl} from '@/api_helper'
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

    close () {
      this.resetItems()
      this.dialog = false
    },

    resetItems () {
      this.$refs.order_form.reset()
      this.order.items = []
      this.addItem()
    },

    parseOrder () {
      const orderItems = this.order.items.map((i) => {
        return {
          product: i.product.id,
          quantity: i.quantity,
          unit_price: i.unit_price
        }
      })

      return {
        client: this.order.client.id,
        items: orderItems
      }
    },

    save () {
      if (!this.$refs.order_form.validate()) {
        return
      }

      const payload = JSON.stringify(this.parseOrder())
      axios.post(buildUrl('orders/'), payload, {
        headers: { 'Content-Type': 'application/json' }
      })
        .then(response => {
          this.$emit('added_order') // letting parent know order was successfully added
          this.close()
        })
        .catch(e => {
          this.errors.push(e)
        })
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
    padding-left: 0;
  }
  .header {
    padding-bottom: 0;
  }
  .container {
    padding-top: 0;
  }
</style>
