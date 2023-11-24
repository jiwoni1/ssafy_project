<template>
    <div class="update-template">
        <h1 id="h1">게시글 수정</h1>
        <hr>
        <form @submit.prevent="update">
            <!-- 게시글 제목 -->
            <div class="row g-3 align-items-center">
                <div class="col-auto">
                    <label for="title" class="col-form-label" id="label">제목</label>
                </div>
                <div class="col">
                    <input type="text" id="title" class="form-control" placeholder="제목을 입력하세요." v-model="title">
                </div>
            </div>
            <br>
            <!-- 게시글 내용 -->
            <div class="mb-3">
                <label for="content" class="form-label" id="label">내용</label>
                <textarea type="text" id="content" cols="30" rows="10" class="form-control" placeholder="내용을 입력하세요." v-model="content"></textarea>
            </div>
            <div>
                <input type="submit" value="수정 완료" class="btn btn-outline-success btn-lg" id="btn">
            </div>
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
.update-template {
    padding: 5% 15%;
}

#h1 {
    color: rgb(102, 175, 102);
    font-weight: bold;
}

#label {
    color: rgb(138, 193, 138);
    font-size: 20px;
}

hr {
    color: rgb(102, 175, 102);
    margin: 3% 0px;
}

#content {
    margin-top: 10px;
}

#btn {
    color : rgb(102, 175, 102);
    float :right;
}
</style>