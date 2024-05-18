<script>
    import api from '@/helpers/api';

    export default {
        data() {
            return {
                services: [],
                tipos: [],
                page: 1,
                perPage: 6,
                filterType: "Todos",
                search: "",
                notFound: false,
            }
        },
        async beforeMount() {
            // Saving the list of all types of services
            const params = new URLSearchParams({
                    page: this.page,
                    per_page: this.perPage,
                }).toString();
            const url = "/services/search?" + params;
            console.log(url);

            const typesResponse = await api.get("/service-types/");
            this.tipos = typesResponse.data.data;
            // Saving the list of services
            const servicesResponse = await api.get(url);
            this.services = servicesResponse.data.data;
        },
        methods: {
            async refreshServices(params) {
                const url = "/services/search?" + params;
                console.log(url);

                const servicesResponse = await api.get(url);
                this.services = servicesResponse.data.data;
                this.notFound = this.services.length === 0;
            },
            async handleSearch(){
                // TODO: Change search parameters
                if(this.type === "Todos"){
                    this.filters.filterType = "";
                }
                const params = new URLSearchParams({
                    page: this.page,
                    per_page: this.perPage,
                    q: this.search,
                    type: this.filterType,
                }).toString();

                this.refreshServices(params);
            },
            async nextPage() {
                this.page++;
                const params = new URLSearchParams({
                    page: this.page,
                    per_page: this.perPage,
                }).toString();

                this.refreshServices(params);
            },
            async previousPage() {
                this.page--;
                const params = new URLSearchParams({
                    page: this.page,
                    per_page: this.perPage,
                }).toString();

                this.refreshServices(params);
            },
            pickColor() {
                // Randomly picks a color from the list of colors
                const colors = ["#c45720", "#d5df62"];
                return colors[Math.floor(Math.random() * colors.length)];

            },
        },
        computed: {
            canPrevious() {
                return this.page != 1;
            },
            canNext() {
                return this.services.length >= this.perPage;
            },
            isAuth() {
                return localStorage.getItem('token') !== null;
            }
        }
    }
</script>

<template>
    <div class=" bg-base-100 p-10 w-full min-h-full shadow-xl">
        <!-- Searchbars -->
        <form action="submit" @submit.prevent="handleSearch">
            <label class="label">
                <span class="label-text">Busque aquí un servicio</span>
            </label>
            <div class=" flex flex-row w-full join">
                <select v-model="filterType" class="select select-bordered join-item">
                    <option selected>Todos</option>
                    <option v-for="tipo in this.tipos" :key="tipo.data">{{tipo}}</option>
                </select>
                <input v-model="search" type="text" class=" input input-bordered join-item w-full flex-1" placeholder="Título de servicio, descripción del servicio, nombre de institución, tags..." />
                <button type="submit" class="btn bg-blue-700 join-item text-white">
                    <svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
                    </svg>
                </button>
            </div>
        </form>
        <div v-if="this.services.length > 0" class="w-full grid grid-cols-1 gap-7 md:grid-cols-2 lg:grid-cols-3 mt-12">
            <div class="card w-full bg-base-300 shadow-xl h-56" v-for="service in this.services" :key="service.id">
                <div class="card-body justify-between overflow-auto">
                    <h2 class="card-title">Servicio: {{ service.name }}</h2>
                    <p class="flex-1">Descripción: {{ service.description }}</p>
                    <div class="card-actions justify-end ">
                        <a class="btn btn-primary bg-[#c45720]" :href="'/service/'+service.id" :disabled="isAuth">Ver más</a>
                    </div>
                </div>

            </div>
        </div>
        <div v-else-if="this.services.length === 0 && ! this.notFound" class="w-full h-full flex items-center justify-center">
            <span class="loading loading-dots loading-lg"></span>
        </div>
        <!-- TODO: fix pagination buttons disappearing -->
        <div v-else class="w-full h-full flex items-center justify-center my-32">
            <h1 class="text-2xl text-gray-950 text-left mb-3">No se encontraron resultados</h1>
        </div>
        <div class="join w-full flex items-center justify-around mt-7 ">
            <div>
                <button class="join-item btn bg-blue-700 text-gray-200" @click="previousPage" :disabled="! canPrevious">«</button>
                <button class="join-item btn bg-blue-700 text-gray-200">Page {{page}}</button>
                <button class="join-item btn bg-blue-700 text-gray-200" @click="nextPage" :disabled="! canNext">»</button>
            </div>
        </div>
    </div>
</template>
