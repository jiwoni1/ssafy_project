<template>
    <div>
      <h1>Login</h1>
      <form @submit.prevent="logIn">
        <input type="text" v-model.trim="username">
        <input type="password" v-model.trim="password">
        <input type="submit">
      </form>
    </div>
  </template>
  
  <script setup>
  // 사용자가 입력하는 정보를 실시간으로 저장해야해 -> ref
  import { ref } from 'vue'
  import { useBankStore } from '@/stores/bank'
  
  const store = useBankStore()
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
  
  </style>