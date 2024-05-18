<script setup>
import MapChart from '../components/map/MapChart.vue';
import ServiceChart from '../components/service/ServiceChart.vue';
import { getWithJWT } from '@/helpers/JWTRequest';
import api from '@/helpers/api';
</script>

<script>
const servAux = {
    "id": 1,
    "name": "Cargando...",
    "description": "Cargando...",
    "instId": "1",
    "instName": "Cargando...",
    "instInfo": "Cargando...",
    "location": "-34.903381,-57.937518",
    "web": "Cargando...",
}

export default {
  data() {
    return {
      serviceInfo: {
        // Service: we aren't showing keywords, service_type and enabled
        id: servAux.id,
        name: servAux.name,
        description: servAux.description,
      },
      institutionInfo: {
        // Institution: we aren't showing address, location, days_and_opening_hours, email, enabled, keywords
        id: servAux.inst,
        name: servAux.instName,
        description: servAux.instInfo,
        location: servAux.location,
        web: servAux.web,
      },
      coordAux: {
        xcoord: -34.903381,
        ycoord: -57.937518,
      },
    };
  },
  async created() {
    const serviceId = this.$route.params.id;
    this.serviceInfo.id = serviceId;

    const response = await getWithJWT(`/services/${serviceId}`);
    const service = response.data;
    // Service
    this.serviceInfo.id = service.id
    this.serviceInfo.name = service.name
    this.serviceInfo.description= service.description

    // Institution
    this.institutionInfo.id = service.institution_id

    const responseInst = await api.get(`/institutions/${service.institution_id}`);
    const institution = responseInst.data.data;

    this.institutionInfo.name = institution.name
    this.institutionInfo.info = institution.info
    this.institutionInfo.location = institution.location
    this.institutionInfo.web = institution.web

    this.coordAux = {
      xcoord: this.getCoords(0, this.institutionInfo.location),
      ycoord: this.getCoords(1, this.institutionInfo.location),
    };
  },
  methods: {
    getCoords: function (aux, str) {
      var strCopy = String(str).split(",");
      var coord = parseFloat(strCopy[aux].trim());
      return coord;
    },
    redirectToHome: function () {
      // Puedes redirigir a la página principal u otra página según tus necesidades
      this.$router.push('/');
    },
  },
  components: { ServiceChart, MapChart },
};

</script>

<template>
  <div class="bg-base-100 p-10 w-full h-full items-top justify-center gap-5 grid grid-cols-1 grid-rows-2 md:grid-cols-2 md:grid-rows-1">
    <div class="flex flex-col justify-left items-center md:items-left">
      <ServiceChart class="" :service="serviceInfo" :institution="institutionInfo"/>
      <router-link :to="'/service-request/' + serviceInfo.id">
        <button class="btn bg-secondary max-w-md text-gray-50 px-3 py-2 my-4">Solicitar</button>
      </router-link>
    </div>
    <div class="flex flex-col items-center">
      <h1 class="text-black text-3xl  flex justify-center p-6"> ¿Cómo llegar? </h1>
      <MapChart class=" max-w-full w-full h-full max-h-full md:max-h-80 rounded border-10 border-red-500" :coords="coordAux"></MapChart>
    </div>
  </div>
</template>
