<template>

    <div class="" id="mapContainer"></div>
  </template>

  <script>
  import "leaflet/dist/leaflet.css";
  import L from "leaflet";

  export default{
    name:"LeafletMap",

    props:{
      coords: {
          type: Object,
          required: true,
          default: () => ({
              xcoord: 0,
              ycoord: 0,
          }),
      },
    },
    data() {
      return {
        map: null,
        xcoord: this.coords.xcoord,
        ycoord: this.coords.ycoord,
      };
    },
    mounted() {
      this.map = L.map("mapContainer").setView([ this.xcoord , this.ycoord] , 14);
      L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", {
        attribution:
          '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      }).addTo(this.map);
      L.marker([this.xcoord , this.ycoord]).addTo(this.map);
    },
    onBeforeUnmount() {
      if (this.map) {
        this.map.remove();
      }
    },
  };


  </script>

  <style>
  #mapContainer {
    width: 50vw;
    height: 50vw;
    z-index: 0;
  }
  </style>
