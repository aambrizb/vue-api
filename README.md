# vue-api-fastapi

| Key    | Description                    |
|--------|--------------------------------|
| Author | Jesús Alejandro Ambríz Bedolla |
| Rev    | Sep/2025                       |

# Summary

This project is created with the objective that combine vue + fastapi.
It is a integral project in where the components known what should do and how should communicate between them

# @globaltechia/utils.js
## Overview

| Util         |
|--------------|
| getRouter    |
| toCapital    |
| HttpRequest  |
| getModalData |
| addModel     |
| removeModel  |
| getFullURI   |
| getForm      |
| openModal    |

## getRouter
### Parameters

| Parameters     | Type          | Description                  |
|----------------|---------------|------------------------------|
| local_routes   | array         | Send local routes for router |
| login_view     | vue component | Indicate LoginView.vue       |
| dashboard_view | vue component | Indicate DashboardView.vue   |


### Example
````js
const router = getRouter(local_routes,LocalLoginView,LocalDashboarView);
console.log(router);
````

## toCapital
### Parameters

| Parameters | Type   | Description                                                                  |
|------------|--------|------------------------------------------------------------------------------|
| value      | string | Value to generate like Capital letter |


### Example
````js

let name = "jesus alejandro"
let _value = toCapital(name);
console.log(_value);

````

## HttpRequest
### Parameters

| Parameters | Type   | Description                             |
|------------|--------|-----------------------------------------|
| method     | string | GET - POST  Describe the request method |
| uri        | string | /method/base/method                     |
| payload    | dict   | It Send payload request                 |

### Example

```js

const handle = () => {
  
  let params = {
    param1:"value1",
    param2:"value2",
  }

  HttpRequest('POST','method/base/getMethod',params).then((ev) => ev.json()).then((data) => {
    console.log(data);
  })
}

```

## getModalData
### Parameters

| Parameters    | Type      | Description                                                                  |
|---------------|-----------|------------------------------------------------------------------------------|
| app           | string    |  |
| model         | string    |  |
| values        | array     |  |
| filters | dict |  |


### Example

````python models.py
class yourModel(utils.FrameModel):
  field_1       = utils.CharField(max_length=120)
  field_2       = utils.CharField(max_length=120,null=True)
  active        = utils.BooleanField()

````

````js
  let _data = {
    field_1:"value 1",
    field_2:"value 2"
  }
    
    getModelData("base","yourModel",_data).then((ev) => ev.json()).then((data) => {
      console.log(data);
    });
````

## addModel
### Parameters

| Parameters | Type    | Description |
|------------|---------|-------------|
| app        | string  | App name    |
| model      | string  | Model name  |
| data       | dict    | Payload     |


### Example

````python models.py
class yourModel(utils.FrameModel):
  field_1       = utils.CharField(max_length=120)
  field_2       = utils.CharField(max_length=120,null=True)

````

````js
    const handleMethod = () => {
       let _values = {
          field_1:"value 1",
          field_2:"value 2"
        };
    
        addModel("base","yourModel",_values).then((ev) => ev.json()).then((data) => {
          console.log(data);
        });
   }
   
````

## removeModel
### Parameters

| Parameters | Type   | Description     |
|------------|--------|-----------------|
| app        | string | App name        |
| model      | string | Model name      |
| id         | number | PK ForeignKey   |


### Example

````python models.py
class yourModel(utils.FrameModel):
  field_1       = utils.CharField(max_length=120)
  field_2       = utils.CharField(max_length=120,null=True)

````

````js
    const handleMethod = () => {
    
        removeModel("base","yourModel","1").then((ev) => ev.json()).then((data) => {
          console.log(data);
        });
   }
   
````

## getFullURI
### Parameters

| Parameters | Type   | Description     |
|------------|--------|-----------------|
| app        | string | App name        |
| model      | string | Model name      |
| id         | number | PK ForeignKey   |


### Example

````js
    console.log(getFullURI("base","yourModel",1));
````

## getForm
### Parameters

| Parameters | Type   | Description   |
|------------|--------|---------------|
| app        | string | App name      |
| view       | string | View Name     |
| id         | number | PK ForeignKey |


### Example

````js
    console.log(getForm("base","yourModel",1));
````

### FormField Field

| Type          | Extends    |
|---------------|------------|
| CharField     | FormField  |
| PasswordField | FormField  |
| TextField     | FormField  |
| TextField     | FormField  |
| DateField     | FormField  |
| DateTimeField | FormField  |
| SelectField   | FormField  |
| BooleanField   | FormField  |

```js
const form = ref({});
form.value['password']         = new PasswordField({required:false,name:"password",label:"Contraseña",label_class:"col-lg-4 col-md-4 col-xs-12",input_class:'col-lg-6 col-md-6 col-xs-12'});
form.value['confirm_password'] = new PasswordField({required:false,name:"confirm_password",label_class:"col-lg-4 col-md-4 col-xs-12",input_class:'col-lg-6 col-md-6 col-xs-12'});
```
### FormField Properties

| Type        | Extends                                 |
|-------------|-----------------------------------------|
| type        | Indicate input type (text,password etc) |
| label       | Indicate label input                    |
| help_text   | Indicate some text for help text        |
| required    | Indicate if the field is required       |
| error       | Add some message when there are errors  |
| value       | Indicate value's field                  |
| disabled    | Indicate if the field is disabled       |
| klass       | Indicate 'class' for input              |
| label_class | Indicate class for label col            |
| input_class | Indicate class for input col            |


## openModal
### Parameters

| Parameters     | Type    | Description                       |
|----------------|---------|-----------------------------------|
| last_component | any     | Variable to assign last component |
| component      | string  | Vue Component                     |
| params         | number  | data modal's parameters           |


### Example

````vue
ModalComponent.vue
````

````js
  const last_component = ref(null);
  
  openModal(last_component,ModalComponent,{pk:2,name:"Alex"});
````

# Install

| Command                      | Description                        |
|------------------------------|------------------------------------|
| npm run dev                  | Run developer mode                 |
| npm run build                | Generate build                     |
| npx serve dist -s            | Run SinglePage                     |
| npm install | Install package.json |





