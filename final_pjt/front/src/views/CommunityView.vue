<template>
    <div>
        <h1>커뮤니티</h1>
        <br>
        <div>
            <h3 @click="goArticleList">게시판</h3>
            <div v-if="store.articles"
            v-for="article in store.articles"
            :key="article.id"
            :article="article">
                <span>{{ article.title }} - {{ article }}</span>
                <!-- <span>{{ store.userData.nickname }}</span> -->
    
            </div>
            <div v-else>
                <p>게시글이 없습니다.</p>
            </div>
        </div>
        <br>
        <div>
            <h3>칼럼</h3>
        </div>
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/article'
import ArticleList from '@/components/ArticleList.vue'

const router = useRouter()
const store = useArticleStore()


const goArticleList = function () {
    router.push({ name: 'ArticleList' })
}

onMounted(() => {
    store.getArticles()
})
</script>

<style scoped>

</style>