<!-- 星盘查询 -->
<template>
    <div class="chat-list">
      <div class="answer" :class="screenWidth<=900?'mb-answer' : ''">
        <div class="BotHeader">
          <img class="avatar" :class="screenWidth<=900 ? 'mbImg' : ''" src="/@/assets/images/aibot.png" alt="">
          <div v-if="screenWidth<=900">天机阁</div>
        </div>
            
            <div class="record-content">
                <div class="allContent"  :class="screenWidth<=900?'mb-all':''">
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
                    <div class="top" :class="screenWidth<=900?'mb-tab':''">
                        <div class="rightPart">
                        <div class="item" @click="changeTab('xp')" :class="tab == 'xp' ? 'active' : '' "> 星盘</div>
                        <div class="item" @click="changeTab('xxwz')" :class="tab == 'xxwz' ? 'active' : '' ">行星位置</div>
                        <div class="item" @click="changeTab('xxgw')" :class="tab == 'xxgw' ? 'active' : '' ">行星宫位</div>
                        <div class="item" @click="changeTab('xxxw')" :class="tab == 'xxxw' ? 'active' : '' ">行星相位</div>
                        </div>
                    </div>
                    <div class="tab-content">
                        <div class="xingpai" v-if="tab=='xp'"  :class="screenWidth<=900?'mb-xingpai' : ''">
                            <div class="tab-box">
                                <ul>
                                    <li class="" @click="changeAstTab('weizhi')" :class="astTab == 'weizhi' ? 'li-active' : '' ">行星位置</li>
                                    <li @click="changeAstTab('shiergong')" :class="astTab == 'shiergong' ? 'li-active' : '' ">十二宫位置</li>
                                    <li @click="changeAstTab('xiangwei')" :class="astTab == 'xiangwei' ? 'li-active' : '' ">行星相位</li>
                                </ul>
                                <div class="table-max">
                                    <div class="table-xingwei" v-if="astTab=='weizhi'">
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
                                                <div class="degree yellowfont"> {{ item.constellationDegrees.name }}</div>
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
                                    <div class="table-shiergong" v-if="astTab=='shiergong'">
                                        <div class="tr">
                                            <div class="th">宫头度数</div>
                                            <div class="th">宫主星</div>
                                            <div class="th r">宫位</div>
                                        </div>
                                        <div class="tr t-body" v-for="(item, index) in presetData[1].housePlanet" :key="index">
                                            <div class="td">
                                                <img class="xingzuo-img" :src="item.constellationDegrees.imgUrl" alt="">
                                                <!-- 摩羯座 -->
                                                <div class="degree yellowfont">{{ item.constellationDegrees.name }}</div>
                                            </div>
                                            <div class="td">
                                                <img class="sun-img" :src="item.planet.imgUrlYellow" alt="">
                                                {{ item.planet.name }}
                                            </div>
                                            <div class="td r">{{ item.house }}</div>
                                        </div>
                                        <!-- <div class="tr t-body">
                                            <div class="td">
                                                <img class="xingzuo-img" src="https://cdnsm.leyunge.com/Public/static/mobile/images/xx0.png" alt="">
                                                摩羯座
                                                <div class="degree yellowfont"> 10°28′</div>
                                            </div>
                                            <div class="td">
                                                <img class="sun-img" src="https://cdnsm.leyunge.com/Public/static/mobile/images/xx0.png" alt="">
                                                太阳
                                            </div>
                                            <div class="td">10宫</div>
                                        </div>
                                        <div class="tr t-body">
                                            <div class="td">
                                                <img class="xingzuo-img" src="https://cdnsm.leyunge.com/Public/static/mobile/images/xx0.png" alt="">
                                                摩羯座
                                                <div class="degree yellowfont"> 10°28′</div>
                                            </div>
                                            <div class="td">
                                                <img class="sun-img" src="https://cdnsm.leyunge.com/Public/static/mobile/images/xx0.png" alt="">
                                                太阳
                                            </div>
                                            <div class="td">10宫</div>
                                        </div> -->

                                    </div>
                                    <div class="table-xingxiang"  v-if="astTab=='xiangwei'">
                                        <div class="tr">
                                            <div class="th item1">行星</div>
                                            <div class="th">相位</div>
                                        </div>
                                        <div class="tr t-body" v-for="(item, index) in presetData[1].planetPhase" :key="index">
                                            <div class="td item1">
                                                <img class="sun-img" :src="item.planet.imgUrlYellow" alt="">
                                                {{ item.planet.name }}
                                            </div>
                                            <div class="td">{{ item.phase }}</div>
                                        </div>
                                        <!-- <div class="tr t-body">
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
                                        </div> -->

                                    </div>
                                </div>
                            </div>
                            <div class="img-box">
                                <img :src="presetData[1].astrolabeImgUrl" alt="" srcset="">
                            </div>
                        </div>
                        <!-- 行星位置 -->
                        <div class="xingxingweizhi" v-if="tab=='xxwz'">
                            <div class="planet-list">
                                <div class="item" v-for="(item, index) in presetData[1].planetPositionDescript" :key="index" @click="chagePlanetPosition(item)">
                                    <img v-if="item.planet == itemPlanetContent.planet" class="planet-img" :src="item.imgUrlYellow" alt="">
                                    <img v-else class="planet-img" :src="item.imgUrl" alt="">
                                    <div class="planet-text">{{ item.planet }}</div>
                                </div>
                            </div>
                            <div class="centerPart">
                                <div class="yellowfont">{{ itemPlanetContent.descript.title }}</div>
                                <div class="imgtext">
                                    <div class="item">
                                        <img class="planet-img" :src="itemPlanetContent.descript.direction[0].imgUrlYellow" alt="">
                                        <div class="planet-text yellowfont">{{ itemPlanetContent.descript.direction[0].name }}</div>
                                    </div>
                                
                                    <div class="jiantou">
                                        <img src="/@/assets/images/arrow-right.png" alt="">
                                    </div>
                                    <div class="item">
                                        <img class="planet-img" :src="itemPlanetContent.descript.direction[1].imgUrl" alt="">   
                                        <div class="planet-text yellowfont">{{ itemPlanetContent.descript.direction[1].name }}</div>
                                    </div>
                                </div>
                            </div>
                            <div class="bottomPart">
                                <div class="yellowfont">{{ itemPlanetContent.descript.basic.title }}</div>
                                <div>{{ itemPlanetContent.descript.basic.content }}</div>
                            </div>
                        </div>
                        <!-- 行星宫位 -->
                        <div class="xingxinggongwei" v-if="tab=='xxgw'">
                            <div class="planet-list">
                                <div class="item" v-for="(item, index) in presetData[1].housePlanetDescript" :key="index" @click="chageHousePlanet(item)">
                                    <img v-if="item.planet == itemHouseContent.planet" class="planet-img" :src="item.imgUrlYellow" alt="">
                                    <img v-else class="planet-img" :src="item.imgUrl" alt="">
                                    <div class="planet-text">{{ item.planet }}</div>
                                </div>
                            </div>
                            <div class="centerPart">
                                <div class="yellowfont">{{ itemHouseContent.descript.title }}</div>
                                <div class="imgtext">
                                    <div class="item">
                                        <img class="planet-img" :src="itemHouseContent.imgUrlYellow" alt="">
                                        <div class="planet-text yellowfont">{{ itemHouseContent.descript.direction[0] }}</div>
                                    </div>
                                
                                    <div class="jiantou">
                                        <img src="/@/assets/images/arrow-right.png" alt="">
                                    </div>
                                    <div class="item">
                                        <!-- <img class="planet-img" src="" alt="">   -->
                                        <div class="plant-numimg yellowfont">{{ itemHouseContent.descript.direction[2] }}</div> 
                                        <div class="planet-text yellowfont">{{ itemHouseContent.descript.direction[1] }}</div>
                                    </div>
                                </div>
                            </div>
                            <div class="bottomPart">
                                <div class="yellowfont">{{ itemHouseContent.descript.basic.title }}</div>
                                <div>{{ itemHouseContent.descript.basic.content }}</div>
                            </div>
                        </div>
                        <!-- 行星相位 -->
                        <div class="xingxingxiangwei" v-if="tab=='xxxw'">
                            <div class="planet-list">
                                <div class="item" v-for="(item, index) in presetData[1].planetPhaseDescript" :key="index" @click="chagePlanetPhase(item)">
                                    <div class="bigfont" :class="item.phase == itemPlanetPhaseContent.phase ? 'yellowfont' : ''">{{ item.phase == '六合' ? '六' : item.phase }}</div>
                                    <div class="text" :class="item.phase == itemPlanetPhaseContent.phase ? 'yellowfont' : ''">{{ item.phase }}</div>
                                </div>
                                <!-- <div class="item">
                                    <div class="bigfont">六</div>
                                    <div class="text">六合</div>
                                </div>
                                <div class="item">
                                    <div class="bigfont">刑</div>
                                    <div class="text">刑</div>
                                </div>
                                <div class="item">
                                    <div class="bigfont">供</div>
                                    <div class="text">供</div>
                                </div>
                                <div class="item">
                                    <div class="bigfont">冲</div>
                                    <div class="text">冲</div>
                                </div> -->
                            </div>
                            <div class="centerPart">
                                <div class="yellowfont">{{ itemPlanetPhaseContent.descript.title }}</div>
                                <div>{{ itemPlanetPhaseContent.descript.content }}</div>
                            </div>
                            <div class="bottomPart">
                                <div class="item" v-for="(item, index) in itemPlanetPhaseContent.descript.direction" :key="index">
                                    <div>
                                        <img class="planet-img" :src="item.imgUrlYellow" alt="">  
                                    </div>
                                    <div>
                                        {{ item.title }}
                                    </div>
                                </div>
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
  const presetData = ref(null)
  const itemPlanetContent = ref(null)
  const itemHouseContent = ref(null)
  const itemPlanetPhaseContent = ref(null)
  //适配
  const store = useStore()
  const screenWidth = computed( () => {
    return store.state.screenWidth
  })
  watch(() => props.presetData, (newValue, oldValue) => {
      presetData.value = newValue
      itemPlanetContent.value = newValue[1].planetPositionDescript[0]
      itemHouseContent.value = newValue[1].housePlanetDescript[0]
      itemPlanetPhaseContent.value = newValue[1].planetPhaseDescript[0]
  })
  presetData.value = props.presetData
  itemPlanetContent.value = props.presetData[1].planetPositionDescript[0]
  itemHouseContent.value = props.presetData[1].housePlanetDescript[0]
  itemPlanetPhaseContent.value = props.presetData[1].planetPhaseDescript[0]
  const astTab = ref('weizhi')
  const tab = ref('xp')
  return {
      presetData,
      astTab,
      tab,
      itemPlanetContent,
      itemHouseContent,
      itemPlanetPhaseContent,
      screenWidth,
  } 
},
components: {
},
methods: {
    changeAstTab(type){
        this.astTab = type
    },
    changeTab(type){
        this.tab = type
    },
    // 行星位置
    chagePlanetPosition(item){
        this.itemPlanetContent = item
    },
    // 行星宫位
    chageHousePlanet(item){
        this.itemHouseContent = item 
    },
    // 行星相位
    chagePlanetPhase(item){
        this.itemPlanetPhaseContent = item 
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
              width: auto;
              cursor: pointer;
              .item{
                // width: 23%;
                color: #ffefdd;
                padding: 0 .3rem;
                text-align: center;
                margin: 0 .15rem;
                border-radius: 0.222rem;
                box-shadow: 0px 4px 20px -6px rgba(0,0,0,0.15);
                // line-height: .685rem;
                height: .685rem;;
                display: flex;
                align-items: center;
                justify-content: center;
                flex: 1;
                white-space: nowrap;
                cursor: pointer;
                &.active{
                  background: #894900;
                  color: #FFFFFF;
                }
              }
            }
            &.mb-tab{
              justify-content: flex-start;
            }
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
            color: #ffefdd;
            z-index: 1111;
            position: relative;
            .xingpai{
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
                        .table-xingwei,.table-shiergong,.table-xingxiang{
                         .tr{
                            display: flex;
                            justify-content: space-between;
                            align-items: center;
                            &.t-body{
                                margin-bottom: 0.2rem;
                            }
                            .th{
                                line-height: 1rem;
                                width: 33.33%;
                            }
                            .td{
                                width: 33.33%;
                                display: flex;
                                align-items: center;
                                justify-content: flex-start;
                            }
                            .sun-img{
                                width: 0.5rem;
                                height: 0.5rem;
                                margin-right: 0.1rem;
                            }
                            .xingzuo-img{
                                width: 0.4rem;
                                height: 0.4rem;
                                margin-right: 0.1rem;
                            }
                            .degree{
                                margin-left: 0.1rem;
                            }
                         }
                        }
                        .table-xingxiang{
                            white-space: nowrap;
                            .tr{
                                justify-content: flex-start;
                                .item1{
                                    width: 28%;
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
                &.mb-xingpai{
                  display:inline-block;
                  .tab-box{
                    width: 100%;
                  }
                  .img-box{
                    width: 100%;
                  }
                }
            }
            .xingxingweizhi,.xingxinggongwei{
                .planet-list{
                    padding: .8rem 0;
                    display: flex;
                    justify-content: space-around;
                }
                .centerPart{
                    text-align: center;
                }
                .planet-img{
                    height: 0.8rem;
                    width: 0.8rem;
                    display: block;
                    cursor: pointer;
                }
                .plant-numimg{
                    height: 0.8rem;
                    line-height: 0.8rem;
                    cursor: pointer;
                    font-size: .75rem;
                }
                .planet-text{
                    line-height: .8rem;
                    text-align: center;
                    cursor: pointer;
                }
                .imgtext{
                    display: flex;
                    justify-content: center;
                    padding: 0.5rem 0;
                    // align-items: center;
                    .item{
                        margin: 0 0.8rem;
                        cursor: pointer;
                    }
                    .jiantou{
                        margin-top: 0.25rem;
                    }
                }
                
            }
            .xingxingxiangwei{
                .planet-list{
                    padding: .8rem 0;
                    display: flex;
                    justify-content: center;
                    .item{
                        margin:0 .4rem;
                        cursor: pointer;
                    }
                    .bigfont{
                        font-size: .8rem;
                    }
                    .text{
                        text-align: center;
                    }
                }
                .bottomPart{
                    margin-top: .48rem;
                    width: 60%;
                    display: flex;
                    flex-wrap: wrap;
                    .item{
                        display: flex;
                        justify-content: flex-start;
                        align-items: center;
                        margin-bottom: .44rem;
                        width: 50%;
                    }
                    .planet-img{
                        width: .8rem;
                        margin-right: .11rem;
                    }
                }
            }
          }
      }
      .allContent{
        &.mb-all{
          font-size: .22rem;
          .rightPart{
              margin-top: .4rem;
              width: 100%;
              .item{
                padding: 0;
              }
          }
          .tab-box{
            ul{
              margin-top: .4rem;
            }
            .table-max{
              .table-xingwei,.table-shiergong{

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
          }
          .tab-content{
            .planet-list{
              flex-wrap: wrap;
              justify-content: flex-start;
              .item{
                width: 16%;
                margin-bottom: .3rem;
                .planet-img{
                  margin: 0 auto;
                }
              
              }
            }
            .xingxingxiangwei{
              .planet-list{
                flex-wrap: nowrap;
                justify-content:space-between;
              }
            }
            .bottomPart{
              width: 100%;
            }
          }
        }
      }
      &.mb-answer{
        display: block;
        width: 99%;
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
          width: 99%;
        }
      }
  }
}
</style>