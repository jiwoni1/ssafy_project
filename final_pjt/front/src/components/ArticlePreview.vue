<template>
    <div v-if="article" class="article">
        <!-- <p>{{ article }}</p> -->
        <h5 @click="goDetail(article.id)">{{ article.title }} ({{ article.comment_count }})</h5>
        <br>
        <div class="user-comment">
            <img src="../../public/profile.png" alt="" class="profile">
            <span class="nickname">{{ article.user.nickname }}</span>
        </div>
        <div>
            <div class="date">등록일 {{ article.updated_at.slice(0,10) }} {{ article.updated_at.slice(11,16) }}</div>
            <hr>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useArticleStore } from '@/stores/article'
import { useRouter, RouterLink } from 'vue-router'

const router = useRouter()

const props = defineProps({
    articleId: Number,
})

const article = ref(null)
const store = useArticleStore()


onMounted(() => {
    getArticle()
})

const getArticle = function () {
    axios({
    method: 'get',
    url: `${store.API_URL}/articles/${props.articleId}/`
})
    .then((res) => {
        console.log(res)
        article.value = res.data
    })
}

const goDetail = function (articleId) {
    router.push({ name: 'ArticleDetail', params: { id: articleId }})
}

const createArticle = function () {
  router.push({ name: 'articleCreate' })
}
</script>

<style scoped>
.profile {
    width: 15px;
    height: 15px;
    margin-left: 5px;
    margin-right: 10px;
}

.date {
    margin: 10px 0px;
}

.article {
    color: rgb(104, 104, 104);
}

</style>