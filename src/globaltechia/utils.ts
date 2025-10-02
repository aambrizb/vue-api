import {createRouter, createWebHistory} from "vue-router";
import type { RouteRecordRaw } from "vue-router";
import LoginView from "./views/LoginView.vue";
import SystemView from "./views/SystemView.vue";
import GenericModelView from "./components/GenericModelView.vue";
import GenericList from "./components/GenericList.vue";
import DashboardView from "./views/DashboardView.vue";
import UserView from "./views/UserView.vue";
import UserViewList from "./views/UserViewList.vue";
import GroupView from "./views/GroupView.vue";
import GroupViewList from "./views/GroupViewList.vue";
import { Modal } from 'bootstrap';
import {markRaw, nextTick, ref} from "vue";
import type { Component } from "vue";
import Swal from "sweetalert2";


const last_component        = ref(null)
const last_component_params = ref(null);

function toCapital(item:string|undefined|null) {

  let words       = ""
  let final_words = ""

  if (item !== undefined && item !== null) {
    words = item.replace("_"," ");
  }

  let split_words = words.split(" ");
  split_words.forEach((x) => {
    final_words += x.charAt(0).toUpperCase() + x.slice(1)+ " ";
  });

  return final_words;
}
class FormField {

    type: string | undefined | null
    name: string | undefined | null
    label: string | undefined | null
    help_text: string | undefined | null
    required: boolean
    error: string | undefined | null
    value: string | undefined | null
    disabled: boolean
    klass: string | undefined | null
    label_class: string | undefined | null
    input_class: string | undefined | null

   constructor({
                  type = null,
                  name = null,
                  label = '',
                  help_text = '',
                  required = true,
                  error = null,
                  value = null,
                  disabled = false,
                  klass = 'form-control',
                  label_class = 'col-lg-2 col-md-2 col-sm-2 col-xs-12',
                  input_class = 'col-lg-2 col-md-2 col-sm-2 col-xs-12'
               }) {
      this.type        = type;
      this.name        = name;
      this.label       = label;
      this.help_text   = help_text;
      this.required    = required;
      this.error       = error;
      this.value       = value;
      this.disabled    = disabled;
      this.klass       = klass;
      this.label_class = label_class;
      this.input_class = input_class;

      if (!this.label || this.label == '' || this.label == undefined) {
        this.label = toCapital(this.name);
      }

   }
}

class CharField extends FormField {
 type = 'text'
}

class PasswordField extends FormField {
 type = 'password'
}
class TextField extends FormField {
 type = 'text'
}

class IntegerField extends FormField {
 type = 'text'
}

class FloatField extends FormField {
 type = 'text'
}

class DateField extends FormField {
  type = 'date'
}

class DateTimeField extends FormField {
  type = 'datetime'
}

class SelectField extends FormField {
  type = 'select'
}

class BooleanField extends FormField {
  type = 'checkbox'
  klass = ''
}

function isAuthenticated() {
  return !!localStorage.getItem('token')
}

function getRouter(
  local_routes   : RouteRecordRaw[],
  _loginView     : Component|null = null,
  _dashboardView : Component|null = null
) {

  if (_loginView === undefined || _loginView === null) {
    _loginView = LoginView
  }

  if (_dashboardView === undefined || _dashboardView === null) {
    _dashboardView = DashboardView
  }

  let view_routes: RouteRecordRaw[] = [
    {
      path      : '',
      name      : 'dashboard',
      component : _dashboardView,
    },
    {
      path: '/view/:app/User/list',
      name: 'list_user',
      component: UserViewList,
    },
    {
      path: '/view/:app/User',
      name: 'create_user',
      component: UserView,
    },
    {
      path: '/view/:app/User/:id(\\d+)',
      name: 'edit_user',
      component: UserView,
    },
    {
      path: '/view/:app/Group/list',
      name: 'list_group',
      component: GroupViewList,
    },
    {
      path: '/view/:app/Group',
      name: 'create_group',
      component: GroupView,
    },
    {
      path: '/view/:app/Group/:id(\\d+)',
      name: 'edit_group',
      component: GroupView,
    },
    {
      path      : ':app/:view',
      name      : 'create',
      component : GenericModelView,
    },
    {
      path      : ':app/:view/:id(\\d+)',
      name      : 'edit',
      component : GenericModelView,
    },
    {
      path      : ':app/:view/list',
      name      : 'list',
      component : GenericList,
    }
  ];

  let final_routes = view_routes.concat(local_routes);

  let base_route: RouteRecordRaw[] = [
    {
      path: '/',
      redirect: () => (isAuthenticated() ? '/view' : '/login')
    },
    {
      path: '/:pathMatch(.*)*',
      redirect: '/'
    },
    {
      path: '/login',
      name: 'login',
      component: _loginView,
    },
    {
      path: '/view',
      component: SystemView,
      children: final_routes
    }
  ]

  const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: base_route
  });

  router.beforeEach((to, from, next) => {
    if (to.name !== 'login' && !isAuthenticated()) {
      return next('/login')
    }

    next()

  })

  return router;

}

function logout() {
  localStorage.removeItem('token');
  window.location.href = '';
}

class VerifyPromise<T> extends Promise<T> {
  private onThenCalled = false;

  then<TResult1 = T, TResult2 = never>(
    onfulfilled?: ((value: T) => TResult1 | PromiseLike<TResult1>) | null,
    onrejected?: ((reason: any) => TResult2 | PromiseLike<TResult2>) | null
  ): Promise<TResult1 | TResult2> {
    this.onThenCalled = true;
    return super.then(onfulfilled, onrejected);
  }

  get consumed() {
    return this.onThenCalled;
  }
}

