<!-- 星座运势 -->
<template>
      <div class="chat-list" :class="screenWidth<=900 ? 'mb' : ''">
        <div class="answer">
            <div class="BotHeader">
              <img class="avatar" :class="screenWidth<=900 ? 'mbImg' : ''" src="/@/assets/images/aibot.png" alt="">
              <div v-if="screenWidth<=900">天机阁</div>
            </div>
              <div class="record-content">
                <div class="allContent">
                  <div class="top">
                    <div class="leftPart">
                        <img :src="presetData.imageUrl" alt="">
                        <div class="text">{{ presetData.title }}</div>
                    </div>
                    <div class="rightPart">
                      <div class="item" @click="changeTab(0)" :class="tab==0? 'active' : ''">今日运势</div>
                      <div class="item" @click="changeTab(1)" :class="tab==1? 'active' : ''">明日运势</div>
                      <div class="item" @click="changeTab(2)" :class="tab==2? 'active' : ''">本周运势</div>
                      <div class="item" @click="changeTab(3)" :class="tab==3? 'active' : ''">本月运势</div>
                      <div class="item" @click="changeTab(4)" :class="tab==4? 'active' : ''">今年运势</div>
                    </div>
                  </div>
                  <div class="fortune-content">
                    <div class="part1">
                      <div v-for="(item, index) in presetData.yunshi" :key="index">
                        <div>{{ item.title }}： <span>{{ item.content }}</span></div>
                      </div>
                    </div>
                    <div class="part1">
                      <div v-for="(item, index) in presetData.describe" :key="index">
                        <div>{{ item.title }}</div>
                        <div>{{ item.content }}</div>
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
    index:{
        type: Number,
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
    const index = ref(null)
    watch(() => props.index, (newValue, oldValue) => {
      index.value = newValue
    })
    index.value = props.index
    const tab = ref(0)
    // const changeTab = (item) =>{
    //    tab.value = item
    // }
    return {
        presetData,
        tab,
        index,
        screenWidth,
    } 
  },
  components: {
  },
  methods: {
    changeTab(item){
       this.tab = item
       const obj = {
        que: this.presetData.question,
        tab: item,
        index: this.index,
      }
       this.$emit('chageTab', obj)
    },
    
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
              justify-content: space-between;
              .leftPart{
                display: flex;
                justify-content: flex-start;
                align-items: center;
                background: #311E00;
                border-radius: 0.907rem;
                .text{
                  margin: 0 .2rem;
                }
              }
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
            }
        }
    }
    .question{
        .text-content{
            justify-content: flex-end;
            .inner{
                margin-right: .1rem;
                background: #00FF66;
                border-radius: .25rem .1rem  .25rem  .25rem;
                color: #000000;
            }
        }
        
    }
    .answer{
        .text-content{
            .inner{
                margin-left: 0.1rem;
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
          .top{
            display: block;
            .rightPart{
              margin-top: .3rem;
              overflow: hidden;
              overflow-x: auto;
              &::-webkit-scrollbar {
                display: none !important;
              }
              .item{
                white-space:nowrap;
                padding: 0;
                width: 20%;
                margin: 0 0.1rem;
              }
            }
          }
        }
      }
    }
}
</style>