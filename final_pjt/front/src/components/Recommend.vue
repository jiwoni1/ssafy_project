<template>
    <div>       
        <h1>적금 및 예금 상품 추천</h1>
            
        <p>{{ articleStore.userData.username }}님과 비슷한 나이, 연봉, 재산을 가진 사람들이 많이 가입한 상품입니다.</p>
        <div v-if="articleStore.userData">
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
            <p>상품이 없습니다.</p>
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

</style>