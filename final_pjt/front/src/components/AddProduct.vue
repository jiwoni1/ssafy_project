<template>
    <div>
        <!-- 가입한 상품 목록 -->
        <h1>가입한 상품들</h1>
        <div v-if="addedDeposits" 
             v-for="product in addedDeposits"
             :key="product.id">
            <p @click="goDepositDetail(product.id)">{{ product.kor_co_nm }} - {{ product.fin_prdt_nm }}</p>
            <button @click="removeDeposit(product)">가입 해지</button>
            <hr>
        </div>
        <div v-if="addedSavings" 
             v-for="product in addedSavings"
             :key="product.id">
            <p @click="goSavingDetail(product.id)">{{ product.kor_co_nm }} - {{ product.fin_prdt_nm }}</p>
            <button @click="removeSaving(product)">가입 해지</button>
            <hr>
        </div>
        
        <div v-if="!addedDeposits && !addedSavings">
            <strong>가입한 상품이 없습니다.</strong>
        </div>



        <!-- 가입한 상품 금리 차트 -->
        <div style="width: 400px; height:500px;">
            <Bar id="myChart" :options="chartOptions" :data="chartData"/>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useBankStore } from '@/stores/bank'

// 차트 제작
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const store = useBankStore()

const addedDeposits = ref([])
const addedSavings = ref([])

const router = useRouter()

// localStorage에서 가입한 상품 가져오기
addedDeposits.value = JSON.parse(localStorage.getItem('deposit')) || []
console.log(typeof(addedDeposits.value[0].depositoptions_set[0].intr_rate))
addedSavings.value =  JSON.parse(localStorage.getItem('saving')) || []

// 가입한 상품 삭제
const removeDeposit = (product) => {
    // localStroage에서 삭제
    // 현재 addedProducts.value에서 삭제
    // 1. 현재 localStroage에 저장된 데이터를 가져오기
    // 이 코드는 valid 하기 위해 한 단계 더 작성했다고 생각하면 됨
    // const addedProducts = JSON.parse(localStorage.getItem('product'))

    // 2. 삭제할 아이템 index 검색
    const itemIdx = addedDeposits.value.findIndex((item) => item.id === product.id)

    // 3. 데이터 삭제
    addedDeposits.value.splice(itemIdx, 1)

    // 4. 삭제된 데이터를 기준으로 데이터를 반영
    localStorage.setItem('product', JSON.stringify(addedDeposits.value))
    
}
const removeSaving = (product) => {
    // localStroage에서 삭제
    // 현재 addedProducts.value에서 삭제
    // 1. 현재 localStroage에 저장된 데이터를 가져오기
    // 이 코드는 valid 하기 위해 한 단계 더 작성했다고 생각하면 됨
    // const addedProducts = JSON.parse(localStorage.getItem('product'))

    // 2. 삭제할 아이템 index 검색
    const itemIdx = addedSavings.value.findIndex((item) => item.id === product.id)

    // 3. 데이터 삭제
    addedSavings.value.splice(itemIdx, 1)

    // 4. 삭제된 데이터를 기준으로 데이터를 반영
    localStorage.setItem('product', JSON.stringify(addedSavings.value))
    
}

// 상품을 클릭하면 상세 페이지로 이동하는 함수
const goDepositDetail = function (depositId) {
    router.push({ name: 'depositDetail', params: { id: depositId }})
}


const goSavingDetail = function (savingId) {
    router.push({ name: 'savingDetail', params: { id: savingId }})
}



// 그래프에 들어갈 데이터 가져오기
// 가입한 상품 금리 그래프
// 그래프 가로 축 => 상품명
const allProducts = ref(addedDeposits.value.concat(addedSavings.value))
const productName = computed(() => {
  const names = allProducts.value.map(product => product.fin_prdt_nm);
  names.unshift('평균 금리');
  return names
})

// 그래프 세로 축1 => 금리
const depositRate1 = computed(() =>
  addedDeposits.value.map(rate => rate.depositoptions_set[0].intr_rate)
);
const savingRate1 = computed(() =>
  addedSavings.value.map(rate => rate.savingoptions_set[0].intr_rate)
);
const mergedDepositRate1 = computed(() => [...depositRate1.value, ...savingRate1.value]);

// 그래프 세로 축2 => 최고 우대 금리
const depositRate2 = computed(() =>
  addedDeposits.value.map(rate => rate.depositoptions_set[0].intr_rate2)
);
const savingRate2 = computed(() =>
  addedSavings.value.map(rate => rate.savingoptions_set[0].intr_rate2)
);
const mergedDepositRate2 = computed(() => [...depositRate2.value, ...savingRate2.value]);

// 전체 상품 금리 평균 구하기
const allDeposits = computed(() => store.deposits.map(rate => rate.depositoptions_set[0].intr_rate));
const allSavings = computed(() => store.savings.map(rate => rate.savingoptions_set[0].intr_rate));
const allRate = computed(() => [...allDeposits.value, ...allSavings.value]);
const avgrate = computed(() => allRate.value.reduce((acc, cur) => acc + cur, 0) / allRate.value.length);

// 전체 상품 최고 우대 금리 평균 구하기
const allDeposits2 = computed(() => store.deposits.map(rate => rate.depositoptions_set[0].intr_rate2));
const allSavings2 = computed(() => store.savings.map(rate => rate.savingoptions_set[0].intr_rate2));
const allRate2 = computed(() => [...allDeposits2.value, ...allSavings2.value]);
const avgrate2 = computed(() => allRate2.value.reduce((acc, cur) => acc + cur, 0) / allRate2.value.length);
mergedDepositRate1.value.unshift(avgrate.value)
mergedDepositRate2.value.unshift(avgrate2.value)

// 차트에 들어갈 데이터
const chartData = ref({
    labels: productName.value,
    datasets: [
        {
            label: ['저축 금리'],
            backgroundColor: 'lightGreen',
            data: mergedDepositRate1.value,
        },
        {
            label: ['최고 우대 금리'],
            backgroundColor: 'lightblue',
            data: mergedDepositRate2.value,
        }
    ]
})

// 차트 옵션
const chartOptions = ref({
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      y: { // defining min and max so hiding the dataset does not change scale range
        min: 0,
        max: 5
      }
    },
    
})

</script>

<style scoped>

</style>