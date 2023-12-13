<script setup lang="ts">
import { ref, watchEffect } from 'vue'
import Grid from './Grid.vue'
import Header from './Header/Header.vue';
interface User {
    id: number,
    email: string,
    first_name: string,
    last_name: string,
    avatar: string
}

const users = ref<User[]>([]);
const searchQuery = ref('')
const gridColumns = ['id', 'email', 'first_name', 'last_name', 'avatar']
watchEffect(async () => {
    try {
        const response = await fetch("https://reqres.in/api/users")
        if (response.ok) {
            users.value = await response.json().then(data=> users.value =data.data);
            console.log('ok',users.value);
        } else {
            console.error('Failed to fetch users:', response.statusText);
        }
    } catch (e) {
        console.error('Failed to fetch users:', e);
    }

})
</script>

<template>
    <!-- <header id="header"/> -->
    <Header/>
    <div>
        <h1>My User List</h1>
        <router-link class="button" to="/add-user" tag="button">Create new user</router-link>
        <!-- <button>Add users</button> -->
        <!-- <route-link to="/add-user" custom v-slot="{ navigate }">
           <span @click="navigate" @keypress.enter="navigate" role="link"> Add new user </span>
        </route-link> -->
    </div>
    <form id="search">
        Search <input name="query" v-model="searchQuery">
    </form>
    <Grid style="margin-top:20px" :data="users" :columns="gridColumns" :filter-key="searchQuery">
    </Grid>
</template>
<style scoped>
.button{
    display:block;
    background-color: blueviolet;
    color:aliceblue;
    justify-content: center;
    align-items: center;
    padding:10;
    width:100px;
    text-decoration: none;
    font-size:20px
}

</style>