<!-- 上升星座 -->
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
                     <div v-if="presetData[0].sex">性别：{{ presetData[0].sex  }}</div>
                </div>
                <div class="part1">
                    <div class="tittle">{{ presetData[1].title }}</div>
                    <div v-html="presetData[1].content"></div>
                    <!-- <div>上升位于金牛座：稳重、金钱、美食。</div>
                    <div>优点：务实，决断力，温柔。</div>
                    <div>上升代表：灵魂，外在行为，生活态度。</div>
                    <div>缺点：顽固，保守，自私。</div>

                    <div class="tittle">潜在特性：</div>               
                    <div>追求物质世界的美好、丰富与拥有。</div>
                    <div class="tittle">基本特质：</div>
                    <div>上升星落在金牛座的人给人的印象是淡泊宁静且稳重优雅。 对所有事都从容不迫，稳健而踏实。 喜欢稳定，任何的改变都会让你感觉不适应，对任何事情都表现出一种坚定不移的执着。</div>
                    <div class="tittle">具体特质：</div>
                    <div>上升星落入金牛座的你外表看起来很稳重，但内心却潜藏着顽固的意志。 你所喜欢的是自然的节奏，而不愿凡事都显得忙忙碌碌。 不过当你一旦着手做某一件事，就不是那么容易罢手。 你很固执，讨厌别人给你的一些忠告或建议，因此你会选择顽强抵抗别人所施加的压力。 你不会轻易的投入一段感情，一旦投入了，便会想要确定彼此稳定的关系，不做改变。 对金钱和美食的需求很强烈。</div>
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
                    <div>性情更稳定，态度更平和，待人处事谨慎有礼。 火相太阳星座遇到上升金牛座，是完美的结合，金牛的耐心与细心可以调和火相星座的冲动、莽撞，而火相星座的动力与外向感性又能让金牛更活泼，更受人欢迎。 而土相太阳星座遇上升金牛座，非常内敛，做事更加细心，给人可靠、信赖之感，但也容易拘泥于细节问题，处事不够果决。</div> -->
                    <!-- <div v-for="(item, index) in list.contents" :key="index">
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
            z-index: 1111;
            position: relative;
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