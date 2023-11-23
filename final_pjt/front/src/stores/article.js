import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import axios from 'axios'


export const useArticleStore = defineStore('article', () => {

  const router = useRouter()
  const API_URL = 'http://127.0.0.1:8000'
  

  // 변수
  const token = ref(null)
  const userName = ref('')
  const articles = ref([])
  const errmsg = ref('')
  const errlogin = ref('')
  const usersData = ref([])

  // 로그인 여부를 알 수 있는 변수
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  
  // 회원가입
  const signUp = function (payload) {
    const { username, password1, password2, nickname, email, age, money, salary } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, nickname, email, age, money, salary
      }
    })
      .then(() => {
        window.alert('회원가입이 완료되었습니다.')
        router.push({ name: 'LogIn' })
      })
      .catch((err) => {
        console.log(err.request.response)
        // errmsg.value = err.request.response
        errmsg.value = 'no'
      })
  }


  // 사용자가 입력한 username과 password를 인자로 전달받고
  // 받고나서 서버로 로그인 요청 + 응답 데이터에 있는 토큰을 받아서 스토어에 있는 토큰에 저장

  
  // 로그아웃
  const logOut = function () {
      axios({
          method: 'post',
          url: `${API_URL}/accounts/logout/`
        })
        .then(()=> {
            token.value = null
            userName.value = ''
            router.push({ name: 'Main' })
        })
    }
    
    
    // 전체 게시글 조회
    const getArticles = function () {
        axios({
            method: 'get',
            url: `${API_URL}/articles/`,
            headers: {
                Authorization: `Token ${token.value}`
            }
        })
        .then((res) => {
            console.log(res)
            articles.value = res.data
            console.log('게시글 조회 완료')
        })
        .catch((err) => {
            console.log(err)
            console.log('게시글 조회 실패')
        })
    }
    
    
                            
                            
    // 유저 정보 받아오기
    const userData = ref([])
    const getUser = function () {
        axios({
            method: 'get',
            url: `${API_URL}/accounts/user/${userName.value}/`,
            
        })
        .then((res) => {
            console.log(res)
            userData.value = res.data
        })
        .catch((err) => {
            console.log(err)
        })
    }

 
                            
    // 로그인
    const logIn = function (payload) {
        const { username, password } = payload
        axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
            username, password
        }
        })
        .then((res) => {
            // 발급받은 토큰 저장
            token.value = res.data.key
            userName.value = username
            console.log(userName.value)
            getUser()
            getUsers()
            router.push({ name: 'Main' })
        })
        .catch((err) => {
            console.log(err)
            errlogin.value = 'no'
        })
    
    }

    // 추천 상품 정보 받아오기
    const getUsers = function () {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      .then((res) => {
        console.log(res)
        usersData.value = res.data
        console.log('추천상품 저장')
      })
      .catch((err) => {
        console.log(err)
        console('추천상품 저장 실패')
      })
    }
  

  return { 
    API_URL, token, isLogin, signUp, logIn, logOut,
    articles, getArticles,
    getUser, userData, userName, errmsg, errlogin, getUsers, usersData }
}, { persist: true })
