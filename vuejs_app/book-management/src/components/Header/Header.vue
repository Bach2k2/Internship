<script setup lang="ts">
import { ref } from 'vue';
import '../Home/Home.css'
import { setAuth, state } from '@/store/store';
import { useRouter } from 'vue-router';

const dropdownVisible = ref(false);
const router =useRouter();
const toggleDropdown = () => {
    dropdownVisible.value = !dropdownVisible.value;
};

const logout = () => {
    // Implement your logout logic here
    // For example, clearing authentication token, redirecting, etc.
    console.log('Logging out...');
    router.push({path:'/'});
    setAuth(false);
    localStorage.clear();

};
</script>

<template>
    <div class="header" id="header">
        <a class="logo">Logo</a>
        <nav class="nav-items">
            <!-- <a href="/">Home</a>
            <a href="/">About</a>
            <a href="/login">Login</a> -->
            <router-link to="/">Home</router-link>
            <router-link to="/about">About</router-link>


            <div v-if="state.authenticated" class="profile-container">
                <button v-if="state.user" @click="toggleDropdown">Hi {{ state.user.username }}</button>
                <div v-if="dropdownVisible" class="dropdown-menu">
                    <router-link to="/books">Books</router-link>
                    <router-link to="/users">Users</router-link>
                    <button @click="logout">Log out</button>
                </div>
            </div>
            <div v-else>
                <router-link to="/login">Login</router-link>
            </div>



        </nav>
        <router-view></router-view>
    </div>
</template>

<style scoped>
.profile-container {
    position: relative;
}

.dropdown-menu {
    position: absolute;
    top: 100%;
    left: 0;
    background-color: #fff;
    border: 1px solid #ccc;
    padding: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    z-index: 10;
}

.dropdown-menu a {
    display: block;
    padding: 8px;
    color: #333;
    text-decoration: none;
}

.dropdown-menu button {
    display: block;
    padding: 8px;
    margin-top: 8px;
    color: #fff;
    background-color: #007bff;
    border: none;
    cursor: pointer;
}
</style>