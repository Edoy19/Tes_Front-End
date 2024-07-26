<!-- src/App.vue -->
<template>
  <header>
    <div id="app">
    <h1>Manajemen Produk</h1>
    <add-route></add-route>
    <route-list></route-list>
    <map-view></map-view>
  </div>
  </header>

  <RouterView />
</template>


<script setup>
import { RouterLink, RouterView } from 'vue-router';
import CategoryList from './components/CategoryList.vue';
import AddProduct from './components/AddProduct.vue';
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
