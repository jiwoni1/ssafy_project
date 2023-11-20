<template>
    <div>
        <RouterLink :to="{ name: 'deposit' }">정기예금</RouterLink>  |
        <RouterLink :to="{ name: 'saving' }">정기적금</RouterLink>
    </div>
    <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>

</style>