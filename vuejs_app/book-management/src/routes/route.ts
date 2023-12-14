import { createRouter, createWebHashHistory } from 'vue-router'
import LoginVue from '../components/Login/Login.vue'
import UserListVue from '../components/UserList.vue'
import HomeVue from '../components/Home/Home.vue'
import NotFoundVue from '../components/NotFound.vue'
import AddUserVue from '../components/AddUser.vue'
import AboutVue from '../components/About.vue'
import BookListVue from '../components/BookList.vue'
const routes = [
    { path: '/', component: HomeVue ,name:'home'},
    { path: '/login', component: LoginVue },
    { path: '/about', component: AboutVue },
    { path: '/users', component: UserListVue },
    { path: '/books', component: BookListVue },
    { path: '/add-user', component: AddUserVue },
    { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFoundVue },
]

export const router = createRouter({
    // Provide the history implementation to use. We are using the hash history for simplicity here.
    history: createWebHashHistory(),
    routes, // short for `routes: routes`
})
