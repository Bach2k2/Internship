
<template>
    <div>
        <p>Add new user</p>
        <form>
            <p>Add new user</p>
            <p>Name <input type="text" required v-model="name"></p>
            <p>Job <input type="number" v-model="job"></p>
            <button type="submit">Add user</button>
          </form>
    </div>
    <div>
        <route-link tag="button">Back</route-link>
    </div>
</template>
<script setup lang="tsx">
import { ref } from 'vue';

const name = ref('')
const job = ref('')
const addItem =()=> {
    let user= {
      name:name,
      job:job
    }
    // this.shoppingList.push(item);
    // this.itemName = null
    // this.itemNumber = null
  }
</script>
