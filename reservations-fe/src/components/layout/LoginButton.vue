<template>
    <div class="login-btn">
        <button @click="toggleLogin">Login</button>
    </div>
</template>

<script>
import {mapActions} from "vuex";

export default {
    name: "LoginButton",
    methods: {
      toggleLogin() {
        this.$router.push({name: "Login"});
      },
    }
}
</script>

<style scoped>
.login-btn button {
    padding: 7px 30px;
    border: #dcb324 1px solid;
    text-transform: uppercase;
    background-color: #d78f00;
    color: #1c212d;
    font-size: 14px;
    cursor: pointer;
    font-weight: 500;
}

.login-btn button:hover {
    background-color: #ffffff;
    border: #d78f00 1px solid;
}
</style>