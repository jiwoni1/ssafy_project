<template>
    <div>
        <div id="carouselExampleAutoplaying" class="carousel slide" data-bs-ride="carousel">
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <img src="../../public/main1.png" class="d-block w-100" alt="...">
                </div>
                 <div class="carousel-item">
                     <img src="../../public/main2.jpg" class="d-block w-100" alt="...">
                </div>
                 <div class="carousel-item">
                    <img src="../../public/main3.jpg" class="d-block w-100" alt="...">
                </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
            </button>
        </div>
        <div class="go">
        <div class="go-deposit" @click="goDeposit">
            <div class="depo-word">
                <p>예금 비교 바로가기</p>
            </div>
            <img class="pig" src="../../public/pig.png" alt="">
        </div>
        <div class="go-exchange" @click="goExchange">
            <div class="depo-word">
                <p>환율 정보 바로가기</p>
            </div>
            <img class="money" src="../../public/money.png" alt="">
        </div>
        <div class="go-recommend" @click="goRecommend">
            <div class="depo-word">
                <p>금융상품 추천 바로가기</p>
            </div>
            <img class="recommend" src="../../public/recommend.png" alt="">
        </div>
    </div>
    </div>
</template>


<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goDeposit = function () {
    router.push({ name: 'deposit'})
}

const goExchange = function () {
    router.push({ name: 'ChangeRate'})
}

const goRecommend = function () {
    router.push({ name: 'recommend'})
}
</script>


<style scoped>
img {
    height: 600px;
    width: 100%;
}

.go {
    margin: 100px 100px;
    justify-content: space-around;
    display: flex;
    flex-direction: row;
    height: 300px;
}
.go-deposit, .go-exchange, .go-recommend{
    border: 1px solid lightgray;
    width: 500px;
    height: 150px;
    margin: 0 10px;
    text-align: center;
    /* background-color: lightgray; */
    display: flex;
    justify-content: center;
    align-items: center;

}

.depo-word {
    width: 180px;
    /* background-color: rgb(255, 255, 255);
    border-radius: 20%; */
    text-align: center;
    font-weight: bold;
    margin: 5px
}
.pig, .money, .recommend {
    width: 90px;
    height: 90px;
    margin: 10px;

}
</style>