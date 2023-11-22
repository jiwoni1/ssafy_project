<template>
    <!--예금 검색창-->
    <div>
        <div class="row">
            <div class="col-md-3" id="search">       
                <!--적금상품과 예금상품 선택링크-->
                <nav>
                    <ul class="nav nav-tabs nav-justified">
                        <li class="nav-item">
                            <RouterLink :to="{ name: 'deposit' }" class="nav-link">정기예금</RouterLink>
                        </li>
                        <li class="nav-item">
                            <RouterLink :to="{ name: 'saving' }" class="nav-link">정기적금</RouterLink>
                        </li>
                    </ul>
                </nav>
                <br>
                <h4>예금 검색하기</h4>
                <h6>검색 조건을 입력하세요</h6>
                <div class="text-success">
                    <hr>
                </div>
                <div class="search_deposit">
                    <label for="bank">은행을 선택하세요</label>
                    <div class="bank" id="bank">
                        <select v-model="bank_selecte" class="form-select form-select-md">
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
                        <select v-model="period_selecte" class="form-select form-select-md">
                            <option value="">전체기간</option>
                            <option value="6">6개월</option>
                            <option value="12">12개월</option>
                            <option value="18">18개월</option>
                            <option value="24">24개월</option>
                        </select>
                    </div>
                    <br>
                    <button @click="change_option" class="btn btn-light" style="float:right;">확인</button>
                </div>
            </div>
        

            <div class="col-md-9" id="search">
                <table class="table">
                    <thead>
                        <tr class="table-success">
                            <th scope="col">공시 제출월</th>
                            <th scope="col">금융 회사명</th>
                            <th scope="col">상품명</th>
                            <th scope="col">기본 금리</th>
                            <th scope="col">최고 금리</th>
                        </tr>
                    </thead>
                    <tbody>
                        <!-- deposit : filteredDeposits의 반환값 -->
                        <tr v-for="deposit in filteredDeposits"
                            :key="deposit.id"
                            @click="goDepositDetail(deposit.id)">
                            <td>{{ deposit.dcls_month }}</td>
                            <td>{{ deposit.kor_co_nm }}</td>
                            <td>{{ deposit.fin_prdt_nm }}</td>     
                            <td>{{ deposit.depositoptions_set[0].intr_rate }}</td>  
                            <td>{{ deposit.depositoptions_set[0].intr_rate2 }}</td>             

                        </tr>
                        <hr>
                        <tr v-if="filteredDeposits.length === 0">
                            <br>
                            <td>해당 상품은 없습니다.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue'
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { useBankStore } from '@/stores/bank'


const store = useBankStore()
const router = useRouter()

const bank_selecte = ref('')
const bank_selected = ref('')
const period_selecte = ref('')
const period_selected = ref('')



// mount되기 전 예금 정보 DB에 저장하기
// onMounted(() => {
//     store.getDeposit()
// })

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

// 상품을 클릭하면 상세 페이지로 이동하는 함수
const goDepositDetail = function (depositId) {
    router.push({ name: 'depositDetail', params: { id: depositId }})
}


</script>

<style scoped>

.nav-link{
    color: green;
}
</style>