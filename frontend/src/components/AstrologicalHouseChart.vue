<!-- 宫位查询 -->
<template>
    <div class="chat-list" :class="screenWidth<=900 ? 'mb' : ''">
      <div class="answer">
            <div class="BotHeader">
              <img class="avatar" :class="screenWidth<=900 ? 'mbImg' : ''" src="/@/assets/images/aibot.png" alt="">
              <div v-if="screenWidth<=900">天机阁</div>
            </div>
            <div class="record-content">
                <div class="allContent">
                    <div class="text-content">
                        <div class="part">
                            <div class="yellowfont">测算者信息: </div>
                            <div>公历生日：{{ presetData[0].gongli }}</div>
                            <div>农历生日：{{ presetData[0].nongli  }}</div>
                            <div>岁数：今年{{ presetData[0].age  }}岁</div>
                            <div>星座：{{ presetData[0].xingzuo  }}座</div>
                            <div>属相：{{ presetData[0].zodiac  }}</div>
                            <div>性别：{{ presetData[0].sex  }}</div>
                        </div>
                    </div>
                    <div class="tab-content">
                        <div class="tab-box">
                            <ul>
                                <!-- <li class="" @click="changeHouseTab('weizhi')" :class="houseTab == 'weizhi' ? 'li-active' : '' ">行星位置</li> -->
                                <li @click="changeHouseTab('shiergong')" :class="houseTab == 'shiergong' ? 'li-active' : '' ">十二宫位内行星</li>
                                <li @click="changeHouseTab('weizhi')" :class="houseTab == 'weizhi' ? 'li-active' : '' ">行星位置</li>
                            </ul>
                            <div class="table-max">
                                <div class="table-shiergong" v-if="houseTab=='shiergong'">
                                    <div class="tr">
                                        <!-- <div class="th">宫头度数</div> -->
                                        <div class="th item1">宫位</div>
                                        <div class="th">行星</div>
                                    </div>
                                    <div class="tr t-body" v-for="(item, index) in presetData[1].housePlanet" :key="index">
                                        <!-- <div class="td">
                                            <img class="xingzuo-img" src="https://cdnsm.leyunge.com/Public/static/mobile/images/xx0.png" alt="">
                                            摩羯座
                                            <div class="degree yellowfont"> 10°28′</div>
                                        </div> -->
                                        
                                        <div class="td item1">{{ item.house }}</div>
                                        <div class="td">
                                            <div class="group" v-for="(item1, index1) in item.planets" :key="index1">
                                                <img class="sun-img" :src="item1.imgUrlYellow" alt="">
                                                {{ item1.name }}
                                            </div>
                                            <!-- <div class="group">
                                                <img class="sun-img" src="https://cdnsm.leyunge.com/Public/static/mobile/images/xx0.png" alt="">
                                                太阳
                                            </div>
                                            <div class="group">
                                                <img class="sun-img" src="https://cdnsm.leyunge.com/Public/static/mobile/images/xx0.png" alt="">
                                                太阳
                                            </div>
                                            <div class="group">
                                                <img class="sun-img" src="https://cdnsm.leyunge.com/Public/static/mobile/images/xx0.png" alt="">
                                                太阳
                                            </div> -->
                                            
                                        </div>
                                    </div>
                                    <!-- <div class="tr t-body">
                                        
                                        <div class="td item1">10宫</div>
                                        <div class="td">
                                            <div class="group">
                                                <img class="sun-img" src="https://cdnsm.leyunge.com/Public/static/mobile/images/xx0.png" alt="">
                                                太阳
                                            </div>
                                        </div>
                                    </div>
                                    <div class="tr t-body">
         
                                        
                                        <div class="td item1">10宫</div>
                                        <div class="td">
                                            <div class="group">
                                                <img class="sun-img" src="https://cdnsm.leyunge.com/Public/static/mobile/images/xx0.png" alt="">
                                                太阳
                                            </div>
                                            <div class="group">
                                                <img class="sun-img" src="https://cdnsm.leyunge.com/Public/static/mobile/images/xx0.png" alt="">
                                                太阳
                                            </div>
                                            <div class="group">
                                                <img class="sun-img" src="https://cdnsm.leyunge.com/Public/static/mobile/images/xx0.png" alt="">
                                                太阳
                                            </div>
                                        </div>
                                    </div> -->

                                </div>
                                <!-- <div class="table-xingxiang"  v-if="houseTab=='weizhi'">
                                    <div class="tr">
                                        <div class="th item1">行星</div>
                                        <div class="th">相位</div>
                                    </div>
                                    <div class="tr t-body">
                                        <div class="td item1">
                                            <img class="sun-img" src="https://cdnsm.leyunge.com/Public/static/mobile/images/xx0.png" alt="">
                                            太阳
                                        </div>
                                        <div class="td">冲木星、合土星、合天王星、合海王星、合天顶、刑上升点</div>
                                    </div>
                                    <div class="tr t-body">
                                        <div class="td item1">
                                            <img class="sun-img" src="https://cdnsm.leyunge.com/Public/static/mobile/images/xx0.png" alt="">
                                            太阳
                                        </div>
                                        <div class="td">六合火星、六合上升点</div>
                                    </div>
                                    <div class="tr t-body">
                                        <div class="td item1">
                                            <img class="sun-img" src="https://cdnsm.leyunge.com/Public/static/mobile/images/xx0.png" alt="">
                                            太阳
                                        </div>
                                        <div class="td">冲木星、合土星、合天王星、合海王星、合天顶、刑上升点</div>
                                    </div>

                                </div> -->
                                <div class="table-xingwei" v-if="houseTab=='weizhi'">
                                    <div class="tr">
                                        <div class="th">行星</div>
                                        <div class="th">行星度数</div>
                                        <div class="th r">宫位</div>
                                    </div>
                                    <div class="tr t-body" v-for="(item, index) in presetData[1].planetPosition" :key="index">
                                        <div class="td">
                                            <img class="sun-img" :src="item.planet.imgUrlYellow" alt="">
                                            {{ item.planet.name }}
                                        </div>
                                        <div class="td">
                                            <img class="xingzuo-img" :src="item.constellationDegrees.imgUrl" alt="">
                                            <!-- 摩羯座 -->
                                            <div class="degree yellowfont">{{ item.constellationDegrees.name }}</div>
                                        </div>
                                        <div class="td r">{{ item.house }}</div>
                                    </div>
                                    <!-- <div class="tr t-body">
                                        <div class="td">
                                            <img class="sun-img" src="https://cdnsm.leyunge.com/Public/static/mobile/images/xx0.png" alt="">
                                            太阳
                                        </div>
                                        <div class="td">
                                            <img class="xingzuo-img" src="https://cdnsm.leyunge.com/Public/static/mobile/images/xx0.png" alt="">
                                            摩羯座
                                            <div class="degree yellowfont"> 10°28′</div>
                                        </div>
                                        <div class="td">10宫</div>
                                    </div>
                                    <div class="tr t-body">
                                        <div class="td">
                                            <img class="sun-img" src="https://cdnsm.leyunge.com/Public/static/mobile/images/xx0.png" alt="">
                                            太阳
                                        </div>
                                        <div class="td">
                                            <img class="xingzuo-img" src="https://cdnsm.leyunge.com/Public/static/mobile/images/xx0.png" alt="">
                                            摩羯座
                                            <div class="degree yellowfont"> 10°28′</div>
                                        </div>
                                        <div class="td">10宫</div>
                                    </div> -->
                                </div>
                            </div>
                        </div>
                        <div class="img-box">
                            <img :src="presetData[1].astrolabeImgUrl" alt="" srcset="">
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
  // 分割
  const queList =  [{"gongli": "1998年3月9日", "nongli": "1998年2月11日", "age": 25, "zodiac": "虎", "xingzuo": "双鱼", "sex": "男"}, {"astrolabeImgUrl": "https://www.smxs.com/Public/xingpan/44729956ac7952f0e57154896a416e9c.png", "housePlanet": [{"house": "1宫", "planets": [{"name": "冥王星", "imgUrl": "https://images.swft.pro/astroAI/planet/mingwangxing.png", "imgUrlYellow": "https://images.swft.pro/astroAI/planet/mingwangxing-yellow.png"}, {"name": "上升点", "imgUrl": "https://images.swft.pro/astroAI/planet/Asc.png", "imgUrlYellow": "https://images.swft.pro/astroAI/planet/Asc-yellow.png"}]}, {"house": "3宫", "planets": [{"name": "金星", "imgUrl": "https://images.swft.pro/astroAI/planet/jinxing.png", "imgUrlYellow": "https://images.swft.pro/astroAI/planet/jinxing-yellow.png"}, {"name": "天王星", "imgUrl": "https://images.swft.pro/astroAI/planet/tianwangxing.png", "imgUrlYellow": "https://images.swft.pro/astroAI/planet/tianwangxing-yellow.png"}, {"name": "海王星", "imgUrl": "https://images.swft.pro/astroAI/planet/haiwangxing.png", "imgUrlYellow": "https://images.swft.pro/astroAI/planet/haiwangxing-yellow.png"}]}, {"house": "4宫", "planets": [{"name": "太阳", "imgUrl": "https://images.swft.pro/astroAI/planet/taiyang.png", "imgUrlYellow": "https://images.swft.pro/astroAI/planet/taiyang-yellow.png"}, {"name": "水星", "imgUrl": "https://images.swft.pro/astroAI/planet/shuixing.png", "imgUrlYellow": "https://images.swft.pro/astroAI/planet/shuixing-yellow.png"}, {"name": "火星", "imgUrl": "https://images.swft.pro/astroAI/planet/huoxing.png", "imgUrlYellow": "https://images.swft.pro/astroAI/planet/huoxing-yellow.png"}, {"name": "木星", "imgUrl": "https://images.swft.pro/astroAI/planet/muxing.png", "imgUrlYellow": "https://images.swft.pro/astroAI/planet/muxing-yellow.png"}]}, {"house": "5宫", "planets": [{"name": "土星", "imgUrl": "https://images.swft.pro/astroAI/planet/tuxing.png", "imgUrlYellow": "https://images.swft.pro/astroAI/planet/tuxing-yellow.png"}]}, {"house": "8宫", "planets": [{"name": "月亮", "imgUrl": "https://images.swft.pro/astroAI/planet/yueliang.png", "imgUrlYellow": "https://images.swft.pro/astroAI/planet/yueliang-yellow.png"}]}, {"house": "10宫", "planets": [{"name": "天顶", "imgUrl": "https://images.swft.pro/astroAI/planet/MC.png", "imgUrlYellow": "https://images.swft.pro/astroAI/planet/MC-yellow.png"}]}], "planetPosition": [{"planet": {"name": "太阳", "imgUrl": "https://images.swft.pro/astroAI/planet/taiyang.png", "imgUrlYellow": "https://images.swft.pro/astroAI/planet/taiyang-yellow.png"}, "constellationDegrees": {"name": "双鱼座17°52′", "imgUrl": "", "imgUrlYellow": ""}, "house": "4宫"}, {"planet": {"name": "月亮", "imgUrl": "https://images.swft.pro/astroAI/planet/yueliang.png", "imgUrlYellow": "https://images.swft.pro/astroAI/planet/yueliang-yellow.png"}, "constellationDegrees": {"name": "巨蟹座27°27′", "imgUrl": "", "imgUrlYellow": ""}, "house": "8宫"}, {"planet": {"name": "水星", "imgUrl": "https://images.swft.pro/astroAI/planet/shuixing.png", "imgUrlYellow": "https://images.swft.pro/astroAI/planet/shuixing-yellow.png"}, "constellationDegrees": {"name": "白羊座0°34′", "imgUrl": "", "imgUrlYellow": ""}, "house": "4宫"}, {"planet": {"name": "金星", "imgUrl": "https://images.swft.pro/astroAI/planet/jinxing.png", "imgUrlYellow": "https://images.swft.pro/astroAI/planet/jinxing-yellow.png"}, "constellationDegrees": {"name": "水瓶座3°5′", "imgUrl": "", "imgUrlYellow": ""}, "house": "3宫"}, {"planet": {"name": "火星", "imgUrl": "https://images.swft.pro/astroAI/planet/huoxing.png", "imgUrlYellow": "https://images.swft.pro/astroAI/planet/huoxing-yellow.png"}, "constellationDegrees": {"name": "白羊座3°4′", "imgUrl": "", "imgUrlYellow": ""}, "house": "4宫"}, {"planet": {"name": "木星", "imgUrl": "https://images.swft.pro/astroAI/planet/muxing.png", "imgUrlYellow": "https://images.swft.pro/astroAI/planet/muxing-yellow.png"}, "constellationDegrees": {"name": "双鱼座7°43′", "imgUrl": "", "imgUrlYellow": ""}, "house": "4宫"}, {"planet": {"name": "土星", "imgUrl": "https://images.swft.pro/astroAI/planet/tuxing.png", "imgUrlYellow":"https://images.swft.pro/astroAI/planet/tuxing-yellow.png"}, "constellationDegrees": {"name": "白羊座18°57′", "imgUrl": "", "imgUrlYellow": ""}, "house": "5宫"}, {"planet": {"name": "天王星", "imgUrl": "https://images.swft.pro/astroAI/planet/tianwangxing.png", "imgUrlYellow": "https://images.swft.pro/astroAI/planet/tianwangxing-yellow.png"}, "constellationDegrees": {"name": "水瓶座10°51′", "imgUrl": "", "imgUrlYellow": ""}, "house": "3宫"}, {"planet": {"name": "海王星", "imgUrl": "https://images.swft.pro/astroAI/planet/haiwangxing.png", "imgUrlYellow": "https://images.swft.pro/astroAI/planet/haiwangxing-yellow.png"}, "constellationDegrees": {"name": "水瓶座1°18′", "imgUrl": "", "imgUrlYellow": ""}, "house": "3宫"}, {"planet": {"name": "冥王星", "imgUrl": "https://images.swft.pro/astroAI/planet/mingwangxing.png", "imgUrlYellow": "https://images.swft.pro/astroAI/planet/mingwangxing-yellow.png"}, "constellationDegrees": {"name": "射手座8°3′", "imgUrl": "", "imgUrlYellow": ""}, "house": "1宫"}, {"planet": {"name": "上升点", "imgUrl": "https://images.swft.pro/astroAI/planet/Asc.png", "imgUrlYellow": "https://images.swft.pro/astroAI/planet/Asc-yellow.png"}, "constellationDegrees": {"name": "天蝎座25°52′", "imgUrl": "", "imgUrlYellow": ""}, "house": "1宫"}, {"planet": {"name": "天顶", "imgUrl": "https://images.swft.pro/astroAI/planet/MC.png", "imgUrlYellow": "https://images.swft.pro/astroAI/planet/MC-yellow.png"}, "constellationDegrees": {"name": "处女座5°19′", "imgUrl": "", "imgUrlYellow": ""}, "house": "10宫"}]}]
  const houseTab = ref('weizhi')
  return {
      presetData,
      queList,   //分割
      houseTab,
      screenWidth,
  } 
},
components: {
},
methods: {
    changeHouseTab(type){
        this.houseTab = type
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
      .avatar{
          width: .8rem;
          height: .8rem;
      }
      .record-content{
          width: 100%;
          padding: 0.6rem .4rem;
          margin-left: .1rem;
          background: linear-gradient(270deg, #341B00 0%, #140B00 100%);
          color: #ffefdd;
          border-radius: 0.1rem 0.25rem 0.25rem 0.25rem;
          position: relative;
          .yellowfont{
            color: #FF9900;
          }
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
          .text-content{
            font-size: 0.259rem;
            color: #d8d3d3;
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
          .tab-content{
            padding: 1rem 0;
            color: #ffefdd;
            z-index: 1111;
            position: relative;
            display: flex;
            justify-content: space-between;

                .tab-box{
                    width: 60%;
                    ul{
                        display: flex;
                        justify-content: flex-start;
                        align-items: center;
                        li{
                            padding: 0 0.2rem 0.2rem;
                            margin-right: 0.3rem;
                            cursor: pointer;
                            &.li-active{
                                border-bottom: 3px solid #894900;
                                color: #FFFFFF;
                            }
                        }
                    }
                    .table-max{
                        .table-xingwei,.table-shiergong{
                         .tr{
                            display: flex;
                            justify-content: flex-start;
                            align-items: center;
                            &.t-body{
                                margin-bottom: 0.2rem;
                            }
                            .th{
                                line-height: 1rem;
                                width: 33.33%;
                            }
                            .td{
                                display: flex;
                                align-items: center;
                                justify-content: flex-start;
                                width: 33.33%;
                            }
                            .sun-img{
                                width: 0.5rem;
                                height: 0.5rem;
                                margin-right: 0.05rem;
                            }
                            .xingzuo-img{
                                width: 0.4rem;
                                height: 0.4rem;
                                margin-right: 0.1rem;
                            }
                            .degree{
                                margin-left: 0.1rem;
                            }
                            .group{
                                margin-right: .25rem;
                            }
                         }
                        }
                        .table-shiergong{
                            white-space: nowrap;
                            .tr{
                                justify-content: flex-start;
                                .item1{
                                    width: 18%;
                                }

                            }
                        }
                    }
                }
                .img-box{
                    width: 40%;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    img{
                        border-radius: 50%;
                        margin-top: 0.5rem;
                        width: 80%;
                        // height: 7rem;
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
        .tab-content{
            display: block;
            .tab-box{
                width: 100%;
                .table-xingwei{
                    .tr{
                        .r{
                            text-align: right;
                        }
                        &.t-body{
                            .r{
                                justify-content: flex-end;
                            }
                        }
                    }
                }
            }
            .img-box{
                width: 100%;
            }
        }
      }
    }
  }
}
</style>