import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import ProductView from '@/views/ProductView.vue'
import BankMapView from '@/views/BankMapView.vue'
import CommunityView from '@/views/CommunityView.vue'
import MyPageView from '@/views/MyPageView.vue'
import ChangeRateView from '@/views/ChangeRateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import DepositList from '@/components/DepositList.vue'
import SavingList from '@/components/SavingList.vue'
import DepositDetail from '@/components/DepositDetail.vue'
import SavingDetail from '@/components/SavingDetail.vue'
import AddProduct from '@/components/AddProduct.vue'

// article
import ArticleCreate from '@/components/ArticleCreate.vue'
import ArticleDetail from '@/components/ArticleDetail.vue'
import ArticleUpdate from '@/components/ArticleUpdate.vue'
import ArticlePreview from '@/components/ArticlePreview.vue'
import CommentDetail from '@/components/CommentDetail.vue'

// profile
import Profile from '@/components/Profile.vue'
import Recommend from '@/components/Recommend.vue'
import ProfileUpdate from '@/components/ProfileUpdate.vue'
import ProfileUpdateItem from '@/components/ProfileUpdateItem.vue'
import AddProductSide from '@/components/AddProductSide.vue'


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
      path: '/community',
      name: 'Community',
      component: CommunityView
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
      component: SavingDetail,
      props: true,
    },
    {
      path: '/addproduct',
      name: 'addProduct',
      component: AddProduct
    },


    {
      path: '/articlecreate',
      name: 'articleCreate',
      component: ArticleCreate
    },

    {
      path: '/profile',
      name: 'Profile',
      component: Profile
    },
    {
      path: '/articledetail/:id',
      name: 'ArticleDetail',
      component: ArticleDetail,

    },
    {
      path: '/articleupdate/:id',
      name: 'ArticleUpdate',
      component: ArticleUpdate,
    },
    {
      path: '/articlepreview',
      name: 'ArticlePreview',
      component: ArticlePreview,
    },
    {
      path: '/commentdetail',
      name: 'CommentDetail',
      component: CommentDetail,
      props: true,
    },
    {
      path: '/recommend',
      name: 'recommend',
      component: Recommend,
      props: true,
    },
    {
      path: '/profileupdate',
      name: 'ProfileUpdate',
      component: ProfileUpdate,
    },
    {
      path: '/profileupdateitem',
      name: 'ProfileUpdateItem',
      component: ProfileUpdateItem,
    },
    {
      path: '/addproductside',
      name: 'AddProductSide',
      component: AddProductSide,
    },

  ]
})

import { useArticleStore } from '@/stores/article.js'

router.beforeEach((to, from) => {
  const articleStore = useArticleStore()
  if (to.name === 'Community' && !articleStore.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogIn' }
  }
})

export default router
