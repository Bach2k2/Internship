<script setup lang="ts">
import { ref } from 'vue'

// give each todo a unique id
let id = 0

const newTodo = ref('') // Input text
const hideCompleted = ref(false)
const todos = ref([
    { id: id++, text: 'Learn HTML', done: true },
    { id: id++, text: 'Learn JavaScript', done: true },
    { id: id++, text: 'Learn Vue', done: false }
])

function addTodo() {
    todos.value.push({ id: id++, text: newTodo.value, done: false })
    newTodo.value = ''
}

function removeTodo(todo: any) {
    todos.value = todos.value.filter((t) => t !== todo)
}
</script>

<template>
    <form @submit.prevent="addTodo">
        <input v-model="newTodo">
        <button>Add Todo</button>
    </form>
    <ul v-if="hideCompleted">
        <span v-for="todo in todos" :key="todo.id">
            <li v-if="!todo.done">
                <input type="checkbox" v-model="todo.done">
                <span :class="{ done: todo.done }">{{ todo.text }}</span>
                <button @click="removeTodo(todo)">X</button>
            </li>
        </span>
    </ul>
    <ul v-else>
        <li v-for="todo in todos" :key="todo.id">
            <input type="checkbox" v-model="todo.done">
            <span :class="{ done: todo.done }">{{ todo.text }}</span>
            <button @click="removeTodo(todo)">X</button>
        </li>
    </ul>
    <button @click="hideCompleted = !hideCompleted">
        {{ hideCompleted ? 'Show all' : 'Hide completed' }}
    </button>
</template>
<style>
.done {
    text-decoration: line-through;
}
</style>