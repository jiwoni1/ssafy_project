<template>
        <div>
            <!-- 댓글 작성자 -->
                <p>{{ comment.user.nickname }}</p>
                <p v-if="!commentEditMode">{{ comment.content }}</p>
                <!-- <input v-else type="text" v-model="content"> -->
                <textarea v-else id="textarea" v-model="content"></textarea>
                <p>{{ comment.updated_at.slice(0,10) }}. {{ comment.updated_at.slice(11,19) }}</p>
                <!-- <button v-if="comment.user.id === store.userData.id && !commentEditMode" @click="updateFormComment">수정</button> -->
                <!-- <button v-if="comment.user.id === store.userData.id && commentEditMode" @click="updateComment(comment.id)">등록</button> -->
                <!-- <button v-if="comment.user.id === store.userData.id" @click="deleteComment(comment.id)">삭제</button> -->
                <img class="pen" v-if="comment.user.id === store.userData.id && !commentEditMode" @click="updateFormComment" src="../../public/pen.png" alt="">
                <img class="pen" v-if="comment.user.id === store.userData.id && commentEditMode" @click="updateComment(comment.id)" src="../../public/pen.png" alt="">
                <img class="close" v-if="comment.user.id === store.userData.id" @click="deleteComment(comment.id)" src="../../public/close.png" alt="">

                <hr>
                <!-- <p v-if="comment.user !== store.userData.id">{{ commentEditMode }}</p>
                <p>{{ comment.user.id }} - {{  store.userData.id }}</p> -->
        </div>
</template>

<script setup>
import axios from 'axios'
import { ref, watch, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/article'


const router = useRouter()
const store = useArticleStore()

const content = ref('')
const commentEditMode = ref(false)


const props = defineProps({
    comment: Object,
})


// 댓글 수정
const updateFormComment = function () {
        commentEditMode.value = !commentEditMode.value
        content.value = props.comment.content
}

const emit = defineEmits()

// 댓글 수정 등록
const updateComment = function (commentId) {
    axios({
        method: 'put',
        url: `${store.API_URL}/articles/comments/${commentId}/`,
        data: {
            content: content.value,
        },
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
        .then((res) => {
            console.log('댓글 수정 완료')

            commentEditMode.value = !commentEditMode.value
            emit('updateComment')

        })
}


watch(() => props.comment, () => {
  content.value = props.comment.content
})

// 댓글 삭제
const deleteComment = function (commentId) {
    axios ({
        method: 'delete',
        url: `${store.API_URL}/articles/comments/${commentId}/`,
        headers: {
                Authorization: `Token ${store.token}`
            }
    })
        .then((res) => {
            console.log('게시글 삭제 완료')
            emit('deleteComment')

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
.pen, .close {
    width: 25px;
    padding-right: 10px;
}

</style>