<script>
    import api from '@/helpers/api';
    import { getWithJWT } from '@/helpers/JWTRequest';
    import { useUserStore } from '@/stores/user';
    import { useToast } from 'vue-toastification';

    const toast = useToast();

    export default {
        name: 'LoginForm',
        data() {
            return {
                email: '',
                password: ''
            }
        },
        methods: {
            async handleLogin(){
                try{
                    const userStore = useUserStore();
                    // Verifies authentication
                    const tokenResponse = await api.post("/auth/", {
                        user: this.email,
                        password: this.password
                    });
                    if (tokenResponse){
                        // If correct, saves token and user, and redirects to home
                        localStorage.setItem('token', tokenResponse.data.token);
                        this.$router.push({name: 'home'});
                        // Get the user data and save it
                        const userResponse = await getWithJWT('/me/profile');
                        userStore.setUser(userResponse.data);
                        // Inform the user
                        toast.success('Sesión iniciada correctamente');
                    }
                } catch (error){
                    console.log(error);
                    // We handle and inform the error
                    if(error.response.status === 401){
                        toast.error('Usuario o contraseña incorrectos');
                    } else {
                        toast.error('Error del servidor');
                    }
                }
            }
        },
        computed: {
            validEmail() {
                return this.email.includes('@')
            },
            validPassword() {
                return this.password.length >= 8
            },
            validForm() {
                return this.validEmail && this.validPassword
            }
        }
    }
</script>

<template>
    <div class="bg-gray-50 shadow-xl rounded-md flex flex-col items-center justify-center w-3xl h-fit my-12 py-8 px-10 md:my-6 ">
        <h1 class="text-2xl text-gray-950 text-left mb-3">Iniciar sesión</h1>
        <form action="submit" @submit.prevent="handleLogin">
            <div class="form-control w-full max-w-xs">
                <!-- Email -->
                <label for="email" class="label ">
                    <span class="label-tex text-gray-600">Email</span>
                    <span v-if="! validEmail" class="label-text-alt text-red-600">El email no es válido</span>
                </label>
                <input type="email" placeholder="Tu email" class="input input-bordered w-full max-w-xs" v-model="email"/>
            </div>
            <div class="form-control w-full max-w-xs">
                <!-- Password -->
                <label for="password" class="label">
                    <span class="label-text text-gray-600">Contraseña</span>
                </label>
                <input type="password" placeholder="**********" class="input input-bordered w-full max-w-xs" v-model="password"/>
            </div>
            <button class="btn btn-block bg-blue-700 mt-5" type="submit">Login</button>
        </form>
    </div>

</template>
