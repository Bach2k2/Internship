<script setup lang="ts">
import { ref, watchEffect } from 'vue'
import Grid from './Grid.vue'
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
    <div>
        <h1>My User List</h1>
    </div>
    <form id="search">
        Search <input name="query" v-model="searchQuery">
    </form>
    <Grid style="margin-top:20px" :data="users" :columns="gridColumns" :filter-key="searchQuery">
    </Grid>
</template>