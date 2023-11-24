<template>
    <div class="detail-template">
        <div v-if="article">
            <div>
                <div class="buttons">
                    <span class="go_articlelist">
                        <button @click="goArticleList">목록</button>
                    </span>
                    <!-- 여기를 띄우기 양끝으로 -->
                    <span class="update_delete">
                        <button v-if="article.user.id === store.userData.id"  @click="goUpdate">수정</button>
                        <button v-if="article.user.id === store.userData.id" @click="deleteArticle">삭제</button>
                    </span>
                </div>
                <br>
                <br>  
                <div class="article_article">
                    <h2 class="gray">{{ article.title }}</h2>
                    <hr>
                    <!-- 양쪽으로 띄어놓기 -->
                    <div class="user_date">
                        <p>작성자 | {{ article.user.nickname }}</p>
                        <p>작성일 | {{ article.updated_at.slice(0,10) }}. {{ article.updated_at.slice(11,19) }}</p>
                    </div>
        
                    <hr>
                    <div class="gray article_content">
                        {{ article.content }}
                    </div>
                    <!-- <p>생성 시간 : {{ article.created_at.slice(0,10) }}. {{ article.created_at.slice(11,19) }}</p>
                    <p>수정 시간 : {{ article.updated_at.slice(0,10) }}. {{ article.updated_at.slice(11,19) }}</p> -->
                    <!-- <p>생성 시간 : {{ article.created_at }}</p>
                    <p>수정 시간 : {{ article.updated_at }}</p> -->
                    <hr>
                    
                </div>
            </div>
        
            <div>
                <h5 class="gray">댓글 ({{ article.comment_count }})</h5>
                <hr>
                <!-- <input type="text" placeholder="댓글을 입력해 주세요." v-model="content"> -->
                <div class="comment_input">
                    <textarea class="form-control" placeholder="댓글을 입력해 주세요." id="textarea" rows="3" v-model="content"></textarea>
                    <!-- <a href="#" @click="createComment">등록</a> -->
                </div>
                <div>
                    <button id="register" class="btn btn-outline-success"  @click="createComment">등록</button>
                </div>
            </div>
            <div class="gray comment-list">
                <CommentDetail v-if="article.comment_count !== 0"
                v-for="comment in article.comment_set"
                :key="comment.id"
                :comment="comment"
                @update-comment="updateComment"
                @delete-comment="deleteComment" />
    
                <div v-if="article.comment_count === 0">
                    댓글이 없습니다.
                </div>
            </div>
        </div>
        <div v-else>
            <p>게시글 로딩중</p>
        </div>
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
        router.push({ name: 'Community' })
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
                router.push({name:'Community'})
                
            })
    }
    
    
    </script>
    
    
    <style scoped>
    #textarea {
        margin-bottom: 2%
    }
    
    #register {
        color : rgb(102, 175, 102);
        float :right;
    }
    .user_date {
        color: gray;
    }
    .article_article {
        margin-top: 40px;
        padding-bottom: 100px;
    }
    .article_content {
        margin: 2% 1% 10%;
    }
    
    .buttons {
        float :right;
    }
    .buttons button {
        border: 1px solid rgb(102, 175, 102);
        border-radius: 8%;
        width: 100px;
        margin: 0px 10px;
        background-color: rgb(255, 255, 255);
        color : rgb(102, 175, 102);
    }
    
    
    .detail-template {
        padding: 3% 20%;
    }
    
    hr {
        color : rgb(102, 175, 102);
    }
    
    .comment-list {
        margin-top: 70px;
    }
    
    .gray {
        color:rgb(96, 95, 95)
    }
    </style>