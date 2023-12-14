<script setup lang="ts">
import '../Home/Home.css'
import { state } from '@/store/store';

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

            <router-link to="/login">Login</router-link>


            <router-link to="/books">Books</router-link>
            <router-link to="/users">Users</router-link>


        </nav>
        <router-view></router-view>
    </div>
</template>