<template>
  <h1 class="text-center">Usuario</h1>
  <h2 class="text-center"></h2>
  <div class="container-fluid">
    <div class="card">
      <div class="card-body">
        <ul class="nav nav-tabs" id="myTab" role="tablist">
          <li class="nav-item" role="presentation">
            <button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home" type="button" role="tab" aria-controls="home" aria-selected="true">
              <span class="fa fa-cog"></span>
              General
            </button>
          </li>
          <li class="nav-item" role="presentation">
            <button class="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile" type="button" role="tab" aria-controls="profile" aria-selected="false">
              <span class="fa fa-user-group"></span>
              Grupos
            </button>
          </li>
          <li class="nav-item" role="presentation">
            <button class="nav-link" id="contact-tab" data-bs-toggle="tab" data-bs-target="#contact" type="button" role="tab" aria-controls="contact" aria-selected="false">
              <span class="fa fa-list"></span>
              Permisos
            </button>
          </li>
        </ul>
        <div class="tab-content p-4" id="myTabContent">
          <div class="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab">
            <GenericItem :item="items['email']" />
          </div>
          <div class="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab">
            Grupos
          </div>
          <div class="tab-pane fade" id="contact" role="tabpanel" aria-labelledby="contact-tab">
            Permisos
          </div>
        </div>
      </div>
      </div>
    </div>

  <button type="button" @click="accion">Accion</button>
  <button type="button" @click="accion_dos">Segundo</button>

  <component :is="last_component"></component>

</template>

<script setup>
import {ref} from "vue";
import {CharField, openModal} from "@/globaltechia/utils.js";
import GenericItem from "@/globaltechia/components/GenericItem.vue";
import GenericModalView from "@/globaltechia/components/GenericModalView.vue";
import PruebaModal from "@/modals/PruebaModal.vue";
import PruebaModalSegundo from "@/modals/PruebaModalSegundo.vue";
const items = ref({});
const last_component = ref(null);


const accion = () => {
  openModal(last_component,PruebaModal);
}

const accion_dos = () => {
  openModal(last_component,PruebaModalSegundo);
}

items.value = {
  'email': new CharField({type:"text",name:"email"})
}


</script>

<style scoped>

</style>