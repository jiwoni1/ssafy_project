<template>
    <div class="user">
        <h1><strong style="color: rgb(102, 175, 102);">{{ articleStore.userData.nickname }}</strong> 님의 회원정보</h1>
        <div class="row user-info">

            <div class="col-md-3 name" id="search">
                <p>회원번호</p>
                <hr>
                <!-- <br> -->
                <p>ID</p>
                <hr>
                <!-- <br> -->
                <!-- <p>이메일</p>
                <hr> -->
                <!-- <br> -->
                <p>닉네임</p>
                <hr>
                <!-- <br> -->
                <p>나이</p>
                <hr>
                <!-- <br> -->
                <p>재산</p>
                <hr>
                <!-- <br> -->
                <p>연봉</p>
            </div>
            <div class="col-md-9 value" id="search">
                <!-- <p>{{ articleStore.userData }}</p> -->
                <p>{{ articleStore.userData.id }}</p>
                <hr>
                <!-- <br> -->
                <p>{{ articleStore.userData.username }}</p>
                <hr>
                <!-- <br> -->
                <!-- <div class="row email">
                    <p class="col-md-10" v-if="articleStore.userData.emai">{{ articleStore.userData.email }}</p>
                    <p class="col-md-10" v-else>이메일 없음</p>
                </div> -->
                <!-- <hr> -->
                <!-- <br> -->
                <div class="row nickname">
                    <p class="col-md-10">{{ articleStore.userData.nickname }}</p>
                </div>
                <hr>
                <!-- <br> -->
                <div class="row age">
                    <p class="col-md-10">{{ articleStore.userData.age }}</p>
                </div>
                <hr>
                <!-- <br> -->
                <div class="row money">
                    <p class="col-md-10">{{ articleStore.userData.money }} 원</p>
                </div>
                <hr>
                <!-- <br> -->
                <div class="row salary">
                    <p class="col-md-10">{{ articleStore.userData.salary }} 원</p>
                </div>
            </div>
        </div>
        <div class="update-button">
            <div class="col-md-2 btn btn-success" @click="proUpdate">수정</div>
        </div>
    </div>
</template>

<script setup>
import { useArticleStore } from '@/stores/article'
import { useRouter } from 'vue-router'

const articleStore = useArticleStore()
const router = useRouter()

const proUpdate = function () {
    router.push({ name: 'ProfileUpdate' })
}

</script>

<style scoped>
.user-info {
    width: 1000px;
    margin: 50px 0;
    border: 1px solid lightgrey;
    padding: 50px 30px;
}
.user {
    /* padding: 40px 30px; */
    padding-right: 40px;
}
.name {
    width: 100px;
    margin-right: 50px;
    font-weight: bold;
}

h1 {
    color: rgb(125, 193, 125);
}
.email, .nickname, .age, .salary, .money {
    width: 679.907px;
    height: 24px;
    padding-bottom: 10px;
}

.btn {
    margin-left: 770px;
}


</style>