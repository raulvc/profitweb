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
<!--              <v-flex xs12 sm6>-->
<!--                <v-input-number v-model="qty" min="1" maxLength="12" outline="false" label="quantity"></v-input-number>-->
<!--              </v-flex>-->
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

export default {
  name: 'OrderFormDialog',
  data () {
    return {
      rowsPerPageItems: [4, 8, 12],
      pagination: {
        rowsPerPage: 4
      },
      clients: [],
      products: [],
      errors: [],
      dialog: false,

      // form data
      selected_client: null,
      qty: 1
    }
  },

  created () {
    axios.get(buildUrl('clients/'))
      .then(response => { this.clients = response.data.results })
      .catch(e => { this.errors.push(e) })

    axios.get(buildUrl('products/'))
      .then(response => { this.products = response.data.results })
      .catch(e => { this.errors.push(e) })
  }
}
</script>

<style scoped>
  #add_button {
    margin-top: 20px;
    margin-left: 50px;
  }
</style>
