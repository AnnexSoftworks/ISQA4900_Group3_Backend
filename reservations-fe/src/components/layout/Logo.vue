<template>
    <router-link to="/" class="logo-area">
        <img src="../../assets/images/logo-icon.webp" alt="logo" class="logo">
        <div class="logo-text">
            <span class="bold-text">Emerald Bay </span>
            <span class="light-text"> Island Resort</span>
        </div>
    </router-link>
</template>

<script>
export default {}
</script>

<style scoped>
.logo {
    height: 5rem;
}

.logo-area {
    display: flex;
    align-items: center;
    gap: 10px;
    color: white;
}

.logo-text {
  font-size: 1.85rem;
  letter-spacing: 0.065rem;
}

.bold-text {
    font-weight: 700;
}
</style>