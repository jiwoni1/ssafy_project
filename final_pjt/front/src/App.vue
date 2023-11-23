<template>
  <header>
    <nav id="navbar" class="navbar navbar-expand-md">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">LOGO</a>

        <!-- 토글 버튼 -->
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <!-- 네비게이션 바 -->
        <div class="collapse navbar-collapse justify-content-between" id="navbarSupportedContent">
          <ul class="navbar-nav nav-underline">
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
        
          <ul class="navbar-nav">
            <span class="btn-group" role="group" aria-label="Basic outlined example">
              <li class="nav-item btn btn-outline-secondary btn-sm" v-if="articleStore.isLogin">
                <RouterLink :to="{ name: 'MyPage' }" class="nav-link">MY PAGE</RouterLink>
              </li>
              <li class="nav-item btn btn-outline-secondary btn-sm" v-if="articleStore.isLogin">
                <form @submit.prevent="articleStore.logOut">
                  <input type="submit" value="로그아웃" class="btn">
                </form>
              </li>
            </span>
            <span class="btn-group" role="group" aria-label="Basic outlined example">
              <li class="nav-item btn btn-outline-secondary btn-sm" v-if="articleStore.isLogin === false">
                <RouterLink :to="{ name: 'SignUp' }" class="nav-link">회원가입</RouterLink>
              </li>
              <li class="nav-item btn btn-outline-secondary btn-sm" v-if="articleStore.isLogin === false">
                <RouterLink :to="{ name: 'LogIn' }" class="nav-link">로그인</RouterLink>
              </li>
            </span>
          </ul>
        </div>
      </div>

    </nav>
    <hr class="border border-success border-0.5 opacity-50">
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
  bankStore.saveExchangeRate()
  // bankStore.GetExchangeRate()
})


</script>


<style scoped>
.container {
  color: #b4eb8a;
}

#navbar {
  height: 100px;
  padding: auto 100px;
}
.nav-link {
  color: black;
}

/* CSS 파일에 추가 */
#navbar {
  padding: 70px 50px 50px;
}

#navbarSupportedContent {
    background-color: white; /* 원하는 배경색으로 변경하세요 */
    padding: 10px; /* 내려오는 메뉴의 여백을 조절할 수 있습니다 */
    z-index: 1;
}
hr {
  z-index: 0;
  margin: 0px;
}



</style>
