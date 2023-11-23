<template>
    <div>
        <h1>정기적금 상세</h1>
        <!-- <p>name : {{ props.id  }}</p> -->
        <!-- <p>{{ bankStore.deposits }}</p> -->

        <div v-for="saving in bankStore.savings">
            <!-- props.id는 문자 -->
            <div v-if="props.id == saving.id">
                <p>공시 제출월 : {{ saving.dcls_month }}</p>
                <p>금융회사명 : {{ saving.kor_co_nm }}</p>
                <p>상품명 : {{ saving.fin_prdt_nm }}</p>
                <p>가입제한 : {{ saving.join_deny }}</p>
                <p>가입대상  : {{ saving.join_member }}</p>
                <p>가입 방법 : {{ saving.join_way }}</p>
                <p v-if="saving.ect_note">기타 유의사항 : {{ saving.ect_note }}</p>
                <p v-if="saving.spcl_cnd">우대 조건 : {{ saving.spcl_cnd }}</p>
                <p>적립 유형명 : {{  saving.rsrv_type_nm }}</p>
                <p>저축 기간 : {{ saving.savingoptions_set[0].save_trm }}</p>
                <p>저축 금리 : {{ saving.savingoptions_set[0].intr_rate }}</p>
                <p>최고 우대금리 : {{ saving.savingoptions_set[0].intr_rate2 }}</p>
                <p>만기 후 이자율 : {{ saving.mtrt_int }}</p>
                <button v-if="articleStore.isLogin" @click="addSavingProduct(saving)">가입하기</button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useBankStore } from '@/stores/bank'
import { useArticleStore } from '@/stores/article'

const bankStore = useBankStore()
const articleStore = useArticleStore()
const router = useRouter()

// 버튼 토글하기
// const toggleText = ref('가입하기')


const props = defineProps({
    id: String,
})

// console.log(router.params.id)

// 장바구니 기능
const addSavingProduct = (saving) => {
    const existingProduct = JSON.parse(localStorage.getItem('saving')) || []
    // 중복 확인
    const isDuplicate = existingProduct.length > 0 && existingProduct.find((item) => item.id === saving.id)

    // 중복이 아니라면 추가
    // 버튼 토글
    if(!isDuplicate) {
        alert('해당 상품에 가입합니다.')
        existingProduct.push(saving)
    } else {
        alert('이미 가입된 상품입니다.')
    }


    // 수정된 카트 데이터를 localStorage에 저장
    localStorage.setItem('saving', JSON.stringify(existingProduct))

    // router.push({ name: 'addProduct' })
}








</script>

<style scoped>

</style>