<template>
    <div v-for="user in articleStore.userData">
        <h1>{{ user.username }}님의 프로필 페이지</h1>
        <div>회원번호</div>
        <div>ID</div>
        <div>EMAIL</div>
        <div>NICKNAME</div>
        <div>나이</div>
        <div>현재 가진 금액</div>
        <div>연봉</div>
        <button @click="articleStore.getUser(user.id)">출력</button>
    </div>
</template>

<script setup>
import { useArticleStore } from '@/stores/article'

const articleStore = useArticleStore()
</script>

<style scoped>

</style>