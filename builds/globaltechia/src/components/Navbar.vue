<template>
  <div class="text-center" v-if="loading">
    <div class="spinner-border text-white" role="status">
      <span class="sr-only">Loading...</span>
    </div>
  </div>
  <ul id="navmenu" class="nav">
    <li class="nav-item" v-for="item in items">
      <div v-if="!item.to" class="sidebar-heading">
        {{ item.name }}
      </div>

      <div v-for="x in item.children">
        <a :href="'/view/'+x.app+'/'+x.view+(x.list ? '/list' : '')" class="nav-link">
          <span class="icon" :class="x.icon_class"></span> &nbsp;
          <span>{{ x.name }}</span>
        </a>
      </div>
    </li>
  </ul>
</template>

<script setup>

import {onBeforeUnmount, onMounted, ref} from "vue";
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

  updateHeights()
  window.addEventListener('resize', updateHeights)

});

onBeforeUnmount(() => {
  window.removeEventListener('resize', updateHeights)
})

const updateHeights = () => {
  let base_height   = 120;
  let total_height  = document.documentElement.scrollHeight;
  let final_height  = total_height-base_height;

  let el            = document.getElementById('navmenu');
  el.style.height   = final_height+"px";
  el.style.overflow = 'auto';

  let cont          = document.getElementById('content');
  cont.style.height   = final_height+"px";
  cont.style.overflow = 'auto';
}

</script>

<style scoped>


</style>
