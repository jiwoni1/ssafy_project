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

                <div class="row nickname">
                    <input class="col-md-10" type="text" v-model="nickname">
                </div>
                <hr>
                <!-- <br> -->
                <div class="row age">
                    <input class="col-md-10" type="text" v-model="age">
                </div>
                <hr>
                <!-- <br> -->
                <div class="row money">
                    <input class="col-md-10" type="text" v-model="money">
                    <span class="col-md-1">만원</span>
                </div>
                <hr>
                <!-- <br> -->
                <div class="row salary">
                    <input class="col-md-10" type="text" v-model="salary">
                    <span class="col-md-1">만원</span>
                </div>
            </div>
        </div>
        <div class="update-button">
            <div class="col-md-2 btn btn-success" @click="proUpdated(articleStore.userData.username)">등록</div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useArticleStore } from '@/stores/article'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { storeToRefs } from 'pinia';

const articleStore = useArticleStore()
const router = useRouter()


const nickname = ref(articleStore.userData.nickname)
const age = ref(articleStore.userData.age)
const money = ref(articleStore.userData.money)
const salary = ref(articleStore.userData.salary)
const password = ref(articleStore.userData.password)

const proUpdated = function (username) {
    axios({
        method: 'put',
        url:`${articleStore.API_URL}/accounts/user/${username}/`,
        data: {

            nickname: nickname.value,
            age: age.value,
            salary: salary.value,
            money: money.value,
            username: username,
            password: password.value
        }
    })
    .then((res) => {
        console.log('유저 정보 수정 완료')
        console.log(res)
        articleStore.getUser()
        router.push({ name: 'MyPage' })
    })
    .catch((err) => {
        console.log('유저 정보 수정 실패')
        console.log(err)
    })
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