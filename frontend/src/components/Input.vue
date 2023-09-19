<!-- 用户输入框 -->
<template>
  <div class="input" :class="screenWidth<=900?'mb':''">
    <template v-if="!selectStatus">
      <input type="text" v-model="question" placeholder="请输入一些内容..." v-on:keyup.enter="sendMessage" @focus="focusHandle">
      <!--  v-if="loginStatus" -->
      <!-- <div v-if="!loginStatus" class="noLogin" @click="focusHangle">请输入一些内容...</div> -->
      <div class="send" @click="sendMessage">
          <!-- <img src="/@/assets/images/sentBnt.svg" alt=""> -->
          发送
      </div>
    </template>
    <template v-if="selectStatus">
      <div class="colse" @click="closeHandle">取消</div>
     
      <div class="delect" v-if="selectType == 'delete'" @click="deleteChat">
        <img src="/@/assets/images/deleteChat.png" alt="" srcset="">
        删除
      </div>
      <template v-if="selectType == 'share'">
        <div class="share"  @click="shareLink('link')">
        <img src="/@/assets/images/shareLink.png" alt="" srcset="">
          复制链接
        </div>
        <div class="sharebox" v-if="screenWidth>900">
          <ul>
            <li @click="shareLink('twitter')"> 
              <img src="/@/assets/images/twitter.png" alt="">
            </li>
            <li @click="shareLink('facebook')">
              <img src="/@/assets/images/facebook.png" alt="">
            </li>
            <!-- <li @click="shareLink('Instagram')">
              <img src="/@/assets/images/Instagram.png" alt="">
            </li> -->
            <li @click="shareLink('weibo')">
              <img src="/@/assets/images/weibo.png" alt="">
            </li>
            <!-- <li @click="shareLink('weChat')">
              <img src="/@/assets/images/friendsCircle.png" alt="">
            </li> -->
            <li @click="shareLink('QQspace')">
              <img src="/@/assets/images/QQspace.png" alt="">
            </li>
          </ul>
        </div>
        <div class="sharebox-mb" v-else @click="showMoreShareDialog">
         <img src="/@/assets/images/moreShare.png" alt="" srcset="">
        </div>
      </template>

    </template>
  </div>
  <moreShareMb
    :moreShareDialog="moreShareDialog"
    @closeMoreShareDialog="closeMoreShareDialog"
    ref="moreShare"
  />
</template>

<script>
 import moreShareMb from '/@/components/ChatComponent/moreShareMb.vue'
