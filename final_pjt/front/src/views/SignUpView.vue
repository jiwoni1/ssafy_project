<template>
  <div class="signup">
    <h2 id="loginTitle">Signup</h2>
    <form @submit.prevent="signUp">
      <div class="mb-3 row">
        <label for="username" class="col-sm-2 col-form-label">아이디 </label>
        <div class="col-sm-10">
          <input type="text" id="username" class="form-control" v-model.trim="username">
        </div>
      </div>
      <div class="mb-3 row">
        <label for="password1" class="col-sm-2 col-form-label">비밀번호 </label>
        <div class="col-sm-10">
          <input type="password" id="password1" class="form-control" v-model.trim="password1">
        </div>
      </div>
      <div class="mb-3 row">
        <label for="password2" class="col-sm-2 col-form-label">비밀번호 확인 </label>
        <div class="col-sm-10">
          <input type="password" id="password2" class="form-control" v-model.trim="password2">
        </div>
      </div>
      <div class="mb-3 row">
        <label for="nickname" class="col-sm-2 col-form-label">닉네임 </label>
        <div class="col-sm-10">
          <input type="text" id="nickname" class="form-control" v-model.trim="nickname">
        </div>
      </div>
      <div class="mb-3 row">
        <label for="email" class="col-sm-2 col-form-label">이메일 </label>
        <div class="col-sm-10">
          <input type="email" id="email" class="form-control" v-model.trim="email">
        </div>
      </div>
      <div class="mb-3 row">
        <label for="age" class="col-sm-2 col-form-label">나이 </label>
        <div class="col-sm-10">
          <input type="text" id="age" class="form-control" v-model.trim="age">
        </div>
      </div>
      <div class="mb-3 row">
        <label for="money" class="col-sm-2 col-form-label">재산 </label>
          <div class="col-sm-10">
            <input type="text" id="money" class="form-control" v-model.trim="money" placeholder="만원">
          </div>
      </div>
      <div class="mb-3 row">
        <label for="salary" class="col-sm-2 col-form-label">연봉 </label>
        <div class="col-sm-10">
          <input type="number" id="salary" class="form-control" v-model.trim="salary" placeholder="만원">
        </div>
      </div>
      <input type="submit"  class="btn btn-success btn-md" style="float:right;">
      <div v-if="store.errmsg">
        {{ errmsg() }}
      </div>
    </form>
  </div>
</template>

<script setup>

import { ref } from 'vue'
import { useArticleStore } from '@/stores/article'
import router from '../router';

const store = useArticleStore()
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const nickname = ref(null)
const email = ref(null)
const age = ref(null)
const money = ref(null)
const salary = ref(null)

const signUp = function () {
  // 전달해줄 데이터 하나의 객체로 묶어서 전달
   const payload = {
    username : username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    age: age.value,
    money: money.value,
    salary: salary.value
   } 
   store.signUp(payload)
  }

const errmsg = function () {
  window.alert('폼에 맞게 다시 작성해주세요.(아이디 중복 or 비밀번호 양식)')
  store.errmsg = ''
  router.go(0)
}
</script>

<style>
.signup {
  padding: 5% 30%;
}
</style>