<template>
    <div>
        <br>
        <RouterLink :to="{ name: 'deposit' }">정기예금</RouterLink>  |
        <RouterLink :to="{ name: 'saving' }">정기적금</RouterLink>
    </div>
    <div>
        <h1>정기예금</h1>
        <table>
            <tr>
                <th>공시 제출일</th>
                <th>금융 회사명</th>
                <th>상품명</th>
                <th>기본 금리</th>
                <th>최고 금리</th>
            </tr>
            <tr v-for="deposit in store.deposits"
                :key="deposit.id"
                :deposit="deposit">
                <td><span>{{ deposit.dcls_month }}</span></td>
                <td><span>{{ deposit.kor_co_nm }}</span></td>
                <td><span>{{ deposit.fin_prdt_nm }}</span></td>    
                <td><span>{{ deposit.depositoptions_set[0].intr_rate }}</span></td>  
                <td><span>{{ deposit.depositoptions_set[0].intr_rate2 }}</span></td>             

            </tr>

        </table>
        
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { useBankStore } from '@/stores/bank'



const store = useBankStore()


// mount되기 전 예금 정보 DB에 저장하기
onMounted(() => {
    store.getDeposit()
})

</script>

<style scoped>
td, th {
}
body {
  padding: 1rem;
}

</style>