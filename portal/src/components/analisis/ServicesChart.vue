<script>
import api from '@/helpers/api'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js'
import { Bar } from 'vue-chartjs'

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)

export default {
  name: 'InstitutionChart',
  components: {
    Bar
  },
  data() {
    return {
      services: [],
      chartData: {
        labels: [],
        datasets: [
          {
            label: 'Pedidos por servicio',
            backgroundColor: '#d64a28',
            data: []
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: true
      }
    }
  },
  mounted() {
    api.get('/analisis/services/ranking').then(({ data }) => {
      this.services = data.data
      this.chartData = {
        labels: this.services.map((service) => service.name),
        datasets: [
          {
            label: 'Pedidos al servicio',
            backgroundColor: '#d64a28',
            data: this.services.map((service) => service.request_count)
          }
        ]
      }
    })
  }
}
</script>

<template>
  <div class="flex flex-col items-center justify-center">
    <h2 class="md:text-2xl font-semibold">Ranking de los servicios mas solicitados</h2>
    <div class=" mt-16 w-full">
      <Bar :data="chartData" :options="options" />
    </div>
  </div>
</template>
