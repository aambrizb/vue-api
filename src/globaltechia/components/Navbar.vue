<template>
  <ul class="nav flex-column">
    <p></p>
    <li class="navbar-item" v-for="item in items">
      <router-link class="nav-link" :to="{ name: item.to, params: { 'app':item.app,'view': item.view }}" v-if="item.to">
        <span class="icon" :class="item.icon_class"></span>
        {{ item.name }}
      </router-link>
      <span v-if="!item.to" class="text-muted">
        <span class="icon" :class="item.icon_class"></span>
        {{ item.name }}
      </span>
    </li>
  </ul>
</template>

<script setup>

const items = [
  {
    name       : 'Administración',
    icon_class : 'fa fa-cog'
  },
  {
    name       : 'Ordenes',
    to         : 'create',
    app        : 'app',
    view       : 'orden',
    icon_class : 'fa fa-times'
  },
  {
    name       : 'Almacen',
    icon_class : 'fa fa-cog'
  },
  {
    name       : 'Productos',
    to         : 'create',
    app        : 'app',
    view       : 'producto',
    icon_class : 'fa fa-slash'
  },
  {
    name       : 'Personalizada',
    to         : 'create',
    app        : 'app',
    view       : 'personalizada',
    icon_class : 'fa fa-slash'
  },
  {
    name       : 'Reportes',
    icon_class : 'fa fa-list'
  },
  {
    name       : 'Activaciones',
    to         : 'reporte_activaciones',
    app        : 'app',
    view       : 'personalizada',
    icon_class : 'fa fa-file'
  },
];
</script>

<style scoped>
.navbar-item .nav-link {
    height: 30px;
    cursor:pointer;
    border-radius: 20px;
}
.navbar-item .nav-link:hover {
    background-color:#c4c4c4;
    font-weight: bold;
}

.navbar-item a {
    font-size:11px;
    color:black;
}

.icon {
    color:dodgerblue;
}

</style>
