<template>
  <div class="login">
    <h1 style="text-align: center;">Login</h1>
    <form @submit.prevent="logIn">
      <div class="mb-3 row">
        <label for="username" class="col-sm-2 col-form-label">USERNAME</label>
        <div class="col-sm-10">
          <input type="text" class="form-control" id="id" v-model.trim="username">
        </div>
      </div>
      <div class="mb-3 row">
        <label for="password" class="col-sm-2 col-form-label">PASSWORD</label>
        <div class="col-sm-10">
          <input type="password" class="form-control" id="password" v-model.trim="password">
        </div>
      </div>
      <input type="submit" class="btn btn-primary mb-3">
    </form>
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
.login {
  width: 60%;
  margin: auto;
}
</style>