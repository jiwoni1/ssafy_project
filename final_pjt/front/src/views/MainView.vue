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
        <div class="go-deposit">
            <p>예금 상품 비교 바로가기</p>
        </div>
        <div class="go-exchange"></div>
        <div class="go-recommend"></div>
    </div>
    </div>
</template>


<script setup>
// const getImage = function () {
//     return new URL('@/images/pubao.png', import.meta.url)
// }

</script>


<style scoped>
img {
    height: 600px;
    width: 100%;
}

.go {
    margin: 100px 0;
    display: flex;
    flex-direction: row;
}
.go-deposit, .go-exchange, .go-recommend{
    border: 1px solid lightgray;
    width: 300px;
    height: 150px;
    margin: 10px;
}
</style>