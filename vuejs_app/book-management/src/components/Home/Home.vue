<script setup lang="ts">
import { onMounted, onUnmounted, onUpdated } from 'vue';
import Header from '../Header/Header.vue';
import './Home.css'
import axios from 'axios';
import { setUser } from '@/store/store';

onMounted(async () => {
    console.log(`the component is now mounted.`)
    const token = await localStorage.getItem('token');
    console.log(token);
    const user_id = await localStorage.getItem('user_id');

    if (user_id && token) {
        const config = {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`
            },
        }
        let userid = parseInt(user_id,10)
        console.log(userid);
        try {
            const res = await axios.get(`http://127.0.0.1:8000/users/${userid}`, config);
            console.log(res);
            setUser(res.data);

        } catch (e) {
            console.log(e);
        }
    }


})
onUnmounted(()=>{
    console.log('Unmounted')
})
onUpdated(()=>{
    console.log('Updated')
})

</script>

<template>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <!-- <header id="header"/> -->
    <Header />
    <main>
        <div class="intro">
            <h1>MY DANANG BOOKSTORES</h1>
            <p>I'm a web developers and love to reading books</p>
            <button>Read more</button>
        </div>
        <div class="achievements">
            <div class="work">
                <i class="fas fa-atom"></i>
                <p class="work-heading">Projects</p>
                <p class="work-text">I have worked on many projects and I am very proud of them. I am a very good developer
                    and I am always looking for new projects.</p>
            </div>
            <div class="work">
                <i class="fas fa-skiing"></i>
                <p class="work-heading">Skills</p>
                <p class="work-text">I have a lot of skills and I am very good at them. I am very good at programming and I
                    am always looking for new skills.</p>
            </div>
            <div class="work">
                <i class="fas fa-ethernet"></i>
                <p class="work-heading">Network</p>
                <p class="work-text">I have a lot of network skills and I am very good at them. I am very good at networking
                    and I am always looking for new network skills.</p>
            </div>
        </div>
        <div class="about-me">
            <div class="about-me-text">
                <h2>About Me</h2>
                <p>I am a web developer and I love to create websites. I am a very good developer and I am always looking
                    for new projects. I am a very good developer and I am always looking for new projects.</p>
            </div>
            <img src="https://images.unsplash.com/photo-1596495578065-6e0763fa1178?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=871&q=80"
                alt="me">
        </div>
    </main>
    <footer class="footer">
        <div class="copy">&copy; 2023 Lee Trọng Bách</div>
        <div class="bottom-links">
            <div class="links">
                <span>Information</span>
                <a href="#">Home</a>
                <a href="#">About</a>
                <a href="#">Contact</a>
            </div>
            <div class="links">
                <span>Social Links</span>
                <a href="#"><i class="fab fa-facebook"></i></a>
                <a href="#"><i class="fab fa-twitter"></i></a>
                <a href="#"><i class="fab fa-instagram"></i></a>
            </div>
        </div>
    </footer>
</template>
