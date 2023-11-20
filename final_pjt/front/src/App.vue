<template>
  <header>
      <nav>
        <RouterLink :to="{ name: 'Main' }">메인페이지</RouterLink> |
        <RouterLink :to="{ name: 'Product' }">예적금 비교</RouterLink> |
        <RouterLink :to="{ name: 'ChangeRate' }">환율 검색</RouterLink> |
        <RouterLink :to="{ name: 'BankMap' }">은행 지도</RouterLink> |
        <RouterLink :to="{ name: 'Article' }">커뮤니티</RouterLink> |
        <RouterLink :to="{ name: 'MyPage' }">MY PAGE</RouterLink> |
        <div v-if="store.isLogin">
          <form @submit.prevent="store.logOut">
            <input type="submit" value="로그아웃">
          </form>
        </div>
        <div v-else>
          <RouterLink :to="{ name: 'SignUp' }">회원가입</RouterLink> |
          <RouterLink :to="{ name: 'LogIn' }">로그인</RouterLink>
        </div>
      </nav>
  </header>

  <RouterView />
</template>


<script setup>
import { onMounted } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { useBankStore } from './stores/bank';
const store = useBankStore()


// 적금, 예금 데이터 DB에 저장해놓기
onMounted(() => {
  store.saveDeposit()
  store.saveSaving()
})




</script>


<style scoped>

</style>
