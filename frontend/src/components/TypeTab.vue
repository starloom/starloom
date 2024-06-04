<template>
  <div class="chatType">
        <div class="mb-top" v-if="screenWidth<=900">
            <div class="add-chat" @click="addChat('add')">
                {{ $t('addChat') }}
            </div>
            <div @click="closeMenuHandle">
                <img src="/@/assets/images/menu-close.png" alt="">
            </div>
        </div>
        <div class="tab">
          <!-- {{ $t('navs') }} -->
            <div class="item" @click="changeChatType('navs')" :class="chatType == 'navs' ? 'active' : ''">{{ $t('navigation') }}</div>
            <div class="item" @click="changeChatType('Chats')" :class="chatType == 'Chats' ? 'active' : ''">{{ $t('askReddit') }}</div>
        </div>
        <div class="serach-content">
            <input v-model="searchText" type="text" :placeholder="$t('search')">
            <img class="search-icon" src="/@/assets/images/search.svg" alt="">
        </div>
        <template v-if="chatType == 'navs'">
            <ul class="coin-list" v-if="showtabList" :class="screenWidth>900? '' : 'mb'">
                <li @click="chooseType(item)" v-for="(item, index) in showtabList" :key="index" :class="item.type == navQueryType.type ? 'active' : ''">
                    <img :src="item.img" alt="">
                    <div class="mid"> 
                      {{  $t(item.displayName ) }} 
                    </div>
                    <div v-if="item.type == navQueryType.type">
                      <img class="activeimg" src="/@/assets/images/activeType.png" alt="">
                    </div>
                </li>
            </ul>
        </template>
        <template v-if="chatType == 'Chats'">
            <!--  !loading-->
            <div class="chat-list">
                <div class="setting">
                        <div>
                            <div v-if="edit" style="padding-left: .2rem;cursor:pointer">
                                <div v-if="!selectAll" @click="selectAllHandle('all')" class="check"></div>
                                <div v-else @click="selectAllHandle('clear')" class="check select">✓</div>
                            </div>
                        </div>
                        <div>
                            <img v-if="checkIsDelete && edit" @click="deleteHandle" src="/@/assets/images/delete.svg" alt="">
                            <img @click="edit = false" v-if="edit" src="/@/assets/images/close.svg" alt="">
                            <img @click="editHandle" v-if="!edit" src="/@/assets/images/edit.svg" alt="">
                        </div>
                </div>
                <ul v-if="loginStatus">
                    <li v-for="(item,index) in showChatList" :key="index" @click="chooseList(item)" :class="item.msggroup == queryId ? 'active' : ''">
                        <template v-if="edit">
                            <div v-if="!item.choose" class="check"></div>
                            <div v-else class="check select">✓</div>
                        </template>
                        <div class="text">
                            {{ item.base64_type == 1 ? '图片解析' : item.base64_type == 2 ? '语音解析' : item.content}}
                        </div>
                          <!-- <img src="/@/assets/imgs/star.svg" alt=""> -->
                    </li>
                </ul>
            </div>
        </template>
        <div class="add-chat" v-if="screenWidth>900" @click="addChat('add')">
            {{ $t('addChat') }}
        </div>
  </div>
</template>

