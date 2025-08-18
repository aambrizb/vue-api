<template>
    <SbAdmin2>
      <template #theme>

        <p style="height:30px;"></p>
        <p style="height:30px;"></p>


        <div class="card" style="width:550px;margin:0px auto;">
          <div class="card-header">
            <h1 class="text-center text-primary">Inicio de Sesión</h1>
          </div>
            <div class="card-body">
              <div class="row m-1">
                <div class="col-lg-4">
                  <span class="fa fa-user"></span>
                  Usuario
                </div>
                <div class="col-lg-8">
                  <input type="text" class="form-control" />
                </div>
              </div>
              <div class="row m-1">
                <div class="col-4">
                  <span class="fa fa-key"></span>
                  Contraseña
                </div>
                <div class="col-8">
                  <input type="password" class="form-control" />
                </div>
              </div>
          </div>
          <div class="card-footer">
            <div class="row">
              <div class="col-lg-6"></div>
              <div class="col-lg-6">
                <button type="button" class="btn btn-primary float-end" @click="login();">
                  Iniciar Sesión
                  <span class="fa fa-arrow-right"></span>
                </button>
              </div>
            </div>
          </div>
        </div>
        <h6>Recuperar Contraseña</h6>

      </template>
    </SbAdmin2>


</template>

<script setup>

  import { useRouter } from 'vue-router'
  import SbAdmin2 from "@/globaltechia/theme/sb-admin-2/SbAdmin2.vue";

  const router = useRouter()
  const login = () => {
    localStorage.setItem('token', 'fake-jwt')
    router.push('/app')
  };
</script>

<style scoped>

</style>
