<!-- 相关问题 -->
<template>
  <div class="RelatedQuestions">
    <div class="title">
        {{ $t('Relatedquestions') }}
    </div>
    <div class="question-list">
        <div class="list">什么是Bitcoin?</div>
        <div class="list">Bitcoin的团队有哪些?</div>
        <div class="list">比特币的投资机构有哪些?</div>
        <div class="list">比特币可以支持的钱包有哪些?</div>
        <div class="list">目前市面上最受欢迎的加密货币有哪些?</div>
        <div class="list">现在比特币的市场趋势?</div>
    </div>
  </div>
</template>

<script>
import { ref, computed, watch } from 'vue';
import { useStore} from 'vuex'

export default {
  name: 'RelatedQuestions',
  setup() {
   return {
    
   } 
  },
  components: {
    
  },
  methods: {
    
  },
  mounted() {
    
  },
  unmounted() {
    
  },
}
</script>

<style scoped lang='scss'>
.RelatedQuestions{
    width: 100%;
    background: #1C1E1F;
    border-radius: .37rem;
    padding: 0.25rem 0.4rem;
    .title{
        margin-top: .3rem;
        font-size: .3rem;
        font-family: Poppins-Bold, Poppins;
        font-weight: bold;
        color: #FFFFFF;
    }
    .question-list{
        margin-top: .2rem;
        .list{
            line-height: 1rem;
            cursor: pointer;
            font-size: .256rem;
            font-family: Inter-Medium, Inter;
            font-weight: 500;
            color: #FFFFFF;
            &:hover{
                color: #777777;
            }
        }
    }
}
</style>