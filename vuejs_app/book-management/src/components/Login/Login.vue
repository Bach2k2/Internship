<script setup lang="ts">
import { ref } from 'vue';
import './Login.css'
import loginImg from "../../assets/login.svg";
import { useRoute, useRouter } from 'vue-router';
import Home from '../Home/Home.vue';
import axios from 'axios'
import { setAuth } from '@/store/store';
const username = ref('viet')
const password = ref('viet1234')
const router = useRouter();
const handleLogin = async () => {

  const config = {
    headers:
    {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    }
  }
  if (username.value == "" || password.value == "") {
    alert('Please enter a username and password')
    return
  }
  // Rest Django token:
  axios.post('http://127.0.0.1:8000/login/', { 'username': username.value, 'password': password.value }, config).then(
    (data) => {
      localStorage.setItem('token', data.data.access_token) // First I did JSON.stringify
      localStorage.setItem('user_id', data.data.user_id)
      // console.log(data)
      router.push({ path: '/' })
      setAuth(true)
      alert('Login successful')
    }
  ).catch(() => {
    setAuth(false)
    alert('Authentication failed')
  })
  // jwt token
  /*
    const response = await fetch('http://127.0.0.1:8000/api/token/', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ 'username': username.value, 'password': password.value })
    })
    if (response.status == 200) {
  
      // router.push({name:'home'});
      
      await router.push({ path: '/' })
    }
    else {
      alert('Ban da dang nhap sai')
    }
  */
  // axios.post('http://127.0.0.1:8000/api/token/', { 'username': username.value, 'password': password.value }, config).then(
  //   (data) => {
  //     localStorage.setItem('token', JSON.stringify(data.data))
  //     // console.log(data)
  //     router.push({path:'/'})
  //     alert('Login successful')
  //   }
  // ).catch(() => {
  //   alert('Authentication failed')
  // })


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
          <input type="text" name="username" placeholder="username" v-model="username" />
        </div>
        <div class="form-group">
          <label htmlFor="password">Password</label>
          <input type="password" name="password" placeholder="password" v-model="password" />
        </div>
      </div>
    </div>
    <div class="footer">
      <button type="button" @click="handleLogin">
        Login
      </button>
    </div>
  </div>
</template>
