<template>
  <div class="chat" ref="chatContent" :class="screenWidth<=900? 'mb-chat' : ''">
    <div class="topDiv">
      <div>{{ $t('shareConversation') }}{{ time }}</div>
      <div class="try" @click="goIndex">
        {{ $t('trynow') }}
      </div>
    </div>
    <div class="chatListbox">
      <template v-for="(item,index) in chatList" :key="index">
          <!-- 文字对话 -->
          <!-- v-if="item.type  == 'text' || item.role == 'user'" -->
          <template  v-if="item.showtype  == 'text' || item.showtype  == 'gpt' || item.type  == 'text' || item.role == 'user'">
              <div class="chat-list" :class="item.role == 'user' ? 'right-content' : ''">
                  <div v-if="item.role == 'user'" class="question">
                  <div class="text-content">
                          <!-- v-html="item.content" -->
                          <div class="inner" >
                            <div v-if="item.base64_type == 1 && item.base64_content">
                              <img :src="item.base64_content" alt="">
                            </div>
                            {{ item.content }}
                          </div>
                  </div>
                  <img v-if="screenWidth>900" src="/@/assets/images/user.png" alt="">
                  </div>
                  <div v-if="item.role == 'assistant'" class="answer">
                    <div class="BotHeader">
                      <img class="avatar" :class="screenWidth<=900 ? 'mbImg' : ''" src="/@/assets/images/aibot.png" alt="">
                      <div v-if="screenWidth<=900">{{ $t('starloom') }}</div>
                    </div>
                      <div class="text-content">
                          <div class="inner" v-html="item.content">
                           
                          </div>
                          <!--   {{item.content}} --> 
                          <!-- v-html="item.content" -->
                      </div>
                  </div>
              </div>
          </template> 
          <template v-if="item.role == 'assistant' && item.showtype == 'tem'">
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
      </template>
    </div>
  
    <div class="xian">
      {{ $t('ContinueOnStarloom') }}
    </div>
    <div class="bottomDiv" :class="screenWidth<=900?'mb':''">
        
        <div  class="noLogin" @click="continueChatting">
            <img src="/@/assets/images/gochat.png" alt="" srcset="">
            {{ $t('continueChatting') }}
        </div>
        <div class="addBtn" @click="addChatHandle">
            <img src="/@/assets/images/add.png" alt="">
            {{ $t('addChat') }}
        </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, watch, onMounted, onUnmounted } from 'vue';
import { useStore} from 'vuex'
import { useRouter,useRoute } from 'vue-router'
import TextComponents from '/@/components/ChatComponent/TextComponents.vue'


