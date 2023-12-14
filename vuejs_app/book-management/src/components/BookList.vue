<script setup lang="ts">
import { ref, watchEffect } from 'vue'
interface Book {
    title: string
    author: string
    year: number
    category: string
}
const books = ref<Book[] | null>(null)
watchEffect(async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/books/")
        if (response.ok) {
            await response.json().then(data => {
                books.value = data.results
                console.log('ok', data.results);
            });

        } else {
            console.error('Failed to fetch users:', response.statusText);
        }
    } catch (e) {
        console.error('Failed to fetch users:', e);
    }

})
</script>

<template>
    <ul>
        <li v-for="book in books" :key="book.title">
            {{ book.title }}
            {{ book.author }}
            {{ book.year }}
        </li>
    </ul>
</template>