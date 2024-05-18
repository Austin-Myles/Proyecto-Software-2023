<script>
import api from '@/helpers/api'
import {
  Chart,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js'
import { formatDuration, intervalToDuration } from 'date-fns'
import { Line as LineChart } from 'vue-chartjs'
import es from 'date-fns/locale/es'
Chart.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend)

export default {
  name: 'InstitutionChart',
  components: {
    LineChart
  },
  data() {
    return {
      institutions: [],
      chartData: {
        labels: [],
        datasets: [
          {
            label: 'Tiempo de resolucion',
            backgroundColor: '#d64a28',
            data: []
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: true,
        plugins: {
          tooltip: {
            callbacks: {
              label: function (context) {
                var label = context.dataset.label || ''

                if (label) {
                  label += ': '
                }
                if (context.parsed.y !== null && context.parsed.y !== 0) {
                  const duration = intervalToDuration({ start: 0, end: context.parsed.y * 1000 })
                  label += formatDuration(duration, { locale: es })
                } else {
                  label += 'Sin promedio'
                }
                return label
              }
            }
          }
        }
      }
    }
  },
  mounted() {
    api.get('/analisis/institutions/ranking').then(({ data }) => {
      const institutions = data.data
      this.institutions = institutions
      this.chartData = {
        labels: institutions.map((institution) => institution.name),
        datasets: [
          {
            label: 'Tiempo de resolucion',
            backgroundColor: '#d64a28',
            data: institutions.map((institution) => institution.time_resolution ?? 0)
          }
        ]
      }
    })
  }
}
</script>

<template>
  <div class="flex flex-col items-center justify-center">
    <h2 class="md:text-2xl font-semibold">
      Ranking de las 10 instituciones con mejor tiempo de resolucion (en horas)
    </h2>
    <div class="w-full mt-16">
      <LineChart :data="chartData" :options="options" />
    </div>
  </div>
</template>
