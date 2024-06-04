<template>
    <div class="chat" ref="chatContent" :class="screenWidth<=900? 'mb-chat' : ''">
      <!-- 问卦 -->
        <div class="chat-list" v-if="$route.query.type || chatList.length == 0">
            <div  class="answer">
              <div class="BotHeader">
                <img class="avatar" :class="screenWidth<=900 ? 'mbImg' : ''" src="/@/assets/images/aibot.png" alt="">
                <div v-if="screenWidth<=900">{{ $t('starloom') }}</div>
              </div>
            <div class="text-content">
                <div class="inner">
                    <div class="zindex">{{ $t('AskReddit_openremarks') }}</div>
                    <div class="xiangyun"></div>
                </div>
            </div>
            </div>
        </div>
      <template v-for="(item,index) in chatList" :key="index">
          <!-- 文字对话 -->
          <!-- v-if="item.type  == 'text' || item.role == 'user'" -->
          <template  v-if="(item.showtype  == 'text' || item.showtype  == 'gpt' || item.type  == 'text' || item.role == 'user') && !item.islike">
              <div class="chat-list" :class="item.role == 'user' ? 'right-content' : ''">
                <div class="select" v-if="selectStatus" @click="item.choose =!item.choose">
                  <img v-if="!item.choose" src="/@/assets/images/choose.png" alt="" srcset="">
                  <img v-if="item.choose" src="/@/assets/images/choose2.png" alt="">
                </div>
                  <div v-if="item.role == 'user'" class="question" @mouseover="onHover(item)" @:mouseleave="onMouseLeave(item)">
                    <div class="text-content">
                    <!-- <el-popover
                        v-model:visible="item.sharePopover"
                        placement="bottom"
                        trigger="click"
                        :show-arrow="false"
                        popper-class="share-popover"
                        v-if="item.funshow && !selectStatus"
                    >
                        <template #reference>
                          <img src="/@/assets/images/more.png" alt="">
                        </template>
                        <template #default>
                          <div class="list" v-if="item.showtype !='tem'" @click="copyHandle(item)"><img src="/@/assets/images/copy.png" alt="" srcset="">{{ $t('copy') }}</div>
                          <div  class="list" @click="shareHandle(item)"><img src="/@/assets/images/share.png" alt="" srcset="">{{ $t('share') }}</div>
                          <div class="list" @click="deleteHandle(item)"><img src="/@/assets/images/deletechat.png" alt="" srcset="">{{ $t('delete') }}</div>
                        </template>
                    </el-popover> -->
                    <el-popover
                      placement="top"
                      effect="dark"
                      :width="screenWidth> 900 ?260 : 220"
                      popper-style="border-radius:0.2rem;background: #000000;padding: 10px;"
                    >
                    <template #reference>
                      <div class="inner">
                        <div v-if="item.base64_type == 1 && item.base64_content">
                          <img :src="item.base64_content" alt="">
                        </div>
                        {{ item.content }}
                        <!-- <div v-html="item.content"></div> -->
                      </div>
                    </template>
                    <template #default>
                      <div class="setList" :class="screenWidth<= 900?'mb-setList':''">
                        <div class="list" v-if="item.showtype !='tem'" @click="copyHandle(item)"><img src="/@/assets/images/copy.png" alt="" srcset="">{{ $t('copy') }}</div>
                        <div class="xian"></div>
                        <div  class="list" @click="shareHandle(item)"><img src="/@/assets/images/share.png" alt="" srcset="">{{ $t('share') }}</div>
                        <div class="xian"></div>
                        <div class="list" @click="deleteHandle(item)"><img src="/@/assets/images/deletechat.png" alt="" srcset="">{{ $t('delete') }}</div>
                      </div>  
                    </template>
                  </el-popover>  
                  </div>
                  <img v-if="screenWidth>900" src="/@/assets/images/user.png" alt="">
                  </div>
                  <div v-if="item.role == 'assistant'" class="answer" @mouseover="onHover(item)" @:mouseleave="onMouseLeave(item)">
                    <div class="BotHeader mb">
                      <div class="left">
                        <img class="avatar" :class="screenWidth<=900 ? 'mbImg' : ''" src="/@/assets/images/aibot.png" alt="">
                        <div v-if="screenWidth<=900">{{ $t('starloom') }}</div>
                      </div> 
                      <!-- <el-popover
                          v-model:visible="item.sharePopover"
                          placement="bottom"
                          trigger="click"
                          :show-arrow="false"
                          popper-class="share-popover"
                          v-if="item.funshow && !selectStatus && screenWidth<=900"
                      >
                          <template #reference>
                            <img src="/@/assets/images/more.png" alt="">
                          </template>
                          <template #default>
                            <div class="list" v-if="item.showtype !='tem'" @click="copyHandle(item)"><img src="/@/assets/images/copy.png" alt="" srcset="">{{ $t('copy') }}</div>
                            <div  class="list" @click="shareHandle(item)"><img src="/@/assets/images/share.png" alt="" srcset="">{{ $t('share') }}</div>
                            <div class="list" @click="deleteHandle(item)"><img src="/@/assets/images/deletechat.png" alt="" srcset="">{{ $t('delete') }}</div>
                          </template>
                      </el-popover> -->
                    </div>
                      <div class="text-content">
                        <el-popover
                          placement="top"
                          effect="dark"
                          :width="screenWidth> 900 ?260 : 220"
                          popper-style="border-radius:0.2rem;background: #000000;padding: 10px;"
                        >
                        <template #reference>
                          <div class="inner" v-html="item.content"></div>
                        </template>
                          <template #default>
                            <div class="setList" :class="screenWidth<= 900?'mb-setList':''">
                              <div class="list" v-if="item.showtype !='tem'" @click="copyHandle(item)"><img src="/@/assets/images/copy.png" alt="" srcset="">{{ $t('copy') }}</div>
                              <div class="xian"></div>
                              <div  class="list" @click="shareHandle(item)"><img src="/@/assets/images/share.png" alt="" srcset="">{{ $t('share') }}</div>
                              <div class="xian"></div>
                              <div class="list" @click="deleteHandle(item)"><img src="/@/assets/images/deletechat.png" alt="" srcset="">{{ $t('delete') }}</div>
                            </div>
                          </template>
                        </el-popover>  
                          <!-- <el-popover
                              v-model:visible="item.sharePopover"
                              placement="bottom"
                              trigger="click"
                              :show-arrow="false"
                              popper-class="share-popover"
                              v-if="item.funshow && !selectStatus && screenWidth>900"
                          >
                              <template #reference>
                                <img src="/@/assets/images/more.png" alt="">
                              </template>
                              <template #default>
                                <div class="list" v-if="item.showtype !='tem'" @click="copyHandle(item)"><img src="/@/assets/images/copy.png" alt="" srcset="">{{ $t('copy') }}</div>
                                <div  class="list" @click="shareHandle(item)"><img src="/@/assets/images/share.png" alt="" srcset="">{{ $t('share') }}</div>
                                <div class="list" @click="deleteHandle(item)"><img src="/@/assets/images/deletechat.png" alt="" srcset="">{{ $t('delete') }}</div>
                              </template>
                          </el-popover> -->
                          <!--   {{item.content}} --> 
                          <!-- v-html="item.content" -->
                      </div>
                  </div>
              </div>
              <div class="chatBotton" v-if="index == chatlist_index && !loading && !selectStatus" :class="screenWidth<=900?'mb_chatBotton' : ''">
            <div class="share" @click="shareHandle(item)">
              <img src="/@/assets/images/share_yellow.svg" alt="" srcset="">
              {{ $t('share') }}
            </div>
            <div class="likediv" v-if="!item.likeType" @click="likeHandle(1,item)">
              <img src="/@/assets/images/like.svg" alt="" srcset="">
              {{ $t('like') }}
            </div>
            <div class="likediv" v-if="!item.likeType" @click="showdislikeDialog(item)">
              <img src="/@/assets/images/dislike.svg" alt="" srcset="">
              {{ $t('dislike') }}
            </div>
            <div class="chooseIsLike" v-if="item.likeType == 1">
              <img src="/@/assets/images/like2.svg" alt="" srcset="">
            </div>
            <div class="chooseIsLike" v-if="item.likeType == 2 || item.likeType == 3 || item.likeType == 4">
              <img src="/@/assets/images/dislike2.svg" alt="" srcset="">
            </div>
          </div>
          </template> 
          <template v-if="item.role == 'assistant' && item.showtype == 'tem' && !item.islike">
                <!-- 生肖查询 -->
                <template v-if="item.submodel == 'a-1'">
                    <ZodiacQuery :presetData="item.content"/>
                </template>
                <!-- 生肖运势 -->
                <template v-if="item.submodel == 'a-2'">
                  <ChineseZodiacFortune :presetData="item.content"/>
                </template>
                <!-- 上升星座 -->
                <template  v-if="item.submodel == 'a-3'">
                  <Ascendant :presetData="item.content"/>
                </template>
                <!-- 下降星座 -->
                <template v-if="item.submodel == 'a-4'">
                  <DescendingZodiac :presetData="item.content"/>
                </template>
                <!-- 星座运势 -->
                <template v-if="item.submodel == 'a-5'">
                    <Horoscope
                      :presetData="item.content"
                      :index="index"
                      @chageTab="chageTab"
                    />
                </template>
                <!-- 星座查询 -->
                <template v-if="item.submodel == 'a-6'">
                  <ConstellationInquir :presetData="item.content"/>
                </template>
                <!-- 星座排行榜 -->
                <template v-if="item.submodel == 'a-7' && item.questionType == 1">
                  <ConstellationRankingList
                  :presetData="item.content"
                  :page="rankPage"
                  :index="index"
                  @chageRankTab="chageRankTab"
                  @getXingzuoRanking="getXingzuoRanking"
                  />
                </template>
                <!-- 排行榜详情 -->
                <template v-if="item.submodel == 'a-7' && item.questionType == 2">
                  <ConstellationRankingItem :presetData="item.content"/>
                </template>
                <!-- 生日花 -->
                <template v-if="item.submodel == 'a-8'">
                  <BirthdayFlower :presetData="item.content" />
                </template>
                <!-- 月亮星座 -->
                <template v-if="item.role == 'assistant' && item.showtype == 'tem' &&item.submodel == 'a-9'">
                  <MoonSign :presetData="item.content"/>
                </template>
                <!-- 48星区 -->
                <template v-if="item.role == 'assistant' && item.showtype == 'tem' &&item.submodel == 'a-10'">
                  <Constellations48 :presetData="item.content"/>
                </template>
                <!-- 生日密码 -->
                <template v-if="item.role == 'assistant' && item.showtype == 'tem' &&item.submodel == 'a-11'">
                  <BirthdatePassword :presetData="item.content" />
                </template>
                <!-- 生日书 -->
                <template v-if="item.role == 'assistant' && item.showtype == 'tem' &&item.submodel == 'a-12'">
                  <BirthdayBook :presetData="item.content"/>
                </template>
                <!-- 测试出轨对象 -->
                <template v-if="item.role == 'assistant' && item.showtype == 'tem' &&item.submodel == 'a-13'">
                  <CheatingPerson :presetData="item.content"/>
                </template>
                 <!-- 星盘查询 -->
                <template v-if="item.role == 'assistant' && item.showtype == 'tem' &&item.submodel == 'a-14'">
                  <AstrologicalChart :presetData="item.content"/>
                </template>
                <!-- 行星落宫位解析 -->
                <template  v-if="item.role == 'assistant' && item.showtype == 'tem' &&item.submodel == 'a-17'">
                  <PlanetInHouse :presetData="item.content"/>
                </template>
                <!-- 行星落星座解析 -->
                <template  v-if="item.role == 'assistant' && item.showtype == 'tem' &&item.submodel == 'a-18'">
                  <PlanetInSign :presetData="item.content"/>
                </template>
                <!-- 宫位查询 -->
                <template v-if="item.role == 'assistant' && item.showtype == 'tem' &&item.submodel == 'a-15'">
                  <AstrologicalHouseChart :presetData="item.content"/>
                </template>
                <!-- 星座血型性格 -->
                <template v-if="item.role == 'assistant' && item.showtype == 'tem' &&item.submodel == 'a-16'">
                  <ConsteBloodPersonality :presetData="item.content"/>
                </template>
          </template>
          <template v-if="item.showtype  =='dateTime' && item.role == 'assistant' && !item.islike ">
              <DateTimeSelect 
                @sendDateTime="sendDateTime"
              />
          </template>
      </template>
      <div class="chat-list" v-if="loading">
          <div class="answer">
              <div class="BotHeader">
                <img class="avatar" :class="screenWidth<=900 ? 'mbImg' : ''" src="/@/assets/images/aibot.png" alt="">
                <div v-if="screenWidth<=900">{{ $t('starloom') }}</div>
              </div>
              <div class="text-content">
                  <div class="inner">
                      <div v-if="step == 1" class="three-bounce"><div class="one"></div><div class="two"></div><div class="three"></div></div>
                      <!-- <TextComponents ref="TextComponents" @onComplete="onComplete"  v-if="step == 2 && chatType  == 'text'" :text="showText" :obj="resObj"/> -->
                      <div class="htmlText" v-if="step == 2" v-html="htmlText"></div>
                      <span class="cursor" v-if="htmlText != ''"></span>
                  </div>
              </div>
          </div>
      </div>
    </div>
    <div class="bottom-input">
        <button class="stop" v-if="loading && step == 2"  @click="stopText">
            <img src="/@/assets/images/stop.svg" alt="">
            {{ $t('stopGenerating') }}
        </button>
        <button class="regenerateResponse" v-if="!loading && !likeLoading && step == 3" @click="regenerateResponse">
            <img src="/@/assets/images/repeat.svg" alt="">
            {{ $t('regenerateResponse') }}
        </button>
    </div>
    <DisLikeReason
      :disLikeDialog="disLikeDialog"
      :likeItemObj="likeItemObj"
      @closeDisLike="closeDisLike"
      ref="disLike"
    />
  </template>
  
  <script>
  import { ref, computed, watch, onMounted, onUnmounted } from 'vue';
  import { useStore} from 'vuex'
  import { useRouter,useRoute } from 'vue-router'
  import TextComponents from '/@/components/ChatComponent/TextComponents.vue'
  import DisLikeReason from '/@/components/ChatComponent/DisLikeReason.vue'
  import Horoscope from '/@/components/Horoscope.vue'
  import ConstellationRankingList from '/@/components/ConstellationRankingList.vue'
  import ConstellationRankingItem from '/@/components/common/ConstellationRankingItem.vue'
  import ZodiacQuery from '/@/components/ZodiacQuery.vue'
  import ConstellationInquir from '/@/components/ConstellationInquir.vue'
  import BirthdatePassword from '/@/components/BirthdatePassword.vue'
  import ChineseZodiacFortune from '/@/components/ChineseZodiacFortune.vue'
  import DescendingZodiac from '/@/components/DescendingZodiac.vue'
  import BirthdayFlower from '/@/components/BirthdayFlower.vue'
  import BirthdayBook from '/@/components/BirthdayBook.vue'
  import ConsteBloodPersonality from '/@/components/ConsteBloodPersonality.vue'
  import Ascendant from '/@/components/Ascendant.vue'
  import MoonSign from '/@/components/MoonSign.vue'
  import Constellations48 from '/@/components/Constellations48.vue'
  import CheatingPerson from '/@/components/CheatingPerson.vue'
  import AstrologicalChart from '/@/components/AstrologicalChart.vue'
  import AstrologicalHouseChart from '/@/components/AstrologicalHouseChart.vue'
  import PlanetInHouse from '/@/components/PlanetInHouse.vue'
  import PlanetInSign from '/@/components/PlanetInSign.vue'
  import DateTimeSelect from '/@/components/ChatComponent/DateTimeSelect.vue'
  
  import { GPTChat, xingzuoYunshi, shengxiaoYunshi, shengxiaoQuery, xingzuoChaxun, xingzuoShengrishu,
   xingzuoShengrimima, xingzuoShengrihua, xingzuoRankingList, xingzuoRankingGet, xingzuoRankingQuestion,
  xingzuoChugui, xingzuoXuexing, queryConstellations48, xingzuoXiajiang, xingzuoYueliang, getMessageList, setUserSharechat, usermsgDelete } from  '/@/api/api.js'

  import EventBus from '/@/utils/EventBus.js'
  import objKeySort from '/@/utils/hexmd5.js'
  import useClipboard from 'vue-clipboard3'
  import { MD5 } from 'crypto-js';
  import { marked } from 'marked'
  const url_pro = 'https://starloom.mpcbot.ai/chat';
  const url_test = 'https://testastroai.mpcbot.ai/chat';
  const baseUrl = import.meta.env.VITE_APP_BASE_API
  import { useI18n } from 'vue-i18n'
  export default {
    name: 'Chat',
    setup() {
      const chatList = ref([])
      const loading = ref(false) //加载状态
      const chatType = ref('') // 接口返回的 对话类型
      const step =  ref('1') //加载过程中的状态， 1 代表正在跟后台请求中， 2 代表 正在显示文字中 3 代表文字显示完毕或者用户中断回答
      const showText = ref('') // 回答的文本
      const chatContent = ref(null)
      const rankPage = ref(1)
      const resObj = ref(null)  //接口返回数据 模版类型，子模版位置等
      const store = useStore()
      const { t } = useI18n();
      const route = useRoute()
      const chatNum = ref(1)
      let chatId = route.params.id
      const saveQuestion = ref('')
      const text = ref('')
      const htmlText = ref('') // 回答的文本
      const disLikeDialog = ref(false)   // 不喜欢弹窗是否展示
      const selectStatus = computed(() => store.state.selectStatus)
      const selectType = computed(() => store.state.selectType)
      const apiurl = computed(() => store.state.apiurl)
      const v1chatUrl = computed(() => store.state.v1chatUrl)
      const userModel = computed(() => store.state.userModel)
      // const likeType = ref('')
      const sharelink = computed(() => store.state.sharelink)//分享链接
      const haveCount =computed( () => store.state.haveCount) // 是否有条数
      const receiveType = computed(() => store.state.receiveType)
      const list_current = ref('')
      const likeItemObj = ref('')
      const likeLoading = ref(false)
      const dateVal = ref('')
      const timeVal = ref('')
      const gender = ref('male')  // 性别

      let eventSource
      const chatlist_index = computed(() => {   //当前模块list
        list_current.value = chatList.value.filter(item => item.role == 'assistant' && !item.islike )
        const leng = list_current.value.length-1
        for(var i=0;i<chatList.value.length;i++){
          if(chatList.value[i]== list_current.value[leng]){
              return i
          }
        } 
      
      })
      const scrollToBottom = ()=> { // 保持滚动条在最底部
          var element = chatContent.value
          element.scrollTop = element.scrollHeight
      }

      //适配
      const screenWidth = computed( () => {
        return store.state.screenWidth
      })
      // 登录状态
      const loginStatus = computed( () => {
        return store.state.loginStatus
      }) 
      const sendMessage = async (requestObj, reqType, temReqObj, tabIndex, index) => {
        let questionText = requestObj.question
        let fileBase64String = requestObj.base64String
        let baseType = requestObj.base64_type
        const user_receive_type = requestObj.base64_type == 2 ? receiveType.value == 'audio'? 2 : 1 : 1// 用户需要返回类型：1-纯文本；2-语音和文本 
        console.log('问题内容：：：', questionText)
        if(loading.value) return
       if(baseType == 2){
          if(fileBase64String == ''){
                return
          } 
        } else {
          if(questionText == '' ){
                return
          } 
        }  
        // if(loading.value || questionText == ''){
        //       return
        // } 
        if(reqType == 'DateTime'){ 
          const dateObj = temReqObj
          if(dateObj){
            dateVal.value = dateObj.date
            timeVal.value = dateObj.time
            gender.value = dateObj.sex
          }
          if(!dateVal.value ){
            ElMessage({
                message: t('pleaseSelectDate'),
                type: 'error',
              })
              return  
          }
          if(!timeVal.value ){
            ElMessage({
                message: t('pleaseSelectTime'),
                type: 'error',
              })
              return  
          }
        } else if(reqType == 'likeFun'){
          const _liketype = temReqObj.likeType
          if(_liketype){
            if(_liketype == 1){ // 喜欢
              questionText = t('likeChat')
            } else if(_liketype == 2){  //不准确
              questionText = t('inaccurateChat')
            } else if(_liketype == 3){ //无益
              questionText = t('unhelpfulChat')
            } else if(_liketype == 4){ //攻击性
              questionText = t('offensiveChat')
            }
          } 
        }
        saveQuestion.value = questionText  
        let chat 
          if(!tabIndex && tabIndex !=0 ){
            chat = {
              role: 'user',
              content:questionText,
              copyText: questionText,
              showtype:'text',
              msggroup: chatId,
              islike: false,
              base64_type: requestObj.base64_type,
              base64_content:fileBase64String,
              user_receive_type: user_receive_type,// 用户需要返回类型：1-纯文本；2-语音和文本 
            }
            if(reqType == 'likeFun'){
              chat.islike = true
            }
            // chatList.value.push(chat)
            if(reqType == 'likeFun'){
              likeLoading.value = true
            }else{
              loading.value = true
            }
            if(requestObj.base64_type ==2 ){
              store.commit('setGptAudioLoading', true)
            }
            // likeType.value = ""
            step.value = 1
          }
          setTimeout(() => {
              scrollToBottom() 
              store.commit('setQuestion', '')
          },50)
          let userQueList = []
          let chat1
          if(reqType == 'likeFun'){
              chat1 = chatList.value.filter(item=>!item.islike)
          }else{
            chat1 = chatList.value
          }
          chat1.forEach(item =>  {
              // if(item.role == 'user'){
                userQueList.push({ 
                  "type": item.role == 'user'|| item.showtype=='date-transfered-message' ? 'user' : item.showtype,
                  "content": item.copyText,
                  "msgId": item.msgId ? item.msgId:'',  
                  "base64_type": item.base64_type ? item.base64_type : 0,  // 是否是图片消息，1是；0否
                  "base64_content": "",
                  "file_type": item.base64_type==2?"mp3":'', // 文件的类型
                  "user_receive_type": item.user_receive_type ? item.user_receive_type : 1,// 用户需要返回类型：1-纯文本；2-语音和文本 
                })
              // }
            })
            if(reqType != 'DateTime'){
              userQueList.push({
                "type": chat.role,
                "content": chat.content,
                "msgId": chat.msgId ? chat.msgId:'',  
                "base64_type": requestObj.base64_type ? requestObj.base64_type : 0,  // 是否是图片消息，1是；0否
                "base64_content": requestObj.base64_type == 1 ? fileBase64String :  requestObj.base64_type == 2 ? fileBase64String.split("base64,")[1] : '', // 文件的base64编码
                "file_type": requestObj.base64_type!=2 ? '' : 'mp3', // 文件的类型
                "user_receive_type": user_receive_type,
              })
            } 
            if(requestObj.base64_type !=2 && reqType != 'DateTime'){
              chatList.value.push(chat)
            } 
            if(timeVal.value){
              timeVal.value = timeVal.value.replace(':', '-')
            }  
            let requestData =  {
              "messages":userQueList,
              "module": "0",
              "msggroup": chatId,
              "gpt_mode": userModel.value == '3.5'? 1 : 2,
              islike: false,
            }
            if(reqType == 'DateTime'){
              requestData.birthday = dateVal.value+'-'+timeVal.value;
              requestData.sex = gender.value;
            }
            if(reqType == 'likeFun'){
              requestData.islike = true
            }
          try{
            eventSource = new SSE(v1chatUrl.value, {
              headers: {
                'Content-Type': 'application/json', 
                'Authorization': localStorage.getItem('starloomAI-token'),
              },
              payload: JSON.stringify(requestData),
              method: "POST"
            });
            console.info(eventSource)
            eventSource.onopen = () => {
                console.log('open')
            }
            let n = 0
            let chat
            eventSource.onmessage = function(event) {
              // 第一次返回： text|tem
            // 如果 是tem ，第二次返回整个json字符串；如果是text，第二次，到第N次按照流输出一个字一个字的，遇到[DONE]结束
              console.log('1111,',event.data)
              const obj = JSON.parse(event.data)
              const objcontent = obj.content
              chat = {
                  role: 'assistant',
                  // content:result.data.data,
                  showtype: obj.type,
                  submodel: obj.modelType,  //a-1
                  msggroup: chatId,
                  msgId: obj.msg_answer_id,
                  islike: obj.islike,
                }
              resObj.value = JSON.parse(event.data)
              if(requestObj.base64_type !=2 && reqType != 'DateTime'){
                const lengthnum = chatList.value.length
                chatList.value[lengthnum-1].msgId =  obj.msg_question_id
              }
              n = 1
              console.log('obj,',obj)
              if(obj.type == 'tem'){ 
                eventSource.close()
                if(sxxzType.value.submodel == 'a-7'){
                  if(obj.content.totalCount){
                    chat.questionType = 1
                    obj.content.noTab = true
                  } else {
                    chat.questionType = 2
                  }
                }
                chat.showtype = obj.type
                chat.content = JSON.parse(event.data)
                chat.copyText = JSON.parse(event.data)
                loading.value = false
                loadingmodel.value = ''
                chatList.value.push(chat)
                console.log('对话list：：：', chatList.value)
              } else if(obj.type == 'gpt'){
                if(requestObj.base64_type != 2){
                  step.value = 2
                  console.log('obj',obj)
                
                  // if (event.data.indexOf('<br><br>') != -1) {
                  //     event.data = event.data.replace('<br><br>', '\n\n')
                  // }
                  // if(event.data.indexOf('<br>') != -1){
                  //   event.data = event.data.replace('<br>','\n')
                  // }
                
                  // if(obj.content == '[DONE]'){
                  //     console.info('结束')
                  //     loading.value = false
                  //     chat.copyText = text.value
                  //     chat.content = marked(text.value)
                  //     chatList.value.push(chat)
                  //     text.value = ''
                  //     htmlText.value = ''
                  //     step.value = 3
                  //     chatNum.value += 1
                  //     n=2
                  //     eventSource.close()
                  // }else{
                    text.value += objcontent
                    htmlText.value = marked(text.value);
                    console.log('text.value,,,',text.value)
                    setTimeout(() => {
                        scrollToBottom() 
                    },50)
                  // }
                }else{
                  text.value += objcontent
                }
                
              } else if(obj.type == 'gpt-audio'){
                store.commit('setGptAudioLoading', false)
                store.commit('setGptAudio',obj.content)
              }else if(obj.type == 'text-user'){
                chat = {
                  role: 'user',
                  content: obj.content,
                  copyText: obj.content,
                  showtype:'text',
                  submodel: obj.modelType,
                  msgId:obj.msg_question_id,
                  msggroup: chatId,
                  islike: false,
                  base64_type: 0,
                  base64_content: '',
                }
                if(requestObj.base64_type ==2 ){
                  chatList.value.push(chat)
                }
              }
              else if(obj.type == 'date-transfered-message'){
                if(reqType == 'DateTime'){
                  chat.msgId = obj.msg_question_id
                  chat.content = obj.content.content
                  chat.copyText = obj.content.content
                  chat.isDateTime = true
                  chatList.value.push(chat)
                }
              }
              else if(obj.type == '[DONE]'){
                    console.info('结束')
                    chat.type = 'gpt'
                    chat.showtype = 'gpt'
                    if(reqType == 'likeFun'){
                      likeLoading.value = false
                    }else{
                      loading.value = false
                    }
                    chat.copyText = text.value
                    chat.content = marked(text.value)
                    chatList.value.push(chat)
                    text.value = ''
                    htmlText.value = ''
                    step.value = 3
                    chatNum.value += 1
                    n=2
                    eventSource.close()
              }
              else if (obj.type == 'error'){
                    console.info('error')
                    if(obj.code == 6001){
                      EventBus.$emit('goSubscribe')
                    }
                    if(obj.code == 7001){
                      chat = {
                        role: 'assistant',
                        // content:result.data.data,
                        showtype: 'dateTime',
                        msggroup: chatId,
                        msgId: obj.msg_answer_id,
                        islike: obj.islike,
                      }
                      chat.content = ''
                      chatList.value.push(chat)
                    }
                    if(obj.code == 8101){
                      ElMessage({
                        message: t('serve500AlertTip'),
                        type: 'error',
                      })
                    }
                    loading.value = false
                    text.value = ''
                    htmlText.value = ''
                    step.value = 3
                    n=2
                    eventSource.close()
              }
            };
            eventSource.onerror = (error) => {
                console.error('EventSource failed:', error)
                loading.value = false
                // loadingmodel.value = ''
                step.value = 3
                eventSource.close()
            };
            eventSource.stream();
              // const result = await GPTChat({
              //   "messages":userQueList,
              //   "module": "0",
              //   "msggroup": chatId,
              // })
              // if(result.code == 200){
              //     const chat = {
              //         role: 'assistant',
              //         content:result.data.data,
              //         showtype:result.data.type,
              //         submodel: result.data.modelType,  //a-1
              //         msggroup: chatId,
              //     }
              //     if(result.data.modelType == 'a-7'){
              //       if(result.data.data.totalCount){
              //         chat.questionType = 1
              //         result.data.data.noTab = true
              //       } else {
              //         chat.questionType = 2
              //       }
              //     }
              //     if(result.data.type == 'text'){
              //       showText.value = result.data.data
              //       resObj.value = result.data
              //       resObj.value.msggroup = chatId
              //       step.value = 2
              //       chatType.value = 'text'
              //     }else{
              //       loading.value = false
              //       chatList.value.push(chat)
              //     }
              //     chatNum.value += 1
              // }else{
              //   loading.value = false
              //   step.value = 3
              // }
          }catch(error){
            loading.value = false
            // loadingmodel.value = ''
            step.value = 3
            eventSource.close()
          }    
      }

      const sendDateTime = async (dateObj) => {
        sendMessage('','DateTime',dateObj)
        return
        if(loading.value){
                return
        } 
        if(dateObj){
          dateVal.value = dateObj.date
          timeVal.value = dateObj.time
          gender.value = dateObj.sex
        }
        if(!dateVal.value ){
          ElMessage({
              message: t('pleaseSelectDate'),
              type: 'error',
            })
            return  
        }
        if(!timeVal.value ){
          ElMessage({
              message: t('pleaseSelectTime'),
              type: 'error',
            })
            return  
        }
            // chatList.value.push(chat)
            loading.value = true
            // likeType.value = ""
            step.value = 1
          setTimeout(() => {
              scrollToBottom() 
              // dateVal.value = ''
              // timeVal.value = ''
              // gender.value = 'male'
          },50)
          let userQueList = []
          chatList.value.forEach(item =>  {
              // if(item.role == 'user'){
                userQueList.push({ 
                  "type": item.role == 'user'? 'user' : item.showtype,
                  "content": item.copyText,
                  "msgId": item.msgId ? item.msgId:'',  
                  "base64_type": item.base64_type?item.base64_type : 0,  // 是否是图片消息，1是；0否
                  "base64_content": '',
                  "file_type": item.base64_type==2?"mp3":'', // 文件的类型
                  "user_receive_type": item.user_receive_type,// 用户需要返回类型：1-纯文本；2-语音和文本 
                })
              // }
            })
          timeVal.value = timeVal.value.replace(':', '-')
          const requestData =  {
                "messages":userQueList,
                "module": "0",
                "msggroup": chatId,
                "gpt_mode": userModel.value == '3.5'? 1 : 2,
                birthday: dateVal.value+'-'+timeVal.value,
                sex: gender.value,
                islike:false,
              }
          try{

            eventSource = new SSE(v1chatUrl.value, {
              headers: {
                'Content-Type': 'application/json', 
                'Authorization': localStorage.getItem('starloomAI-token'),
              },
              payload: JSON.stringify(requestData),
              method: "POST"
            });
            console.info(eventSource)
            eventSource.onopen = () => {
                console.log('open')
            }
            let n = 0
            let chat
            eventSource.onmessage = function(event) {
              console.log('1111,',event.data)
              const obj = JSON.parse(event.data)
              const objcontent = obj.content
              chat = {
                  role: 'assistant',
                  // content:result.data.data,
                  showtype: obj.type,
                  submodel: obj.modelType,  //a-1
                  msggroup: chatId,
                  msgId: obj.msg_answer_id,
                  islike: obj.islike,
                }
              resObj.value = JSON.parse(event.data)
              n = 1
              console.log('obj,',obj)
              if(obj.type == 'tem'){ 
                eventSource.close()
                if(sxxzType.value.submodel == 'a-7'){
                  if(obj.content.totalCount){
                    chat.questionType = 1
                    obj.content.noTab = true
                  } else {
                    chat.questionType = 2
                  }
                }
                chat.showtype = obj.type
                chat.content = JSON.parse(event.data)
                chat.copyText = JSON.parse(event.data)
                loading.value = false
                loadingmodel.value = ''
                chatList.value.push(chat)
                console.log('对话list：：：', chatList.value)
              } else if(obj.type == 'gpt'){
                step.value = 2
                console.log('obj',obj)
              
                // if (event.data.indexOf('<br><br>') != -1) {
                //     event.data = event.data.replace('<br><br>', '\n\n')
                // }
                // if(event.data.indexOf('<br>') != -1){
                //   event.data = event.data.replace('<br>','\n')
                // }
               
                // if(obj.content == '[DONE]'){
                //     console.info('结束')
                //     loading.value = false
                //     chat.copyText = text.value
                //     chat.content = marked(text.value)
                //     chatList.value.push(chat)
                //     text.value = ''
                //     htmlText.value = ''
                //     step.value = 3
                //     n=2
                //     eventSource.close()
                // }else{
                  text.value += objcontent
                  htmlText.value = marked(text.value);
                  console.log('text.value,,,',text.value)
                  setTimeout(() => {
                      scrollToBottom() 
                  },50)
                // }
              }else if(obj.content == '[DONE]'){
                    console.info('结束')
                    loading.value = false
                    chat.showtype ='gpt'
                    chat.copyText = text.value
                    chat.content = marked(text.value)
                    chatList.value.push(chat)
                    text.value = ''
                    htmlText.value = ''
                    step.value = 3
                    n=2
                    eventSource.close()
                }
              else if (obj.type == 'error'){
                    console.info('error')
                    if(obj.code == 6001){
                      EventBus.$emit('goSubscribe')
                    }
                    loading.value = false
                    text.value = ''
                    htmlText.value = ''
                    step.value = 3
                    n=2
                    eventSource.close()
              }
            };
            eventSource.onerror = (error) => {
                console.error('EventSource failed:', error)
                loading.value = false
                loadingmodel.value = ''
                step.value = 3
                eventSource.close()
            };
            eventSource.stream();
          }catch(error){
            console.log('error',error)
          }
        
    }

      const stopText = () =>{
        eventSource.close()
        const chat = {
          role: 'assistant',
          copyText: text.value,
          content: marked(text.value),
          showtype: 'text',
          submodel: resObj.value.modelType,  //a-1
          msggroup: chatId,
          msgId: resObj.value.msg_answer_id,
          islike: false,
        }
        chatList.value.push(chat)
        text.value = ""
        htmlText.value=''
        step.value = 3
        loading.value = false
      }

      //新旧对话框 判断并获取记录
      const getChatHistory = async(id) =>{
      
          chatList.value = []

        if(route.query.type == 'newChat'){
            setTimeout(() => {
                //对话记录增加一条数据
               // "content": saveQuestion.value == '' ? t('addChat') : saveQuestion.value,
                const chatListObj = {
                  "content": t('addChat'),
                  "type": "user",
                  "msggroup": route.params.id,
                  "type":'newChat',
                  "is_pic":0,
              }
              saveQuestion.value = ''
              EventBus.$emit('addChatList', chatListObj)
            },400)
        }
        if(route.query.type == 'continueChat'){
            setTimeout(() => {
                //对话记录增加一条数据
               // "content": saveQuestion.value == '' ? t('addChat') : saveQuestion.value,
                const chatListObj = {
                  "content": t('addChat'),
                  "type": "user",
                  "msggroup": route.params.id,
                  "type":'newChat'
              }
              EventBus.$emit('addChatList', chatListObj)
            },400)
            const list = JSON.parse(localStorage.getItem('shareChatList') ) 
            list.forEach(item=>{
              item.funshow = false
              item.choose = false
              item.sharePopover = false
            })
            chatList.value = list
            return
        }
        if(!localStorage.getItem('starloomAI-token')) return
          const res = await getMessageList({
              msggroup: id
          })
          if(res.code == 200){
            const list = res.data.messageList
            list.forEach(item => {
                const obj = {
                    role: item.type == 'user' ? 'user' : 'assistant',
                    content:  item.type == 'text' || item.type == 'gpt'? marked(item.content) :item.type == 'user' ? item.base64_type==2 ? item.gen_by_gpt : item.content : JSON.parse(item.content),   // item.type == 'user' ||
                    copyText: item.type == 'user' || item.type == 'text' || item.type == 'gpt'? item.content : JSON.parse(item.content),
                    showtype: item.type == 'user' || item.type == 'text' || item.type == 'gpt'? 'gpt' : item.type,
                    submodel: item.sub_module,
                    msgId:item.id,
                    base64_type:item.base64_type,
                    base64_content:item.base64_content,
                }
                if(item.sub_module == 'a-7'){
                    if(item.content.totalCount){
                      obj.questionType = 1
                    } else {
                      obj.questionType = 2
                    }
                  }
                chatList.value.push(obj)
            });
            console.log(chatList.value)
          }
      }

      watch(() => route.params.id, (val, oldCoinCode) => {
        chatId = val
        step.value = '1'
        if(loading.value){
          loading.value = false
          eventSource.close()
        }
        getChatHistory(val)
      })

      onMounted(() =>{
        getChatHistory(chatId)
    })
      // 获取星座运势数据
      const getHoroscopeData = async (questionText, tabIndex, index) => {
        // 监听对话的回调 目前分为预设1,2,3 以及文本对话
        console.log('问题内容：：：', questionText)
        if(loading.value || questionText == ''){
              return
        }
        if(!tabIndex && tabIndex !=0){
        const chat = {
          role: 'user',
          content:questionText,
          copyText:questionText,
          showtype:'text',
          islike: false,
        }
        chatList.value.push(chat)
        loading.value = true
        step.value = 1
        }
        setTimeout(() => {
          // scrollToBottom() 
          store.commit('setQuestion', '')
        },50)
        console.log('xingzuoyunshi')
        try{
            const result = await xingzuoYunshi({
              query: questionText,
              index: tabIndex ? tabIndex : 0,
            })
            if(result.code == 200){
                const chat = {
                    role: 'assistant',
                    content: result.data.data,
                    copyText: result.data.data,
                    showtype: result.data.type,
                    submodel: result.data.modelType,
                    islike: false,
                }
                if(result.data.type == 'text'){
                  showText.value = result.data.data
                  resObj.value = result.data
                  step.value = 2
                  chatType.value = 'text'
                }else{
                  if(tabIndex || tabIndex==0){
                    chatList.value[index] = chat
                  } else{
                    chatList.value.push(chat)
                  }
                  loading.value = false
                  console.log('对话list：：：', chatList.value)
                }
                // chatList.value.push(chat)
            }else{
              loading.value = false
              step.value = 3
            }
        }catch(error){

        }      
      }
      //  星座运势查询更改tab调用
      const chageTab = (obj) => { 
        getHoroscopeData(obj.que, obj.tab, obj.index)
      }

      const chageRankTab = (obj) => {
        rankPage.value = obj.page
        getRankingList(obj.type, obj.page, obj.pageSize, obj.index)
      }

      const getRankingList = async (type, page, pageSize, index) =>{
        console.log('xingzuoRankingList')
        setTimeout(() => {
            scrollToBottom() 
            store.commit('setQuestion', '')
        },50)
        try{
          const result = await xingzuoRankingList({
            type: type, 
            page: page, 
            pageSize: pageSize,
          })
          if(result.code == 200){
              const chat = {
                  role: 'assistant',
                  content:result.data.data,
                  copyText: result.data.data,
                  showtype:result.data.type,
                  submodel: result.data.modelType,  //a-7
                  islike: false,
                  questionType: 1,
              }
              if(result.data.type == 'text'){
                showText.value = result.data.data
                resObj.value = result.data
                step.value = 2
                chatType.value = 'text'
              }else{
                if(index || index==0){
                  chatList.value[index] = chat
                } else{
                  chatList.value.push(chat)
                }
                loading.value = false
                console.log('对话list：：：', chatList.value)
              }  
          }else{
            loading.value = false
            step.value = 3
          }
        }catch(error){

        }
      }

      const getXingzuoRanking = async (item) =>{
        console.log('xingzuoRankingGet')
        const chat = {
            role: 'user',
            content: item.title,
            copyText: item.title,
            showtype:'text',
            msggroup: chatId,
            islike: false,
          }
        chatList.value.push(chat)
        loading.value = true
        step.value = 1
        try{
        const result = await xingzuoRankingGet({
          id: item.id,
          "msggroup": chatId,
          title: item.title,
        })
        if(result.code == 200){
            const chat = {
                role: 'assistant',
                content:result.data.data,
                copyText: result.data.data,
                showtype:result.data.type,
                submodel: result.data.modelType,  //a-7
                msggroup: chatId,
                islike: false,
                questionType: 2,
            }
            if(result.data.type == 'text'){
              showText.value = result.data.data
              resObj.value = result.data
              step.value = 2
              chatType.value = 'text'
            }else{
              chatList.value.push(chat)
              setTimeout(() => {
                  scrollToBottom() 
              },50)
              loading.value = false
              console.log('对话list：：：', chatList.value)
            }
        }else{
          loading.value = false
          step.value = 3
        }
        }catch(error){

        }
      }
      const shareLinkHandle =  async(mul) =>{ //md5Handle
        // const { MD5 } = require('crypto-js');
        
        const time = new Date().getTime()
        var privateKey = 'Gxo2lx^2(oBl3cx92(ixvG4Vy32g4'; 
        const list = chatList.value.filter(item => item.choose)
        console.log(list)
        if(list.length==0){
          ElMessage({
              message: t('mustSelectOneShare'),
              type: 'error',
            })
            return
        }
        var dex_str = objKeySort(list, time);
        const md5Hash = MD5(dex_str + privateKey)
        const md5Hex = md5Hash.toString();
        console.log('md5Hex,,,',md5Hex)
        let url
          if(location.href.indexOf('defi.swftcoin.com') != -1){
            url = 'https://defi.swftcoin.com/view/astroai_web-test/index.html#/'
          } else if(location.href.indexOf('starloom.ai') != -1 || location.href.indexOf('tianjige') != -1 ){
            url = 'https://starloom.ai//#/'
          } else{
            url = 'http://192.168.124.3:5173/#/'
          }
        const link = `${url}chat/${md5Hex}`
        if(mul == 'link'){
            const { toClipboard } = useClipboard()
            try {
              // 复制
              await toClipboard(link)
              // 复制成功
            } catch (e) {
              // 复制失败
            }
          }
        const result = await setUserSharechat({
          code: md5Hex,
          t:time,
          contents:list,
        })
        if(result.code == 200){
         
          store.commit('setSelectStatus', false)
          store.commit('setSelectType', '')
          
          store.commit('setSharelink',link)
          console.log('sharelink,,,',link)
          if(mul == 'link'){
            // const { toClipboard } = useClipboard()
            // try {
              // 复制
              // await toClipboard(link)
              // ElNotification({
              //   duration: 5000,
              //   message: '复制链接成功',
              //   customClass: 'notify',
              //   'show-close': false,
              // })
              ElMessage({
                message:  t('linkCopiedSuccess'),
                type: 'success',
              })
            //   // 复制成功
            // } catch (e) {
            //   // 复制失败
            // }
          }else{
            EventBus.$emit('shareMultimedia', mul)
          }
          chatList.value.forEach(item =>{
            item.choose = false
            item.funshow = false
            item.sharePopover = false
          })       
        }else{
          // toClipboard.clearSelection();
          window.clipboardData.setData("Text","")
        }
      }
      const deleteChat =  async() =>{ //md5Handle
        const arr = chatList.value.filter(item => item.choose)
        console.log(arr)
        // let a //最后一条是否选中
        // const num =  list_current.value.length-1
        // if(list_current.value[num].choose){
        //   a = "Y"
        // }    
        let list = []
        arr.forEach(item => {
          list.push(item.msgId)
        })
        if(list.length==0){
          ElMessage({
              message: t('mustSelectOneDelete'),
              type: 'error',
            })
            return
        }
        console.log('list,,,',list)
        chatList.value = chatList.value.filter(item => !arr.includes(item));
        // if(a=="Y") likeType.value = ''
        if(!loginStatus.value){
          store.commit('setSelectStatus', false)
          store.commit('setSelectType', '') 
          ElMessage({
            message: t('deletedSuccess'),
            type: 'success',
          })
          return
        }
        const result = await usermsgDelete({
          "msgIds": list,
        })
        if(result.code == 200){
          // ElNotification({
          //   duration: 5000,
          //   message: '删除成功',
          //   customClass: 'notify',
          //   'show-close': false,
          // })
          ElMessage({
            message: t('deletedSuccess'),
            type: 'success',
          })
          store.commit('setSelectStatus', false)
          store.commit('setSelectType', '') 
          chatList.value.forEach(item =>{
            item.choose = false
            item.funshow = false
            item.sharePopover = false
          })
        }
      }
      const copyHandle =  async(item) => {
        const { toClipboard } = useClipboard()
        let copyReplace = item.copyText
        if (copyReplace.indexOf('<br><br>') != -1) {
          copyReplace = copyReplace.replace(/<br><br>/g, '\n\n')
        }
        if(copyReplace.indexOf('<br>') != -1){
          copyReplace = copyReplace.replace(/<br>/g,'\n')
        }
        if(copyReplace.indexOf('<p>') != -1){
          copyReplace = copyReplace.replace(/<p>/g,'')
        }
        if(copyReplace.indexOf('</p>') != -1){
          copyReplace = copyReplace.replace(/<\/?p>/g, '');
        }
        if(copyReplace.indexOf('<stong>') != -1){
          copyReplace = copyReplace.replace(/<strong>/g,'')
        }
        if(copyReplace.indexOf('</strong>') != -1){
          copyReplace = copyReplace.replace(/<\/?strong>/g, '');
        }
        if(copyReplace.indexOf('<b>') != -1){
          copyReplace = copyReplace.replace(/<b>/g,'')
        }
        if(copyReplace.indexOf('</b>') != -1){
          copyReplace = copyReplace.replace(/<\/?b>/g, '');
        }
        if(copyReplace.indexOf('**') != -1){
          copyReplace = copyReplace.replace(/\*\*/g, '');
        }
        try {
          // 复制
          await toClipboard(copyReplace)
          console.log('success', ElMessage)
          // ElNotification({
          //   duration: 5000,
          //   message: '复制成功',
          //   customClass: 'notify',
          //   'show-close': false,
          // })
          ElMessage({
            message: t('copysuccess'),
            type: 'success',
          })
          // 复制成功
        } catch (e) {
          // 复制失败
        }
      }

      const likeHandle = (liketype, obj)=>{
        obj.likeType = liketype
        sendMessage('','likeFun',obj)
        return
        let questionText
        if(liketype == 1){ // 喜欢
          questionText = t('likeChat')
        } else if(liketype == 2){  //不准确
          questionText = t('inaccurateChat')
        } else if(liketype == 3){ //无益
          questionText = t('unhelpfulChat')
        } else if(liketype == 4){ //攻击性
          questionText = t('offensiveChat')
        }
        const list_notlike =  chatList.value.filter(item=>!item.islike)
        // likeType.value = liketype
        const chat = {
          role: 'user',
          content:questionText,
          copyText: questionText,
          showtype:'text',
          msggroup: chatId,
          islike: true,
          "base64_type": 0,  // 是否是图片消息，1是；0否
          "base64_content": '',
          "file_type": "", // 文件的类型
          "user_receive_type": 1,// 用户需要返回类型：1-纯文本；2-语音和文本 
        }
        chatList.value.push(chat)
        list_notlike.push(chat)
        let userQueList = []
        list_notlike.forEach(item =>  {
            userQueList.push({ 
              "type": item.role == 'user'? 'user' : item.showtype,
              "content": item.content,
              "msgId": item.msgId ? item.msgId:'',  
              "base64_type": item.base64_type?item.base64_type : 0,  // 是否是图片消息，1是；0否
              "base64_content": '',
              "file_type": item.base64_type == 2?"mp3":'', // 文件的类型
              "user_receive_type": item.user_receive_type,// 用户需要返回类型：1-纯文本；2-语音和文本 
            })
        })
        likeLoading.value = true
          const requestData =  {
              "module":"0",
              // "sub_module":sxxzType.value.submodel,
              "messages":userQueList,
              "msggroup": chatId,
              "gpt_mode": userModel.value == '3.5'? 1 : 2,
              islike: true,
            }
        try{
          eventSource = new SSE(v1chatUrl.value, {
            headers: {
              'Content-Type': 'application/json', 
              'Authorization': localStorage.getItem('starloomAI-token'),
            },
            payload: JSON.stringify(requestData),
            method: "POST"
          });
          console.info(eventSource)
          eventSource.onopen = () => {
              console.log('open')
          }
          let n = 0
          let chat
          eventSource.onmessage = function(event) {
            // 第一次返回： text|tem
          // 如果 是tem ，第二次返回整个json字符串；如果是text，第二次，到第N次按照流输出一个字一个字的，遇到[DONE]结束
            console.log('1111,',event.data)
            // if(n==2) return
            // if(n==0){
            //   const obj = JSON.parse(event.data)
            //   chat = {
            //     role: 'assistant',
            //     // content:result.data.data,
            //     showtype: obj.type,
            //     submodel: obj.modelType,  //a-1
            //     msggroup:chatId,
            //     msgId: obj.msgIds[1],
            //     islike: obj.islike,
            //   }
            //   resObj.value = JSON.parse(event.data)
            //   const lengthnum = chatList.value.length
            //   chatList.value[lengthnum-1].msgId =  obj.msgIds[0]
            //   n = 1
            // }else {
            //   if(chat.showtype == 'tem'){
            //     eventSource.close()
            //     if(sxxzType.value.submodel == 'a-7'){
            //       if(event.data.totalCount){
            //         chat.questionType = 1
            //         event.data.data.noTab = true
            //       } else {
            //         chat.questionType = 2
            //       }
            //     }
            //     chat.content = JSON.parse(event.data)
            //     chat.copyText = JSON.parse(event.data)
            //     chatList.value.push(chat)
            //     console.log('对话list：：：', chatList.value)
            //   } else if (chat.showtype == 'text'){
            //     if (event.data === '[DONE]') {
            //       console.info('结束')
            //       chat.content = marked(text.value)
            //       chat.copyText = text.value
            //       chatList.value.push(chat)
            //       text.value = ""
            //       n=2
            //       eventSource.close()
            //       likeLoading.value = false
            //     } else {
            //         console.log('event.data,,,',event.data)
            //         text.value += event.data
            //         console.log('text.value,,,',text.value)
            //     }
            //   }
            // }

            const obj = JSON.parse(event.data)
            const objcontent = obj.content
            chat = {
                role: 'assistant',
                // content:result.data.data,
                showtype: obj.type,
                submodel: obj.modelType,  //a-1
                msggroup: chatId,
                msgId: obj.msg_answer_id,
                islike: true,
              }
              resObj.value = JSON.parse(event.data)
              const lengthnum = chatList.value.length
              chatList.value[lengthnum-1].msgId =  obj.msg_question_id
              n = 1
              console.log('obj,',obj)
              if(obj.type == 'tem'){ 
                eventSource.close()
                if(sxxzType.value.submodel == 'a-7'){
                  if(obj.content.totalCount){
                    chat.questionType = 1
                    obj.content.noTab = true
                  } else {
                    chat.questionType = 2
                  }
                }
                chat.content = JSON.parse(event.data)
                chat.copyText = JSON.parse(event.data)
                chatList.value.push(chat)
                console.log('对话list：：：', chatList.value)
              } else if(obj.type == 'gpt'){
                step.value = 2
                console.log('obj',obj)
              
                // if (event.data.indexOf('<br><br>') != -1) {
                //     event.data = event.data.replace('<br><br>', '\n\n')
                // }
                // if(event.data.indexOf('<br>') != -1){
                //   event.data = event.data.replace('<br>','\n')
                // }
               
                // if(obj.content == '[DONE]'){
                //     console.info('结束')
                //     loading.value = false
                //     chat.copyText = text.value
                //     chat.content = marked(text.value)
                //     chatList.value.push(chat)
                //     text.value = ''
                //     htmlText.value = ''
                //     step.value = 3
                //     n=2
                //     likeLoading.value = false
                //     eventSource.close()
                // }else{
                  console.log('event.data,,,',objcontent)
                  text.value += objcontent
                  console.log('text.value,,,',text.value)
                // }
              } else if (obj.type == 'error'){
                    console.info('error')
                    if(obj.code == 6001){
                      EventBus.$emit('goSubscribe')
                    }
                    loading.value = false
                    text.value = ''
                    htmlText.value = ''
                    step.value = 3
                    n=2
                    eventSource.close()
              }  if(obj.content == '[DONE]'){
                    console.info('结束')
                    loading.value = false
                    chat.showtype = 'gpt'
                    chat.copyText = text.value
                    chat.content = marked(text.value)
                    chatList.value.push(chat)
                    text.value = ''
                    htmlText.value = ''
                    step.value = 3
                    n=2
                    likeLoading.value = false
                    eventSource.close()
                } 
          };
          eventSource.onerror = (error) => {
              console.error('EventSource failed:', error)
              loading.value = false
              loadingmodel.value = ''
              step.value = 3
              eventSource.close()
          };
          eventSource.stream();
        }catch(error){

        }
            
      }
      const showdislikeDialog = (item) => {
        likeItemObj.value = item
        disLikeDialog.value = true
      }
      const closeDisLike = () => {
        disLikeDialog.value = false
      }
              
      EventBus.$on('sendMessage', sendMessage)

      onUnmounted(() => {
        EventBus.$off('sendMessage', sendMessage)
      })
      return {
        chatList,
        loading,
        step,
        showText,
        chatContent,
        sendMessage,
        scrollToBottom,
        chatType,
        chageTab,
        chageRankTab,
        rankPage,
        getXingzuoRanking,
        resObj,
        getHoroscopeData,
        chatNum,
        screenWidth,
        loginStatus,
        text,
        stopText,
        htmlText,
        apiurl,
        v1chatUrl,
        chatlist_index,
        likeHandle,
        showdislikeDialog,
        closeDisLike,
        disLikeDialog,
        selectStatus,
        selectType,
        shareLinkHandle,
        deleteChat,
        copyHandle,
        // likeType,
        sharelink,
        likeItemObj,
        likeLoading,
        userModel,
        haveCount,
        dateVal,
        timeVal,
        gender,
        sendDateTime,
        // RelatedQuestions,
      } 
    },
    components: {
      TextComponents,
      Horoscope,
      ConstellationRankingList,
      ConstellationRankingItem,
      ZodiacQuery,
      ConstellationInquir,
      BirthdatePassword,
      ChineseZodiacFortune,
      DescendingZodiac,
      BirthdayFlower,
      BirthdayBook,
      ConsteBloodPersonality,
      Ascendant,
      MoonSign,
      Constellations48,
      CheatingPerson,
      AstrologicalChart,
      AstrologicalHouseChart,
      PlanetInHouse,
      PlanetInSign,
      DisLikeReason,
      DateTimeSelect,
    },
    watch:{
      chatNum(val,old){
        if(!this.$route.query.type) return
        EventBus.$emit('getMsgGroupList')
      },
      selectStatus(val,old){
        if(val == false){
          this.chatList.forEach(item =>{
            item.choose = false
            item.funshow = false
            item.sharePopover = false
          })
        }
      }
    },
    methods: {
      //文字展示完成的回调
      onComplete(text, obj){
        const self = this
        const chat = {
            role: 'assistant',
            content:text,
            copyText:text,
            showtype: 'text',
            submodel: obj.modelType,  //a-1
            msggroup: obj.msggroup,
        }
        self.chatList.push(chat)
        self.loading = false
        setTimeout(() => {
            self.step = 3
        },100)
      },
      // 重新响应
      regenerateResponse(){
        // if(!this.haveCount){
        //   EventBus.$emit('goSubscribe')
        //   return
        // }
        const userList = this.chatList.filter( item => item.role == 'user' && !item.islike)
        this.sendMessage(
          {
            question: userList[userList.length - 1].content,
            base64String: userList[userList.length - 1].base64_content,
            base64_type: userList[userList.length - 1].base64_type,
          }
        )
        const self = this
        setTimeout(() => {
            self.scrollToBottom() 
        },500)
      },
      //停止响应
      stop(){
          this.$refs.TextComponents.stop()
      },
      onHover(item){  //鼠标经过展示三点 其他功能
        item.funshow =  true
      },
      onMouseLeave(item){
        if(item.sharePopover) return
        item.funshow= false
      },
      shareHandle(item){
        item.choose = true
        this.$store.commit('setSelectStatus', true)
        this.$store.commit('setSelectType', 'share')
      },
      deleteHandle(item){
        item.choose = true
        this.$store.commit('setSelectStatus', true)
        this.$store.commit('setSelectType', 'delete')
      }
    },
    mounted() {
      EventBus.$on('shareLinkHandle', this.shareLinkHandle)
      EventBus.$on('deleteChat', this.deleteChat)
      EventBus.$on('likeHandle', (type,obj) => {
        this.likeHandle(type,obj)
      })
    },
    unmounted() {
      EventBus.$off('shareLinkHandle', this.shareLinkHandle)
      EventBus.$off('deleteChat', this.deleteChat)
      EventBus.$off('likeHandle', (type,obj) => {
        this.likeHandle(type,obj)
      })
    },
  }
  </script>
  
  <style scoped lang='scss'>
  .chat{
      width: 98%;
      height: calc(100% - 0.8rem);
      margin: 0 auto;
      overflow: hidden;
      overflow-y: auto;
      padding: 0rem 1.5rem 0;
      padding-bottom: 1.2rem;
      margin-top: .8rem;
      // height: calc(100% - 1.2rem);
      &::-webkit-scrollbar {
          width: 2px; /* 滚动条的宽度 */
          height: 5px; /* 滚动条的高度 */
      }
      &::-webkit-scrollbar-track {
          background-color: #888; /* 滚动条轨道的背景颜色 */
      }
      &::-webkit-scrollbar-thumb {
          background-color: #333333; /* 滚动条拇指的颜色 */
          border-radius: 2px; /* 拇指的边框半径 */
      }
      .chat-list{
              text-align: left;
              display: flex;
              margin-top: .3rem;
              // &:last-child{
              //   padding-bottom: 1rem; 
              // }
              .select{
                margin-right: .2rem;
                img{
                  width: .4rem;
                }
              }
             &.right-content{
              justify-content: flex-end;
              .select{
                display: flex;
                justify-content: flex-start;
                align-items: center;
                flex: 1;
              }
             }
              .question,.answer{
                  display: flex;
                  width:100%;
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
                      align-items:flex-start;  
                      .inner{
                          padding: .25rem .4rem;
                          // font-size: 12px;
                          font-size: .259rem;
                          line-height: 16px;
                          font-family: Poppins-Regular, Poppins;
                          max-width: calc(100% - 1rem);
                          cursor:default;
                      }
                  }
                  .record-content{
                      width: 100%;
                      margin-left: .1rem;
                  }
              }
              .question{
                  .text-content{
                      justify-content: flex-end;
                      .inner{
                        margin-right: .1rem; 
                        background: #FFECBD;
                        border-radius: .3rem .1rem  .3rem  .3rem;
                        color: #000000;
                        word-break: break-all;
                        cursor:default;
                        img{
                          width: 100%;
                          height: 100%;
                          margin-bottom: 0.2rem;
                        }
                      }
                  }
                 
              }
              .answer{
                  .text-content{    
                    .inner{
                      margin-left: .1rem;
                      background: linear-gradient(270deg, #341B00 0%, #140B00 100%);
                      border-radius:  0.1rem 0.3rem 0.3rem 0.3rem;
                      position: relative;
                      color: #ffefdd;
                      line-height: 0.45rem;
                      font-size:  0.259rem;
                      cursor:default;
                      // font-size: .24rem;
                      .zindex{
                          z-index: 1111;
                          position: relative;
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
                    }
                  }
              }
      }
      .chatBotton{
        display: flex;
        margin-left: 1.1rem;
        margin-top: 0.1rem;
        font-size: .259rem;
        .share{
          background: #FFF5E5;
          border-radius: .55rem;   
          color: #FF870F;
          display: flex;
          align-items: center;
          height: .7rem;
          padding: 0 .3rem;
          cursor: pointer;
          margin-right: .2rem;
          img{
            margin-right: .1rem;
          }
        }
        .likediv{
          width: 1.81rem;
          border-radius: .55rem;   
          color: #2C2216;
          display: flex;
          align-items: center;
          justify-content: center;
          height: .7rem;
          // padding: 0 .3rem;
          border: 1px solid #130A00;
          cursor: pointer; 
          margin-right: .2rem;
          img{
            margin-right: .1rem;
          }
        }
        .chooseIsLike{
          width: 1rem;
          border-radius: .55rem;   
          display: flex;
          align-items: center;
          justify-content: center;
          height: .7rem;
          // padding: 0 .3rem;
          border: 1px solid #FF3D00;
          cursor: pointer; 
          margin-right: .2rem;
        }
        &.mb_chatBotton{
            margin-left: .1rem;
          }

      }
      &.mb-chat{
        padding: 0rem 5% 0;
        margin-top: .3rem;
        height: calc(100% - 0.3rem);
        padding-bottom: 1.2rem;
        .chat-list{
          .select{
            margin-right: .3rem;
            img{
              width: .4rem;
            }
          }
          .answer{
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
              &.mb{
                justify-content: space-between;
                .left{
                  display: flex;
                  align-items: center;
                }
              }
            }
            .text-content{
              margin-top: .2rem;
              .inner{
                max-width: 100%;
                cursor:default;
              }
            }
          }
        }
      }
  }
  .setList{
        display: flex;
        width: 240px;
        margin: 0 auto;
        justify-content: space-around;
        .list{
          display: flex;
          align-items: center;
          // margin-right: .2rem;
          cursor: pointer;
          font-size: 0.26rem;
          font-family: Poppins-Regular, Poppins;
          img{
            margin-right: .05rem;
            width: .5rem;
          }
        }
        .xian{
          background: #FFFFFF;
          height: 20px;
          opacity: 0.6;
          width: 1px;
        }
        &.mb-setList{
          width: 200px;
        }
      }
  
  </style>
  <style>
  .el-popper[data-popper-placement^=top] .el-popper__arrow::before {
    background: #000000;
}

  .three-bounce {
      text-align: left;
      display: flex;
      align-items: center;
  }
  .three-bounce .one {
      -webkit-animation-delay: -.32s;
      animation-delay: -.32s;
  }
  .three-bounce .two {
      -webkit-animation-delay: -.16s;
      animation-delay: -.16s;
  }
  .three-bounce>div {
      display: inline-block;
      width: 14px;
      height: 14px;
      border-radius: 100%;
      top: 50%;
      background: #aeadba;
      -webkit-animation: bouncedelay 1.4s infinite ease-in-out;
      animation: bouncedelay 1.4s infinite ease-in-out;
      -webkit-animation-fill-mode: both;
      animation-fill-mode: both;
  }
  
  @keyframes bouncedelay {
      0%,100%,80% {
          transform: scale(0);
          -webkit-transform: scale(0)
      }
  
      40% {
          transform: scale(1);
          -webkit-transform: scale(1)
      }
  }
  </style>