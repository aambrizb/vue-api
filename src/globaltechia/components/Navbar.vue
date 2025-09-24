<template>
  <div class="text-center" v-if="loading">
    <div class="spinner-border text-white" role="status">
      <span class="sr-only">Loading...</span>
    </div>
  </div>
  <ul class="nav" style="height:750px;overflow:auto;">
    <li class="nav-item" v-for="item in items">
      <div v-if="!item.to" class="sidebar-heading">
        {{ item.name }}
      </div>

      <div v-for="x in item.children">
        <router-link class="nav-link" href="#" :to="{ name: x.to, params: { 'app':x.app,'view': x.view }}" v-if="x.to" aria-expanded="true" aria-controls="collapseTwo">
          <span class="icon" :class="x.icon_class"></span> &nbsp;
          <span>{{ x.name }}</span>
        </router-link>
      </div>
    </li>
  </ul>
</template>

<script setup>

import {onMounted, ref} from "vue";
import {HttpRequest} from "../utils";

const loading = ref(true);
const items   = ref([]);

onMounted(() => {
  loading.value = true;
  HttpRequest("GET","method/base/navbar")
    .then((json_data) => json_data.json())
    .then((data) => {

    items.value   = data;
    loading.value = false;
  });

});

</script>

<style scoped>


</style>
