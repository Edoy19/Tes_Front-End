<!-- src/components/CategoryList.vue -->
<template>
    <div>
      <div v-if="loading">Loading...</div>
      <div v-else>
        <ul>
          <li v-for="category in categories" :key="category.id">
            {{ category.name }}
            <ProductList :products="category.products" />
            <CategoryList v-if="category.subcategories" :categories="category.subcategories" />
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  import { useProductStore } from '../stores/productStore';
  import { computed } from 'vue';
  import ProductList from './ProductList.vue';
  
  export default {
    components: {
      ProductList,
    },
    setup() {
      const store = useProductStore();
      store.fetchCategories();
  
      const categories = computed(() => store.categories);
      const loading = computed(() => store.loading);
  
      return {
        categories,
        loading,
      };
    },
  };
  </script>
  