<template>
  <ul class="nav flex-column">
    <p></p>
    <div class="text-center" v-if="loading">
      <div class="spinner-border text-white" role="status">
        <span class="sr-only">Loading...</span>
      </div>
    </div>
    <li class="nav-item" v-for="item in items">
      <router-link class="nav-link collapsed" href="#" data-toggle="collapse" :to="{ name: item.to, params: { 'app':item.app,'view': item.view }}" v-if="item.to" aria-expanded="true" aria-controls="collapseTwo">
        <span class="icon" :class="item.icon_class"></span> &nbsp;
        <span>{{ item.name }}</span>
      </router-link>

      <div v-if="!item.to" class="sidebar-heading">
        {{ item.name }}
      </div>

    </li>
  </ul>
</template>

<script setup>

import {onMounted, ref} from "vue";
import {HttpRequest} from "@/globaltechia/utils.js";

const loading = ref(true);
const items  = ref([]);

onMounted(() => {
  loading.value = true;
  HttpRequest("GET","base","navbar")
    .then((json_data) => json_data.json())
    .then((data) => {

    items.value = data;
    loading.value = false;
  });

});

</script>

<style scoped>


</style>
