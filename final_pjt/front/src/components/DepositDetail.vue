<template>
    <div>
        <h1>정기예금 상세</h1>
        <div v-for="deposit in bankStore.deposits">
            <div v-if="props.id == deposit.id">
                <p>공시 제출월 : {{ deposit.dcls_month }}</p>
                <p>금융회사명 : {{ deposit.kor_co_nm }}</p>
                <p>상품명 : {{ deposit.fin_prdt_nm }}</p>
                <p>가입제한 : {{ deposit.join_deny }}</p>
                <p>가입대상  : {{ deposit.spcl_cnd }}</p>
                <p>가입 방법 : {{ deposit.join_way }}</p>
                <p v-if="deposit.spcl_cnd">우대 조건 : {{ deposit.spcl_cnd }}</p>
                <p v-if="deposit.ect_note">기타 유의사항 : {{ deposit.ect_note }}</p>
                <p>저축 기간 : {{ deposit.depositoptions_set[0].save_trm }}</p>
                <p>저축 금리 : {{ deposit.depositoptions_set[0].intr_rate }}</p>
                <p>최고 우대금리 : {{ deposit.depositoptions_set[0].intr_rate2 }}</p>
                <p>만기 후 이자율 : {{ deposit.mtrt_int }}</p>
                <button v-if="articleStore.isLogin" @click="addDepositProduct(deposit)">{{ isRegistered(deposit) }}</button>
            </div>
        </div>
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

</style>