import EventBus from '/@/utils/EventBus.js'
import { getUserSharechat } from '/@/api/api'
export default {
  name: 'Chat',
  setup() {
    const chatList = ref([])
    const time = ref('')
    const loading = ref(false) //加载状态
    const chatType = ref('') // 接口返回的 对话类型
    const step =  ref('1') //加载过程中的状态， 1 代表正在跟后台请求中， 2 代表 正在显示文字中 3 代表文字显示完毕或者用户中断回答
    const showText = ref('') // 回答的文本
    const chatContent = ref(null)
    const store = useStore()
    const route = useRoute()
    const router = useRouter()
    let shareKey = route.params.shareKey
    
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
    const goIndex = () => {
        router.push({ name: 'index' })
    }
    const sendMessage = async (questionText,queryData) => {

        // 监听对话的回调 目前分为预设1,2,3 以及文本对话
        console.log('问题内容：：：', questionText)
        if(loading.value || questionText == ''){
                return
        }
        const chat = {
            role: 'user',
            content:questionText,
        }
        chatList.value.push(chat)
        loading.value = true
        step.value = 1

        setTimeout(() => {
            scrollToBottom() 
            store.commit('setQuestion', '')
        },50)



        if(!queryData){
            try{
                const result = await mpcbot({
                    content: chatList.value,
                    sourceFlag: "widget",
                    sourceType: "H5",
                    equipmentNo:'0xcef7e44d13286e23782e12d654455f'

                })
                if(result.resCode == 800){
                    showText.value = result.data.content
                    step.value = 2
                    chatType.value = 'text'
                }else{
                    loading.value = false
                    step.value = 3
                }
            }catch(err){
                loading.value = false
                step.value = 3
            }
         }else if(queryData.type == 'preset1'){
            console.log('预设1')
            try{
                const result = await getKlineInfo({
                    code: queryData.code
                })
                if(result.code == 200){
                    const chat = {
                        role: 'assistant',
                        content:result.data,
                        type:'preset1',
                    }
                    chatList.value.push(chat)
                }
                loading.value = false
            }catch(error){

            }
         }else if(queryData.type == 'preset2'){
            console.log('预设2')
            try{
                const result = await getPresetTwo({
                    code: queryData.code
                })
                if(result.code == 200){
                    const chat = {
                        role: 'assistant',
                        content:result.data,
                        type:'preset2',
                    }
                    chatList.value.push(chat)
                }
                loading.value = false
            }catch(error){

            }
         }else if(queryData.type == 'preset3'){
            console.log('预设3')
            try{
                const result = await getData({
                    coin: 'ETH'
                })
                if(result.code == 200){
                    const chat = {
                        role: 'assistant',
                        content:result.data,
                        type:'preset2',
                    }
                    chatList.value.push(chat)
                }
                loading.value = false
            }catch(error){

            }
         }
    }
    const getChatList = async (key) =>{
      const result = await getUserSharechat({
        code: key,
      }) 
      if(result.code == 200){
        chatList.value = result.data.contents
        time.value =new Date(parseInt(result.data.time)).toLocaleString().replace(/:d(1,2)$/,' ') 
        return ;
      }
    }
    const addChatHandle = () =>{
        // if(type=='add'){
        //     if(loginStatus.value == false){
        //         ElMessageBox.confirm(
        //             '请您登录以获得更加优质的使用体验',
        //             '',
        //             {
        //                 confirmButtonText: '登录/注册',
        //                 cancelButtonText: t('cancel'),
        //                 cancelButtonClass: 'cancel',
        //                 confirmButtonClass:'ok'
        //             }
        //         )
        //         .then(() => {
        //             EventBus.$emit('showLoginHandle')
        //         })
        //         .catch(() => {
                
        //         })
        //         return
        //     }
        // }
        if(chatType.value != 'Chats'){
            store.commit('setChatType', 'Chats')
        }
        const time = new Date().getTime() + localStorage.getItem('userId')
        // EventBus.$emit('closeDrawer', '')
        router.push({ 
            path: `/askDivination/${time}`,
            query:{
                type: 'newChat'
            }
        })
    }
    const continueChatting =() =>{
      if(loginStatus.value){
        if(chatType.value != 'Chats'){
            store.commit('setChatType', 'Chats')
        }
        const chatid = chatList.value[0].msggroup
        router.push({ 
            path: `/askDivination/${chatid}`,
        })
      }else{
        localStorage.setItem('shareChatList',JSON.stringify(chatList.value))
        const time = new Date().getTime() + localStorage.getItem('userId')
        // EventBus.$emit('closeDrawer', '')
        router.push({ 
            path: `/askDivination/${time}`,
            query:{
                type: 'continueChat'
            }
        })
      }
    }
     
    
    onMounted(() =>{
      getChatList(shareKey)
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
      screenWidth,
      time,
      getChatList,
      goIndex,
      addChatHandle,
      continueChatting,
      loginStatus,
    } 
  },
  components: {
    TextComponents, 
  },
  methods: {
    //文字展示完成的回调
    onComplete(text){
      const self = this
      const chat = {
          role: 'assistant',
          content:text,
          type:'text',
      }
      self.chatList.push(chat)
      self.loading = false
      setTimeout(() => {
          self.step = 3
      },100)
  },
  // 重新响应
  regenerateResponse(){
    const userList = this.chatList.filter( item => item.role == 'user')
    this.sendMessage(userList[userList.length - 1].content)
    const self = this
    setTimeout(() => {
        self.scrollToBottom() 
    },500)
  },
  //停止响应
  stop(){
      this.$refs.TextComponents.stop()
  },
  },
  mounted() {
    
  },
 
}
</script>

<style scoped lang='scss'>
.chat{
    width: 100%;
    height: 100%;
    overflow: hidden;
    overflow-y: auto;
    padding: 0.4rem 6% 0;
    padding-bottom: .2rem;
    display: flex;
    flex-direction: column;
    color: #ffefdd;
    .topDiv{
      width: 98%;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      color: #271401;
      height: 1.3rem;
      border-bottom: 1px solid #A19581;
      padding-bottom: .3rem;
      // margin-bottom: .3rem;
      .try{
        border: 1px solid #130A00;
        color: #130A00;
        padding: 0 .3rem;
        border-radius: .4rem;
        line-height: .6rem;
        cursor: pointer;
      }
    }
    .chatListbox{
      height: calc(100% - 2.3rem);
      height: 100%;
      overflow: hidden;
      overflow-y: auto;
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
    }
    .chat-list{
              text-align: left;
              display: flex;
              margin-top: .3rem;
              // &:last-child{
              //   padding-bottom: 1rem; 
              // }
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
                      margin-left: .1rem;
                  }
              }
              .question{
                  .text-content{
                      justify-content: flex-end;
                      .inner{
                        margin-right: .1rem; 
                        background: #FFECBD;
                        border-radius: .25rem .1rem  .25rem  .25rem;
                        color: #000000;
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
                      border-radius:  .1rem  .25rem  .25rem .25rem;
                      position: relative;
                      color: #ffefdd;
                      line-height: 0.45rem;
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
      &.mb-chat{
        padding: 0.3rem 5% 0 6%;
        margin-top: .3rem;
        height: calc(100% - 0.3rem);
        // padding-bottom: 1.2rem;
       width: 98%;
        .chat-list{
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
            }
            .text-content{
              margin-top: .2rem;
            }
          }
        }
      }
    .xian{
        width: 100%;
        // background: #A19581;
        border-top: 1px solid #A19581;
        height: 1rem;
        line-height: 1.2rem;
        // margin-bottom: .5rem;
        color: #130A00;
        margin-top: .3rem;
    }
    .bottomDiv{
        margin: 0 auto;
        width: 100%;
        display: flex;
        align-items: center;
        margin-bottom: .2rem;
        color: #ffefdd;
        .noLogin{
            flex: 1;
            height: 1rem;
            background: #130A00;
            box-shadow: 0px 4px 20px -6px rgba(0,0,0,0.15);
            border-radius: .37rem;
            font-size: .296rem;
            box-sizing: border-box;
            padding: 0 .3rem;
            line-height: 1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            img{
                margin-right: .2rem;
            }
        }
        .addBtn{
            margin-left: .4rem;
            cursor: pointer;
            width: 2.759rem;
            height: 1rem;
            line-height: 1rem;
            text-align: center;
            background: #130A00;
            border-radius: 0.3rem;
        }
        &.mb{
        width: 85%;
        }
    }

}
// .bottom-input{
//         position: absolute;
//         bottom: .3rem; 
//         width: 100%;
//         left: 0;
//         display: flex;
//         justify-content: center;
//         .stop,.regenerateResponse{
//             border: 1px solid #ffffff;
//             border-radius: .1rem;
//             background: #161819;
//             cursor: pointer;
//             display: flex;
//             align-items: center;
//             height: .7rem;
//             font-size: .26rem;
//             font-family: Poppins-Regular, Poppins;
//             color: #ffffff;
//            img{
//                 width: .4rem;
//                 height: .4rem;
//                 margin-right: .1rem;
//             }
//         }
//     }
</style>
