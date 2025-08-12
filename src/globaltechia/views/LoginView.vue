<template>

    <h1 class="text-center text-primary">Inicio de Sesión</h1>

    <div class="card" style="width:400px;margin:0px auto;">
      <div class="card-header"></div>
        <div class="card-body">
          <div class="row m-1">
            <div class="col-4">Usuario</div>
            <div class="col-8">
              <input type="text" class="form-control" />
            </div>
          </div>
          <div class="row m-1">
            <div class="col-4">Contraseña</div>
            <div class="col-8">
              <input type="password" class="form-control" />
            </div>
          </div>
      </div>
      <div class="card-footer">
        <div class="row">
          <div class="col-6"></div>
          <div class="col-6">
            <button type="button" class="btn btn-primary" @click="login();">
              Iniciar Sesión
              <span class="fa fa-arrow-right"></span>
            </button>
          </div>
        </div>

      </div>
    </div>

</template>

<script setup>

  import { useRouter } from 'vue-router'

  const router = useRouter()
  const login = () => {
    localStorage.setItem('token', 'fake-jwt')
    router.push('/app')
  };
</script>

<style scoped>

</style>
