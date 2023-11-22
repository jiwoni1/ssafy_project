<template>
    <div>
        <h3>{{ article.id }}번 글의 상세 페이지</h3>
        <!-- 작성자 수정 -->
        <p>작성자 : {{ article.user }}</p>
        <p>제목 : {{ article.title }}</p>
        <p>내용 : {{ article.content }}</p>
        <p>생성 시간 : {{ article.created_at }}</p>
        <p>수정 시간 : {{ article.updated_at }}</p>

        <button v-if="article.user === store.userData.id"  @click="goUpdate">수정</button>
        <button v-if="article.user === store.userData.id" @click="deleteArticle">삭제</button>
    </div>

    <div>
        <h4>댓글 {{ article.comment_count }}</h4>
        <input type="text" placeholder="댓글을 입력해주세요." v-model="content">
        <button @click="createComment">등록</button>

        <div>
            <h5>댓글 목록</h5>
            <CommentDetail v-if="article.comment_count !== 0"
            v-for="comment in article.comment_set"
            :key="comment.id"
            :comment="comment"
            @update-comment="updateComment"
            @delete-comment="deleteComment" />

            <div v-if="article.comment_count === 0">
                <p>댓글이 없습니다.</p>
            </div>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/article'
import CommentDetail from '@/components/CommentDetail.vue'

const article = ref({})
const route = useRoute()
const router = useRouter()
const store = useArticleStore()

const content = ref(null)
const commentEditMode = ref(false)

onMounted(() => {
    getArticle()
})

const getArticle = function () {
    axios({
    method: 'get',
    url: `${store.API_URL}/articles/${route.params.id}/`
})
    .then((res) => {
        console.log(res)
        article.value = res.data
    })
}

const goUpdate = function () {
    router.push({ name: 'ArticleUpdate', params: { id: article.id } })
}

// 댓글 생성
const createComment = function () {
    axios({
        method: 'post',
        url:`${store.API_URL}/articles/${route.params.id}/comments/`,
        data: {
            content: content.value,
        },
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
        .then((res) => {
            console.log(res)
            getArticle()
            content.value = ''


    })
}

// 댓글 수정 등록
const updateComment = function () {
    getArticle()
    console.log('수정 완료')
}

// 댓글 삭제
const deleteComment = function () {
    getArticle()
    console.log('삭제 완료')
}


// 게시글 삭제
const deleteArticle = function () {
    axios ({
        method: 'delete',
        url: `${store.API_URL}/articles/${route.params.id}/`,
        headers: {
                Authorization: `Token ${store.token}`
            }
    })
        .then((res) => {
            console.log('게시글 삭제 완료')
            // 본인페이지로 router.push는 reload가 안돼
            store.getArticles()
            router.push({name:'ArticleList'})
            
        })
}


</script>


<style scoped>

</style>