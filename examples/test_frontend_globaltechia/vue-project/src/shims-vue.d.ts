declare module '*.vue' {
  import { DefineComponent } from 'vue';
  const component: DefineComponent<{}, {}, any>;
  export default component;
}

declare global {
  interface Window {
    PROJECT_NAME  : string;
    PROJECT_TITLE : string;
    END_POINT     : string;
  }
}

export {};