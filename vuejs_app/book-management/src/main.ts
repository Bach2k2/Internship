// import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import LoginVue from './components/Login/Login.vue'
import UserListVue from './components/UserList.vue'
import { createRouter, createWebHashHistory } from 'vue-router'
import HomeVue from './components/Home/Home.vue'
import NotFoundVue from './components/NotFound.vue'
import AddUserVue from './components/AddUser.vue'
import AboutVue from './components/About.vue'
import HeaderVue from './components/Header/Header.vue'


const routes = [
    { path: '/', component: HomeVue },
    { path: '/login', component: LoginVue },
    { path: '/about', component: AboutVue },
    { path: '/users', component: UserListVue },
    { path: '/add-user', component: AddUserVue },
    { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFoundVue },
]

// 3. Create the router instance and pass the `routes` option
// You can pass in additional options here, but let's
// keep it simple for now.
//   const router = VueRouter.createRouter({
//     // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
//     history: VueRouter.createWebHashHistory(),
//     routes, // short for `routes: routes`
//   })
const router = createRouter({
    // Provide the history implementation to use. We are using the hash history for simplicity here.
    history: createWebHashHistory(),
    routes, // short for `routes: routes`
})

const app = createApp(App);

//Global Registration
app.component('header', HeaderVue)
app.use(router)
app.mount('#app')
