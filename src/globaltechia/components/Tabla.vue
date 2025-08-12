<template>
  <div>
    <div class="row m-1">
      <div class="col-10">
        <input type="text" class="form-control" placeholder="Buscar.." />
      </div>
      <div class="col-1">
        <button class="btn btn-sm btn-secondary">
          <span class="fa fa-search"></span>
          Buscar
        </button>
      </div>
      <div class="col-1">
        <button class="btn btn-sm btn-secondary -pull-right">
          <span class="fa fa-download"></span>
        </button>
      </div>
    </div>
    <table class="table table-bordered table-hover table-striped table-sm">
      <thead>
        <tr>
          <th style="width:75px;">
            <input type="checkbox" /> Todo
          </th>
          <th class="th-">Id</th>
          <th class="th-">Nombre</th>
          <th class="th-">Paterno</th>
          <th class="th-">Materno</th>
          <th class="th-">Email</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items">
          <td>
            <input type="checkbox" />
          </td>
          <td>1</td>
          <td>JESUSNombre</td>
          <td>Paterno</td>
          <td>Materno</td>
          <td>Email</td>
        </tr>
      </tbody>
    </table>
    <div class="row">
      <div class="col-2"></div>
      <div class="col-8">
        <ul class="pagination" style="width:300px;margin:0px auto;">
          <li class="page-item">
            <a class="page-link" href="#">
              <span class="fa fa-arrow-left"></span>
            </a>
          </li>
          <li class="page-item"><a class="page-link" href="#">1</a></li>
          <li class="page-item"><a class="page-link" href="#">2</a></li>
          <li class="page-item"><a class="page-link" href="#">3</a></li>
          <li class="page-item">
            <a class="page-link" href="#">
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
 import {ref} from "vue";

 const items = ref([{},{},{}]);
</script>

<style scoped>

</style>
