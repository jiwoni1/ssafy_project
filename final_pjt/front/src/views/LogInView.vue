<template>
  <div id="container">
  <div class="login">
    <div id="loginTitle">Login</div>
    <form @submit.prevent="logIn">
    <!-- 아이디, 비번, 버튼 박스 -->
      <div class="inputBox">
       
          <div class="input-form-box"><span>아이디 </span><input type="text" name="id" class="form-control" v-model="username"></div>
          <div class="input-form-box"><span>비밀번호 </span><input type="password" name="pw" class="form-control" v-model="password"></div>
          <div class="button-login-box" >
            <input type="submit" class="btn btn-primary btn-xs" style="width:100%" value="로그인">
          </div>
        </div>
    </form>
    </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useArticleStore } from '@/stores/article'

const store = useArticleStore()
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
</script>

<style>
* { padding: 0; margin: 0; }

html, body {
  height: 100%;
  background: #ffffff;
}

#container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  height: 100%;
}

#loginBox {
  width: 300px;
  text-align: center;
  background-color: #ffffff;
}
.input-form-box {
  border: 0px solid #ff0000;
  display: flex;
  margin-bottom: 5px;
}
.input-form-box > span {
  display: block;
  text-align: left;
  padding-top: 5px;
  min-width: 65px;
}
.button-login-box {
  margin: 10px 0;
}
#loginBoxTitle {
  color:#000000;
  font-weight: bold;
  font-size: 32px;
  text-transform: uppercase;
  padding: 5px;
  margin-bottom: 20px;
  background: linear-gradient(to right, #270a09, #8ca6ce);
  /* -webkit-background-clip: text; */
  -webkit-text-fill-color: transparent;
}
#inputBox {
  margin: 10px;
}

#inputBox button {
  padding: 3px 5px;
}

</style>