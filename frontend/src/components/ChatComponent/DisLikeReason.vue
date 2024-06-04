<template>
    <div class="disloke-box" :class="screenWidth<=800 ? 'mb-login-box' : ''">
      <el-dialog
        v-model="show"
        :show-close="false"
        :before-close="handleClose"
        :width="screenWidth<=800 ? '80%' :'470px'"
        center
        >
        <!-- <template #header="{ close }">
            <div class="close" @click="close">
              <img src="/@/assets/images/closeDialog.png" alt="">
            </div>
        </template> -->
        <div class="cont">
          <div class="text">{{ $t('feedbackTip') }}</div>
          <div class="reasonbox">
            <ul>
              <li @click="chooseReason(2)">
                <img src="/@/assets/images/Inaccurate.png" alt="" srcset="">
                {{ $t('inaccurate') }}
              </li>
              <li @click="chooseReason(3)">
                <img src="/@/assets/images/useless.png" alt="" srcset="">
                {{ $t('unhelpful') }}
              </li>
              <li @click="chooseReason(4)">
                <img src="/@/assets/images/Aggression.png" alt="" srcset="">
                {{ $t('offensive') }}
              </li>
              <!-- <li>
                <img src="/@/assets/images/otgerRea.png" alt="" srcset="">
                其他
              </li> -->
            </ul>
          </div>
          <div class="bottom">
            <div class="closeBtn" @click="handleClose">
              {{ $t('close') }}
            </div>
          </div>
        </div>

      </el-dialog>
    </div>
  </template>
  
  <script>
  import { ref, computed, watch } from 'vue';
  import { useStore} from 'vuex'
  import { useI18n } from 'vue-i18n'
  import EventBus from '/@/utils/EventBus.js'
  
  export default {
    name: 'Login',
    props:['disLikeDialog','likeItemObj'],
    setup(props) {
      const store = useStore()
      const { t } = useI18n();
      const show = ref(props.disLikeDialog)
      const obj = ref(props.likeItemObj)
      //适配
      const screenWidth = computed( () => {
        return store.state.screenWidth
      })
      const lang = computed(() => {
        return store.state.lang
      })
     return {
      show: show,
      screenWidth,
      obj,
     } 
    },
    components: {
    },
    watch: {
      'likeItemObj'(a){
        this.obj = a  
      },
      'disLikeDialog'(a){
        this.show = a  
      },

    },
    methods: {
      handleClose(done){
        this.show = false
        this.$emit('closeDisLike','closeDisLike')
      },
      chooseReason (type){
        EventBus.$emit('likeHandle', type, this.obj)
        this.handleClose()
      },
     
    },
    mounted() {
      
    },
    unmounted() {
      
    },
  }
  </script>
  
  <style scoped lang='scss'>
  
  .disloke-box{
    // .maxbg{
    //   position: absolute;
    //   top: 0;
    //   left: 0;
    //   width: 100%;
    //   height: 100%;
    //   img{
    //     width: 100%;
    //     height: 100%;
    //   }
    // }
    :deep(.el-dialog) {
      background-color: #FFF1D9 !important;  
      // background: url(/@/assets/images/LoginBg_zh.png) no-repeat 100% 100%;
      // height: 389px;
      // background-size: contain;
      box-shadow: none;
      border-radius: 10px;
    }
    :deep(.el-overlay-dialog)  {
      backdrop-filter: blur(5px);
    }
    :deep(.el-dialog__header ){
      padding: 0.2rem;
      padding-bottom: 0.2rem;
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
        color: #000;
        .text{
          text-align: center;
        }
        .reasonbox{
          margin-top: .4rem;
          
          ul{
            display: flex;
            justify-content: space-between;
            align-items: center;
            li{
              // height: 1.388rem;
              border: 2px solid #D9C5A1;
              width: 28%;
              // margin: 0 3.5%;
              border-radius: .37rem;
              text-align: center;
              cursor: pointer;
              padding: 0.1rem;
              img{
                display: block;
                margin: 0 auto;
                width: .862rem;
                margin-bottom: .1rem;
              }

            }
          }
        }
      }
      .bottom{
        border-top: 2px solid #D9C5A1;
        // height: 1.1rem;
        padding-top: .4rem;
        margin-top: .6rem;
        .closeBtn{
          background: #130A00;
          color: #FFFFFF;
          text-align: center;
          line-height: .9rem;
          border-radius:.629rem ;
          font-size: .35rem;
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
