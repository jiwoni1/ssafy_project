<template>
    <div class="detail-template">
        <h1 id="h1">상품 상세 정보</h1>
        <hr>
        <table class="table">
            <div v-for="saving in bankStore.savings">
                <div v-if="props.id == saving.id">
                    <tbody>
                        <tr>
                            <th scope="col">공시 제출월</th>
                            <td>{{ saving.dcls_month }}</td>
                        </tr>
                        <br>
                        <br>
                        <tr>
                            <th scope="col">금융 회사명</th>
                            <td>{{ saving.kor_co_nm }}</td>
                        </tr>
                        <br>
                        <br>
                        <tr>
                            <th scope="col">상품명</th>
                            <td>{{ saving.fin_prdt_nm }}</td>
                        </tr>
                        <br>
                        <br>
                        <tr>
                            <th scope="col">가입 제한</th>
                            <td>{{ saving.join_deny }} (1:제한없음, 2:서민전용, 3:일부제한)</td>
                        </tr>
                        <br>
                        <br>
                        <tr>
                            <th scope="col">가입 대상</th>
                            <td>{{ saving.join_member }}</td>
                        </tr>
                        <br>
                        <br>
                        <tr>
                            <th scope="col">가입 방법</th>
                            <td>{{ saving.join_way }}</td>
                        </tr>
                        <br>
                        <br>
                        <tr v-if="saving.spcl_cnd">
                            <th scope="col">우대 조건</th>
                            <td>{{ saving.spcl_cnd }}</td>
                        </tr>
                        <br>
                        
                        <tr v-if="saving.ect_note">
                            <th scope="col">최고 금리</th>
                            <td>{{ saving.ect_note }}</td>
                        </tr>
                        <br>
                        <br>
                        <tr>
                            <th scope="col">저축 기간</th>
                            <td>{{ saving.savingoptions_set[0].save_trm }}</td>
                        </tr>
                        <br>
                        <br>
                        <tr>   
                            <th scope="col">저축 금리</th>
                            <td>{{ saving.savingoptions_set[0].intr_rate }}</td>
                        </tr>
                        <br>
                        <br>
                        <tr>
                            <th scope="col">최고 우대금리</th>
                            <td>{{ saving.savingoptions_set[0].intr_rate2 }}</td>
                        </tr>
                        <br>
                        <br>
                        <tr> 
                            <th>만기 후 이자율</th>
                            <td>{{ saving.mtrt_int }}</td>            
                        </tr>
                        <br>
                        <br>

                    </tbody>
                    <br>
                    <button v-if="articleStore.isLogin" @click="addSavingProduct(saving)" class="btn btn-outline-success btn-lg" id="btn">가입하기</button>
                </div>
            </div>
        </table>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useBankStore } from '@/stores/bank'
import { useArticleStore } from '@/stores/article'

const bankStore = useBankStore()
const articleStore = useArticleStore()
const router = useRouter()

// 버튼 토글하기
// const toggleText = ref('가입하기')


const props = defineProps({
    id: String,
})

// console.log(router.params.id)

// 장바구니 기능
const addSavingProduct = (saving) => {
    const existingProduct = JSON.parse(localStorage.getItem('saving')) || []
    // 중복 확인
    const isDuplicate = existingProduct.length > 0 && existingProduct.find((item) => item.id === saving.id)

    // 중복이 아니라면 추가
    // 버튼 토글
    if(!isDuplicate) {
        alert('해당 상품에 가입합니다.')
        existingProduct.push(saving)
    } else {
        alert('이미 가입된 상품입니다.')
    }


    // 수정된 카트 데이터를 localStorage에 저장
    localStorage.setItem('saving', JSON.stringify(existingProduct))

    // router.push({ name: 'addProduct' })
}


</script>

<style scoped>
.detail-template {
    padding: 5% 15%;
}

#h1 {
    color: rgb(102, 175, 102);
    font-weight: bold;
}

tr > th {
    width: 20%;
    text-align: center;
    color: rgb(81, 81, 81);
}

tr > td {
    color: rgb(89, 89, 89);
}

.table {
    margin: 5% 0px 2%;
}

#btn {
    color : rgb(102, 175, 102);
    float :right;
}

</style>