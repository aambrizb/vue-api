<template>
    <nav class="navbar navbar-dark fixed-top bg-dark flex-md-nowrap p-0 shadow" style="height: 55px;">
      <a class="navbar-brand col-sm-3 col-md-2 mr-0" href="#">
        &nbsp;
        GlobalTechIA
      </a>
      <ul class="navbar-nav px-3">
        <li class="nav-item text-nowrap">
          <a class="nav-link" href="#" @click="logout();">
            Salir
            <span class="fa fa-sign-out"></span>
          </a>
        </li>
      </ul>
    </nav>

    <div class="container-fluid" style="padding-top:50px;">
      <div class="row">
        <nav class="col-md-1 d-none d-md-block bg-light sidebar">
          <div class="sidebar-sticky">
            <Navbar />
          </div>
        </nav>

        <main role="main" class="col-md-11 ml-sm-auto col-lg-11 px-4 p-4">
          <router-view />
        </main>
      </div>
    </div>

</template>

<script setup>

  import { useRouter } from 'vue-router'
  import Navbar from "@/globaltechia/components/Navbar.vue";

  const router = useRouter()
  const logout = () => {
    localStorage.removeItem('token');
    router.push('/login')
  };

</script>

<style scoped>

</style>
