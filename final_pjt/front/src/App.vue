<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
      <nav>
        <RouterLink :to="{ name: 'Main' }">메인페이지</RouterLink> |
        <RouterLink :to="{ name: 'Product' }">예적금 비교</RouterLink> |
        <RouterLink :to="{ name: 'ChangeRate' }">환율 검색</RouterLink> |
        <RouterLink :to="{ name: 'BankMap' }">은행 지도</RouterLink> |
        <RouterLink :to="{ name: 'Article' }">커뮤니티</RouterLink> |
        <RouterLink :to="{ name: 'MyPage' }">MY PAGE</RouterLink> |
        <RouterLink :to="{ name: 'SignUp' }">회원가입</RouterLink> |
        <RouterLink :to="{ name: 'LogIn' }">로그인</RouterLink> |


      </nav>
  </header>

  <RouterView />
</template>

<style scoped>

</style>
