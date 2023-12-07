<script setup lang="ts">
interface Book {
  title: string
  author: string
  year: number
}
const books = [
    {title:'1', author:'haha',year:2002},
    {title:'2', author:'haha2',year:2002},
    {title:'3', author:'haha3',year:2002},
    {title:'4', author:'hello',year:2002}
]

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