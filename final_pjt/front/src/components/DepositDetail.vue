<template>
    <div>
        <h1>상품 상세 조회</h1>
        <p>name : {{ props.id  }}</p>
    </div>
</template>

<script setup>
import { useBankStore } from '@/stores/bank'

const store = useBankStore()

const props = defineProps({
    id: Number
})

console.log(props.id)

</script>

<style scoped>

</style>