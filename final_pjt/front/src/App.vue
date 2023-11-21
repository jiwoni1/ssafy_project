<template>
  <header>
      <nav class="navbar navbar-expand-md" style="background-color: #e3f2fd;">
        <div class="container-fluid">
          <a class="navbar-brand" href="/main">LOGO</a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse justify-content-between" id="navbarNav">
            <ul class="nav">
              <!-- <li class="nav-item">
                <RouterLink :to="{ name: 'Main' }" class="nav-link">메인페이지</RouterLink>
              </li> -->
              <li class="nav-item">
                <RouterLink :to="{ name: 'Product' }" class="nav-link">예적금 비교</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink :to="{ name: 'ChangeRate' }" class="nav-link">환율 검색</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink :to="{ name: 'BankMap' }" class="nav-link">은행 지도</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink :to="{ name: 'Community' }" class="nav-link">커뮤니티</RouterLink>
              </li>
            </ul>
            <ul class="nav">
            
                <li class="nav-item" v-if="articleStore.isLogin">
                  <RouterLink :to="{ name: 'MyPage' }" class="nav-link">MY PAGE</RouterLink>
                </li>
                <li class="nav-item" v-if="articleStore.isLogin">
                    <form @submit.prevent="articleStore.logOut">
                      <input type="submit" value="로그아웃">
                    </form>
                </li>
              
                <li class="nav-item" v-if="articleStore.isLogin === false">
                  <RouterLink :to="{ name: 'SignUp' }" class="nav-link">회원가입</RouterLink>
                </li>
                <li class="nav-item" v-if="articleStore.isLogin === false">
                  <RouterLink :to="{ name: 'LogIn' }" class="nav-link">로그인</RouterLink>
                </li>
            </ul>
        </div>
      </div>
      </nav>
  </header>

  <RouterView />
</template>


<script setup>
import { onMounted } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { useBankStore } from './stores/bank'
import { useArticleStore } from '@/stores/article'

const bankStore = useBankStore()
const articleStore = useArticleStore()


// 적금, 예금 데이터 DB에 저장해놓기
onMounted(() => {
  bankStore.saveDeposit()
  bankStore.saveSaving()
  bankStore.getDeposit()
  bankStore.getSaving()
})


</script>


<style scoped>

</style>