async function HttpRequest(method:string,uri:string,payload:any) {
  const url    = window.END_POINT+"/"+uri
  const _token = localStorage.getItem('token');

  let _opts: RequestInit = {
    method  : method,
    headers : {
      "Content-Type":"application/json",
      "Authorization":"Bearer "+_token
    }
  }

  if (payload !== undefined && payload !== null) {
    _opts['body']                    = JSON.stringify(payload);
  }

  const _fetch = await fetch(url,_opts);

  if (_fetch.status == 401) {
    logout();
  }

  return _fetch

}

async function getModelData(app:string,model:string,values:any,filters:any) {

  let params = {
    app       : app,
    model     : model,
    values    : values,
    filters   : filters
  };

  return HttpRequest('POST','method/base/getModelData',params);

}

async function addModel(app:string,model:string,data:any) {

  let params = {
    "app"   : app,
    "model" : model,
    "data"  : data
  };

  return HttpRequest('POST','method/base/addModel',params);

}

async function removeModel(app:string,model:string,id:number) {

  let params = {
    "app"   : app,
    "model" : model,
    "id"    : id
  };

  return HttpRequest('POST','method/base/removeModel',params);
}

const getFullURI = (app:string,view:string,id:number|null) => {

  let full_uri = app+"/"+view;

  if (id) {
    full_uri += "/"+id;
  }

  return full_uri;

};

async function getForm(app:string,view:string,id:number|null) {

  let full_uri = getFullURI(app,view,id);

  const response = await HttpRequest("GET",full_uri,null);
  const data     = await response.json()

  if (response.status == 200) {
    return data;
  }

}
const ValidateData = (items:any) => {

   let valid = true;

   Object.keys(items).forEach((key) => {
     let item = items[key];
     if (item.required && !item.value) {
       item.error = "Es requerido capturar este campo."
       valid = false;
     }
   });

   return valid;

};
const getFormData = (items:Record<string, any>) => {
  let final_data:Record<string, any> = {};
  Object.keys(items).forEach((key) => {
    let item = items[key];

    if (item.type !== 'checkbox') {
      final_data[item.name] = item.value;
    }
    else {
      final_data[item.name] = item.value ? item.value:false;
    }

  });

  return final_data;
};
function openModal(component:any,params:any = {}) {

  last_component.value = markRaw(component);
  last_component_params.value = params;

  nextTick(() => {
    const last = document.getElementById('frame_modal');
    if (last) {
      const myModal = Modal.getOrCreateInstance(last);
      myModal.show();
    }
  });
}

const RemoveModal = () => {
  const modalElement = document.getElementById("frame_modal");

  if (modalElement) {
    const myModal = Modal.getInstance(modalElement);
    if (myModal) {
      myModal.hide();
      setTimeout(function() {
          myModal.dispose();
          last_component.value = null;
          last_component_params.value = null;
          document.querySelectorAll('.modal-backdrop').forEach(el => el.remove());
        },200);
    }
  }
}
const DefaultBtnSave = (type:string,app:string,view:string,items:any,id?:number|null): VerifyPromise<any> | void => {

  let is_valid = ValidateData(items.value);
  let data     = getFormData(items.value);
  let full_uri = getFullURI(app,view,id ? id:null);

  if (!is_valid) return;

  const promise = new VerifyPromise<any>((resolve, reject) => {
    HttpRequest("POST",full_uri,data)
      .then((data_json) => data_json.json())
      .then((data) => {
        Swal.fire('Operación realizada con éxito', "", "success");
        setTimeout(function() {

          if (!promise.consumed) {
            let base_url = '/view/'+getFullURI(app,view,null);

            if (type === 'SAVE_EDIT' && (data.id == null || data.id == undefined)) {
              type = 'SAVE_LIST';
            }

            if (type === 'SAVE_ANOTHER') {
              window.location.href = base_url;
            }
            else if (type === 'SAVE_EDIT') {
              window.location.href = base_url+"/"+data.id;
            }
            else if (type == 'SAVE_LIST') {
              window.location.href = base_url+"/list";
            }
          }

          resolve(data);

        },800);
      }).catch(reject);
    });

  return promise;

};

const DefaultBtnDelete = (app:string,view:string,id:number,title?:string|null): Promise<{ app: string; view: string; id: number; msg: string }> => {

  return new Promise((resolve, reject) => {
    let final_title = title ?? "¿Realmente desea eliminar este elemento?";

    Swal.fire({
      title: final_title,
      showDenyButton: true,
      confirmButtonText: "Si",
      denyButtonText: `No`
    }).then((result) => {

      if (result.isConfirmed) {
        removeModel(app, view, id).then((ev) => ev.json()).then((data) => {
          Swal.fire(data.msg, "", "success");

          const event = new CustomEvent("RemoveModel", {
            detail: {
              app: app,
              view: view,
              id: id
            },
          });

          document.dispatchEvent(event);

          resolve({ app, view, id, msg: data.msg });

        }).catch(reject);
      }
    });
  });
}

const FormatMoney = new Intl.NumberFormat('es-MX', {
  style: 'currency',
  currency: 'MXN',
});

export {
   toCapital,
   FormField,
   CharField,
   IntegerField,
   FloatField,
   PasswordField,
   TextField,
   DateField,
   DateTimeField,
   SelectField,
   BooleanField,
   getRouter,
   getModelData,
   addModel,
   removeModel,
   HttpRequest,
   getFullURI,
   getForm,
   ValidateData,
   getFormData,
   openModal,
   RemoveModal,
   DefaultBtnSave,
   DefaultBtnDelete,
   FormatMoney,
   last_component,
   last_component_params
}
