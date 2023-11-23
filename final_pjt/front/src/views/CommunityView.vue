<template>
    <div class="community-template">
        <h1 id="title">커뮤니티</h1>
        <br>
        <div>
            <div class="table">
                <h4 class="sub-title">게시판</h4>
                <button class="btn btn-success" @click="createArticle">게시글 생성</button>
            </div>
        <hr>
        <div>
            <div v-if="store.articles.length > 0">
                <div class="sample-articles">
                    <div v-for="article in store.articles" :key="article.id">
                        <ArticlePreview :articleId="article.id" class="sample-article"/>
                    </div>
                </div>
            </div>
            <div v-else>
                <p>게시글이 없습니다.</p>
            </div>
        </div>
        
    </div>
    <br>
</div>
</template>

<script setup>
import { onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/article'
// import ArticleList from '@/components/ArticleList.vue'
import ArticlePreview from '@/components/ArticlePreview.vue'

const router = useRouter()
const store = useArticleStore()


// const goArticleList = function () {
//     router.push({ name: 'ArticleList' })
// }

onMounted(() => {
    store.getArticles()
})


const createArticle = function () {
  router.push({ name: 'articleCreate' })
}
</script>

<style scoped>
.community-template {
    padding: 7% 10%;
}

#title {
    color: rgb(102, 175, 102);
    font-weight: bold;
}

#search {
    border-right: solid 1px rgb(102, 175, 102);
}

.sub-title {
    color: rgb(102, 175, 102);
}

.table {
    display: flex;
    justify-content: space-between;
}
</style>