<template>
    <div>
        <h1>커뮤니티</h1>
        <br>
        <div>
            <h2 @click="goArticleList">게시판</h2>
            <hr>
            <!-- 게시글 한 3개정도만 나오게 -->
            <div v-if="store.articles"
            v-for="num in store.articles.length"
            :key="num"
            :article="num">
                <ArticlePreview :articleId="num"/>
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
// import ArticleList from '@/components/ArticleList.vue'
import ArticlePreview from '@/components/ArticlePreview.vue'

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