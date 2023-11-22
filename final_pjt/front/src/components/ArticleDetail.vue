<template>
    <div v-if="article">
        <div>
            <div class="button">
                <span class="go_articlelist">
                    <button @click="goArticleList">목록</button>
                </span>
                <!-- 여기를 띄우기 양끝으로 -->
                <span class="update_delete">
                    <button v-if="article.user.id === store.userData.id"  @click="goUpdate">수정</button>
                    <button v-if="article.user.id === store.userData.id" @click="deleteArticle">삭제</button>
                </span>
            </div>
            <h3>{{ article.id }}번 글의 상세 페이지</h3>
            <hr>
            <div class="article_article">
                <h4>{{ article.title }}</h4>
                <!-- 양쪽으로 띄어놓기 -->
                <div class="user_date">
                    <p>작성자 | {{ article.user.nickname }}</p>
                    <p>작성일 | {{ article.updated_at.slice(0,10) }}. {{ article.updated_at.slice(11,19) }}</p>
                </div>
    
                <hr>
                <div class="article_content">
                    <p>{{ article.content }}</p>
                </div>
                <!-- <p>생성 시간 : {{ article.created_at.slice(0,10) }}. {{ article.created_at.slice(11,19) }}</p>
                <p>수정 시간 : {{ article.updated_at.slice(0,10) }}. {{ article.updated_at.slice(11,19) }}</p> -->
                <!-- <p>생성 시간 : {{ article.created_at }}</p>
                <p>수정 시간 : {{ article.updated_at }}</p> -->
                <hr>
                
            </div>
        </div>
    
        <div>
            <h5>댓글 ({{ article.comment_count }})</h5>
            <hr>
            <!-- <input type="text" placeholder="댓글을 입력해 주세요." v-model="content"> -->
            <div class="comment_input">
                <label for="textarea"></label>
                <textarea placeholder="댓글을 입력해 주세요." id="textarea" v-model="content"></textarea>
                <!-- <a href="#" @click="createComment">등록</a> -->
                <button class="comment_register"  @click="createComment">등록</button>
            </div>
    
            <div>
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
    </div>
    <div v-else>
        <p>게시글 로딩중</p>
    </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/article'
import CommentDetail from '@/components/CommentDetail.vue'

const article = ref(null)
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

// 목록으로 가기
const goArticleList = function () {
    router.push({ name: 'ArticleList' })
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
  textarea {
    width: 90%;
    border: 1px solid gray;
    height: 6.25em;
    resize: none;
}

.comment_register {
    height: 6.25em;
    border: 1px solid gray;
}
.comment_input {
    height: 8em;
  }
.user_date {
    color: gray;
}
.article_article {
    padding-bottom: 100px;
}
.article_content {
    padding-bottom: 20px;
}

.button button {
    border: 1px solid gray;
    width: 100px;
    margin: 10px  0 15px 0;
    background-color: rgb(255, 255, 255);
}
.update_delete button {
    margin: 0 5px;
}
</style>