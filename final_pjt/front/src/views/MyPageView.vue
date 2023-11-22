<template>
    <div>
        <RouterLink :to="{ name: 'Profile' }">회원 기본 정보</RouterLink>  |
        <RouterLink :to="{ name: 'addProduct' }">포트폴리오</RouterLink>
    </div>
    <RouterView />
</template>

<script setup>
import { RouterView, RouterLink} from 'vue-router'

</script>

<style scoped>

</style>