import {createRouter, createWebHistory} from 'vue-router'
import Home from "../components/Home.vue"
import Login from "../components/Login.vue"
import Register from "../components/Register.vue"


const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: "Home",
            component: Home,
        }, {
            path: '/user/login',
            name: "Login",
            component: Login,
        },
        {
            name: "Register",
            path: "/user/register",
            component: Register,
        }
    ]
})

export default router
