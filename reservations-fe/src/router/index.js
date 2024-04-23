import {createRouter, createWebHistory} from 'vue-router'
import Home from '@/components/Home.vue'
import Auth from '@/components/Auth.vue'
import Register from '@/components/Register'
import GuestList from '@/components/GuestList'
import GuestCreate from '@/components/GuestCreate'
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
        path: '/guest-list',
        name: 'GuestList',
        component: GuestList
    },
    {
        path: '/guest-list/:msg',
        name: 'GuestUpdatedList',
        component: GuestList
    },
    {
        path: '/guest-create',
        name: 'GuestCreate',
        component: GuestCreate
    },
    {
        path: '/guest-create/:pk',
        name: 'GuestUpdate',
        component: GuestCreate
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
