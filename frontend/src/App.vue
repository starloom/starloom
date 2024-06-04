<template>
 <div class="main-app">
  <Header/>
  <div class="container" :class="screenWidth<=900?'mb-cont':''">
    <div class="left" v-if="screenWidth>900 && pathName != 'chat'">
      <TypeTab />
    </div>
    <div class="main-router">
      <img class="chatBg" src="/@/assets/images/chatBg.png" alt="">
      <div class="right">
        <div class="router-content">
          <router-view></router-view>
        </div>
        <InputContent v-if="pathName != 'chat'"/>
      </div> 
    </div>
  </div>
 </div>
  <selectModelDialog 
    :showModelDialog ="showModelDialog"
  />
</template>
<script>
import { ref, computed, onMounted, watch } from 'vue'
import { useStore} from 'vuex'
import { useRouter,useRoute } from 'vue-router'
import Header from '/@/components/Header.vue'
import selectModelDialog from '/@/components/ChatComponent/selectModelDialog.vue'
import TypeTab from '/@/components/TypeTab.vue'
import InputContent from '/@/components/Input.vue'
import { checkLogin } from '/@/api/api.js'
import EventBus from '/@/utils/EventBus.js'
export default {
  name: 'App',
  setup() {
    const store = useStore()
    const route = useRoute()
    const showModelDialog = ref(false)
    // 登录状态
    const loginStatus = computed( () => {
      return store.state.loginStatus
    }) 
    //适配
    const screenWidth = computed( () => {
      return store.state.screenWidth
    })
    // const pathName = route.name
    const pathName = computed( () => {
      return route.name
    })
    const checkLoginHandle = async() => {
      const res = await checkLogin({
        timestamp:new Date().getTime()
      })
      if(res.code == 200){
        store.commit('setLoginStatus',true)
        store.commit('setAccount',res.data.account)
        localStorage.setItem('userId',res.data.user_id)
      }else{
        store.commit('setLoginStatus',false)
      }
    }
    watch(() => loginStatus.value, (newValue, oldValue) => {
      // if (!newValue) {
      //     store.commit("setUserModel", "3.5");
      // }
    })
    onMounted(() => {
      checkLoginHandle()
      window.onresize = () => {
        return (() => {
          store.commit('setScreenWidth', document.body.clientWidth)
        })()
      }
    })
    return {
      loginStatus,
      screenWidth,
      pathName,
      showModelDialog,
    }
  },
  components:{
    Header,
    TypeTab,
    InputContent,
    selectModelDialog,
  },
  methods: {
    showModelDialogHandle(){
      this.showModelDialog = true
    },
    //获取cookie
    getCookie(cname) {
      var name = cname + '='
      var ca = document.cookie.split(';')
      for (var i = 0; i < ca.length; i++) {
        var c = ca[i]
        while (c.charAt(0) == ' ') c = c.substring(1)
        if (c.indexOf(name) != -1) return c.substring(name.length, c.length)
      }
      return ''
    },
  },
  watch: {
    $route: {
      handler(to, from) {
        if (to.name === '') {
          this.$store.commit('setChatType', 'navs')
        } else if (to.name === 'askDivination') {
          this.$store.commit('setChatType', 'Chats')
        }
      },
      deep: true,
    },
  },
 async created(){
  
  },
  mounted() {
    EventBus.$on('showModelDialogHandle', this.showModelDialogHandle)
    const firstLogin = this.getCookie('firstLogin')
    this.$store.commit('setFirstLogin', firstLogin)
  },
  unmounted() {
    EventBus.$off('showModelDialogHandle', this.showModelDialogHandle)
  },
}
</script>

<style scoped lang="scss">
.main-app{
 width: 100%;
 height: 100%;
 display: flex;
 flex-direction: column;
 font-size: 14px;
 background: #0A0600;
}
.container{
  height: calc(100% - 1.48rem);
  display: flex;
  padding: .4rem 0 .4rem 0rem;
  background: url(/@/assets/images/maxBg.svg) no-repeat;
  background-size: cover;
  padding-top: .1rem;
  &.mb-cont{
    padding: 0;
    height: 100%;
  }
  .left{
    width: 300px;
    padding-top: .3rem;
    padding-left: 0.4rem;
  }
  .main-router{
    // background: url(/@/assets/images/chatBg.png) no-repeat 100%;
    // background-size: cover;
    flex: 1;
    padding-top: .1rem;
    // padding-left: .4rem;
    position: relative;
    .chatBg{
      width: 100%;
      height: 100%;
    }
    .right{
      overflow: hidden;
      display: flex;
      flex-direction: column;
      width: 100%;
      height: 100%;
      position: absolute;
      top: 0px;
    }
    .router-content{
      flex: 1;
      overflow: hidden;
     position: relative;
    }
  }
}

</style>
