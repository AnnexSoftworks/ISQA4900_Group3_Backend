<template>

    <TheHeader v-if="!isLoginPage" class="header"></TheHeader>
    <router-view class="content"/>
</template>

<script>
import TheHeader from "@/components/layout/Header.vue";
import {mapState} from "vuex";

export default {
    name: "App",
    components: {
        TheHeader,
    },
    created() {
      this.$store.dispatch('auth/autoLogin');
    },
    computed: {
      ...mapState('route', ['name']),
      isLoginPage() {
        return this.name === 'Login' || this.name === 'EmailConfirmation';
      }
    }
}

</script>