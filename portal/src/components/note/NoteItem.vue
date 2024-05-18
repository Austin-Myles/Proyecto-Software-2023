<template>
  <div class="note-item">
    <p class="author">{{ note.author.username }}:</p>
    <p class="text">{{ note.text }}</p>
    <p class="date">Fecha de Creación: {{ formatDate(note.creation_date) }}</p>
  </div>
</template>

<script>
export default {
  props: {
    note: {
      type: Object,
      required: true,
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
  },
};
</script>

<style scoped>
.note-item {
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin: 10px;
  padding: 16px;
  transition: transform 0.3s ease-in-out;
}

.note-item:hover {
  transform: scale(1.02);
}

.header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 8px;
}

.author {
  font-weight: bold;
  color: #007BFF;
  margin-right: 8px;
}

.date {
  color: #555;
  font-size: 14px;
}

.text {
  font-style: italic;
  color: #333;
}
</style>
