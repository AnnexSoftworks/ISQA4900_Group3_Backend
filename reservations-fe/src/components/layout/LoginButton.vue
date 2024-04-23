<template>
  <div class="login-btn" v-if="!authenticated" @click="register">
    <button @click="login">Login</button>
  </div>
</template>

<script>
import router from '../../router';
import {APIService} from '@/http/ApIService';
const apiService = new APIService();
export default {
  name: "LoginButton",
  data: () => ({
    authenticated: false,
    dialog: false,
    menu: [
      {title: 'Home', url: "/"},
      {title: 'Guests', url: "/guest-list"},
    ]
  }),
  mounted() {
    if (localStorage.getItem("isAuthenticated") &&
        JSON.parse(localStorage.getItem("isAuthenticated")) === true) {
      this.authenticated = true
    } else {
      this.authenticated = false
    }
    if (this.authenticated === true) {
      apiService.getGuestList().then(response => {
        this.authenticated = true;
      }).catch(error => {
        if (error.response.status === 401) {
          localStorage.clear();
          localStorage.setItem("isAuthenticated", false);
          this.authenticated = false;
        }
      });
    }
  },
  methods: {
    getUser() {
      if (localStorage.getItem("isAuthenticated") &&
          JSON.parse(localStorage.getItem("isAuthenticated")) === true
      ) {
        this.validUserName = JSON.parse(localStorage.getItem("log_user"));
      }
    },
    logout() {
//clear local storage items and set authenticated to false
      localStorage.clear();
      localStorage.setItem("isAuthenticated", false);
      this.authenticated = false;
      window.location = "/";
    },
    login() {
      router.push("/auth");
    },
    home() {
      window.location = "/";
    },
    register() {
      router.push("/register");
    }
  }
}
</script>

<style scoped>
.login-btn button {
  padding: 7px 30px;
  border: #d78f00 1px solid;
  text-transform: uppercase;
  background-color: #ffd234;
  color: #1c212d;
  font-size: 14px;
  cursor: pointer;
  font-weight: 500;
}

.login-btn button:hover {
  background-color: #ffffff;
  border: #ffd234 1px solid;
}
</style>