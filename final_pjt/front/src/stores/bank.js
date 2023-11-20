import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useBankStore = defineStore('bank', () => {
  // 토큰 생성
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const router = useRouter()
  // 로그인 여부를 알 수 있는 변수
  // 토근에 따라서, 토큰이 변할 때만 다시 계산되면 돼(computed)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  
  // 회원가입
  const signUp = function (payload) {
    // 2. 구조 분해 할당
    const { username, password1, password2, nickname, email, age, money, salary } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, nickname, email, age, money, salary
      }
    })
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
  }

    // 로그인 이후에 토근을 발급받게됨. 토근을 중앙저장소에 저장해야해
  // 모든 컴포넌트가 인증이 필요할 때, 토큰을 써야하므로
  // 그래서 로그인 함수는 store에 있어야!

  // 사용자가 입력한 username과 password를 인자로 전달받고
  // 받고나서 서버로 로그인 요청 + 응답 데이터에 있는 토큰을 받아서 스토어에 있는 토근에 저장

  const logIn = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
    // 발급받은 토큰 저장
      .then((res) => {
        token.value = res.data.key
        router.push({ name: 'Main' })

      })
      .catch((err) => {
        console.log(err)
      })

  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`
    })
    .then(()=> {
      token.value = null
      router.push({ name: 'Main' })
    })
  }
  

  return { signUp, logIn, token, isLogin, logOut }
}, { persist: true })
