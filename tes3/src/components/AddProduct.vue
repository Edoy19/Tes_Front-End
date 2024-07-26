<!-- src/components/AddProduct.vue -->
<template>
    <div>
      <form @submit.prevent="addProduct">
        <input v-model="name" placeholder="Product Name" />
        <input v-model="price" placeholder="Product Price" />
        <button type="submit">Add Product</button>
      </form>
    </div>
  </template>
  
  <script>
  import { useProductStore } from '../stores/productStore';
  import { ref } from 'vue';
  
  export default {
    setup() {
      const store = useProductStore();
      const name = ref('');
      const price = ref('');
  
      const addProduct = () => {
        store.addProduct({ name: name.value, price: parseFloat(price.value) });
        name.value = '';
        price.value = '';
      };
  
      return {
        name,
        price,
        addProduct,
      };
    },
  };
  </script>
  