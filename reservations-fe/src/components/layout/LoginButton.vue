<template>
  <div>
    <div class="login-btn" v-if="!authenticated" @click="register">
      <button @click="login">Login</button>
    </div>
    <div class="logout-btn" v-else @click="logout">
      <button>Logout</button>
    </div>
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
  }),
  mounted() {
    if (localStorage.getItem("isAuthenticated") &&
        JSON.parse(localStorage.getItem("isAuthenticated")) === true) {
      this.authenticated = true;
    } else {
      this.authenticated = false;
    }
  },
  methods: {
    logout() {
      localStorage.clear();
      localStorage.setItem("isAuthenticated", false);
      this.authenticated = false;
      window.location = "/";
    },
    login() {
      router.push("/auth");
    },
    register() {
      router.push("/register");
    }
  }
}
</script>

<style scoped>
.login-btn button, .logout-btn button {
  padding: 7px 30px;
  border: #dcb324 1px solid;
  text-transform: uppercase;
  background-color: #d78f00;
  color: #1c212d;
  font-size: 14px;
  cursor: pointer;
  font-weight: 500;
}

.login-btn button:hover, .logout-btn button:hover {
  background-color: #ffffff;
  border: #d78f00 1px solid;
}
</style>
