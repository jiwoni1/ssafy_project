<template>
    <div>
        <div class="card">
            <h2>환율 계산기</h2>
            <div class="card-body">
                <ul class="list-group list-group-flush">
                    <select v-model="selected_country" class="form-select list-group-item" aria-label="Default select example">
                    <option value="">국가를 선택하세요.</option>
                    <option v-for="rate in store.exchangeRateDatas" :key="rate.cur_nm">{{ rate.cur_nm }}</option>
                    </select>
                </ul>
                <br>
                <ul class="list-group list-group-horizontal list-group-flush">
                    <input class="input list-group-item" type="text" v-model="wonRate" placeholder="입력하세요">
                    <div class="list-group-item">{{ otherMoney }}</div>
                </ul>
                <br>
                <ul class="list-group list-group-horizontal list-group-flush">
                    <input class="input list-group-item" type="text" v-model="otherRate" placeholder="입력하세요">
                    <div class="list-group-item">₩</div>
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

// 다른 나라 통화 단위
const otherMoney = ref(null)

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
watch(selected_country, () => {
      const rate = store.exchangeRateDatas.find(rate => selected_country.value === rate.cur_nm);
      if (rate) {
          wonRate.value = wonRate.value * rate.deal_bas_r;
          otherMoney.value = rate.cur_unit;
      }
  });
  



</script>

<style scoped>
.card {
    width: 50%;
    margin: 100px auto;
    padding: 50px;
    text-align: center;
  }
</style>