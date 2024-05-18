<script>

export default{
    props: {
        service: {
            type: Object,
            required: true
        },
        institution: {
            type: Object,
            required: true
        }
    },
};
</script>

<template>
  <div class="bg-base-100">
    <h1 class="text-black text-3xl  flex justify-center p-6"> {{ service.name }} </h1>
    <div class="bg-base-200 p-6">
        <h1 class="text-black text-xl p-3 pl-0">Detalle</h1>
        <p class="bg-base-300">{{ service.description }}</p>
    </div>
    <div class="bg-base-200 p-6">
        <h1 class="text-black text-xl p-3 pl-0" >Institution: {{ institution.name }}</h1>
        <p class="bg-base-300">Descripción: <b>{{ institution.info }}</b></p>
        <p class="bg-base-300">Web: <b><a :href="institution.web">{{ institution.web }}</a></b></p>

    </div>
  <br>
  </div>
</template>
