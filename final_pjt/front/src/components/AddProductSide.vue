<template>
    <div class="row mypage">
        <div class="col-md-2 routers" >
            <div class="router">
                <RouterLink style="color: grey;" :to="{ name: 'MyPage' }">회원 기본 정보</RouterLink>
            </div>
            <div class="router">
                <RouterLink style="color: rgb(125, 193, 125);" :to="{ name: 'AddProductSide' }">가입한 상품</RouterLink>
            </div>
            <!-- 수정하기 -->
            <div class="router">
                <RouterLink style="color: gray;" :to="{ name: 'addProduct' }">포트폴리오</RouterLink>
            </div>
            <div class="router">
                <RouterLink style="color: gray;" :to="{ name: 'recommend' }">상품 추천 받기</RouterLink>
            </div>
        </div>
        <div class="col-md-10">
            <AddProduct />
        </div>
    </div>
    <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
import AddProduct from '@/components/AddProduct.vue'

</script>

<style scoped>
.mypage {
    padding: 80px 50px;
}

.routers {
    margin: 60px 0;
}
.router {
    margin: 50px 0;
    color: gray;
}

</style>