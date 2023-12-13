<script setup lang="ts">
import { createApp } from 'vue'
const count = 0;
const app1 = createApp({
    data() {
        return {
            count: 0
        }
    }
})
app1.mount('#app1')
</script>
<template>
    <div id="app1">
        <button @click="count++"> {{ count }}</button>
    </div>
</template>
