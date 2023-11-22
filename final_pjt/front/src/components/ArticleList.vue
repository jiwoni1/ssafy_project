<template>
    <div>
        <div>
            <RouterLink :to="{ name: 'Community' }">커뮤니티</RouterLink>
            <button @click="createArticle">게시글 생성</button>
        </div>
        <div v-if="store.articles.length !== 0"
        v-for="article in store.articles"
        :key="article.id">
            <ArticlePreview :articleId="article.id"/>
        </div>
        <div v-else>
            <p>게시글이 없습니다.</p>
        </div>

    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter, RouterLink } from 'vue-router'
import { useArticleStore } from '@/stores/article'
import ArticlePreview from '@/components/ArticlePreview.vue'

const store = useArticleStore()
const router = useRouter()

onMounted(() => {
    store.getArticles()
})

const createArticle = function () {
  router.push({ name: 'articleCreate' })
}



</script>

<style scoped>

</style>