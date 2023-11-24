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
                <RouterLink style="color: rgb(125, 193, 125);" :to="{ name: 'recommend' }">상품 추천 받기</RouterLink>
            </div>
        </div>  
        <div class="col-md-10">
            <div>
                <h1 id="h1">적금 및 예금 상품 추천</h1>
                <hr>
                <h6 class="gray"><strong>{{ articleStore.userData.nickname }}</strong>님과 비슷한 <strong>나이, 연봉, 재산</strong>을 가진 사람들이 많이 가입한 상품입니다.</h6>
                <br>
                <br>
                <div v-if="articleStore.usersData.same_product.length > 0">
                    <div v-for="data in articleStore.usersData.same_product" :key="data.id">
                        <div v-for="saving in savings">
                            <div v-if="data===saving.fin_prdt_cd">
                                <div>[정기적금] {{ saving.kor_co_nm }} - {{ saving.fin_prdt_nm }}</div>
                                <hr>
                                <br>
                            </div>
                        </div>
                        <div v-for="deposit in deposits">
                            <div v-if="data===deposit.fin_prdt_cd">
                                <div>[정기예금] {{ deposit.kor_co_nm }} - {{ deposit.fin_prdt_nm }}</div>
                                <hr>
                                <br>
                            </div>
                        </div>
                    </div>
                </div>
                <div v-else>
                    <p class="gray">상품이 없습니다.</p>
                </div>
            </div>
            <div class="child">
                <h2 id="h1">추가 상품 추천</h2>
                <hr>
                <div>
                    <p style="color: gray;">우리 아이, 반려 동물을 위한 예적금 상품을 추천해드립니다.</p>
                    <br>
                    <br>
                    <div>
                        <div class="row">
                            <br>
                            <div class="col-md-5">
                                <label for="child_sel" class="child-label">▶ 자녀가 있으신가요?</label>
                            </div>
                            <div class="col-md-7">
                                <button @click="change_option" class="btn btn-success">추천 받기</button>
                            </div>
                        </div>
                        <br>
                        <div v-if="selected">
                            <div>[정기적금] {{ childSaving.kor_co_nm }} - {{ childSaving.fin_prdt_nm }}</div>
                            <p style="color: gray;">15세 이하의 개인에게 연 2.50%의 높은 금리를 적용합니다.</p>
                        </div>
                    </div>
                    <br>
                    <br>
                    <div>
                        <div class="row">
                            <br>
                            <div class="col-md-5">
                                <label for="child_sel" class="child-label">▶ 반려 동물이 있으신가요?</label>
                            </div>
                            <div class="col-md-7">
                                <button @click="change_option_animal" class="btn btn-success">추천 받기</button>
                            </div>
                        </div>
                        <br>
                        <br>
                        <div v-if="selected_animal">
                            <p style="color: gray;">우대이율 6개월제 최대 0.55%, 12개월제 최대 0.90% 적용</p>
                            <div>[정기적금] {{ animalSaving1.kor_co_nm }} - {{ animalSaving1.fin_prdt_nm }}</div>
                            <hr>
                            <br>
                            <p style="color: gray;">우대이율 6개월제 최대 0.55%, 12개월제 최대 0.90% 적용</p>
                            <div>[정기적금] {{ animalSaving2.kor_co_nm }} - {{ animalSaving2.fin_prdt_nm }}</div>
                            <hr>
                            <br>
                            <p style="color: gray;">반려동물 요금제, 반려동물애정활동에 따른 금리 우대</p>
                            <div>[정기적금] {{ animalSaving3.kor_co_nm }} - {{ animalSaving3.fin_prdt_nm }}</div>
                        </div>

                    </div>

                </div>
            </div>
        </div>     
    </div>
</template>

<script setup>
import { useArticleStore } from '@/stores/article'
import { useBankStore } from '@/stores/bank'
import { ref } from 'vue';
const articleStore = useArticleStore()
const bankStore = useBankStore()

// 예적금 데이터
const savings = bankStore.savings
const deposits = bankStore.deposits

const childyn = ref('')
const selected = ref(false)
const selected_animal = ref(false)
const childSaving = ref(null)
const animalSaving1 = ref(null)
const animalSaving2 = ref(null)
const animalSaving3 = ref(null)


const change_option = function () {
    selected.value = true
    for (const bank of bankStore.savings) {
        if (bank.id == 62) {
            childSaving.value = bank
        }
    }
}

const change_option_animal = function () {
    selected_animal.value = true
    for (const bank of bankStore.savings) {
        if (bank.id == 10) {
            animalSaving1.value = bank
        } 
        if (bank.id == 11) {
            animalSaving2.value = bank
        }
        if (bank.id == 38) {
            animalSaving3.value = bank
        }
    }
}

</script>

<style scoped>
.recommend-template {
    padding: 5% 7%;
}

#h1 {
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

.child {
    margin-top: 200px;
}
.child-label {
    font-weight: bold;
}

</style>