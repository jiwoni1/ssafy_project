<template>
    <div v-if="article">
        <!-- <p>{{ article }}</p> -->
        <h5>{{ article.title }}({{ article.comment_count }})</h5>
        <br>
        <p>{{ article.user.nickname }}</p>
        <div>
            <p>등록일 {{ article.updated_at.slice(0,10) }} {{ article.updated_at.slice(11,16) }}</p>
            <RouterLink :to="{ name: 'ArticleDetail', params: { id: article.id }}">Detail</RouterLink>
            <hr>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useArticleStore } from '@/stores/article'
import { RouterLink } from 'vue-router'


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

</script>

<style scoped>

</style>