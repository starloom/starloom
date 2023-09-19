<!-- 下降星座 -->
<template>
    <div class="chat-list" :class="screenWidth<=900 ? 'mb' : ''">
      <div class="answer">
            <div class="BotHeader">
              <img class="avatar" :class="screenWidth<=900 ? 'mbImg' : ''" src="/@/assets/images/aibot.png" alt="">
              <div v-if="screenWidth<=900">天机阁</div>
            </div>
            <div class="record-content">
              <div class="fortune-content">
                <div class="part">
                    <div class="yellowfont">测算者信息: </div>
                    <div>公历生日：{{ presetData[0].gongli }}</div>
                    <div>农历生日：{{ presetData[0].nongli  }}</div>
                    <div>岁数：今年{{ presetData[0].age  }}岁</div>
                    <div>星座：{{ presetData[0].xingzuo  }}座</div>
                    <div>属相：{{ presetData[0].zodiac  }}</div>
                    <div v-if="presetData[0].sex">性别：{{ presetData[0].sex }}</div>
                </div>
                <div class="part1">
                    <div class="tittle">{{ presetData[1].title }}</div>
                    <div v-html="presetData[1].content"></div>
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
          padding: 0.6rem .4rem;
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
          .fortune-content{
             font-size: 0.259rem;
            color: #ffefdd;
            .part1{
              margin-top: .5rem;
            }
            .tittle{
                color: #FF9900;
                margin-top: .27rem;
                span{
                    color: #ffefdd;
                }
            }
          }
      }
  }
  &.mb{
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
      }
    }
  }
}
</style>