<template>
    <div class="chat-list" :class="screenWidth<=900 ? 'mb' : ''">
      <div class="answer">
            <div class="BotHeader 111">
              <img class="avatar" :class="screenWidth<=900 ? 'mbImg' : ''" src="/@/assets/images/aibot.png" alt="">
              <div v-if="screenWidth<=900">{{ $t('starloom') }}</div>
            </div>
            <div class="record-content">
              <div class="fortune-content">
                <div>{{ $t('selectBirthTip') }}</div>
                <div class="dateTimeMaxDiv">
                  <div class="flexDiv" v-if="navQueryType.type=='hypd'"  :class="screenWidth<=550? 'flexWrap':''">
                    <div class="nameBox" v-if="navQueryType.type=='hypd'">
                      <div :class="lang=='en'?'textdiv':''"> {{ $t('femaleName')  }}：</div>
                      <div class="inputDiv" :class="screenWidth<=550? 'width100':''" >
                        <input v-model="femaleName" type="text" class="nameInput" :placeholder="$t('pleaseEnterfemaleName')">
                      </div>
                    </div>
                    <div class="birthBox">
                      <div :class="lang=='en'? 'dateTextDiv':''"> {{  $t('femaleGregorianBirthdate') }}：</div>
                      <div class="dateTimeDiv">
                          <div class="datePicker">
                            <el-config-provider :locale="locale">
                              <el-date-picker
                                  v-model="dateVal2"
                                  type="date"
                                  :placeholder="$t('selectDate')"
                                  :size="small"
                                  prefix-icon=""
                                  value-format="YYYY-MM-DD"
                                  :disabled-date="disabledDate"
                              />
                            </el-config-provider>
                          </div>
                          <div class="timePicker">
                            <el-config-provider :locale="locale">
                              <el-time-picker 
                              v-model="timeVal2" 
                              :placeholder="$t('selectTime')"
                              format="HH:mm"
                              value-format="HH-mm"
                              />
                            </el-config-provider>
                          </div>
                      </div>
                    </div>
                  </div>  
                  <div class="bottomDiv">
                    <div class="flexDiv" :class="screenWidth<=550? 'flexWrap':''">
                        <div class="nameBox" v-if="navQueryType.type=='hypd'">
                          <div :class="lang=='en'?'textdiv':''"> {{ $t('maleName')  }}：</div>
                          <div class="inputDiv" :class="screenWidth<=550? 'width100':''">
                            <input v-model="maleName" type="text" class="nameInput" :placeholder="$t('pleaseEnterMaleName')" >
                          </div>
                        </div>
                        <div class="birthBox">
                          <div :class="navQueryType.type=='hypd' && lang=='en'? 'dateTextDiv':''" > {{ navQueryType.type=='hypd' ? $t('maleGregorianBirthdate') : $t('gregorianBirthdate')}}：</div>
                          <div class="dateTimeDiv">
                            <div class="datePicker">
                              <el-config-provider :locale="locale">
                                <el-date-picker
                                  v-model="date"
                                  type="date"
                                  :placeholder="$t('selectDate')"
                                  :size="small"
                                  prefix-icon=""
                                  value-format="YYYY-MM-DD"
                                  :disabled-date="disabledDate"
                                />
                              </el-config-provider>
                            </div>
                            <div class="timePicker">
                              <el-config-provider :locale="locale">
                                <el-time-picker 
                                  v-model="time" 
                                  :placeholder="$t('selectTime')"
                                  format="HH:mm"
                                  value-format="HH-mm"
                                />
                              </el-config-provider>
                                <!--  -->
                            </div>
                          </div>
                        </div>

                    </div>

                    <div class="genderDiv" v-if="navQueryType.type!='hypd'">
                        {{ $t('gender') }}：
                        <div class="malebox" @click="chooseGender('male')">
                          <div class="wai">
                            <div class="nei" :class="gender=='male'?'active':''"></div>
                          </div>
                          {{ $t('male') }}
                        </div>
                        <div class="femalebox" @click="chooseGender('female')">
                          <div class="wai">
                            <div class="nei" :class="gender=='female'?'active':''"></div>
                          </div>
                          {{ $t('female') }}
                        </div>
                      </div>
                      <div class="okBtn" @click="sendDateTime">
                        {{ $t('sure') }}
                      </div>
                  </div>

                    <!-- <div class="genderDiv">
                      {{ $t('gender') }}：
                      <div class="malebox" @click="chooseGender('male')">
                          <div class="wai">
                          <div class="nei" :class="gender=='male'?'active':''"></div>
                          </div>
                          {{ $t('male') }}
                      </div>
                      <div class="femalebox" @click="chooseGender('female')">
                          <div class="wai">
                          <div class="nei" :class="gender=='female'?'active':''"></div>
                          </div>
                          {{ $t('female') }}
                      </div>
                    </div>
                    <div class="okBtn" @click="sendDateTime">
                      {{ $t('sure') }}
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
  import { useI18n } from 'vue-i18n'
  import EventBus from '/@/utils/EventBus.js'
  import zhCn from 'element-plus/dist/locale/zh-cn.mjs'
  import EN from 'element-plus/dist/locale/en.mjs'
  export default {
    props:[],
    setup(){
      const store = useStore()
      const lang = computed(() => store.state.lang)
      const date = ref('')
      const time = ref('')
      const dateVal2 = ref('')
      const timeVal2 = ref('')
      const maleName = ref('')
      const femaleName = ref('')
      const gender = ref('male')
      const navQueryType = computed(() => store.state.navQueryType)
      //适配
      const screenWidth = computed( () => {
        return store.state.screenWidth
      })
      const locale = computed(()=>{
        if(lang.value=='en'){
          return EN
        }else{
          return zhCn
        }
      })
      watch(() => lang.value,(val,old) => {
        if(val=='en'){
          locale.value = EN
        }else{
          locale.value = zhCn
        }
      })
      const chooseGender = (g)=>{
        gender.value = g
      }
      const disabledDate = (date) => {
        const currentDate = new Date();
        const year = date.getFullYear();
        const currentYear = currentDate.getFullYear();
        const currentMonth = currentDate.getMonth();
        const currentDay = currentDate.getDate();
        
        // 禁用1900年之前和当前日期之后的日期
        return year < 1900 || (year === currentYear && date > currentDate) || year > currentYear;
      };
      return {
        date,
        time,
        gender,
        chooseGender,
        locale,
        disabledDate,
        dateVal2,
        timeVal2,
        maleName,
        femaleName,
        lang,
        screenWidth,
        navQueryType,
     } 
    },
    mounted() {
    },
    beforeDestroy() {
  
    },
    watch: {
    },
    methods: {
      // chooseGender(g){
      //   this.$emit('chooseGender',g) 
      // },
      sendDateTime(){
        const obj = {
          date:this.date,
          time:this.time,
          sex:this.gender,
          dateVal2:this.dateVal2,
          timeVal2:this.timeVal2,
          maleName: this.maleName,
          femaleName: this.femaleName,
        }
        this.$emit('sendDateTime',obj) 
      }
    }
  };
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
.dateTimeMaxDiv{
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  white-space: nowrap;
  .birthBox{
    display: flex;
    align-items: center;
    margin-top: .2rem;
    flex-wrap: wrap;
    .dateTextDiv{
      width: 3.67rem;
    }
    .dateTimeDiv{
      display: flex;
      .datePicker{
        margin-right: .2rem;
      }
      .timePicker{
        margin-right: .2rem;
      }
      
    }
  }
  .bottomDiv{
    display: flex;
    align-items: center;
    flex-wrap: wrap;
  }
  .flexDiv{
    display: flex;
    align-items: center;
    // flex-wrap: wrap;
    &.flexWrap{
      flex-wrap: wrap;
    }
    .nameBox{
      // width: 4rem;
      margin-right: .5rem;
      margin-top: 0.2rem;
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      white-space: nowrap;
      .textdiv{
        width: 2.07rem;
      }
      .width100{
        width: 100%;
      }
      .nameInput{
        background: #FFF3DE;
        outline: none;
        border: none;
        height: 30px;
        width: 3.5rem;
        border-radius: 0.05rem;
        padding-left: 10px;

      }
      .nameInput::-webkit-input-placeholder{
        color: #a7abb3;
      }
    }
  }
  .genderDiv{
      display: flex;
      align-items: center;
      margin-top: .2rem;
      .malebox,.femalebox{
        display: flex;
        align-items: center;
        margin-right: .15rem;
        cursor: pointer;
        .wai{
          background: #FFF3DE;
          border-radius: 4px;
          width: 0.37rem;
          height: 0.37rem;
          margin-right: .1rem;
          display: flex;
          align-items: center;
          justify-content: center;
          .nei{
            border-radius: 4px;
            width: 0.259rem;
            height: 0.259rem;
            &.active{
              background: #FF8800;
            }
          }
        }
      }
    }
    .okBtn{
      margin-top: .2rem;
      width: 1.44rem;
      height: .55rem;
      background: linear-gradient(180deg, #FDE8A5 0%, #E2A544 100%);
      border-radius: 4px;
      font-family: Inter-Medium, Inter;
      // font-weight: 500;
      color: #000000;
      text-align: center;
      line-height: .55rem;
      cursor: pointer;
    }
}
</style>
<style>
.el-input__wrapper {
 background:#FFF3DE;
}
.el-date-editor {
  --el-date-editor-width: 140px;
}
</style>