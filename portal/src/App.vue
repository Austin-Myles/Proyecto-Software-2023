<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useRouter } from 'vue-router'
import { computed } from 'vue'
import { useUserStore } from '@/stores/user'
import { useToast } from 'vue-toastification';

const toast = useToast();

const router = useRouter()
const userStore = useUserStore()

function handleLogout() {
  localStorage.clear();
  userStore.clearUser();
  router.push({ name: 'login' });
  toast.error('Sesión cerrada correctamente');
}

const logged = computed(() => userStore.user !== null)

const loggedMenu = [
  {
    name: 'Análisis',
    path: '/analisis'
  },
  {
    name: 'Mis Solicitudes',
    path: '/service_request_list'
  }
]

const menu = computed(() => [
  {
    name: 'Home',
    path: '/'
  },
  {
    name: 'Buscar Servicios',
    path: '/search'
  },
  ...(logged.value ? loggedMenu : [])
])
</script>

<template>
  <div class="drawer min-h-screen">
    <input id="my-drawer-3" type="checkbox" class="drawer-toggle" />
    <div class="drawer-content">
      <!-- Navbar -->
      <div class="w-full navbar bg-gray-50 fixed top-0 z-10 shadow-xl">
        <div class="flex-none lg:hidden">
          <label for="my-drawer-3" aria-label="open sidebar" class="btn btn-square btn-ghost">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              class="inline-block w-6 h-6 stroke-current"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 6h16M4 12h16M4 18h16"
              ></path>
            </svg>
          </label>
        </div>
        <div class="flex-1 px-2 mx-2 text-xl">
          <a href="/" class="flex flex-row justify-center items-center">
            <img src="/cidepint_logo.png" class="max-w-10 max-h-10" />
            <p class="indent-3">CIDEPINT</p>
          </a>
        </div>

        <div class="flex-none hidden lg:block">
          <ul class="menu menu-horizontal flex justify-center items-center">
            <!-- Navbar menu content here -->

            <li class="mr-2" v-for="link in menu" :key="link.path">
              <RouterLink :to="link.path">{{ link.name }}</RouterLink>
            </li>
            <li v-if="logged">
              <button class="btn btn-outline btn-error flex content-center" @click="handleLogout">
                Cerrar sesión
              </button>
            </li>
            <li v-else>
              <a class="btn btn-outline btn-info flex content-center" href="/login"
                >Iniciar sesión</a
              >
            </li>
          </ul>
        </div>
      </div>
      <!-- Page content here -->
      <main class="mt-12 py-8 px-4 min-h-full md:p-8">
        <RouterView />
      </main>

      <!-- Footer -->
      <footer class="footer p-10 bg-base-300 text-base-content">
        <nav>
          <header class="footer-title text-blue-700">Servicios</header>
          <a class="link link-hover" href="/service_request_list">Búsqueda</a>
          <a class="link link-hover" href="/">Listar por institución</a>
          <a class="link link-hover" href="/">Realizar solicitud</a>
        </nav>
        <nav>
          <header class="footer-title text-blue-700">Institución</header>
          <a class="link link-hover" href="/contact">Contacto</a>
        </nav>
        <nav>
          <header class="footer-title text-blue-700">Social</header>
          <div class="grid grid-flow-col gap-4">
            <a href="https://twitter.com/cidepint" target="_blank">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                class="fill-current"
              >
                <path
                  d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"
                ></path>
              </svg>
            </a>
            <a href="https://www.facebook.com/cidepintok/" target="_blank"
              ><svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                class="fill-current"
              >
                <path
                  d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"
                ></path></svg
            ></a>
            <a href="https://www.instagram.com/cidepint/" target="_blank"
              ><svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 16 16"
                class="fill-current"
              >
                <path
                  d="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.917 3.917 0 0 0-1.417.923A3.927 3.927 0 0 0 .42 2.76C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.048 3.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.333 1.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.916 3.916 0 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 16 8s-.01-2.445-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.926 3.926 0 0 0-.923-1.417A3.911 3.911 0 0 0 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0h.003zm-.717 1.442h.718c2.136 0 2.389.007 3.232.046.78.035 1.204.166 1.486.275.373.145.64.319.92.599.28.28.453.546.598.92.11.281.24.705.275 1.485.039.843.047 1.096.047 3.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.47 2.47 0 0 1-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.478 2.478 0 0 1-.92-.598 2.48 2.48 0 0 1-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.233 0-2.136.008-2.388.046-3.231.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92.28-.28.546-.453.92-.598.282-.11.705-.24 1.485-.276.738-.034 1.024-.044 2.515-.045v.002zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 0 0-1.92zm-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217zm0 1.441a2.667 2.667 0 1 1 0 5.334 2.667 2.667 0 0 1 0-5.334z"
                /></svg
            ></a>
          </div>
        </nav>
      </footer>
    </div>
    <div class="drawer-side">
      <label for="my-drawer-3" aria-label="close sidebar" class="drawer-overlay"></label>
      <ul class="menu p-4 w-80 min-h-full bg-base-200 flex justify-between">
        <!-- Sidebar content here -->
        <div class="flex flex-col pt-12">
          <li class="text-blue-500 font-bold" v-for="link in menu" :key="link.path">
            <RouterLink :to="link.path">{{ link.name }}</RouterLink>
          </li>
        </div>
        <button v-if="logged" class="btn btn-outline btn-error flex content-center" @click="logout">
          Cerrar sesión
        </button>
        <a v-else class="btn btn-outline btn-info flex content-center" href="/login"
          >Iniciar sesión
        </a>
      </ul>
    </div>
  </div>
  <!--
  <nav class="sticky top-0 left-0 flex gap-8 p-8 bg-primary">
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/analisis">Analisis</RouterLink>
  </nav>
  -->
</template>

<style>
main {
  background-image: url('/fondo2.png');
  background-position: center;
  background-repeat: repeat;
  /* TODO: Fix background not properly repeating */
  background-size: auto;
}
</style>
