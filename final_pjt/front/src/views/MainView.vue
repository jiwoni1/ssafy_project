<template>
    <div>
        <h1>메인</h1>
        <button @click.prevent="LogOut">로그아웃</button>
    </div>
</template>

<script setup>
import { useBankStore } from '../stores/bank'
const store = useBankStore()


const LogOut = function () {
    store.logOut()
}

</script>

<style scoped>

</style>