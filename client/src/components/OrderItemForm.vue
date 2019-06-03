<template>
  <v-layout row justify-center>

    <v-container class="container" grid-list-md>
      <v-layout wrap>

        <v-flex xs12 sm10>
          <v-combobox
            v-model="item.product"
            :items="products"
            label="Select a product"
            item-text="name"
            :rules="[v => !!v || 'Item is required']"
            @change="suggestPrice"
          >
          </v-combobox>
        </v-flex>

        <v-flex xs12 sm1 v-if="getProfitability() !== ''">
          <v-badge :color="getProfitabilityColor()">
            <template v-slot:badge>
              <span class="badge_text">P</span>
            </template>
          </v-badge>
        </v-flex>

        <v-flex xs12 sm1 v-if="!isDivisible()">
          <v-badge color="red">
            <template v-slot:badge>
              <span class="badge_text">M</span>
            </template>
          </v-badge>
        </v-flex>

        <v-flex xs12 sm6>
          <v-currency-field label="Quantity" :max="max_num" :min="min_quantity"
                            v-model="item.quantity" :precision="0"
                            :rules="[ validateQuantity ]"></v-currency-field>
        </v-flex>
        <v-flex xs12 sm6>
          <v-currency-field label="Price" :max="max_num" :min="min_price"
                            v-model="item.unit_price"
                            :rules="[ validatePrice ]"
                            prefix="$"
          ></v-currency-field>
        </v-flex>

      </v-layout>
    </v-container>

  </v-layout>
</template>

<script>

export default {
  name: 'OrderItemForm',
  props: {
    products: Array,
    index: Number
  },
  data () {
    return {
      item: {
        product: null,
        quantity: 1,
        unit_price: 0.01
      },

      min_quantity: 1,
      min_price: 0.01,
      max_num: 9999999999.99
    }
  },

  methods: {
    suggestPrice (product) {
      this.item.unit_price = product.unit_price
    },

    getProfitability () {
      if (this.item.product) {
        const productCost = this.item.product.unit_price
        const itemPrice = this.item.unit_price
        if (itemPrice > productCost) {
          return 'Great'
        }
        if (itemPrice > (0.9 * productCost)) {
          return 'Good'
        }
        return 'Bad'
      }
      return ''
    },

    getProfitabilityColor () {
      const profitability = this.getProfitability()
      switch (profitability) {
        case 'Great':
          return 'green'
        case 'Good':
          return 'yellow'
        default:
          return 'red'
      }
    },

    isDivisible () {
      if (this.item.product && this.item.product.multiplier) {
        return this.item.quantity % this.item.product.multiplier === 0
      }
      return true
    },

    updateReference () {
      // keeping parent list up to date
      this.$emit('changed', {
        item: this.item,
        index: this.index
      })
    },

    validateQuantity (value) {
      if (!value) {
        return 'Item is required'
      }
      if (!this.isDivisible()) {
        return 'Quantity must be divisible by ' + this.item.product.multiplier
      }
      return true
    },

    validatePrice (value) {
      if (!value) {
        return 'Item is required'
      }
      if (this.getProfitability() === 'Bad') {
        return 'Price must be at least $ ' + (this.item.product.unit_price * 0.9).toFixed(2)
      }
      return true
    }
  },

  created () {
    this.updateReference()
  },

  watch: {
    item: {
      handler (val) {
        this.updateReference()
      },
      deep: true
    }
  }
}
</script>

<style scoped>
  .badge_text {
    text-align: center;
  }
  .container {
    padding-left: 2px;
  }
</style>
