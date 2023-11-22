<template>
    <div>
        <h3>수정하기</h3>
        <form @submit.prevent="update">
            <label for="title">제목 : </label>
            <input type="text" id="title" v-model="title">
            <label for="content">내용 : </label>
            <input type="text" id="content" v-model="content">
            <input type="submit" value="수정하기">
        </form>
    </div>
</template>

<script setup>
// 수정하기 -> 원래 데이터 조회, 수정하기 누르면 put요청 보내는거

import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/article'


const store = useArticleStore()

const route = useRoute()
const router = useRouter()
const title = ref('')
const content = ref('')

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/articles/${route.params.id}/`,
        headers: {
            Authorization: `Token ${store.token}`
        }

    })
        .then((res) => {
            console.log(res)
            title.value = res.data.title
            content.value = res.data.content
        })
})

const update = function () {
    axios({
        method: 'put',
        url: `${store.API_URL}/articles/${route.params.id}/`,
        data: {
            title: title.value,
            content: content.value,
        }
    })
        .then((res) => {
            console.log(res.data)
            router.push({ name: 'ArticleDetail', params: { id: route.params.id} })

        })
}

</script>

<style scoped>

</style>