<template>
    <div>
            <h1>{{ articleStore.userData.username }}님의 프로필 페이지</h1>
            <div>회원번호</div>
            <div>ID</div>
            <div>EMAIL</div>
            <div>NICKNAME</div>
            <div>나이</div>
            <div>현재 가진 금액</div>
            <div>연봉</div>
   
    </div>
</template>

<script setup>
import { useArticleStore } from '@/stores/article'

const articleStore = useArticleStore()

</script>

<style scoped>

</style>