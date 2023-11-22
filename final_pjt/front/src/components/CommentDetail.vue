<template>
        <div>
            <!-- 댓글 작성자 -->
                <p>{{ comment.user }}</p>
                <p v-if="!commentEditMode">{{ comment.content }}</p>
                <input v-else type="text" v-model="content">
                <p>{{ comment.updated_at.slice(0,10) }}. {{ comment.updated_at.slice(11,19) }}</p>
                <button v-if="comment.user === store.userData.id && !commentEditMode" @click="updateFormComment">수정</button>
                <button v-if="comment.user === store.userData.id && commentEditMode" @click="updateComment(comment.id)">등록</button>
                <button v-if="comment.user === store.userData.id" @click="deleteComment(comment.id)">삭제</button>
                <hr>

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

</style>