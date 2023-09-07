import settings from './settings'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import naive from 'naive-ui'
import axios from "axios";

// 通用字体
import 'vfonts/Lato.css'

// 设置reset-css
import './assets/reset.css'

const app = createApp(App)

app.provide('settings', settings)
app.provide('axios', axios)


app.use(naive)

app.use(router)

axios.defaults.withCredentials = false // 阻止附带cookie

app.mount('#app')
