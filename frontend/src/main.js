import { createApp } from 'vue/dist/vue.esm-bundler';
import { Quasar } from 'quasar'
// Import icon libraries
import '@quasar/extras/material-icons/material-icons.css'
import JournalView from "./components/JournalView.vue";
import AboutView from "./components/AboutView.vue";
import { createRouter, createWebHistory } from 'vue-router';

// Import Quasar css
import 'quasar/src/css/index.sass'

import App from './App.vue'

const routes = [
    { path: '/', component: JournalView },
    { path: '/about', component: AboutView },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})


const myApp = createApp(App)
myApp.use(Quasar, {
    plugins: {}, // import Quasar plugins and add here
})

myApp.use(router)

// Assumes you have a <div id="app"></div> in your index.html
myApp.mount('#app')



