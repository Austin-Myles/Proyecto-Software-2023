<script setup>
    import LoginForm from '../components/form/LoginForm.vue'
    import { useUserStore } from '@/stores/user'
    import { useRouter } from 'vue-router'

    const userStore = useUserStore()
    const router = useRouter()
    if(! localStorage.getItem('token') ){
        router.push({ name: 'login' });
        userStore.clearUser();
    } else {
        router.push({ name: 'home' });
    }

</script>

<template>
    <div class=" w-full h-full flex justify-center items-center">
        <LoginForm />
    </div>
</template>