<script>
import { ref, computed, watch, onUnmounted, getCurrentInstance } from 'vue';
import { useStore} from 'vuex'
import { useI18n } from 'vue-i18n'
import { useRouter, useRoute } from 'vue-router'
import EventBus from '/@/utils/EventBus.js'
import { getMsgGroupList, delMsgGroupList } from  '/@/api/api.js'
import axios from 'axios'
export default {
  name: '',
  setup() {
    const router = useRouter()
    const route = useRoute()
    const store = useStore()
    const instance = getCurrentInstance();
    // 登录状态
    const loginStatus = computed( () => {
      return store.state.loginStatus
    }) 
    const { t } = useI18n();
    const loading = ref(false) //加载状态
    const navQueryType = computed({
      get: () => store.state.navQueryType,
      set: (newValue) => {
        store.commit('setNavQueryType', newValue)
      }
    })
    //适配
    const screenWidth = computed( () => {
      return store.state.screenWidth
    })
    // 切换导航里的tab
    const chooseType = (item) => {
        router.push({ name: 'index' })
      store.commit('setNavQueryType', item)
      store.commit('setImgBase64', '')
      EventBus.$emit('closeVectorHandle')
      if(screenWidth.value<=900){
        instance.proxy.closeMenuHandle()
      }
    }
    const  changeChatType = async (type)=>{
        // chatType.value = type
        if(type=='navs'){
            store.commit('setChatType', type)
            router.push({ name: 'index' })
            chatList.value = []
        } else if (type=='Chats' && chatType.value != 'Chats'){
            store.commit('setChatType', type)
            await instance.proxy.getMsgGroupList()
            addChat()
            // router.push({ name: 'askDivination' })
        }
        EventBus.$emit('closeVectorHandle')
        store.commit('setImgBase64', '')
        store.commit('setSelectStatus', false)
        store.commit('setSelectType', '')
    }
    const chooseList = (item) =>{
        if(edit.value){
            item.choose = !item.choose
        }else{
            // EventBus.$emit('closeDrawer', '')
            router.push({ path: `/askDivination/${item.msggroup}` })
            if(screenWidth.value<=900){
                instance.proxy.closeMenuHandle()
            }
        }
    }
    const chatType = computed(() => store.state.chatType)
    const tabList = computed(()=> store.state.tabList)
    const chatList = ref([])
    //搜索
    watch(() => chatType.value,(val) => {
        searchText.value = ''
    })
    const showtabList = computed(() => {
        if(searchText.value == ''){
            return tabList.value
        }else{
            const list = tabList.value.filter(item => t(item.displayName).indexOf((searchText.value)) != -1)
            return list
        }
    })
    const showChatList = computed(() => {
        if(searchText.value == ''){
            return chatList.value
        }else{
            const list = chatList.value.filter(item => item.content.indexOf((searchText.value)) != -1 )
            return list
        }
    })
    const queryId = ref(route.params.id)
    watch(() => route.params.id,(val, oldCoinCode) => {
        queryId.value = val
    })
    const addChatList = (obj) => {
        store.commit('setChatType', 'Chats')
        chatList.value.unshift(obj)
    }

    //删除聊天记录列表
    const deleteHandle = async() => {
        const deletaList = chatList.value.filter( item => item.choose)
        if(deletaList.length == 0) return
        const id = []
        deletaList.forEach(item => {
            id.push(item.msggroup)
        })
        ElMessageBox.confirm(
            t('deleteSure'),
            '',
            {
                confirmButtonText: t('sure'),
                cancelButtonText: t('cancel'),
                // type: 'warning',
                cancelButtonClass: 'cancel',
                confirmButtonClass:'ok'
            }
        )
        .then(async() => {
            const result = await delMsgGroupList({
                msggroup: id
            })
            chatList.value =  chatList.value.filter(item => !item.choose)
            edit.value = false
            // 判断当前聊天页面是否被删除
            const ishave = chatList.value.filter( item => item.msggroup == queryId.value)
            if(ishave.length == 0){
                //当前路由被删除
                router.push({ path: `/askDivination/${chatList.value[0].msggroup}` })
            }
        })
        .catch(() => {
           
        })
    }
    const addChat = async (type) => {
        if(type=='add'){
            if(loginStatus.value == false){
                ElMessageBox.confirm(
                    '请您登录以获得更加优质的使用体验',
                    '',
                    {
                        confirmButtonText: '登录/注册',
                        cancelButtonText: t('cancel'),
                        cancelButtonClass: 'cancel',
                        confirmButtonClass:'ok'
                    }
                )
                .then(() => {
                    EventBus.$emit('showLoginHandle')
                })
                .catch(() => {
                
                })
                return
            }
        }
        if(chatType.value != 'Chats'){
            await instance.proxy.getMsgGroupList()
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
        if(screenWidth.value<=900){
            instance.proxy.closeMenuHandle()
        }
    }
    EventBus.$on('addChatList', addChatList)
    onUnmounted(() => {
      EventBus.$off('addChatList', addChatList)
    })
    const searchText = ref('')
    const edit = ref(false)
    const checkIsDelete =  computed(() => {
        const list = chatList.value
        let _b = false
        list.forEach(item => {
            if(item.choose){
                 _b = true
            }
        })
        return _b
    })
    const coinList = ref([])
    // 聊天记录全选
    const selectAll = computed( () => {
        let status = true
        chatList.value.forEach( item => {
            if(!item.choose){
                status = false
            }
        })
        return status
    })
    const selectAllHandle  = (type) => {
        if(type == 'all'){ // 全选
            chatList.value.forEach( item => {
                item.choose = true
            })
        }else{
            chatList.value.forEach( item => {
                item.choose = false
            })
        }
    }
    return {
        chatType,
        searchText,
        edit,
        chatList,
        checkIsDelete,
        chooseList,
        coinList,
        tabList,   // 分割线
        navQueryType,
        chooseType,
        changeChatType,
        showtabList,
        addChat,
        showChatList,
        addChatList,
        deleteHandle,
        queryId,
        selectAll,
        selectAllHandle,
        loginStatus,
        loading,
        screenWidth,
    } 
  },
  components: {
    
  },
  watch:{
    loginStatus(val, old){
       if(val){
        this.getMsgGroupList()
       }
    },
    // chatType(val, old){
    //    if(val=="Chats"){
    //     this.getMsgGroupList()
    //    }
    // }
  },
  methods: {
    FloatingNumber(str){
        if(str.indexOf('-') == -1){
            return true
        }else{
            return false
        }
    },
    editHandle(){
        this.edit = true
        this.chatList.forEach( item => {
            item.choose = false
        })
    },
    // changeChatType(type){
    //     // chatType.value = type
    //     if(type=='navs'){
    //         this.$store.commit('setChatType', type)
    //         this.$router.push({ name: 'index' })
    //     } else if (type=='Chats' && chatType.value != 'Chats'){
    //         this.$store.commit('setChatType', type)
    //         this.getMsgGroupList()
    //         addChat()
    //         // router.push({ name: 'askDivination' })
    //     }
    // },
    async getMsgGroupList(){
        if(!localStorage.getItem('starloomAI-token')) return
        this.loading = true
        const res = await getMsgGroupList()
        if(res.code == 200){
            if(this.chatList.length == 1){
                const msggroup = this.chatList[0].msggroup
                const isHave = res.data.messageList.filter(item => item.msggroup == msggroup)
                if(isHave.length == 0){
                    this.chatList = [...this.chatList,...res.data.messageList.reverse()]
                }else{
                    this.chatList = res.data.messageList.reverse()
                }
            }else{
                this.chatList = res.data.messageList.reverse()
            }
        }
        this.loading = false
    },
    closeMenuHandle(){
        // this.$emit("closeDrawer")
        EventBus.$emit('closeDrawer', '')
    }
  },
  mounted() {
    this.getMsgGroupList()
    EventBus.$on('getMsgGroupList', () => {
        this.getMsgGroupList()
    })
  },
  unmounted() {
    EventBus.$off('getMsgGroupList', () => {
      this.getMsgGroupList()
    })
  },
}
</script>

<style scoped lang='scss'>
.chatType{
    height: 100%;
    display: flex;
    flex-direction: column;
}
.mb-top{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: .4rem;
    img{
        width: 1rem;
    }
    .add-chat{
        margin-top: 0;
        width: calc(100% - 1.4rem);
    }
}
.tab{
    width: 100%;
    display: flex;
    height: .8888rem;
    background: #443228;
    box-shadow: 0px 4px 20px -6px rgba(0,0,0,0.15);
    border-radius: .3rem;;
    .item{
        border-radius: .3rem;
        font-size: .296rem;
        font-family: Alimama-DongFangDaKai;
        color: #FFFFFF;
        flex: 1;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        &.active{
            background: #ffcd55;
            box-shadow: 0px 4px 20px 0px rgba(0,0,0,0.15);
            opacity: 1;
            border-image: linear-gradient(180deg, rgba(220, 180, 84, 1), rgba(254, 254, 158, 1)) 1 1;
            color: #443228;
        }
    }
}
.serach-content{
    margin-top: .2rem;
    width: 100%;
    position: relative;
    input{
        border: none;
        width: 100%;
        height: .9rem;                     
        background: #130A00;
        box-shadow: 0px 4px 20px -6px rgba(0,0,0,0.15);
        opacity: 1;
        border: 1px solid #5E5342;
        border-radius: .3rem;
        font-size: .296rem;
        color: #FFFFFF;
        outline: none;
        box-sizing: border-box;
        padding: 0 .3rem 0 .9rem;
    }
    .search-icon{
        position: absolute;
        left: .3rem;
        height: .38rem;
        width: .38rem;
        top: 50%;
        margin-top: -.19rem;
    }
}
.coin-list{
    flex: 1;
    margin-top: .2rem;
    padding: .3rem;
    border-radius: .3rem;
    padding-bottom: 1rem;
    overflow: hidden;
    overflow-y: auto;
    background: rgba(0,0,0,0.39);
    box-shadow: 0px 4px 20px -6px rgba(0,0,0,0.15);
    border: 1px solid #6B5C44;
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
    li{
        margin-top: 0.2rem;
        display: flex;
        align-items: center;
        cursor: pointer;
        padding: .1rem 0.2rem;
        border-radius: .37rem;
        font-family: Alimama-DongFangDaKai;
        color: #FFFFFF;
        height: 1.111rem;
        &.active{
          background: linear-gradient(360deg, #D8A01C 0%, #FFE29B 100%);
          border-radius: 15px;
          opacity: 1;
          color: #0A0600;
          border-image: linear-gradient(180deg, rgba(255, 238, 195, 1), rgba(255, 184, 0, 1)) 1 1;
        }  
        &:first-child{
            margin-top: 0;
        }    
        // img{
        //     width: 1rem;
        //     height: 1rem;
        // }
        // .activeimg{
        //   width: 0.8rem;
        //   height: 0.8rem;
        // }
        .mid{
            flex: 1;
            margin-left: .4rem;
            .coin-name{
                font-size: .296rem;
                color: #FFFFFF;
            }
            .coin-text{
                margin-top: .12rem;
                font-size: 12px;
                color: #a3adb1;
            }
        }
    }
    &.mb{
        img{
            width: .8rem;
        }
    }
}
.chat-list{
    flex: 1;
    margin-top: .2rem;
    padding: .3rem;
    border-radius: .3rem;
    padding-bottom: 1rem;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    background: rgba(0,0,0,0.39);
    opacity: 1;
    border: 1px solid #6B5C44;
    .setting{
        padding-bottom: .3rem;
        display: flex;
        justify-content: space-between;
        img{
            width: .37rem;
            height: .37rem;
            cursor: pointer;
            margin-right: .3rem;
        }
        .check{
            width: .37rem;
            height: .37rem;
            border-radius: 100px;
            border: 1px solid rgba(255,255,255,.5);
            margin-right: .2rem;
            &.select{
                border: 1px solid #ffffff;
                color: #ffffff;
                font-size: 12px;
                text-align: center;
                line-height: calc(.37rem - 2px);
            }
        }
    }
    ul{
        flex: 1;
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
    li{
        margin-top: .2rem;
        display: flex;
        align-items: center;
        cursor: pointer;
        padding: .2rem;
        border-radius: .1111rem;
        position: relative;
        font-size: .256rem;
        font-family: Inter-Medium, Inter;
        color: #FFFFFF;
        &:hover,&.active{
            background: rgba(63,63,63,0.5);
        }
        .check{
            width: .37rem;
            height: .37rem;
            border-radius: 100px;
            border: 1px solid rgba(255,255,255,.5);
            margin-right: .2rem;
            &.select{
                border: 1px solid #ffffff;
                color: #ffffff;
                font-size: 12px;
                text-align: center;
                line-height: calc(.37rem - 2px);
            }
        }
        &:first-child{
            margin-top: 0;
        }
        .text{
            width: calc(100% - 0.57rem);
        }
    }
}
.add-chat{
    cursor: pointer;
    margin-top: .3rem;
    width: 100%;
    height: .95rem;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: .296rem;
    color: #CEBA98;
    border-radius: .3rem;
    background: rgba(0,0,0,0.25);
    box-shadow: 0px 4px 20px -6px rgba(0,0,0,0.15);
    opacity: 1;
    border: 1px solid #6B5C44;
    &:hover{
      box-shadow: 0 2px 12px 0 rgba(255,255,255,.1);
    }
}
</style>