<!-- src/components/ProductList.vue -->
<template>
    <div>
      <ul>
        <li v-for="product in products" :key="product.id">
          {{ product.name }} - {{ product.price }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      products: Array,
    },
  };
  </script>
  