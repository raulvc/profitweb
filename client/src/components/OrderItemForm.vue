<template>
  <v-layout row justify-center>
    <v-form ref="item_form" persistent max-width="600px" lazy-validation>
      <v-container grid-list-md>
        <v-layout wrap>

          <v-flex xs12>
            <v-combobox
              v-model="item.product"
              :items="products"
              label="Select a product"
              item-text="name"
            >
            </v-combobox>
          </v-flex>

          <v-flex xs12 sm6>

            <v-input-number class="number_input" label="Quantity" :maxLength="max_digits" :min="min_quantity"
                            v-model="item.quantity"
                            :rules="[v => !!v || 'Item is required']"></v-input-number>

            <v-input-number class="number_input" label="Price" :maxLength="max_digits" :min="min_price"
                            v-model="item.unit_price"
                            :rules="[v => !!v || 'Item is required']"></v-input-number>
          </v-flex>

        </v-layout>
      </v-container>
    </v-form>
  </v-layout>
</template>

<script>

export default {
  name: 'OrderItemForm',
  props: {
    parent_item: Object,
    products: Array
  },
  data () {
    return {
      errors: [],
      item: {
        product: null,
        quantity: 1,
        unit_price: 0.00
      },

      min_quantity: 1,
      min_price: 0.01,
      max_digits: 12
    }
  }
}
</script>

<style scoped>
  .number_input > div > div > i {
    display: none;
  }
</style>
