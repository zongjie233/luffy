import settings from "./settings";
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

// 设置reset-css
import "./assets/reset.css"

const app = createApp(App)

// 设置全局属性settings
app.provide('$settings', settings);

// 设置element-plus-ui
app.use(ElementPlus)



app.use(router)

app.mount('#app')


