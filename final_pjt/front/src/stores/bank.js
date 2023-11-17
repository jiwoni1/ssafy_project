import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useBankStore = defineStore('bank', () => {

  const token = ref(null)
  const router = useRouter()

  // 회원가입
  const signUp = function (payload) {
    // 2. 구조 분해 할당
    const { username, password1, password2 } = payload
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/signup/',
      data: {
        // 1. 객체의 단축 속성
        // username: payload.username,
        // password1 : payload.password1
        // password2 : payload.password2
        username, password1, password2
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
      url: 'http://127.0.0.1:8000/accounts/login/',
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

  // const logOut = function () {
  //   axios({
  //     method: 'post',
  //     url: 'http://127.0.0.1:8000/accounts/logout/'
  //   })
  //   .then(()=> {
  //     console.log('로그아웃됨')
  //   })
  // }
  

  return { signUp, logIn, token }
})
