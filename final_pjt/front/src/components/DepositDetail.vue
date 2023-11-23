<template>
    <div class="detail-template">
        <h1 id="h1">상품 상세 정보</h1>
        <hr>
        <table class="table">
            <div v-for="deposit in bankStore.deposits">
                <div v-if="props.id == deposit.id">
                    <tbody>
                        <tr>
                            <th scope="col">공시 제출월</th>
                            <td>{{ deposit.dcls_month }}</td>
                        </tr>
                        <br>
                        <br>
                        <tr>
                            <th scope="col">금융 회사명</th>
                            <td>{{ deposit.kor_co_nm }}</td>
                        </tr>
                        <br>
                        <br>
                        <tr>
                            <th scope="col">상품명</th>
                            <td>{{ deposit.fin_prdt_nm }}</td>
                        </tr>
                        <br>
                        <br>
                        <tr>
                            <th scope="col">가입 제한</th>
                            <td>{{ deposit.join_deny }} (1:제한없음, 2:서민전용, 3:일부제한)</td>
                        </tr>
                        <br>
                        <br>
                        <tr>
                            <th scope="col">가입 대상</th>
                            <td>{{ deposit.join_member }}</td>
                        </tr>
                        <br>
                        <br>
                        <tr>
                            <th scope="col">가입 방법</th>
                            <td>{{ deposit.join_way }}</td>
                        </tr>
                        <br>
                        <br>
                        <tr v-if="deposit.spcl_cnd">
                            <th scope="col">우대 조건</th>
                            <td>{{ deposit.spcl_cnd }}</td>
                        </tr>
                        <br>
                        
                        <tr v-if="deposit.ect_note">
                            <th scope="col">최고 금리</th>
                            <td>{{ deposit.ect_note }}</td>
                        </tr>
                        <br>
                        <br>
                        <tr>
                            <th scope="col">저축 기간</th>
                            <td>{{ deposit.depositoptions_set[0].save_trm }}</td>
                        </tr>
                        <br>
                        <br>
                        <tr>   
                            <th scope="col">저축 금리</th>
                            <td>{{ deposit.depositoptions_set[0].intr_rate }}</td>
                        </tr>
                        <br>
                        <br>
                        <tr>
                            <th scope="col">최고 우대금리</th>
                            <td>{{ deposit.depositoptions_set[0].intr_rate2 }}</td>
                        </tr>
                        <br>
                        <br>
                        <tr> 
                            <th>만기 후 이자율</th>
                            <td>{{ deposit.mtrt_int }}</td>            
                        </tr>
                        <br>
                        <br>
                        
                    </tbody>
                    <br>
                    <button v-if="articleStore.isLogin" @click="addDepositProduct(deposit)" class="btn btn-outline-success btn-lg" id="btn">{{ isRegistered(deposit) }}</button>
                </div>
            </div>
        </table>
        <!-- <button v-if="articleStore.isLogin" @click="addDepositProduct(deposit)" class="btn btn-outline-success btn-lg" id="btn">가입</button> -->

    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useBankStore } from '@/stores/bank'
import { useArticleStore } from '@/stores/article'

const bankStore = useBankStore()
const articleStore = useArticleStore()
const router = useRouter()
const registerd = ref(false)
const registeredDeposits = ref([])

const props = defineProps({
    id: String,
})

const getRegisteredDepositsFromStorage = () => {
  const existingProducts = JSON.parse(localStorage.getItem('deposit')) || []
  registeredDeposits.value = existingProducts
}

// 장바구니 기능
const addDepositProduct = (deposit) => {
    const existingProduct = JSON.parse(localStorage.getItem('deposit')) || []
    // 중복 확인
    const isDuplicate = existingProduct.length > 0 && existingProduct.find((item) => item.id === deposit.id)

    // 중복이 아니라면 추가
    if(!isDuplicate) {
        alert('해당 상품에 가입합니다.')
        existingProduct.push(deposit)
        registerd.value = true
    } else {
        alert('이미 가입된 상품입니다.')
    }

    // 수정된 카트 데이터를 localStorage에 저장
    localStorage.setItem('deposit', JSON.stringify(existingProduct))

    router.go(0)

}


const isRegistered = (deposit) => {
  const isDuplicate = registeredDeposits.value.some((item) => item.id === deposit.id)
  return isDuplicate ? '가입완료' : '가입하기'
}

onMounted(() => {
  const existingProducts = JSON.parse(localStorage.getItem('deposit')) || []
  registeredDeposits.value = existingProducts
})



</script>

<style scoped>
.detail-template {
    padding: 5% 15%;
}

#h1 {
    color: rgb(102, 175, 102);
    font-weight: bold;
}

tr > th {
    width: 20%;
    text-align: center;
    color: rgb(81, 81, 81);
}

tr > td {
    color: rgb(89, 89, 89);
}

.table {
    margin: 5% 0px 2%;
}

#btn {
    color : rgb(102, 175, 102);
    float :right;
}



</style>