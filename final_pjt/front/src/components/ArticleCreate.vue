<template>
    <div class="create-template">
        <h1 id="h1">게시글 생성</h1>
        <hr>
        <form @submit.prevent="createArticle">
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
                <input type="submit" value="create" class="btn btn-outline-success btn-lg" id="btn">
            </div>
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
            router.push({ name: "Community" })
        })
}

</script>

<style scoped>
.create-template {
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