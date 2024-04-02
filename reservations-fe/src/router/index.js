import {createRouter, createWebHistory} from 'vue-router'
import Home from '@/components/Home.vue'
import Auth from '@/components/Auth.vue'
import Register from '@/components/Register'
import ClientList from '@/components/ClientList'
import ClientCreate from '@/components/ClientCreate'
import About from '@/components/About'
import Service from '@/components/Services'
import Contact from '@/components/Contact'
import Reservations from '@/components/Reservations'
import Login from '@/components/Login'
import BaseDialog from "@/components/ui/BaseDialog.vue";

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/client-list',
        name: 'ClientList',
        component: ClientList
    },
    {
        path: '/client-list/:msg',
        name: 'ClientUpdatedList',
        component: ClientList
    },
    {
        path: '/client-create',
        name: 'ClientCreate',
        component: ClientCreate
    },
    {
        path: '/client-create/:pk',
        name: 'ClientUpdate',
        component: ClientCreate
    },
    {
        path: '/auth',
        name: 'Auth',
        component: Auth
    },
    {
        path: '/register',
        name: 'Register',
        component: Register
    },
    {
        path: '/about',
        name: 'About',
        component: About
    },
    {
        path: '/services',
        name: 'Services',
        component: Service
    },
    {
        path: '/contact',
        name: 'Contact',
        component: Contact
    },
    {
        path: '/reservations',
        name: 'Reservations',
        component: Reservations
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    }
]
const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
