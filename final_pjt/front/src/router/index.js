import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import ProductView from '@/views/ProductView.vue'
import BankMapView from '@/views/BankMapView.vue'
import ArticleView from '@/views/ArticleView.vue'
import MyPageView from '@/views/MyPageView.vue'
import ChangeRateView from '@/views/ChangeRateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import DepositList from '@/components/DepositList.vue'
import SavingList from '@/components/SavingList.vue'
import DepositDetail from '@/components/DepositDetail.vue'
import SavingDetail from '@/components/SavingDetail.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Main',
      component: MainView
    },
    {
      path: '/product',
      name: 'Product',
      component: ProductView
    },
    {
      path: '/bankmap',
      name: 'BankMap',
      component: BankMapView
    },
    {
      path: '/changerate',
      name: 'ChangeRate',
      component: ChangeRateView
    },
    {
      path: '/article',
      name: 'Article',
      component: ArticleView
    },
    {
      path: '/mypage',
      name: 'MyPage',
      component: MyPageView
    },
    {
      path: '/signup',
      name: 'SignUp',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogIn',
      component: LogInView
    },

    {
      path: '/deposit',
      name: 'deposit',
      component: DepositList
    },
    {
      path: '/saving',
      name: 'saving',
      component: SavingList
    },
    {
      path: '/deposit/:id',
      name: 'depositDetail',
      component: DepositDetail,
      props: true,
    },
    {
      path: '/saving/:id',
      name: 'savingDetail',
      component: SavingDetail
    },

  ]
})

export default router
