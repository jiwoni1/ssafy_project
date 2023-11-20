<template>
    <div>
        <h1>은행</h1>
        <div id="map" style="width: 500px;height: 400px;"></div>
    </div>
</template>


<script setup>
import { onMounted } from 'vue'

const initMap = function () {
    const container = document.getElementById('map')
    const options = {
        center: new kakao.maps.LatLng(33.450701, 126.570667),
        level: 3
    }
    const map = new kakao.maps.Map(container, options)
}

onMounted(() => {
    initMap()
})

</script>

<style scoped>
#map {
    width: 500px;
    height: 400px;
}
</style>