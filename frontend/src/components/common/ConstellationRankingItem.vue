<!-- 预设1 -->
<template>
    <div class="chat-list" :class="screenWidth<=900 ? 'mb' : ''">
      <div class="answer">
            <div class="BotHeader">
              <img class="avatar" :class="screenWidth<=900 ? 'mbImg' : ''" src="/@/assets/images/aibot.png" alt="">
              <div v-if="screenWidth<=900">天机阁</div>
            </div>
            <div class="record-content">
              <div class="ranking-list">
                <div class="item-list" v-for='(item, index) in presetData' :key="index">
                    <div class="img-box">
                        <img :src="item.imgUrl" alt="">
                    </div>
                    <div>
                        <div class="Q">{{ item.name }}</div>
                        <div>{{ index+1 }}</div>
                        <!-- <div>{{ item.votesNum }}票</div> -->
                    </div>
                </div>
              </div>
              <div class="xiangyun"></div>
            </div>
        </div>
  </div>
</template>

<script>
import { ref, computed, watch } from 'vue';
import { useStore} from 'vuex'
export default {
name: '',
props:{
  presetData:{
      type: Object,
      default: null
  },
},
setup(props) {
  const store = useStore()
  //适配
  const screenWidth = computed( () => {
    return store.state.screenWidth
  })
  const presetData = ref(null)
  watch(() => props.presetData, (newValue, oldValue) => {
      presetData.value = newValue
  })
  presetData.value = props.presetData
  return {
      presetData,
      screenWidth,
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
.chat-list{
  text-align: left;
  display: flex;
  margin-top: .3rem;
  &.right-content{
  justify-content: flex-end;
  }
  .question,.answer{
      display: flex;
      width: calc(100% - 1rem);
      align-items: flex-start;
      img,.img{
          width: .8rem;
          height: .8rem;
      }
      .text-content{
          flex: 1;
          min-height: 1rem;
          box-sizing: border-box;
          display: flex;
          align-items: center;
          .inner{
              padding: .25rem .4rem;
              font-size: 12px;
              line-height: 16px;
              font-family: Poppins-Regular, Poppins;
          }
      }
      .record-content{
          width: 100%;
          padding: 0.7rem .4rem;
          margin-left: .1rem;
          background: linear-gradient(270deg, #341B00 0%, #140B00 100%);
          color: #ffefdd;
          border-radius: 0.1rem 0.25rem 0.25rem 0.25rem;
          position: relative;
          .xiangyun{  
              position: absolute;
              background: url(/@/assets/images/xiangyun.svg) no-repeat 100% 80%;
              top: 0;
              left: 0;
              width: 100%;
              height: 100%;
              background-size: contain;
          }
          .ranking-list{
             font-size: 0.259rem;
            display: flex;
            justify-content: space-between;
            z-index: 1111;
            position: relative;
            .item-list{
                display: flex;
                flex-direction: column;
                font-family: Inter-Regular, Inter;
                font-size: 0.222rem;
                text-align: center;
                align-items: center;
                .img-box{
                    width: .8148rem;
                    height: .8148rem;
                }
                .Q{
                    margin-bottom: .185rem;
                    line-height: .559rem;
                }
            }
          }
      }
  }
  &.mb{
    font-size: .22rem;
    .answer{
      display: block;
      width: 98%;
      .BotHeader{
        display: flex;
        align-items: center;
        color: #000000;
        img{
          margin-right: .2rem;
          &.mbImg{
            width: .5rem;
            height: .5rem;
          }
        }
      }
      .record-content{
        margin-top: .2rem;
        .ranking-list{
          flex-wrap: wrap;
          justify-content: flex-start;
          .item-list{
            width: 16.66%;
            margin-bottom: .4rem;
          }
        }
      }
    }
  }
}
</style>