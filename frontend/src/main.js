import './assets/main.css'
import './assets/tailwind.css'

import { createApp } from 'vue'

import App from './App.vue'
import router from './router'

import axios from 'axios'
import { defaults } from 'cypress/types/lodash'

axios = defaults.baseURL = 'http://127.0.0.1:8000/'

const app = createApp(App)

app.use(router)

app.mount('#app')
