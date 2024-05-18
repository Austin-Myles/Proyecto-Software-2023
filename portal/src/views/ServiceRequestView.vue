<template>
  <div class="bg-base-100 p-10">
    <div v-if="logged">
      <div v-if="existError" class="flex flex-col items-center p-6">
      <p class="text-red-500 text-xl p-6">Error: Servicio no encontrado.</p>
      <button @click="redirectToHome" class="btn bg-secondary text-white mt-4">Ir a la página principal</button>
      </div>
      <div v-else>
        <h1 class="text-black text-3xl mb-6">
          Solicitud de Servicio - {{ fullServiceTitle }}
        </h1>
        <label for="title" class="block text-sm font-medium text-gray-700 mt-4">
          Título*
        </label>
        <input
          v-model="title"
          id="title"
          name="title"
          type="text"
          class="mt-1 p-2 border rounded-md w-full"
          required
        />
        <label
          for="description"
          class="block text-sm font-medium text-gray-700 mt-4"
        >
          Descripción del trabajo*
        </label>
        <textarea
          v-model="description"
          id="description"
          name="description"
          rows="4"
          class="mt-1 p-2 border rounded-md w-full"
          required
        ></textarea>
        <button
          class="btn bg-secondary text-gray-50 px-3 py-2 mt-4"
          @click="submitRequest"
          :disabled="isFormInvalid"
        >
          Enviar Solicitud
        </button>
      </div>
    </div>
    <div v-else>
      <p class="text-center text-red-500 mb-4">
        Debes iniciar sesión para solicitar un servicio.
      </p>
      <router-link to="/login">
        <button class="btn btn-block bg-blue-700 mt-5" type="button">
          Iniciar Sesión
        </button>
      </router-link>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { getWithJWT } from '@/helpers/JWTRequest';
import { postWithJWT } from '@/helpers/JWTRequest';
import { useUserStore } from '@/stores/user';
import { useToast } from 'vue-toastification';

const toast = useToast(); // Inicializa el servicio de toasts

const serviceTitle = ref(null);
const serviceName = ref(null);

export default {

  data() {
    return {
      title: '',
      description: '',
      existError: false,
      errorNum: '',
    };
  },
  async beforeMount() {
    const serviceId = this.$route.params.id;

    try {
      const response = await getWithJWT(`/services/${serviceId}`);
      const service = response.data;
      serviceTitle.value = 'Servicio';
      serviceName.value = service.name;
    } catch (error) {
      console.error('Error al obtener la información del servicio:', error);
      this.existError = true;
    }
  },
  computed: {
    fullServiceTitle() {
      return `${serviceTitle.value} - ${serviceName.value}`;
    },
    logged() {
      const userStore = useUserStore();
      return userStore.user !== null;
    },
    isFormInvalid() {
      return !this.title || !this.description;
    },
  },
  methods: {
    async submitRequest() {
      if (this.isFormInvalid) {
        console.log('Campos obligatorios no completados');
        return;
      }

      try {
        const response = await postWithJWT('/me/requests/', {
          title: this.title,
          description: this.description,
          service_id: this.$route.params.id,
        });

        console.log('Respuesta del servidor:', response);

        // Verificar si la respuesta tiene la propiedad 'success' antes de acceder a ella
        if (response.status == 201) {
          toast.success('Solicitud procesada exitosamente');

          const serviceId = this.$route.params.id;
          this.$router.push(`/service/${serviceId}`);
        } else {
          toast.error('Hubo un problema al procesar la solicitud');
        }
      } catch (error) {
        console.error('Error al enviar la solicitud:', error);
        this.existError = true;
        toast.error('Hubo un error al procesar la solicitud');
      }
    },
    redirectToHome: function () {
      // Puedes redirigir a la página principal u otra página según tus necesidades
      this.$router.push('/');
    },
  },
};
</script>

<style scoped>
</style>
