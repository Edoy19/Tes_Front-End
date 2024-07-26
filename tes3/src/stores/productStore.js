// src/stores/productStore.js
import { defineStore } from 'pinia';
import { gql, useQuery, useMutation } from '@apollo/client';

const FETCH_CATEGORIES = gql`
  query {
    categories {
      id
      name
      products {
        id
        name
        price
      }
      subcategories {
        id
        name
        products {
          id
          name
          price
        }
      }
    }
  }
`;

const ADD_PRODUCT = gql`
  mutation($input: ProductInput!) {
    addProduct(input: $input) {
      id
      name
      price
    }
  }
`;

export const useProductStore = defineStore('productStore', {
  state: () => ({
    categories: [],
    loading: false,
  }),
  getters: {
    calculateTotalPrice: (state) => (category) => {
      let total = 0;
      if (category.products) {
        total += category.products.reduce((sum, product) => sum + product.price, 0);
      }
      if (category.subcategories) {
        total += category.subcategories.reduce((sum, subcat) => sum + calculateTotalPrice(subcat), 0);
      }
      return total;
    },
  },
  actions: {
    async fetchCategories() {
      this.loading = true;
      try {
        const { data } = await useQuery(FETCH_CATEGORIES);
        this.categories = data.categories;
      } finally {
        this.loading = false;
      }
    },
    async addProduct(product) {
      const { data } = await useMutation(ADD_PRODUCT, { variables: { input: product } });
      this.categories.push(data.addProduct);
    },
    // Add edit and delete actions here
  },
});
