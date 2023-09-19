<!-- 星座查询 -->
<template>
    <div class="chat-list" :class="screenWidth<=900 ? 'mb' : ''">
      <div class="answer">
            <div class="BotHeader">
              <img class="avatar" :class="screenWidth<=900 ? 'mbImg' : ''" src="/@/assets/images/aibot.png" alt="">
              <div v-if="screenWidth<=900">天机阁</div>
            </div>
            <div class="record-content">
              <div class="allContent">
                <div class="fortune-content">
                  <div class="part">
                    <div class="yellowfont">测算者信息: </div>     
                    <div>公历生日：{{ presetData[0].gongli }}</div>
                    <div>农历生日：{{ presetData[0].nongli  }}</div>
                    <div>岁数：今年{{ presetData[0].age  }}岁</div>
                    <div>星座：{{ presetData[0].xingzuo  }}座</div>
                    <div>属相：{{ presetData[0].zodiac  }}</div>
                  </div>
                  <div class="top">
                      <div class="rightPart">
                          <div class="item" @click="changeTab(0)" :class="tab==0? 'active' : ''">简介</div>
                          <div class="item" @click="changeTab(1)" :class="tab==1? 'active' : ''">神化传说</div>
                          <div class="item" @click="changeTab(2)" :class="tab==2? 'active' : ''">开运水晶</div>
                          <div class="item" @click="changeTab(3)" :class="tab==3? 'active' : ''">男生性格</div>
                          <div class="item" @click="changeTab(4)" :class="tab==4? 'active' : ''">女生性格</div>
                          <div class="item" @click="changeTab(5)" :class="tab==5? 'active' : ''">男生爱情</div>
                          <div class="item" @click="changeTab(6)" :class="tab==6? 'active' : ''">女生爱情</div>
                      </div>
                  </div>
                  <div class="part1">
                      <div class="tittle" v-if="tab==0 ||  tab==1 || tab==5">{{ presetData[1][tab].title }}</div>   <!-- <span>（6月22日-7月22日）</span> -->
                      <div v-if="tab==0" v-html="presetData[1][tab].content"></div>
                      <div v-for="(item, index) in presetData[1][tab].contents" :key="index">
                          <div class="tittle">{{ item.title }}</div>
                          <div v-html="item.content"></div>
                      </div>
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
  const tab = ref(0)
  const changeTab = (item) =>{
       tab.value = item
    }
  return {
      presetData,
      tab,
      changeTab,
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
          .allContent{
            z-index: 1111;
            position: relative;
          }
          .top{
            display: flex;
            justify-content: flex-end;
            .rightPart{
              background: #120900;
              display: flex;
              justify-content: space-around;
              align-items: center;
              border-radius: 0.222rem;
              height: .907rem;
              .item{
                color: #ffefdd;
                padding: 0 .3rem;
                text-align: center;
                margin: 0 .2rem;
                border-radius: 0.222rem;
                box-shadow: 0px 4px 20px -6px rgba(0,0,0,0.15);
                // line-height: .685rem;
                height: .685rem;;
                display: flex;
                align-items: center;
                justify-content: center;
                cursor: pointer;
                &.active{
                  background: #894900;
                  color: #FFFFFF;
                }
              }
            }
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
        .rightPart{
          margin-top: .3rem;
          width: 100%;
          overflow: hidden;
          overflow-x: auto;
          justify-content: flex-start;
          &::-webkit-scrollbar {
            display: none !important;
          }
          .item{
            white-space:nowrap;
            padding: 0 0.1rem;
            // width: 20.28%;
            margin: 0 0.05rem;
          }
        }
      }
    }
  }
}
</style>