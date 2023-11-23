<template>
    <div>       
        <h1>적금 및 예금 상품 추천</h1>
       
        <p>{{ articleStore.userData.username }}님과 나이가 비슷한 사람들이 가입한 상품입니다.</p>
        <p>{{ articleStore.usersData.same_product }}</p>
    </div>
</template>

<script setup>
import { useArticleStore } from '@/stores/article'
const articleStore = useArticleStore()


</script>

<style scoped>

</style>