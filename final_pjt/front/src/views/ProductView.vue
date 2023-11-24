<template>
    <div>
        <DepositList />
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import DepositList from '@/components/DepositList.vue'
import { useBankStore } from '@/stores/bank.js'

const bankStore = useBankStore()

onMounted(() => {
  bankStore.saveDeposit()
  bankStore.saveSaving()
  bankStore.getDeposit()
  bankStore.getSaving()
})

</script>

<style scoped>

</style>