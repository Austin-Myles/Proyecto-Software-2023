<script setup>
import { useUserStore } from '@/stores/user'
import { computed } from 'vue'
const userStore = useUserStore()
const username = computed(() => (userStore.username ? ` ${userStore.username}` : ''))
</script>

<template>
  <div
    class="bg-gray-50 rounded-md px-3 md:px-5 flex flex-col justify-center items-center shadow-xl"
  >
    <img src="/Logo.jpg" class="p-5" />
    <h1 class="text-black text-xl md:text-3xl text-center p-8">Bienvenido{{ username }}!</h1>

    <div class="carousel rounded-box w-100vw h-60 border-8 border-accent">
      <div class="carousel-item">
        <img src="/backgrounds/1.jpg" alt="Burger" />
      </div>
      <div class="carousel-item">
        <img src="/backgrounds/2.jpg" alt="Burger" />
      </div>
      <div class="carousel-item">
        <img src="/backgrounds/3.jpg" alt="Burger" />
      </div>
      <div class="carousel-item">
        <img src="/backgrounds/5.jpg" alt="Burger" />
      </div>
      <div class="carousel-item">
        <img src="/backgrounds/6.jpg" alt="Burger" />
      </div>
    </div>
    <div class="">
      <p class="text-start text-lg md:text-xl p-6">
        En la actualidad, el CIDEPINT es una institución que depende del sistema CICPBA-CONICET-UNLP
        y ha ampliado considerablemente su campo de experiencia. El centro cuenta hoy con personal
        capacitado en el desarrollo y caracterización de pinturas anticorrosivas y decorativas,
        antiincrustantes, con propiedades antifúngicas, entre otras con aplicaciones específicas. De
        la misma manera se incorporaron líneas de trabajo en el área de pretratamientos de aceros,
        biodeterioro de materiales estructurales, inhibición de la corrosión, galvanoplastía y
        siderurgia, muchas de las cuales se enfocan en la obtención de alternativas ecológicas que
        reduzcan el impacto de la industria sobre el medio ambiente.
      </p>
      <div class="collapse collapse-arrow bg-base-200 mb-3">
        <input type="checkbox" name="my-accordion-2" />
        <div class="collapse-title text-xl font-medium">Realizar búsqueda de servicios</div>
        <div class="collapse-content bg-base-300">
          <p class="p-6">
            Cualquier usuario autenticado en la aplicación podra realizar búsquedas de los distintos
            servicios que estan disponibles, traidos a usted por la gran gama de instituciones
            pertenecientes a la aplicación.
          </p>
        </div>
      </div>
      <div class="collapse collapse-arrow bg-base-200 mb-3">
        <input type="checkbox" name="my-accordion-2" />
        <div class="collapse-title text-xl font-medium">Listar servicios por institución</div>
        <div class="collapse-content bg-base-300">
          <p class="p-6">
            Es posible acceder a una sección en la cual se listaran todos los servicios prestados
            por cada una de las instituciones asociadas a la aplicación.
          </p>
        </div>
      </div>
      <div class="collapse collapse-arrow bg-base-200 mb-3">
        <input type="checkbox" name="my-accordion-2" />
        <div class="collapse-title text-xl font-medium">Iniciar una solicitud de servicio</div>
        <div class="collapse-content bg-base-300">
          <p class="p-6">
            Podrá realizar una solicitud al servicio que usted seleccione, podra ver la información
            asociada a la institución seleccionada, el servicio que presta y se le mostrara un
            formulario el cual debera completar para realizar la solicitud del servicio deseado.
          </p>
        </div>
      </div>
    </div>
  </div>
  <br />
</template>