import { ref, computed, watch, onUnmounted } from 'vue';
import { useStore} from 'vuex'
import EventBus from '/@/utils/EventBus.js'
import { loginOut,payAccount } from '/@/api/api'
export default {
  name: '',
  setup() {
    const store = useStore()
    const selectStatus = computed(() => store.state.selectStatus)
    const selectType = computed(() => store.state.selectType)
    const sharelink = computed(() => store.state.sharelink)//分享链接
    const userModel = computed(() => store.state.userModel)
    const moreShareDialog = ref(false)
    const userAccountInfo = ref({})
    const haveCount =computed( () => store.state.haveCount) // 是否有条数
    //适配
    const screenWidth = computed( () => {
      return store.state.screenWidth
    })
    const question = computed({
      get: () => store.state.question,
      set: (newValue) => {
        store.commit('setQuestion', newValue)
      }
    })
    const sendMessage = () => {
      // if(loginStatus.value == false){
      //   EventBus.$emit('showLoginHandle')
      //   return
      // }
      if(haveCount.value == false){
        EventBus.$emit('goSubscribe')
        return
      }
      EventBus.$emit('sendMessage', question.value)
    }
    // 登录状态
    const loginStatus = computed( () => {
      return store.state.loginStatus
    }) 
    // 焦点进入判断是否登录
    const focusHangle = () => {
      if(loginStatus.value == false){
        EventBus.$emit('showLoginHandle')
      }
    }
    const shareLink = (mul) => {
      EventBus.$emit('shareLinkHandle',mul)
    }
    const deleteChat = ()=>{
      EventBus.$emit('deleteChat')
    }
    const shareMultimedia = (mul)=>{
      const u = encodeURIComponent(sharelink.value)
      const shareTitle = encodeURIComponent('你不知道自己的命运，但是AI也许知道！快来天机阁免费体验')
      console.log('u,,,,,,',u)
      if(mul == 'twitter'){
        window.open(`https://twitter.com/intent/tweet?text=${shareTitle}&url=${u}`)
      }
      if(mul == 'facebook'){
        window.open(`https://www.facebook.com/sharer/sharer.php?quote=${shareTitle}&u=${u}`)
      }
      if(mul=='Instagram'){
        window.open(`instagram://share?text=${shareTitle}&url=${u}`)
      }
      if(mul=='weibo'){
        window.open(`https://service.weibo.com/share/share.php?title=${shareTitle}&url=${u}`)
      }
      // if(mul=='weChat'){
      //   if (navigator.share && navigator.canShare) {
      //   // 检查浏览器是否支持分享功能
      //   navigator
      //     .share({
      //       text: '',
      //       url: u
      //     })
      //     .then(() => {
      //       console.log("分享成功！");
      //     })
      //     .catch(error => {
      //       console.error("分享失败：", error);
      //     });
      //   }
      // }
      if(mul=='QQspace'){
        window.open(`http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?title=${shareTitle}&url=${u}`)
        // window.open(`http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?title=${encodeURIComponent(shareTitle)}&summary=${encodeURIComponent(shareSummary)}&url=${encodeURIComponent(shareURL)}&pics=${encodeURIComponent(sharePics.join('|'))}`)
      }
    }
    const showMoreShareDialog = () => {
      moreShareDialog.value = true
    }
    const closeMoreShareDialog = () => {
      moreShareDialog.value = false
    }
    const getUserPayAccount = async () =>{
      if(!loginStatus.value || userModel.value=='3.5'){
        // haveCount.value = true
        store.commit('setHaveCount',true)
        return
      }
      const result = await payAccount({}) 
      if(result.code == 200){
        userAccountInfo.value = result.data
        // userAccountInfo.value ={
        //     "allowance_num": 0,
        //     "user_account": {
        //         "id": 86278752300044288,
        //         "userid": 44,
        //         "terminable_card_type": null,
        //         "terminable_time": null,
        //         "terminable_time_history_total": null,
        //         "un_terminable_card_type": 1,
        //         "un_terminable_time": 0,
        //         "un_terminable_time_history_total": 1,
        //         "due_date": null
        //     }
        // }
        // userAccountInfo.value.user_account = null
        // userAccountInfo.value.allowance_num=0
        // userAccountInfo.value.user_account.terminable_time = 0
        // userAccountInfo.value.user_account.un_terminable_time = 0
        if(!userAccountInfo.value.user_account ){
          if(userAccountInfo.value.allowance_num == 0){
            // EventBus.$emit('goSubscribe')
            // haveCount.value = false
            store.commit('setHaveCount',false)
            return
          }else{
            // haveCount.value = true
            store.commit('setHaveCount',true)
          }
        }else if(!userAccountInfo.value.user_account?.terminable_time && !userAccountInfo.value.user_account?.un_terminable_time){
          if(userAccountInfo.value.allowance_num == 0){
            // EventBus.$emit('goSubscribe')
            // haveCount.value = false
            store.commit('setHaveCount',false)
            return
          }else{
            // haveCount.value = true
            store.commit('setHaveCount',true)
          }
        }else{
          // if(!userAccountInfo.value.user_account && !userAccountInfo.value.user_account.terminable_time && userAccountInfo.value.user_account.un_terminable_time){
            // EventBus.$emit('goSubscribe')
            store.commit('setHaveCount',true)
            // haveCount.value = false
          //   return
          // }else{
          //   store.commit('setHaveCount',true)
          //   // haveCount.value = true
          // }
        }
      }
    }
    const focusHandle = () =>{
      if(haveCount.value == false){
        EventBus.$emit('goSubscribe')
      }
    }
    EventBus.$on('shareMultimedia', shareMultimedia)
    EventBus.$on('shareLink', shareLink)
    onUnmounted(() => {
      EventBus.$on('shareMultimedia', shareMultimedia)
      EventBus.$on('shareLink', shareLink)
    })
    return {
        question,
        sendMessage,
        loginStatus,
        focusHangle,
        screenWidth,
        selectStatus,
        shareLink,
        selectType,
        deleteChat,
        shareMultimedia,
        sharelink,
        moreShareDialog,
        showMoreShareDialog,
        closeMoreShareDialog,
        getUserPayAccount,
        userModel,
        haveCount,
        focusHandle,
        haveCount,
    } 
  },
  components: {
    moreShareMb,
  },
  created() {
    this.init()
  },
  methods: {
    closeHandle(){
      this.$store.commit('setSelectStatus', false)
    },
    init(){
      clearInterval(this.timer)
      this.getUserPayAccount()
      this.timer = setInterval(() => {
        this.getUserPayAccount()
      }, 5000)
    }
  },
  mounted() {
   
  },
  unmounted() {
    clearInterval(this.timer)
  },
}
</script>

<style scoped lang='scss'>
.input{
    margin: 0 auto;
    width: 75%;
    display: flex;
    align-items: center;
    margin-bottom: .2rem;
    input,.noLogin,.share,.delect{
        flex: 1;
        height: 1rem;
        background: #130A00;
        box-shadow: 0px 4px 20px -6px rgba(0,0,0,0.15);
        border-radius: .3rem;
        border: none;
        outline: none;
        font-size: .296rem;
        color: #FFFFFF;
        outline: none;
        box-sizing: border-box;
        padding: 0 .3rem;
        line-height: 1rem;
        cursor: pointer;
    }
    // .share{
    //   width: ;
    // }
    .noLogin{
      color: #757575;
      line-height: 1rem;
    }
    .share{
      text-align: center;
    }
    .send{
        margin-left: .4rem;
        cursor: pointer;
        width: 2.759rem;
        height: 1.129rem;
        line-height: 1.129rem;
        text-align: center;
        background: url(/@/assets/images/sentBnt.svg) no-repeat 100% 100%;
        background-size: cover;
        color: #000000;
        font-size: 0.33rem;
    }
    .colse{
      background: #130A00;
      box-shadow: 0px 4px 20px -6px rgba(0,0,0,0.15);
      border-radius: .37rem;
      height: 1rem;
      line-height: 1rem;
      width: 2.759rem;
      text-align: center;
      margin-right: .3rem;
      cursor: pointer;
      // flex: 1;
    }
    .delect{
      display: flex;
      align-items: center;
      justify-content: center;
      background: #750000;
    }
    .sharebox{
      // flex: 2;
      margin-left: .2rem;
      ul{
        display: flex;
        align-items: center;
        flex-wrap: nowrap ;
        li{
          cursor: pointer;
          margin-left: .1rem;
          img{
            width: .9rem;
          }
        }
      }
    }
    .sharebox-mb{
      background: #130A00;
      box-shadow: 0px 4px 20px -6px rgba(0,0,0,0.15);
      border-radius: .37rem;
      width: 1.3rem;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 1rem;
      margin-left: .2rem;
      img{
        width: 0.5rem;
      }
    }
    &.mb{
      width: 85%;
    }
}
</style>