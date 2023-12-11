<script setup lang="ts">
import { ref } from 'vue';
import './Login.css'
import loginImg from "../../assets/login.svg";
const username = ref('')
const password = ref('')
const handleLogin = ()=>{

}
</script>
<template>
  <div class="base-container" ref={this.props.containerRef}>
    <div class="header">Login</div>
    <div class="content">
      <div class="image">
        <img :src="loginImg" />
      </div>
      <div class="form">
        <div class="form-group">
          <label htmlFor="username">Username</label>
          <input type="text" name="username" placeholder="username" v-model="username"/>
        </div>
        <div class="form-group">
          <label htmlFor="password">Password</label>
          <input type="password" name="password" placeholder="password"  v-model="password"/>
        </div>
      </div>
    </div>
    <div class="footer">
      <button type="button" class="btn" @click="handleLogin">
        Login
      </button>
    </div>
  </div>
</template>
