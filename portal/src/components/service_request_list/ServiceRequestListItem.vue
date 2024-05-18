<template>
  <div>
    <p class="title">{{ serviceRequestListItem.title }}</p>
    <p class="date">{{ formatDate(serviceRequestListItem.creation_date) }}</p>
    <p class="description">{{ serviceRequestListItem.description }}</p>
    <p class="status">{{ serviceRequestListItem.status }}</p>
    <div class="notes-container" @click="navigateToNotePage">
      <p class="notes-text">Notas</p>
      <router-link :to="{ name: 'NotePage', params: { id: serviceRequestListItem.id } }">
        <span class="note-icon">
          <FontAwesomeIcon icon="sticky-note" />
        </span>
      </router-link>
    </div>
  </div>
</template>

<script>
import { format } from 'date-fns'; //para el formato del creation date
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'; //para el icono de notas
// import { faStickyNote } from '@fortawesome/free-solid-svg-icons';


export default {
  components:{
    FontAwesomeIcon,
  },
  props: {
    serviceRequestListItem: {
      type: Object,
      required: true,
    },
  },
  methods: {
    formatDate(date) {
      return format(new Date(date), 'dd/MM/yyyy');
    },
    navigateToNotePage() {
      // Navegar a la página de notas al tocar cualquier parte del contenedor
      this.$router.push({ name: 'NotePage', params: { id: this.serviceRequestListItem.id } });
    },
  },
};
</script>

<style scoped>
  div {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 10px;
    border: 1px solid #ccc;
    margin: 10px;
    background-color: #fff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease-in-out;
  }

  div:hover {
    transform: scale(1.05);
  }

  p {
    margin: 0;
    font-size: 16px;
    color: #333;
  }

  .title {
    font-size: 20px;
    font-weight: bold;
    color: #333;
  }
  .date {
    font-weight: bold;
    color: #007BFF;
  }

  .description {
    font-style: italic;
  }

  .status {
    color: #28A745;
  }
  .notes-container {
  display: flex;
  align-items: center;
  padding: 5px; /* Ajusta el relleno según tu diseño */
  background-color: #007BFF; /* Color azul para el fondo */
  color: #fff; /* Color blanco para el texto */
  cursor: pointer;
}

.notes-text {
  margin-right: 10px;
  font-size: 18px;
}

.note-icon {
  font-size: 24px;
  color: #fff; 
}
</style>
