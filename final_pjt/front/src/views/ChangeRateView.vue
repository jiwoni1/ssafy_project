<template>
    <div class="exchange-template">
        <div class="cal">
            <h3 id="title">환율 계산기</h3>
            <div class="text-success">
                <hr>
            </div>
            <br>
            <div>
                <select v-model="selected_country" class="form-select form-select-lg mb-3" aria-label="Large select example">
                <option value="">국가를 선택하세요.</option>
                <option v-for="rate in store.exchangeRateDatas" :key="rate.cur_nm">{{ rate.cur_nm }}</option>
                </select>
                
                <br>
                <div class="row">
                    <div class="col-md-9" id="input">
                        <input class="form-control form-control-lg" type="text" placeholder="값을 입력하세요." aria-label=".form-control-lg example" v-model="otherRate">
                    </div>
                    <div class="col-md-3" id="won">{{ otherMoney }}</div>
                </div>

                <br>
                <div class="row">
                    <div class="col-md-9" id="input">
                        <input class="form-control form-control-lg" type="text" placeholder="값을 입력하세요." aria-label=".form-control-lg example" v-model="wonRate">
                    </div>
                    <div class="col-md-3" id="won">₩</div>
                </div>
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
/* .card {
    width: 50%;
    margin: 100px auto;
    padding: 50px;
    text-align: center;
  } */

.exchange-template {
    background-color: rgb(242, 250, 242);
    padding: 8% 30%;
}

#title {
    color: rgb(102, 175, 102);
    font-weight: bold;
}

.cal {
    /* border: solid 1px rgb(102, 175, 102); */
    background-color: white;
    padding: 12%;
    border-radius: 0.5%;
    /* background-color: rgb(241, 248, 241); */
}

#won {
    text-align: center;
    padding : 10px 0;
}
</style>