<template>
    <div>
        <div class="card">
            <div class="card-header">환율 계산기</div>
            <div class="card-body">
                <ul class="list-group list-group-horizontal">
                    <li class="list-group-item">
                        <select v-model="selected_country" class="form-select" aria-label="Default select example">
                            <option value="">국가를 선택하세요.</option>
                            <option v-for="rate in store.exchangeRateDatas">{{ rate.cur_nm }}</option>
                        </select>
                    </li>
                    <li class="list-group-item"><input class="input" type="text" v-model="wonRate"></li>
                </ul>
            </div>
        </div>




        <!-- <h1>환율검색</h1>
        <select v-model="selected_country">
            <option value="">국가를 선택하세요.</option>
            <option v-for="rate in store.exchangeRateDatas">{{ rate.cur_nm }}</option>
        </select>
        <br>
        <input type="text" v-model="otherRate">
        <br>
        <input type="text" v-model="wonRate"> -->
     
    </div>
</template>

<script setup>
import { useBankStore } from '@/stores/bank'
import { ref, onMounted, watch } from 'vue'

const store = useBankStore()

onMounted(() => {
    store.GetExchangeRate()
})


// 국가 선택
const selected_country = ref('')


// 원화 -> 다른 나라 통화
// 다른 나라 통화 -> 원화
const otherRate = ref(null)
const wonRate = ref(null)


// 환율 계산
// 다른 나라 통화 -> 원화
const wonWatch = watch(wonRate, (newValue, oldValue) => {
    store.exchangeRateDatas.forEach(rate => {
        if (selected_country.value === rate.cur_nm) {
            otherRate.value = newValue / rate.deal_bas_r
            console.log(otherRate.value)
        }
    })
})

// 원화 -> 다른 나라 통화
const otherWatch = watch(otherRate, (newValue, oldValue) => {
    store.exchangeRateDatas.forEach(rate => {
        if (selected_country.value === rate.cur_nm) {
            wonRate.value = (rate.deal_bas_r * newValue)
        }
    })
})



</script>

<style scoped>
.form-select {
    border: none;
}

.input {
    border: none;
}
</style>