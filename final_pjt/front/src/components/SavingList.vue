<template>
    <div>
        <br>
        <RouterLink :to="{ name: 'deposit' }">정기예금</RouterLink>  |
        <RouterLink :to="{ name: 'saving' }">정기적금</RouterLink>
    </div>

    <div>
        <h1>정기적금</h1>
        <div>
            <h3>적금 검색하기</h3>
            <h4>검색 조건을 입력하세요</h4>
            <hr>
            <div class="search_saving">
                <label for="bank">은행을 선택하세요</label>
                    <div class="bank" id="bank">
                        <select v-model="bank_selected">
                            <option disabled value="">전체은행</option>
                            <option value="">경남은행</option>
                            <option value="">국민은행</option>
                            <option value="">농협은행주식회사</option>
                            <option value="">대구은행</option>
                            <option value="">부산은행</option>
                            <option value="">수협은행</option>
                            <option value="">우리은행</option>
                            <option value="">전북은행</option>
                            <option value="">주식회사 카카오뱅크</option>
                            <option value="">주식회사 케이뱅크</option>
                            <option value="">중소은행</option>
                            <option value="">제주은행</option>
                            <option value="">토스뱅크 주식회사</option>
                            <option value="">한국산업은행</option>
                        </select>
                    </div>

                    <br>

                    <label for="period">예치기간</label>
                    <div class="period" id="period">
                        <select v-model="period_selected">
                            <option disabled value="">전체기간</option>
                            <option>6개월</option>
                            <option>12개월</option>
                            <option>18개월</option>
                            <option>24개월</option>
                        </select>
                    </div>

                    <br>

                <button @click="change_option">확인</button>
            </div>
                
                
            </div>
            <div>
                <table>
                    <tr>
                        <th>공시 제출일</th>
                    <th>금융 회사명</th>
                    <th>상품명</th>
                    <th>기본 금리</th>
                    <th>최고 금리</th>
                </tr>
                <tr v-for="saving in store.savings"
                    :key="saving.id"
                    :saving="saving">
                    <td><span>{{ saving.dcls_month }}</span></td>
                    <td><span>{{ saving.kor_co_nm }}</span></td>
                    <td><span>{{ saving.fin_prdt_nm }}</span></td>    
                    <td><span>{{ saving.savingoptions_set[0].intr_rate }}</span></td> 
                    <td><span>{{ saving.savingoptions_set[0].intr_rate2 }}</span></td>            
                </tr>
    
            </table>
        </div>
        

    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { useBankStore } from '@/stores/bank'

const store = useBankStore()
const bank_selected = ref('')
const period_selected = ref('')

// mount되기 전 예금 정보 DB에 저장하기
onMounted(() => {
    store.getSaving()
})


// 적금 검색
const change_option = function () {

}



</script>

<style scoped>

</style>