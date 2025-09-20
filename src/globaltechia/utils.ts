import {createRouter, createWebHistory} from "vue-router";
import LoginView from "@/globaltechia/views/LoginView.vue";
import SystemView from "@/globaltechia/views/SystemView.vue";
import GenericModelView from "@/globaltechia/components/GenericModelView.vue";
import GenericList from "@/globaltechia/components/GenericList.vue";
import DashboardView from "@/globaltechia/views/DashboardView.vue";
import UserView from "@/globaltechia/views/UserView.vue";
import { Modal } from 'bootstrap';
import {markRaw, nextTick, ref} from "vue";

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

class TextAreaField extends FormField {
  type = 'textarea'
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

function getRouter(local_routes:any,_loginView:any,_dashboardView:any) {

  if (_loginView === undefined) {
    _loginView = LoginView
  }

  if (_dashboardView === undefined) {
    _dashboardView = DashboardView
  }

  let view_routes = [
    {
      path      : '',
      name      : 'dashboard',
      component : _dashboardView,
    },
    {
      path      : ':app/:view',
      name      : 'create',
      component : GenericModelView,
    },
    {
      path      : ':app/:view/:id',
      name      : 'edit',
      component : GenericModelView,
    },
    {
      path      : ':app/:view/list',
      name      : 'list',
      component : GenericList,
    },
    {
      path      : ':app/User',
      name      : 'user',
      component : UserView,
    }
  ];

  let final_routes = view_routes.concat(local_routes);

  let base_route = [
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

  let router = createRouter({
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

export {
   toCapital,
   FormField,
   CharField,
   PasswordField,
   TextField,
   TextAreaField,
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
   last_component,
   last_component_params
}
