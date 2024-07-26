// src/routes.js
import CategoryList from './components/CategoryList.vue';
import AddProduct from './components/AddProduct.vue';

const routes = [
  { path: '/', component: CategoryList },
  { path: '/add-product', component: AddProduct },
];

export default routes;
