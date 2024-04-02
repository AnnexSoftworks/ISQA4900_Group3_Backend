import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import "./assets/css/font-awesome.min.css"
import "./assets/css/ionicons.min.css"
import "./assets/css/owl.theme.default.min.css"
import "./assets/css/gallery.css"
import "./assets/css/vit-gallery.css"
import "./assets/css/bootstrap-select.min.css"
import "./assets/sass/styles.scss"
import BaseDialog from "@/components/ui/BaseDialog.vue";

// import the fontawesome icons
import { library } from "@fortawesome/fontawesome-svg-core";
import { faTrash, faPencil, faPlus } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
library.add(faTrash, faPencil, faPlus);
createApp(App).use(store, axios).use(router).component("font-awesome-icon",
FontAwesomeIcon).component('base-dialog', BaseDialog).mount('#app')