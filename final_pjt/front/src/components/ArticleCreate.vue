<template>
    <div>
        <h1>게시글 생성 페이지</h1>
        <form @submit.prevent="createArticle">
            <label for="title">제목 : </label>
            <input type="text" id="title" v-model="title">
            <label for="content">내용 : </label>
            <input type="text" id="content" v-model="content">
            <input type="submit" value="create">
        </form>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/article'

const router = useRouter()
const store = useArticleStore()

const title = ref(null)
const content = ref(null)

const createArticle = function () {
    axios({
        method: 'post',
        url: `${store.API_URL}/articles/`,
        data: {
            title: title.value,
            content: content.value,
        },
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
        .then((res) => {
            console.log(res)
            router.push({ name: "ArticleList" })
        })
}

</script>

<style scoped>

</style>