<template>
    <SbAdmin2>
      <template #theme>

        <p style="height:30px;"></p>
        <p style="height:30px;"></p>
        <slot name="logo"></slot>
        <div style="width: 750px;margin:0px auto;">
          <Notification v-for="item in messages" :type="item.type" :msg="item.msg" />
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
                  <input type="text" class="form-control" v-model="username" v-on:keyup.enter="login();" />
                </div>
              </div>
              <div class="row m-1">
                <div class="col-lg-4">
                  <span class="fa fa-key"></span>
                  Contraseña
                </div>
                <div class="col-lg-8">
                  <input type="password" class="form-control" v-model="password" v-on:keyup.enter="login();" />
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
        </div>

      </template>
    </SbAdmin2>


</template>

<script setup>

  import { useRouter } from 'vue-router'
  import SbAdmin2 from "@/globaltechia/theme/sb-admin-2/SbAdmin2.vue";
  import {ref} from "vue";
  import Notification from "@/globaltechia/components/Notification.vue";
  import {HttpRequest} from "@/globaltechia/utils.ts";

  const router   = useRouter();
  const messages = ref([]);
  const username = ref(null);
  const password = ref(null);

  const login = () => {

    console.log(username.value);
    console.log(password.value);

    if (username.value == null || password.value == null || username.value == '' || password.value == '') {
      messages.value = [{
        type : 'danger',
        msg  : "Por favor capture usuario y contraseña para poder continuar"
      }];
    }
    else {
      HttpRequest("POST",'method/base/login',{
        username : username.value,
        password : password.value
      })
          .then( (data_json) => data_json.json())
          .then((data) => {
            if (data.status == 200 && data.token) {
              localStorage.setItem('token', data.token)
              localStorage.setItem('name', data.fullname)
              router.push('/app')
            } else {
              messages.value = [{
                type : 'danger',
                msg  : data.msg
              }];
            }
          });

      messages.value = [{
        type : 'success',
        msg  : "Operación realizada con éxito"
      }];
    }


  };
</script>

<style scoped>

</style>
