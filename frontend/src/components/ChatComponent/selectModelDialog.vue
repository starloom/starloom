<template>
    <div class="selectmoudel-box" :class="screenWidth<=800 ? 'mb-login-box' : ''">
      <el-dialog
        v-model="show"
        :show-close="false"
        :before-close="handleClose"
        :close-on-click-modal="false"
        :width="screenWidth<=800 ? '85%' :'400px'"
        center
        >
        <!-- <template #header="{ close }">
            <div class="close" @click="close">
              <img src="/@/assets/images/closeDialog.png" alt="">
            </div>
        </template> -->
        <div class="cont">
          <div class="text">{{ $t('selectModel') }}</div>
          <div class="reasonbox">
            <ul>
              <li class="moudel_li" @click="changeModel('3.5')" :class="userModel=='3.5'? 'greenBorder' : ''">
                <div class="allCont">
                  <div class="topmaxDiv">
                    <div class="top_div">
                      <div class="left">
                        <template v-if="userModel=='3.5'">
                          <img class="moudelchoose_green" src="/@/assets/images/moudelchoose_green.svg" alt="">
                          <div class="choosetext activeGreen">{{ $t('selected') }}</div>
                        </template>
                        <template v-else>
                          <img  class="moudelchoose_grey" src="/@/assets/images/moudelchoose_grey.svg" alt="">
                          <div class="choosetext">{{ $t('select') }}</div>
                        </template>
                      </div>
                      <div class="right green">
                        {{ $t('limitedTimeFree') }}
                      </div>
                    </div>
                  </div>
                  <div class="bottomdiv " :class="userModel=='3.5'? 'active' : ''">   
                    <div class="modelType">{{ $t('basic') }}</div>
                  </div>
                </div>
                <div class="xiangyunBox">
                  <img v-if="userModel=='3.5'" src="/@/assets/images/xiangyun_green.svg" alt="">
                  <img v-else src="/@/assets/images/xiangyun_white.svg" alt="">
                </div>
              </li>
              <li class="moudel_li" @click="changeModel('4')" :class="userModel=='4'? 'yellowBorder' : ''">
                <div class="allCont">
                  <div class="topmaxDiv">
                    <div class="top_div">
                      <div class="left">
                        <template v-if="userModel=='4'">
                          <img class="moudelchoose_green" src="/@/assets/images/moudelchoose_yellow.svg" alt="">
                          <div class="choosetext activeYellow">{{ $t('selected') }}</div>
                        </template>
                        <template v-else>
                          <img  class="moudelchoose_grey" src="/@/assets/images/moudelchoose_grey.svg" alt="">
                          <div class="choosetext">{{ $t('select') }}</div>
                        </template>
                      </div>
                      <div class="right yellow">
                        {{ $t('limited2Free') }}
                      </div>
                    </div>
                  </div>
                  <div class="bottomdiv " :class="userModel=='4'? 'active' : ''">
                    <div class="modelType">{{ $t('plus') }}</div>
                    <div class="btn" v-if="userModel=='4'" @click="SubscribeOpen">
                      {{ $t('subscribe') }}
                    </div>
                  </div>             
                </div>
                <div class="xiangyunBox">
                  <img v-if="userModel=='4'" src="/@/assets/images/xiangyun_yellow.svg" alt="">
                  <img v-else src="/@/assets/images/xiangyun_white.svg" alt="">
                </div>
              </li>
            </ul>
          </div>
          <div class="bottom">
            <div class="closeBtn" @click="handleClose">
              {{ $t('enterToChat') }}
            </div>
          </div>
        </div>

      </el-dialog>
    </div>
    <!-- <SubscribeType 
      :subscribeDialog="subscribeDialog"
    /> -->
  </template>
  
  <script>
  import { ref, computed, watch } from 'vue';
  import { useStore} from 'vuex'
  import { useI18n } from 'vue-i18n'
  import EventBus from '/@/utils/EventBus.js'
  import SubscribeType from '/@/components/ChatComponent/SubscribeType.vue'
  
  export default {
    name: 'Login',
    props:['showModelDialog'],
    setup(props) {
      const store = useStore()
      const { t } = useI18n();
      const show = ref(props.showModelDialog)
      //适配
      const screenWidth = computed( () => {
        return store.state.screenWidth
      })
      const lang = computed(() => {
        return store.state.lang
      })
      const userModel = computed(() => {
        return store.state.userModel
      })
      // const subscribeDialog = ref(false)
      const changeModel = (modelType)=>{
        store.commit('setUserModel',modelType)
        localStorage.setItem('userModel',modelType)
      }
      const SubscribeOpen = () =>{
        EventBus.$emit('goSubscribe')
      }
     return {
      show: show,
      screenWidth,
      changeModel,
      // subscribeDialog,
      // goSubscribe,
      userModel,
      SubscribeOpen,
     } 
    },
    components: {
      SubscribeType,
    },
    watch: {
      'showModelDialog'(a){
        this.show = a  
      },
    },
    methods: {
      handleClose(done){
        this.show = false
        // this.$emit('closeModelDialog','closeModelDialog')
      },
    },
    mounted() {
      
    },
    unmounted() {
      
    },
  }
  </script>
  
  <style scoped lang='scss'>
  
  .selectmoudel-box{
    font-family: Poppins-Regular, Poppins;
    color: #000000;
    :deep(.el-dialog) {
      background: linear-gradient(180deg, #FFFBF5 0%, #FFF0D9 100%) !important;
      box-shadow: none;
      border-radius: 40px;
    }
    :deep(.el-overlay-dialog)  {
      backdrop-filter: blur(5px);
    }
    :deep(.el-dialog__header ){
      padding: 0.2rem 0; 
      padding-bottom: 0; 
      margin-right: 0; 
      height: 0;
      position: relative;
    }
    // :deep( .el-dialog--center .el-dialog__body ){ 
    //   padding-top: 0px;
    // }
      .close{
        width: .5rem;
        height: .5rem;
        z-index: 1114;
        position: absolute;
        right: 15px;
        // top: 60px;
        cursor: pointer;
        img{
          width: 100%;
        }
      }
      .cont{
        .text{
          text-align: left;
          font-size: .44rem;
          color: #000000;
        }
        .reasonbox{
          margin-top: .4rem;
          
          ul{ 
           .moudel_li{
            background: rgba(255,255,255,0.49);
            border-radius: .37rem;
            opacity: 1;
            position: relative;
            margin-bottom: .3rem;
            &.greenBorder{
              border: 2px solid #199D3E;
              background: #EAFFD9;
            }
            &.yellowBorder{
              border: 2px solid #BC5A00;
              background: linear-gradient(180deg, #FFFBF5 0%, #FFF0D9 100%);
            }
            .allCont{
             
              z-index: 1111;
              padding: .2rem;
              cursor: pointer;
              .topmaxDiv{
                position: absolute;
                z-index: 1111;
                padding: .2rem;
                top: 0;
                left: 0;
                height: .5rem;
                width: 100%;
                .top_div{
                  display: flex;
                  justify-content: space-between;
                  align-items: center;
                }
                .left{
                  display: flex;
                  justify-content: space-around;
                  align-items: center;
                 
                  img{
                    margin-right: -.3rem;
                    z-index: 1;
                    &.moudelchoose_green{
                      width: .6rem;
                    }
                    &.moudelchoose_grey{
                      width: .5rem;
                    }
                  }

                  .choosetext{
                    background: #FFFFFF;
                    border: 1px solid #ECECEC;
                    height: .45rem;
                    padding: 0 .3rem 0  0.4rem;
                    border-radius: .3rem;
                    line-height: .45rem;
                    color: #AAAAAA;
                    &.activeGreen{
                      border: 1px solid transparent;
                      color: #1E7F39;
                    }
                    &.activeYellow{
                      border: 1px solid transparent;
                      color: #E78B00;
                    }
                  }
                }
                .right{
                  border-radius: .22rem;
                  opacity: 1;
                  line-height: .5rem;
                  height: .5rem;
                  padding: 0 .2rem;
                  &.green{
                    border: 1px solid #04DB00;
                    background: #A2FFBC;
                    color: #007737;
                    white-space: nowrap;
                  }
                  &.yellow{
                    color: #7E6200;
                    border: 1px solid #FFAB2C;
                    background: #FFDA7D;
                  }
                }
              }
              .bottomdiv{
                font-size: 0.49rem;
                font-family: Poppins-Bold, Poppins;
                font-weight: bold;
                color: #A3A3A3;
                height: 100%;
                position: relative;
                z-index: 1112;
                // position: absolute;
                // padding: .2rem;
                // top: 0;
                // left: 0;
                // height: .5rem;
                width: 100%;
                .modelType{
                  height: 0.9rem;
                  // line-height: 1.35rem;
                  text-align: center;
                  display: flex;
                  justify-content: center;
                  align-items: center;
                  margin-top: .45rem;
                }
                &.active{
                  color: #000000;
                }
              }
              .btn{
                background: linear-gradient(87deg, #FFC56C 0%, #FFD38E 100%);
                margin-top: .05rem;
                color: #5D441D;
                text-align: center;
                height: .9rem;
                line-height: .9rem;
                border-radius: .37rem;
                font-size: .34rem;
              }
            }
            .xiangyunBox{
              position: absolute;
              top: 0;
              left: 0;
              width: 100%;
              padding: 0.2rem;
              // height: 1.75rem;
              // padding: .2rem;
              img{
                // width: 50%;
                height: 1.35rem;
              }
            }
           }
          }
        }
      }
      .bottom{
        margin-top: .2rem;
        .closeBtn{
          background: #130A00;
          color: #FFFFFF;
          text-align: center;
          line-height: 1rem;
          border-radius:.3rem ;
          font-size: .35rem;
          cursor: pointer;
        }
      }

    &.mb-login-box{
      font-size: .22rem;
      :deep(.el-dialog) {
      }
      .close{
        // width: .54rem;
        // height: .54rem;
        position: absolute;
        right: 15px;
        // top: 35px;
        cursor: pointer;
      }

    }
  }
  </style>
