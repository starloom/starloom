<!-- 币种预测 页面显示预设 -->
<template>
  <div class="crypto">
    <!-- <div class="normal-box">
        <div class="list" v-for="(item,index) in normalList" :key="index" @click="cryptoInfo(item)">
          <PresetItem :logo="item.logo" :text="item.text" />
        </div>
    </div>
    <div class="line">
        PLUS function
    </div>
    <div class="vip-box">
        <div class="list" v-for="(item,index) in vipList" :key="index">
          <PresettVip :text="item.text"/>
        </div>
      </div> -->
  </div>
</template>

<script>
import { ref, computed, watch } from 'vue';
import { useStore} from 'vuex'
import EventBus from '/@/utils/EventBus.js'
import { useRouter } from 'vue-router'

export default {
  name: '',
  setup() {
    const router = useRouter()
    const cryptoInfo = (item)=> {
      router.push({ name: 'chat' })
      setTimeout(() => {
        EventBus.$emit('sendMessage', item.text,{type:item.type,code:'bitcoin'})
      },500)
    }
    return {
      cryptoInfo,
      normalList: [
          {
            logo: 'https://transfer.swft.pro/swft-v3/images/coins/BTC.png',
            text:'Price analysis and data breakdown of BTC',
            type:'preset1'
          },
          {
            logo: 'https://transfer.swft.pro/swft-v3/images/coins/BTC.png',
            text:"BTC's online exchanges, wallets, and supported chains, as well as data on the chain",
            type:'preset2'

          },
          {
            logo: 'https://transfer.swft.pro/swft-v3/images/coins/BTC.png',
            text:'BTC Investment Institutions and Social Media Details',
            type:'preset3'

          },
        ],
        vipList:[
          {
              text: 'AI Price Forecast'
          }
        ]
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
.normal-box,.vip-box{
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  .list{
    width: 30%;
    margin-bottom: .3rem;
  }
}
.line{
  font-size: .3333rem;
  font-family: Poppins-Bold, Poppins;
  font-weight: bold;
  color: #FFFFFF;
  padding: .8rem 0;
}
</style>