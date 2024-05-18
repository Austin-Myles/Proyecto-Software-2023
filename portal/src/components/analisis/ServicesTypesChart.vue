<script>
import api from '@/helpers/api'
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'
import { Pie } from 'vue-chartjs'

ChartJS.register(ArcElement, Tooltip, Legend)

export default {
  name: 'InstitutionChart',
  components: {
    Pie
  },
  data() {
    return {
      serviceTypes: [],
      chartData: {
        labels: [],
        datasets: [
          {
            label: 'Pedidos por tipo de servicio',
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
    api.get('/analisis/services/types').then(({ data }) => {
      this.services = data.data
      this.chartData = {
        labels: Object.keys(this.services),
        datasets: [
          {
            label: 'Pedidos al tipo de servicio',
            backgroundColor: ['#d64a28', '#66823c', '#edee3f', '#6094cd'],
            data: Object.values(this.services)
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
    <div class="mt-16 w-full">
      <Pie :data="chartData" :options="options" />
    </div>
  </div>
</template>
