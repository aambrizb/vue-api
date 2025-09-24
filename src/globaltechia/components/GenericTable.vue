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
    </div>
    <div class="row">
      <div class="col-1">
        <span class="fa fa-trash-alt text-danger ml-4" style="cursor:pointer;" @click="RemoveItems"></span>
      </div>
    </div>
    <table class="table table-bordered table-hover table-striped table-sm">
      <thead>
        <tr>
          <th class="text-center" style="width:75px;" v-if="props.selectable == true || props.selectable == 'true'">
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
            <a :href="'/view/'+props.app+'/'+props.view+'/'+x[y.name]" v-if="y.name === 'id'">
              {{ x[y.name] }}
            </a>
            <span v-if="y.name !== 'id' && !y.boolean">
              {{ x[y.name] }}
            </span>
            <span v-if="y.name !== 'id' && y.boolean">
              <span class="fa" :class="x[y.name] ? 'fa-check-circle text-success':'fa-times-circle text-danger' "></span>
            </span>
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
 import {HttpRequest} from "../utils";
 import {useRouter} from "vue-router";
 import Swal from "sweetalert2";

 const props        = defineProps(['to','app','view','selectable','query_params']);
 const emit         = defineEmits(["loaded"]);

 const name         = ref('');
 const items        = ref({});
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
      app  : props.app,
      view : props.view
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
  HttpRequest("GET",props.app+"/"+props.view+"/list"+props.query_params)
        .then((data_json) => data_json.json())
        .then((data) => {

          name.value   = data.verbose_name;
          items.value  = data;
          config.value = data.props;

          if (data.props.search !== undefined) {
            searchbar.value = true;
          }

          if (data.props && data.props.pagination && data.props.pagination.total_pages !== undefined) {
            total_pages.value = data.props.pagination.total_pages;
          }

          emit("loaded",name);
        });
 }

 const RemoveItems = () => {
   let selected = items.value.data.filter((item) => item.selected);
   if (selected.length == 0) {
    Swal.fire("Debe seleccionar al menos un elemento.", "", "warning");
   }
   else {

       Swal.fire({
        title: "¿Realmente desea eliminar este elemento?",
        showDenyButton: true,
        confirmButtonText: "Si",
        denyButtonText: `No`
      }).then((result) => {
        if (result.isConfirmed) {
         const ids = selected.map(item => item.id);
         HttpRequest("POST","method/base/removeItems",{
           app   : props.app,
           view  : props.view,
           data  : JSON.stringify(ids)
         }).then(
           (item) => item.json()
         ).then((data) => {
           if (data.code == 200) {
             Swal.fire(data.msg, "", "success");
             search();
           }
         })
        }
      });
   }

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
