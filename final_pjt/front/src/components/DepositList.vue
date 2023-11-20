<template>
    <div>
        <br>
        <RouterLink :to="{ name: 'deposit' }">정기예금</RouterLink>  |
        <RouterLink :to="{ name: 'saving' }">정기적금</RouterLink>
    </div>
    <div>
        <h1>정기예금</h1>        
            <h3>예금 검색하기</h3>
            <h4>검색 조건을 입력하세요</h4>
            <hr>
            <div class="search_deposit">
                <label for="bank">은행을 선택하세요</label>
                    <div class="bank" id="bank">
                        <select v-model="bank_selecte">
                            <option value="" selected>전체은행</option>
                            <option value="경남은행">경남은행</option>
                            <option value="국민은행">국민은행</option>
                            <option value="농협은행">농협은행</option>
                            <option value="대구은행">대구은행</option>
                            <option value="부산은행">부산은행</option>
                            <option value="수협은행">수협은행</option>
                            <option value="우리은행">우리은행</option>
                            <option value="전북은행">전북은행</option>
                            <option value="카카오뱅크">카카오뱅크</option>
                            <option value="케이뱅크">케이뱅크</option>
                            <option value="중소기업은행">중소기업은행</option>
                            <option value="제주은행">제주은행</option>
                            <option value="토스뱅크">토스뱅크</option>
                            <option value="한국산업은행">한국산업은행</option>
                        </select>
                    </div>

                    <br>

                    <label for="period">예치기간</label>
                    <div class="period" id="period">
                        <select v-model="period_selecte">
                            <option value="">전체기간</option>
                            <option value="6">6개월</option>
                            <option value="12">12개월</option>
                            <option value="18">18개월</option>
                            <option value="24">24개월</option>
                        </select>
                    </div>

                    <br>

                <button @click="change_option">확인</button>
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
                    <!-- deposit : filteredDeposits의 반환값 -->
                    <tr v-for="deposit in filteredDeposits"
                        :key="deposit.id"
                        :deposit="deposit">
                        <td><span>{{ deposit.dcls_month }}</span></td>
                        <td><span>{{ deposit.kor_co_nm }}</span></td>
                        <td><span>{{ deposit.fin_prdt_nm }}</span></td>     
                        <!-- <td><span>{{ deposit }}</span></td>  -->
                        <td><span>{{ deposit.depositoptions_set[0].intr_rate }}</span></td>  
                        <td><span>{{ deposit.depositoptions_set[0].intr_rate2 }}</span></td>             
        
                    </tr>
                    <tr v-if="filteredDeposits.length === 0">
                        <br>
                        <td>해당 상품은 없습니다.</td>
                    </tr>
        
        
                </table>
            </div>
        
    </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { useBankStore } from '@/stores/bank'



const store = useBankStore()
const bank_selecte = ref('')
const bank_selected = ref('')
const period_selecte = ref('')
const period_selected = ref('')



// mount되기 전 예금 정보 DB에 저장하기
onMounted(() => {
    store.getDeposit()
})

// 예금 검색
// 필터링된 예금 정보 반환
const filteredDeposits = computed(() => {
    return store.deposits.filter(deposit => {
        // 조건이 없을때, 조건이 있을 때
        const bankFilter =  bank_selected.value === '' || bank_selected.value === deposit.kor_co_nm
        // 문자열 -> 숫자로 변환
        const periodFilter = period_selected.value === '' || parseInt(period_selected.value) === deposit.depositoptions_set[0].save_trm
        return bankFilter && periodFilter
    })
})
const change_option = function () {
    // 확인 누르기 전에는 출력되는 내용이 바뀌지 않도록
    // select와 연결된 (v-model) 변수의 값을 확인버튼을 누를 시 %_selected에 넣어주고
    // 그 값으로 비교
    bank_selected.value = bank_selecte.value
    period_selected.value = period_selecte.value
    console.log(filteredDeposits.value)
}


</script>

<style scoped>


</style>