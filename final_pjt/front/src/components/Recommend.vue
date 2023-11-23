<template>
    <div class="row recommend-template">    
        <div class="col-md-2 routers" >
            <div class="router">
                <RouterLink style="color: grey;" :to="{ name: 'MyPage' }">회원 기본 정보</RouterLink>
            </div>
            <!-- <div class="router">
                <RouterLink style="color: rgb(125, 193, 125);" :to="{ name: 'AddProductSide' }">가입한 상품</RouterLink>
            </div> -->
            <!-- 수정하기 -->
            <div class="router">
                <RouterLink style="color: gray;" :to="{ name: 'AddProductSide' }">포트폴리오</RouterLink>
            </div>
            <div class="router">
                <RouterLink style="color: gray;" :to="{ name: 'recommend' }">상품 추천 받기</RouterLink>
            </div>
        </div>  
        <div class="col-md-10">
            <h3 id="h3">적금 및 예금 상품 추천</h3>
            <hr>
                
            <h6 class="gray">{{ articleStore.userData.username }}님과 비슷한 나이, 연봉, 재산을 가진 사람들이 많이 가입한 상품입니다.</h6>
            <br>
            <div v-if="articleStore.userData.length > 0">
                <div v-for="data in articleStore.usersData.same_product" :key="data.id">
                    <div v-for="saving in savings">
                        <div v-if="data===saving.fin_prdt_cd">
                            <div>[정기적금] {{ saving.kor_co_nm }} - {{ saving.fin_prdt_nm }}</div>
                            <br>
                        </div>
                    </div>
                    <div v-for="deposit in deposits">
                        <div v-if="data===deposit.fin_prdt_cd">
                            <div>[정기예금] {{ deposit.kor_co_nm }} - {{ deposit.fin_prdt_nm }}</div>
                            <br>
                        </div>
                    </div>
                </div>
            </div>
            <div v-else>
                <p class="gray">상품이 없습니다.</p>
            </div>
        </div>     
    </div>
</template>

<script setup>
import { useArticleStore } from '@/stores/article'
import { useBankStore } from '@/stores/bank'
const articleStore = useArticleStore()
const bankStore = useBankStore()

// 예적금 데이터
const savings = bankStore.savings
const deposits = bankStore.deposits

</script>

<style scoped>
.recommend-template {
    padding: 5% 7%;
}

#h3 {
    color: rgb(102, 175, 102);
    font-weight: bold;
}

.mypage {
    padding: 80px 15% 50px 70px;
}

.routers {
    margin: 60px 0;
}
.router {
    margin: 50px 0;
    color: gray;
}

.gray {
    color: rgb(90, 89, 89)
}

</style>