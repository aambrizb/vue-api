<template>
  <div>
    <div class="row m-1" v-if="searchbar">
      <div class="col-10">
        <input ref="inputSearch" type="text" class="form-control" placeholder="Buscar.." v-model="searchtext" v-on:keyup.enter="btnSearch()"/>
      </div>
      <div class="col-1">
        <button class="btn btn-sm btn-secondary" @click="btnSearch()">
          <span class="fa fa-search"></span>
          Buscar
        </button>
      </div>
      <div class="col-1">
        <button class="btn btn-sm btn-secondary -pull-right" hidden>
          <span class="fa fa-download"></span>
        </button>
      </div>
    </div>
    <table class="table table-bordered table-hover table-striped table-sm">
      <thead>
        <tr>
          <th style="width:75px;" v-if="props.selectable == true || props.selectable == 'true'">
            <input type="checkbox" @click="selectAll()" v-model="todo" /> Todo
          </th>
          <th v-for="x in items.headers" :class="'th-'+x.name">{{ x.label }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="x in items.data">
          <td class="text-center" v-if="props.selectable == true || props.selectable == 'true'">
            <input type="checkbox" v-model="x.selected"/>
          </td>
          <td :class="'td-'+y.name" v-for="y in items.headers">
            <router-link  v-if="y.name === 'id'" :to="{ name: 'edit', params: { 'app':$route.params.app,'view': $route.params.view,'id': x[y.name] }}">
              {{ x[y.name] }}
            </router-link>
            <span v-if="y.name !== 'id'">{{ x[y.name] }}</span>
          </td>
        </tr>
      </tbody>
    </table>
    <div class="row" v-if="config && config.pagination">
      <div class="col-2"></div>
      <div class="col-8">
        <ul class="pagination" style="width:300px;margin:0px auto;">
          <li class="page-item">
            <a class="page-link" href="#" @click="prevPage()">
              <span class="fa fa-arrow-left"></span>
            </a>
          </li>
          <li class="page-item" v-for="x in parseInt(config ? config.pagination.total_pages:0)">
            <a class="page-link" v-if="x !== current_page" style="cursor:pointer;" @click="goPage(x)">{{ x }}</a>
            <span class="page-link bg-primary text-white" v-if="x === current_page">{{ x }}</span>
          </li>
          <li class="page-item">
            <a class="page-link" href="#" @click="nextPage();">
              <span class="fa fa-arrow-right"></span>
            </a>
          </li>
        </ul>

      </div>
      <div class="col-2"></div>
    </div>
  </div>

</template>

<script setup>
 import {onMounted, ref} from "vue";
 import {HttpRequest} from "@/globaltechia/utils.ts";
 import {useRoute, useRouter} from "vue-router";

 const props        = defineProps(['app','view','selectable','query_params']);
 const items        = ref({});
 const route        = useRoute()
 const router       = useRouter()
 const todo         = ref(false);
 const searchtext   = ref(null);
 const searchbar    = ref(false);
 const inputSearch  = ref(null);
 const current_page = ref(null);
 const total_pages  = ref(null);
 const config       = ref(null);

 onMounted(() => {
   search();

   let searchParams = new URLSearchParams(props.query_params);
   let queryParamsObject = Object.fromEntries(searchParams);
   searchtext.value = queryParamsObject.search;

   if (queryParamsObject.page !== undefined) {
    current_page.value = parseInt(queryParamsObject.page);
   }
   else {
     goPage(1);
   }

 });

 const selectAll = () => {

   items.value.data.forEach((x) => {
     x.selected = !todo.value;
   });

 }

 const btnSearch = () => {

   let tmp = router.resolve({
    name: 'list',
    params: {
      app  : route.params.app,
      view : route.params.view
    },
  });

   window.location.href = tmp.fullPath+"?search="+searchtext.value;

 }

 const goPage = (page) => {
   current_page.value = page;

   let params = new URLSearchParams(document.location.search);
   params.set("page",page);

   window.location.href = window.location.pathname+"?"+params

 };
 const nextPage = () => {
   if (current_page.value < total_pages.value) {
     goPage(current_page.value += 1);
   }
 }

 const prevPage = () => {
   if (current_page.value > 1) {
     goPage(current_page.value -= 1);
   }
 }

 const search = () => {
  HttpRequest("GET",route.params.app+"/"+route.params.view+"/list"+props.query_params)
        .then((data_json) => data_json.json())
        .then((data) => {
          items.value  = data;
          config.value = data.props;

          if (data.props.search !== undefined) {
            searchbar.value = true;
          }

          if (data.props && data.props.pagination && data.props.pagination.total_pages !== undefined) {
            total_pages.value = data.props.pagination.total_pages;
          }

        });
 }
</script>

<style scoped>
.td-id,.th-id {
  width:45px;
  text-align: center;
}

.table {
  font-size:13px;
}
</style>
