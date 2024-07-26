import { createApp, provide, h } from 'vue';
import App from './App.vue';
import { createPinia } from 'pinia';
import { createRouter, createWebHistory } from 'vue-router';
import { DefaultApolloClient } from '@vue/apollo-composable';  // Pastikan ini terimpor dengan benar
import apolloClient from './apolloClient';
import routes from './routes'; // Pastikan Anda memiliki file routes.js

const pinia = createPinia();
const router = createRouter({
  history: createWebHistory(),
  routes,
});

const app = createApp({
  setup() {
    provide(DefaultApolloClient, apolloClient);
  },
  render: () => h(App),
});

app.use(pinia);
app.use(router);
app.mount('#app');
