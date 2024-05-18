<script setup>
import InstitutionsChart from '../components/analisis/InstitutionsChart.vue'
import ServicesChart from '../components/analisis/ServicesChart.vue'
import ServicesTypesChart from '../components/analisis/ServicesTypesChart.vue'
</script>

<template>
  <section class="grid grid-cols-1 grid-rows-3 gap-8 items-center bg-gray-100 p-12 lg:grid-cols-2 lg:grid-rows-2">
    <InstitutionsChart class="bg-base-200 p-5 rouded-lg h-full" />
    <ServicesChart class="bg-base-200 p-5 rouded-lg h-full" />
    <ServicesTypesChart class="bg-base-200 p-5 rouded-lg h-full" />
  </section>
</template>
