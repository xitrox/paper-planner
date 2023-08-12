import { createApp } from 'vue/dist/vue.esm-bundler';
import { createPinia } from 'pinia';
import { Quasar, Notify } from 'quasar'
// Import icon libraries
import '@quasar/extras/material-icons/material-icons.css'
import JournalView from "./components/JournalView.vue";
import AboutView from "./components/AboutView.vue";
import LiteratureView from "./components/LiteratureView.vue";
import PhaseEinarbeitungView from "./components/PhaseEinarbeitungView.vue";
import { createRouter, createWebHistory } from 'vue-router';

// Import Quasar css
import 'quasar/src/css/index.sass'

import App from './App.vue'

const routes = [
    { path: '/', component: JournalView },
    { path: '/about', component: AboutView },
    { path: '/literature', component: LiteratureView },
    { path: '/about', component: AboutView },
    { path: '/einarbeitung', component: PhaseEinarbeitungView }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})


const myApp = createApp(App)
const pinia = createPinia();


myApp.use(Quasar, {
    plugins: {
        Notify
    }, // import Quasar plugins and add here
    config: {
        brand: {
            primary: '#b219d1',
            secondary: '#26A69A',
            accent: '#9C27B0',

            dark: '#1d1d1d',
            'dark-page': '#121212',

            positive: '#21BA45',
            negative: '#C10015',
            info: '#31CCEC',
            warning: '#F2C037'
        }
    },
})

myApp.use(router)

// Assumes you have a <div id="app"></div> in your index.html
myApp.use(pinia);
myApp.mount('#app')

