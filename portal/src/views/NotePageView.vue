<template>
  <form class="note-page" @submit.prevent="addNote">
    <h2 class="page-title">Notas de la Solicitud</h2>
    <div v-if="loading">Cargando notas...</div>
    <div v-else>
      <div v-if="formattedNotes.length > 0">
        <NoteItem v-for="note in formattedNotes" :key="note.id" :note="note" />
      </div>
      <div v-else>
        <p class="no-notes-message">No hay notas para esta solicitud.</p>
      </div>
    </div>
    <textarea v-model="newNote" placeholder="Agregar nueva nota" class="new-note-input" required></textarea>
    <button class="add-note-btn" :disabled="isAddNoteDisabled" type="submit">Agregar Nota</button>
  </form>
</template>

<script>
import { getWithJWT, postWithJWT } from '@/helpers/JWTRequest';
import NoteItem from '@/components/note/NoteItem.vue';

export default {
  data() {
    return {
      notes: [],
      newNote: '',
      loading: true,
      serviceRequestId: null,
    };
  },
  computed: {
    formattedNotes() {
      return this.notes.map((note) => {
        return {
          ...note,
          creation_date: this.formatDate(note.creation_date),
        };
      });
    },
  },
  methods: {
    formatDate(dateString) {
      const formattedDate = new Date(dateString);
      const options = {
        year: 'numeric', month: '2-digit', day: '2-digit',
        hour: '2-digit', minute: '2-digit',
        timeZone: Intl.DateTimeFormat().resolvedOptions().timeZone,
      };
      return formattedDate.toLocaleDateString(undefined, options);
    },
    addNote() {
      const route = `/me/requests/${this.serviceRequestId}/notes`;
      postWithJWT(route, { text: this.newNote })
        .then((response) => {
          console.log('Nueva nota agregada:', response);
          this.loadNotes();
          this.newNote = '';
        })
        .catch((error) => {
          console.error('Error al agregar nota:', error);
        });
    },
    loadNotes() {
      const route = `/me/requests/${this.serviceRequestId}`;
      getWithJWT(route)
        .then((response) => {
          console.log(response.notes);

          this.notes = response.data.data.notes;
        })
        .catch((error) => {
          console.error('Error al cargar notas:', error);
        })
        .finally(() => {
          this.loading = false;
        });
    },
  },
  components: {
    NoteItem
  },
  mounted() {
    this.serviceRequestId = this.$route.params.id;
    this.loadNotes();
  },
};
</script>

<style scoped>
.note-page {
  background-color: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
}

.page-title {
  color: #007bff;
  font-size: 24px;
  margin-bottom: 20px;
}

.no-notes-message {
  margin-top: 20px;
}

.new-note-input {
  width: 100%;
  margin-bottom: 10px;
}

.add-note-btn {
  background-color: #007bff;
  color: #fff;
  padding: 8px 16px;
  border: none;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  cursor: pointer;
}

.add-note-btn:hover {
  background-color: #0056b3;
}

.note-warning {
  color: red;
  margin-top: 5px;
}
</style>
