<template>
    <div class="subscribe-box" :class="screenWidth<=800 ? 'mb-login-box' : ''">
      <el-dialog
        v-model="show"
        :show-close="false"
        :before-close="handleClose"
        :width="screenWidth<=800 ? '85%' :'500px'"
        center
        >
        <!-- <template #header="{ close }">
            <div class="close" @click="close">
              <img src="/@/assets/images/closeDialog.png" alt="">
            </div>
        </template> -->
        <div class="maxbox">
          <div class="cont">
            <div class="text">{{ $t('chooseSubscriptionType') }}</div>
            <div class="contBox">
              <div class="advantages">
                <div>{{ $t('subscribeSloganTittle') }}</div>
                <!-- <span class="fontYellow">16% </span> 的折扣。 -->
              </div>
              <ul class="advantagesBox">
                <li>
                  <img src="/@/assets/images/duigou_green.svg" alt="">
                  {{ $t('subscribeSlogan1') }}
                </li>
                <li>
                  <img src="/@/assets/images/duigou_green.svg" alt="">
                  {{ $t('subscribeSlogan2') }}
                </li>
                <li>
                  <img src="/@/assets/images/duigou_green.svg" alt="">
                  {{ $t('subscribeSlogan3') }}
                </li>
                <li>
                  <img src="/@/assets/images/duigou_green.svg" alt="">
                  {{ $t('subscribeSlogan4') }}
                </li>
              </ul>
              <ul class="type_ul">
                <li class="ci" v-for="(item, index) in paylist.slice(0, 2)" :key="index" @click="chooseCardTypeHandle(item)" :class="user_card_type?.card_type == item.card_type ? 'active' : ''">
                  <div class="left">
                    {{ item.time }}{{ item.time==1? $t('Time1') : $t('Times15')}}  {{ $t('unlimited') }}
                    <span class="fontYellow">{{ item.real_price }} </span> 
                    <span class="originalPrice">￥{{ item.display_price }}</span>
                  </div>
                  <div class="right" v-if="item.discount_description">
                    {{ $t('limitedTime30') }}
                  </div>
                </li>
              </ul>
              <ul class="cycleType_ul">
                <li class="cycle" v-for="(item1, index1) in paylist.slice(2, 5)" :key="index1" @click="chooseCardTypeHandle(item1)" :class="user_card_type?.card_type == item1.card_type ? 'active' : ''">
                  <div class="topbox">
                    <div class="card">{{ item1.card_name }}</div>
                    <div class="cishu">{{item1.time}} {{  $t('Times15') }}</div>
                  </div>
                  <div class="price">￥{{ item1.real_price }} <span class="originalPrice">￥{{ item1.display_price }}</span></div>
                </li>
              </ul> 
            </div>
            <div class="bottom">
              <div class="closeBtn" @click="PaymentMethod">
              {{ plus ? $t('renewal'): $t('subscribe')  }}
              </div>
            </div>
          </div>
          <div class="PulsBGBox">
            <img src="/@/assets/images/PLUS.svg" alt="" srcset="">
          </div>
        </div>
      

      </el-dialog>
    </div>

  </template>
  
  <script>
  import { ref, computed, watch } from 'vue';
  import { useStore} from 'vuex'
  import { useI18n } from 'vue-i18n'
  // import express from 'express'
  import stripe from 'stripe';
  import EventBus from '/@/utils/EventBus.js'
  import BigNumber from 'bignumber.js'
  
  export default {
    name: 'Login',
    props:['subscribeDialog','isPlus','paytypelist'],
    setup(props) {
      const store = useStore()
      const { t } = useI18n();
      const account = computed(() => store.state.account)
      const show = ref(props.subscribeDialog)
      const plus = ref(props.isPlus)
      const paylist = ref(props.paytypelist)
      //适配
      const screenWidth = computed( () => {
        return store.state.screenWidth
      })
      const lang = computed(() => {
        return store.state.lang
      })
      const user_card_type = ref(null)
      const chooseCardTypeHandle = (item)=>{
        user_card_type.value = item
      }
    
     return {
      show: show,
      screenWidth,
      paylist,
      user_card_type,
      chooseCardTypeHandle,
      plus,
      account,
     } 
    },
    components: {
    },
    watch: {
      'subscribeDialog'(a){
        this.show = a  
      },
      'isPlus'(a){
        this.plus = a  
      },
      'paytypelist'(a){
        this.paylist = a  
        this.user_card_type = this.paylist[1]
      },
    },
    methods: {
      handleClose(done){
        this.show = false
        this.$emit('closeSubscribeDialog','closeSubscribeDialog')
      },
      async PaymentMethod (){
        if(!this.user_card_type) return
        let url
        if(location.href.indexOf('defi.swftcoin.com') != -1){
          url = 'https://defi.swftcoin.com/view/astroai_web-test/index.html#/'
        } else if(location.href.indexOf('starloom.ai') != -1 || location.href.indexOf('tianjige') != -1 ){
          url = 'https://starloom.ai//#/'
        } else{
          url = 'http://192.168.124.3:5173/#/'
        }
        // const express = require('express');
        // const app = express();
        const currentTimestampInSeconds = Math.floor(Date.now() / 1000);
        const halfHourLaterTimestampInSeconds = currentTimestampInSeconds + 30 * 60; // 30分钟 * 60秒
        const stripeInstance = stripe('');

        // app.post('/create-checkout-session', async (req, res) => {
          const session = await stripeInstance.checkout.sessions.create({
            payment_method_types: ['card'],  // 'alipay', 'wechat_pay'
            payment_method_options: {
              wechat_pay: {
                client: 'web'
              }
            },
            expires_at: halfHourLaterTimestampInSeconds,
            customer_email: this.account,
            payment_intent_data: {
                metadata: {
                    'source': 'stripe',
                    'email': this.account,
                    'productCats': this.user_card_type.card_type, // 卡类型：1-1次；2-15次；3-月卡；4-季卡；5-年卡
                    'platform': 'starloom',
                    'userId': Number(localStorage.getItem('userId')),
                }
            },
            line_items: [{
              price_data: {
                currency: 'cny',
                product_data: {
                  name: this.user_card_type.card_name,
                },
                unit_amount: BigNumber(this.user_card_type.real_price ).multipliedBy(100).toNumber(),//this.user_card_type.real_price 
              },
              quantity: 1,
            }],
            mode: 'payment',
            success_url: `${url}?paystatus=success`,
            cancel_url: `${url}?paystatus=fail`,
          });
          console.log(JSON.stringify(session))
          location.href=session.url
          // res.sendStatus(200);
        // });
        // app.listen(4242, () => console.log(`Listening on port ${4242}!`));
      },
    },
    mounted() {
    //  this.getPayCardInfoList()
    },
    unmounted() {
      
    },
  }
  </script>
  
  <style scoped lang='scss'>
  
  .subscribe-box{
    font-family: Poppins-Regular, Poppins;
    color: #000000;
    :deep(.el-dialog) {
      background: linear-gradient(180deg, #FFFAF3 0%, #FFF0D9 100%)!important;
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
      .maxbox{
        position: relative;
        .PulsBGBox{
          position: absolute;
          right: 0.3rem;
          top: .47rem;
        }
      }
      .cont{
        .text{
          text-align: left;
          font-size: .44rem;
          color: #000000;
        }
        .contBox{
          margin-top: .4rem;
          color: #000000;
          .fontYellow{
            color: #FF5C00;
            font-weight:bold ;
            font-family: Poppins-SemiBold, Poppins;
          }
          .advantages{
            font-family: Roboto-Medium, Roboto;
            font-weight: 500;
            font-size: .32rem;
            margin-bottom: .2rem;
          }
          .advantagesBox{
            li{
              font-family: Roboto-Medium, Roboto;
              font-weight: 500;
              font-size: .32rem;
              margin-bottom: .2rem;
              display: flex; 
              justify-content: flex-start; 
              align-items: flex-start;
              img{
                margin-right: .15rem;
              }

            }
          }
          .type_ul{
            .ci{
              background: #FFF7EC;
              border-radius: .74rem;
              display: flex;
              justify-content: space-between;
              align-items: center;
              padding: .2rem;
              font-size: .35rem;
              // height: .8rem;
              margin-bottom: .15rem;
              .right{
                background: #FF5C00;
                padding: 0 .3rem;
                font-family: Roboto-Bold, Roboto;
                font-weight: bold;
                color: #FFFFFF;
                height: .6rem;
                line-height: .6rem;
                border-radius: .4rem;
                white-space: nowrap;
              }
              .originalPrice{
                font-family: Roboto-Medium, Roboto;
                font-weight: 500;
                color: #352000;
                text-decoration-line: line-through;
                font-size: .24rem;
                margin-left: .1rem;
              }
              &.active{
                border: 1px solid #FF5C00;
                background: #ffffff;
              }
            } 
          }
          .cycleType_ul{
            display: flex;
            justify-content: space-between;
            align-items: center;
            .cycle{
              background: #FFF7EC;
              padding: .2rem;
              border-radius: .3rem;
              width: 32%;
              &.active{
                border: 1px solid #FF5C00;
                background: #ffffff;
              }
              .topbox{
                display: flex;
                align-items: center;
                justify-content: space-between;
                margin-bottom: .2rem;
                .card{
                  font-size: .32rem;
                }
                .cishu{
                  color: #878787;
                }
              }
            }
            .price{
              font-size: .3rem;
              font-family: Poppins-SemiBold, Poppins;
              display: flex;
              align-items: center;
              justify-content:flex-start;
              span{
                color: #878787;
                text-decoration-line: line-through;
                font-size: .24rem;
                margin-left: .1rem;
              }
            }
          }
        }
      }
      .bottom{
        margin-top: .2rem;
        .closeBtn{
          background: linear-gradient(87deg, #FFC56C 0%, #FFD38E 100%);
          text-align: center;
          line-height: 1rem;
          border-radius:.3rem ;
          font-size: .35rem;
          font-weight: bold;
          color: #5D441D;
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
