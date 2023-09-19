<!-- 抽签算命模版 -->
<template>
  <div class="chat-list" :class="screenWidth <= 900 ? 'mb' : ''">
    <div class="answer">
      <div class="BotHeader">
        <img
          class="avatar"
          :class="screenWidth <= 900 ? 'mbImg' : ''"
          src="/@/assets/images/aibot.png"
          alt=""
        />
        <div v-if="screenWidth <= 900">天机阁</div>
      </div>
      <div class="record-content">
        <div class="allContent">
          <div class="top">
            <div class="leftPart">
              <!-- <img :src="presetData.imgUrl" alt="" /> -->
              <div class="text">
                <span class="titleDispaly">{{
                  subTitle(presetData[0].title)[0] + '，'
                }}</span>
                <span>{{ subTitle(presetData[0].title)[1] }}</span>
              </div>
            </div>
          </div>
          <div class="fortune-content">
            <!-- <div class="part1">
              <div>{{ presetData.content }}</div>
            </div> -->
            <div class="part1">
              <div v-for="(item, index) in presetData" :key="index">
                <div v-if="index != 0" class="tittle">{{ item.title }}</div>
                <div v-if="index != 0" v-html="turnString(item.content)"></div>
              </div>
              <!-- <div v-for="(item, index) in list.contents" :key="index">
                          <div>{{ item.title }}</div>
                          <div v-html="item.content">
                          </div>
                      </div> -->
            </div>
          </div>
        </div>
        
        <div class="xiangyun"></div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, watch } from 'vue'
import { useStore } from 'vuex'
export default {
  name: '',
  props: {
    presetData: {
      type: Object,
      default: null,
    },
  },
  setup(props) {
    const store = useStore()
    //适配
    const screenWidth = computed(() => {
      return store.state.screenWidth
    })
    const presetData = ref(null)
    watch(
      () => props.presetData,
      (newValue, oldValue) => {
        presetData.value = newValue
      },
    )
    presetData.value = props.presetData
    console.log(presetData.value)
    return {
      presetData,
      screenWidth,
    }
  },
  components: {},
  methods: {
    turnString(str) {
      if (str.indexOf('<br/>') == 0) {
        console.log(str + '  6666   ' + str.indexOf('<br/>'))
        const str1 = str.substring(5)
        return str1
      } else {
        return str
      }
    },
    subTitle(val) {
      let arr = val.split('，')
      return arr
    },
  },
  mounted() {},
  unmounted() {},
}
</script>

<style scoped lang="scss">
.chat-list {
  text-align: left;
  display: flex;
  margin-top: 0.3rem;
  &.right-content {
    justify-content: flex-end;
  }
  .question,
  .answer {
    display: flex;
    width: calc(100% - 1rem);
    img,
    .img {
      width: 0.8rem;
      height: 0.8rem;
    }
    .text-content {
      flex: 1;
      min-height: 1rem;
      box-sizing: border-box;
      display: flex;
      align-items: center;
      .inner {
        padding: 0.25rem 0.4rem;
        font-size: 12px;
        line-height: 16px;
        font-family: Poppins-Regular, Poppins;
      }
    }
    .record-content {
      width: 100%;
      padding: 0.6rem 0.4rem;
      margin-left: 0.1rem;
      background: linear-gradient(270deg, #341b00 0%, #140b00 100%);
      color: #ffefdd;
      border-radius: 0.1rem 0.25rem 0.25rem 0.25rem;
      position: relative;
      .xiangyun {
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
      .top {
        display: flex;
        justify-content: space-between;
        .leftPart {
          display: flex;
          justify-content: flex-start;
          align-items: center;
          background: #311e00;
          border-radius: 0.907rem;
          padding: 5px;
          .titleDispaly {
            color: #ff9900;
          }
          .text {
            // margin: 0 0.2rem;
          }
        }
      }
      .fortune-content {
        font-size: 0.259rem;
        color: #ffefdd;
        p {
          margin: 0.2rem 0;
        }
        .part1 {
          margin-top: 0.5rem;
        }
        .tittle {
          color: #ff9900;
          margin-top: 0.27rem;
          span {
            color: #ffefdd;
          }
        }
        .yellow {
          color: #ff9900;
        }
        .jianshu {
          margin: 0.2rem 0;
        }
      }
    }
  }
  .allContent{
      &.mb {
        .answer {
          display: block;
          width: 98%;
          .BotHeader {
            display: flex;
            align-items: center;
            color: #000000;
            img {
              margin-right: 0.2rem;
              &.mbImg {
                width: 0.5rem;
                height: 0.5rem;
              }
            }
          }
          .record-content {
            margin-top: 0.2rem;
          }
        }
      }    
    }
 
}
</style>
