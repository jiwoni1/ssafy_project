import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useBankStore = defineStore('bank', () => {
  const router = useRouter()
  const API_URL = 'http://127.0.0.1:8000'


  // 예적금 데이터 저장
  const savings = ref(null)
  const deposits = ref(null)


  // 예금 데이터 DB에 저장하기
  const saveDeposit = function () {
    axios({
      method: 'get',
      url: `${API_URL}/finlife/save-deposit-products/`
    })
    .then(res => {
      console.log('저장 완료')
    })
    .catch(err => {
      console.log(err)
      console.log('저장 실패')
    })
  } 
  
  
  // 적금 데이터 DB에 저장하기 
  const saveSaving = function () {
    axios({
      method: 'get',
      url: `${API_URL}/finlife/save-saving-products/`
    })
    .then(res => {
      console.log('저장 완료')
    })
    .catch(err => {
      console.log(err)
      console.log('저장 실패')
    })
  } 
  
  
  // 예금 상품 출력하기
  const getDeposit = function () {
    axios({
      method: 'get',
      url: `${API_URL}/finlife/deposit-products/`
    })
    .then(res => {
      console.log(res)
      deposits.value = res.data
    })
    .catch(err => {
      console.log(err)
    })
  } 
  
  
  // 적금 상품 출력하기
  const getSaving = function () {
    axios({
      method: 'get',
      url: `${API_URL}/finlife/saving-products/`
    })
    .then(res => {
      console.log(res)
      savings.value = res.data
    })
    .catch(err => {
      console.log(err)
    })
  } 


    // 환율 데이터 저장
    const saveExchangeRate = function() {
      axios({
          method: 'get',
          url: `${API_URL}/finlife/save-exchange-rate/`
      })
      .then((res) => {
          console.log("환율 데이터 저장 완료")
          console.log(res)
      })
      .catch((err) => {
          console.log(err)
      })
      }

    // 환율 데이터 받아오기
    const exchangeRateDatas = ref('')
    const GetExchangeRate = function() {
    axios({
        method: 'get',
        url: `${API_URL}/finlife/exchange-rate/`
    })
    .then((res) => {
        exchangeRateDatas.value = res.data
        console.log("환율 데이터 로드 완료")
        console.log(res)
    })
    .catch((err) => {
        console.log(err)
    })
    }

  
  return { 
    savings, deposits, saveDeposit, saveSaving, getDeposit, getSaving, 
    exchangeRateDatas, GetExchangeRate, saveExchangeRate  }
}, { persist: true })
