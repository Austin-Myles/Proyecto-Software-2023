<template>
  <div class="bg-base-100 p-4 md:p-10 w-full h-full rounded-md shadow-lg">
    <div class="max-w-full mx-auto">
      <h2 class="title mb-4 md:mb-8 text-center">Listado de Solicitudes de Servicio</h2>

      <!-- Verifica si el usuario está autenticado -->
      <div v-if="logged == false">
        <p class="text-center text-red-500 mb-4">Debes iniciar sesión para consultar tus solicitudes.</p>
        <router-link to="/login">
          <button class="btn btn-block bg-blue-700 mt-5" type="button">Iniciar Sesión</button>
        </router-link>
      </div>

      <!-- Muestra el contenido si el usuario está autenticado -->
      <div v-else>
        <div v-if="loading">Cargando...</div>
        <div v-else>
          <div v-if="userRequests.length > 0">
            <div v-for="request in userRequests" :key="request.id">
              <!-- Incluye el componente ServiceRequestItem para cada solicitud -->
              <ServiceRequestListItem :serviceRequestListItem="request"/>
            </div>
          </div>
          <div v-else>
            No hay solicitudes de servicio realizadas por este usuario.
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { getWithJWT } from '@/helpers/JWTRequest';
import ServiceRequestListItem from '../components/service_request_list/ServiceRequestListItem.vue';
import { computed } from 'vue';
import { useUserStore } from '@/stores/user';

export default {
  setup() {
    const userRequests = ref([]);
    const loading = ref(true);
    const userStore = useUserStore();
    let logged = computed(() => userStore.user !== null);

    onMounted(async () => {
      if (logged.value == false) {
        return;
      }

      try {
        // Ruta de la API para obtener los pedidos del usuario
        const route = '/me/requests?page=1&per_page=10&sort=creation_date&order=desc';

        const response = await getWithJWT(route);
        userRequests.value = response.data.data;
      } catch (error) {
        console.error('Error fetching user requests:', error);
      } finally {
        loading.value = false;
      }
    });

    return { userRequests, loading, logged };
  },
  components: { ServiceRequestListItem }
};
</script>

<style scoped>
  /* Estilos para el título */
  .title {
    color: #333;
    font-size: 36px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 20px;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
  }
</style>
