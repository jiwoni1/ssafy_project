<template>
  <div id="container">
    <div class="login">
        <h2 id="loginTitle">Login</h2>
        <form @submit.prevent="logIn">
        <!-- 아이디, 비번, 버튼 박스 -->
        <div class="inputBox">
          <div class="input-form-box"><span>아이디 </span><input type="text" name="id" class="form-control" v-model="username"></div>
          <br>
          <div class="input-form-box"><span>비밀번호 </span><input type="password" name="pw" class="form-control" v-model="password"></div>
          <br>
          <div class="button-login-box" >
            <input type="submit" class="btn btn-success btn-md" style="width:100%" value="로그인">
          </div>
        </div>
        <div v-if="store.errlogin">
          {{ errlogin() }}
        </div>
    </form>
    </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/article'

const store = useArticleStore()
const router = useRouter()
const username = ref(null)
const password = ref(null)

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value,
  }
  // 호출하면서 payload를 전달
  store.logIn(payload)
}

const errlogin = function () {
  window.alert('해당하는 로그인 정보가 없습니다.')
  store.errlogin = ''
  router.go(0)
}

</script>

<style>

#container {
  padding: 10% 35%;
}

#loginTitle {
    color:rgb(102, 175, 102);
    margin-bottom: 30px;
}


</style>