<!-- 月亮星座 -->
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
                    <div v-for="(item, index) in presetData[1].contents" :key="index">
                        <div class="tittle">{{ item.title }}</div>
                        <div v-html="item.content"></div>
                    </div> 

                    <!-- <div>你的月亮星座是“<span class="yellow">巨蟹座</span>"</div>  
                    <div class="tittle">性格特点：</div>            
                    <div>月亮的正面特征特别强烈，很能照顾别人，深具同情心;对家庭欢念甚强，家庭与婚姻的保障非常重要。感觉敏锐，想象力丰富，情绪化。小心不要太依赖别人，并且避免太顽固。如果相位不佳，会有溺爱孩子的情况发生。</div>
                    <div class="tittle">行为模式：</div>
                    <div>月亮落入巨蟹座，代表此人和自己及他人内心的那个脆弱、需要抚慰、好依赖的婴儿，有紧密的联结。他们本身也需要别人的滋养和保护。</div>
                    <div class="tittle">才能：</div>
                    <div>月亮星座巨蟹座的人能体会到别人的感觉，而且直觉地知道该如何让别人安适和舒服，甚至连小狗小猫的脆弱易感，他们也都感受得到。月亮星座巨蟹座的人通常有高度的想象力，可以应用在艺术和文学的追求上。对往事的关注，令他们在历史和文化遗产上面特别有研究才能。他们也善于烹饪。</div>
                    <div class="tittle">外形特征：</div>               
                    <div>额头、嘴唇线条优美。 动作缓慢，大都为丰满型，但身材比例匀称，而且声音浑厚，肤质较好。</div>
                    <div class="tittle">外型：</div>
                    <div>宽肩、厚背，脖子略粗，骨架结实，手掌柔，厚实，腿部结实有力，宽臀重心低，行动缓和，看起来十分稳健，整体印象是丰满的脂肪型，却十分性感。</div>
                    <div class="tittle">容貌：</div>
                    <div>鼻子略短不露骨，嘴唇偏厚而敏感，脸颊丰满，头发细软发线低，眼神安定柔和，中年之后会有发福的现象，可能会出现双下巴。 声音低沉而明亮，十分悦耳。</div>
                    <div class="tittle">气质：</div>               
                    <div>沉默、宁静、诚恳、脚踏实地，不容易在快节奏的竞争行列中生存，成年之后对于理财投资很有概念。</div>
                    <div class="tittle">行事风格：</div>
                    <div>你有温暖大方的天性，因此能用轻松的态度去处理事情，从而能发散出镇静优雅的味道。 你行动谨慎，因此完成工作的进度相对会很稳定，自己的精力也不会白白浪费，而且能收到实质的成效。</div>
                    <div class="tittle">上升星座金牛座性格特点：</div>
                    <div>性情更稳定，态度更平和，待人处事谨慎有礼。 火相太阳星座遇到上升金牛座，是完美的结合，金牛的耐心与细心可以调和火相星座的冲动、莽撞，而火相星座的动力与外向感性又能让金牛更活泼，更受人欢迎。 而土相太阳星座遇上升金牛座，非常内敛，做事更加细心，给人可靠、信赖之感，但也容易拘泥于细节问题，处事不够果决。</div>
                    <div v-for="(item, index) in list.contents" :key="index">
                        <div class="tittle">{{ item.title }}</div>
                        <div v-html="item.content">

                        </div>
                    </div> -->
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
            .yellow{
                color: #FF9900;
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
      }
    }
  }
  
}
</style>