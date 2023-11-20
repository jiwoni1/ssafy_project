<template>
    <div>
      <h1>Signup</h1>
      <form @submit.prevent="signUp">
        <label for="username">아이디 : </label>
        <input type="text" id="username" v-model.trim="username"><br>

        <label for="password1">비밀번호 : </label>
        <input type="password" id="password1" v-model.trim="password1"><br>

        <label for="password2">비밀번호 확인 : </label>
        <input type="password" id="password2" v-model.trim="password2"><br>

        <label for="nickname">닉네임 : </label>
        <input type="text" id="nickname" v-model.trim="nickname"><br>

        <label for="email">이메일 : </label>
        <input type="email" id="email" v-model.trim="email"><br>

        <label for="age">나이 : </label>
        <input type="text" id="age" v-model.trim="age"><br>

        <label for="money">재산 : </label>
        <input type="text" id="money" v-model.trim="money"><br>

        <label for="salary">연봉 : </label>
        <input type="number" id="salary" v-model.trim="salary"> 만원<br>
        <br>
        <input type="submit">
      </form>
    </div>
  </template>
  
  <script setup>

  import { ref } from 'vue'
  import { useBankStore } from '@/stores/bank'

  const store = useBankStore()
  const username = ref(null)
  const password1 = ref(null)
  const password2 = ref(null)
  const nickname = ref(null)
  const email = ref(null)
  const age = ref(null)
  const money = ref(null)
  const salary = ref(null)
  
  const signUp = function () {
    // 전달해줄 데이터
    // 하나의 객체로 묶어서 전달
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
  
  </script>
  
  <style>
  
  </style>