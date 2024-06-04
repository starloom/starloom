<!-- 登录 -->
<template>
  <div class="headerbox">
    <div class="header" :class="screenWidth>900? '' : 'm'">
      <div class="left" v-if="screenWidth>900" @click="goIndex">
        <img v-if="lang=='en'" src="/@/assets/images/logo_en.png" alt="" class="logo">
        <img v-else src="/@/assets/images/logo_zh.png" alt="" class="logo">
      </div>
      <div class="left" v-if="screenWidth<=900" @click="goIndex">
        <img v-if="lang=='en'" src="/@/assets/images/logo_mb_en.png" alt="" class="logo">
        <img v-else src="/@/assets/images/logo_mb_zh.png" alt="" class="logo">
      </div>
      <div class="right">
        <div class="func-icon">
          <el-popover v-model:visible="languagePopover" placement="bottom" trigger="click" :show-arrow="false" popper-class="language-popover">
            <template #reference>
              <div class="lang">{{ lang=='en'? 'EN' : 'CN' }}</div>
            </template>
            <template #default>
              <div @click="changeLanguage('zh')" class="list" :class="lang == 'zh' ? 'active' : ''">简体中文</div>
              <div @click="changeLanguage('en')" class="list" :class="lang == 'en' ? 'active' : ''">English</div>
            </template>
          </el-popover>
        </div>
        <div class="func-icon" v-if="loginStatus==false" @click="showLoginHandle">
          <div class="login">{{ $t('logInAndRegister') }}</div>
        </div>
        <!-- v-if="loginStatus" -->
        <div class="chooseModelBox">
          <el-popover v-model:visible="userPopover" placement="bottom-end" trigger="click" :show-arrow="false" popper-class="user-popover">
            <template #reference>
              <!-- <img class="userimg" src="/@/assets/images/user.png" alt=""> -->
              <div v-if="userModel=='3.5'" class="typeTab baseType">{{ $t('basic') }}</div>
              <div v-if="userModel=='4'" class="typeTab plusType">{{ $t('plus') }}</div>
            </template>
            <template #default>
              <div v-if="loginStatus && screenWidth<=900" class="account">
                <div class="userPicture"></div> {{ account }}
              </div>
              <div class="chooseModel">
                <div class="plusBox" :class="userModel=='4'?'acivePlus':''">
                  <div class="part1">
                    <img v-if="userModel=='4'" src="/@/assets/images/headerChoose_black.svg" alt="" srcset="">
                    <img v-else src="/@/assets/images/headerChoose_grey.svg" alt="" srcset="">
                    <div class="xianmian">{{ $t('limitedTimeFree') }}</div>
                    {{ $t('basic') }}
                  </div>
                </div>
                <!-- <div class="baseBox" @click="changeMosel('3.5')" :class="userModel=='3.5'?'aciveBase':''">
                          <div class="part1">
                            <img v-if="userModel=='3.5'" src="/@/assets/images/headerChoose_black.svg" alt="" srcset="">
                            <img v-else src="/@/assets/images/headerChoose_grey.svg" alt="" srcset="">
                            <div class="timefree">{{ $t('limitedTimeFree') }}</div>
                            {{ $t('basic') }}
                          </div>
                        </div> -->
                <!-- <div class="plusBox" @click="changeMosel('4')" :class="userModel=='4'?'acivePlus':''">
                          <div class="part1">
                            <img v-if="userModel=='4'" src="/@/assets/images/headerChoose_black.svg" alt="" srcset="">
                            <img v-else  src="/@/assets/images/headerChoose_grey.svg" alt="" srcset="">
                            {{ $t('plus') }}
                          </div>
                          <template v-if="accountInfo.user_account">
                            <div class="timestime" v-if=" accountInfo.user_account.terminable_time ">
                              <div class="times"><div class="allcishu"><span class="fontbold">{{ accountInfo.user_account?.terminable_time }}</span>
                                <el-tooltip
                                    class="box-item"
                                    effect="dark"
                                    :content="$t('PLUS2timesGiven')"
                                    placement="top-start"
                                    v-if="accountInfo.user_account.terminable_time && accountInfo.allowance_num"
                                  >
                                    <div class="add2">+{{ accountInfo.allowance_num }}</div>
                                  </el-tooltip> 
                                </div>
                                 /{{ accountInfo.user_account.terminable_time_history_total }}</div>
                              <div class="time"> {{ $t('expired') }}：{{ accountInfo.user_account.due_date.split(" ")[0] }}</div>
                            </div>
                            <div class="timestime" v-if="accountInfo.user_account.un_terminable_time"  >
                              <div class="times"><div class="allcishu"><span class="fontbold">{{ accountInfo.user_account.un_terminable_time }} </span>
                                  <el-tooltip
                                    class="box-item"
                                    effect="dark"
                                    :content="$t('PLUS2timesGiven')"
                                    placement="top-start"
                                    v-if="!accountInfo.user_account.terminable_time && accountInfo.allowance_num"
                                  >
                                    <div class="add2">+{{ accountInfo.allowance_num }}</div>
                                  </el-tooltip> 
                                </div>
                                /{{ accountInfo.user_account.un_terminable_time_history_total }}</div>
                              <div class="time">{{ $t('unlimited') }}</div>
                            </div>
                          </template>
                          
                          <div class="timestime" v-if="!accountInfo.user_account?.terminable_time && !accountInfo.user_account?.un_terminable_time ">
                            <el-tooltip
                              class="box-item"
                              effect="dark"
                              :content="$t('PLUS2timesFree')"
                              placement="top-start"
                            >
                              <div v-if="!loginStatus" class="xianmian">{{ $t('limited2Free') }}</div>
                              <div v-else class="xianmian">{{ $t('limitedNFree',{num: accountInfo.allowance_num}) }}</div>
                            </el-tooltip>
                           
                            <div class="time">{{ $t('expired') }}：{{ expirationTime }}</div>
                          </div>
                          <div v-if="userModel=='4'"  class="bottomBtn" @click="goSubscribe">{{ accountInfo?.user_account?  $t('renewal'): $t('subscribe') }}</div>
                        </div> -->
                <div class="signout-mb" v-if="loginStatus && screenWidth<=900" @click="logout">{{ $t('logout') }}</div>
              </div>
            </template>
          </el-popover>
        </div>
        <template v-if="screenWidth>900">
          <div class="userAccount" v-if="loginStatus">
            <img src="/@/assets/images/user.png" alt="">
            <div>{{ cutAddress(account) }}</div>
          </div>
          <div class="func-icon" v-if="loginStatus" @click="logout">
            <div class="signout">{{ $t('logout') }}</div>
          </div>
        </template>
        <div class="mb-header" v-if="screenWidth<=900">
          <!-- <div>
              <el-popover
                v-model:visible="userPopover"
                placement="bottom-end"
                trigger="click"
                :show-arrow="false"
                popper-class="user-popover"
              >
                  <template #reference>
                      <div class="typeTab baseType">基础版</div>
                      <div class="typeTab plusType">Plus版</div>
                  </template>
                  <template #default>
                      <div v-if="loginStatus" class="account"><div class="userPicture"></div> {{ account }}</div>
                      <div class="chooseModel">
                        <div class="baseBox">
                          <div class="part1">
                            <img src="/@/assets/images/headerChoose_grey.svg" alt="" srcset="">
                            基础版
                          </div>
                        </div>
                        <div class="plusBox">
                          <div class="part1">
                            <img src="/@/assets/images/headerChoose_grey.svg" alt="" srcset="">
                            Plus版
                          </div>
                          <div class="timestime">
                            <div class="times">40/20</div>
                            <div class="time">到期：2024.09.23</div>
                          </div>
                          <div class="bottomBtn">续费</div>
                        </div>
                      </div>
                      <div class="signout-mb" v-if="loginStatus" @click="logout">退出</div>
                  </template>
              </el-popover>
            </div> -->

          <div class="mb-menu" @click="drawer = true">
            <img src="/@/assets/images/right-menu.png" alt="">
            <div class="menu">{{ $t('mbNav') }}</div>
          </div>
        </div>

        <!-- <div class="user-info">
              <div class="img"></div>
              <div class="text">
                  wwww.baidu.com
              </div>
          </div> -->
      </div>
    </div>
    <!-- <div class="mb-menu" v-if="screenWidth<=900">
      <div class="menu">
        <img  @click="drawer = true" src="/@/assets/images/right-menu.png" alt="">
      </div>
    </div> -->
    <div class="sloganBox" v-if="screenWidth<=900">
      <div class="content">
        <div class="zhPart">
          <img src="/@/assets/images/slogan_left.svg" alt="">
          <div class="text_zh"> 你不知道你的命运，但也许<span>AI</span>知道</div>
          <img src="/@/assets/images/slogan_right.svg" alt="">
        </div>
        <div class="enPart">You may not know your fate, but maybe Al does</div>
      </div>
    </div>
    <el-drawer v-model="drawer" direction="btt" :before-close="handleClose" :show-close="false" :with-header="false" class="menu-drawer" size="calc(100% - 1.2rem)" :modal="false">
      <!--      -->
      <TypeTab />
    </el-drawer>
  </div>
  <Login :loginShow="loginShow" @closeLogin="closeLogin" @loginSuccess="loginSuccess" ref="Login" />
  <SubscribeType :subscribeDialog="subscribeDialog" :isPlus="accountInfo.user_account" :paytypelist="paylist" @closeSubscribeDialog="closeSubscribeDialog" />
</template>

<script>
import { ref, computed, watch, onUnmounted } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import EventBus from "/@/utils/EventBus.js";
import Login from "/@/components/Login.vue";
import { useI18n } from "vue-i18n";
import { loginOut, payCardInfo, payAccount } from "/@/api/api";
export default {
  name: "",
  setup() {
    const router = useRouter();
    const goIndex = () => {
      router.push({ name: "index" });
    };
    const store = useStore();
    const { t } = useI18n();
    const lang = computed(() => store.state.lang);
    console.log("lang,,", lang.value);
    const languagePopover = ref(false);
    const userPopover = ref(false);
    const loginShow = ref(false);
    const account = computed(() => store.state.account);
    const userModel = computed(() => store.state.userModel);
    const accountInfo = ref({});
    const expirationTime = ref("");
    const paylist = ref([]);
    const haveCount = computed(() => store.state.haveCount); // 是否有条数
    // 登录状态
    const loginStatus = computed(() => {
      return store.state.loginStatus;
    });
    //适配
    const screenWidth = computed(() => {
      return store.state.screenWidth;
    });
    const drawer = ref(false);
    const showLoginHandle = () => {
      loginShow.value = true;
    };
    const loginSuccess = (account) => {
      store.commit("setLoginStatus", true);
      store.commit("setAccount", account);
    };
    const logout = () => {
      userPopover.value = false;
      ElMessageBox.confirm(t("logoutUre"), "", {
        confirmButtonText: t("logout"),
        cancelButtonText: t("cancel"),
        cancelButtonClass: "cancel",
        confirmButtonClass: "ok",
      })
        .then(() => {
          loginOut().then((res) => {
            store.commit("setLoginStatus", false);
            store.commit("setAccount", "");
            localStorage.setItem("starloomAI-token", "");
            // store.commit('setUserModel', '3.5')
            accountInfo.value.user_account = null;
          });
        })
        .catch(() => {});
    };
    const loginTipMessageBox = () => {
      ElMessageBox.confirm(t("loginTip"), "", {
        confirmButtonText: t("logInAndRegister"),
        cancelButtonText: t("cancel"),
        cancelButtonClass: "cancel",
        confirmButtonClass: "ok",
      })
        .then(() => {
          showLoginHandle();
        })
        .catch(() => {});
    };
    const handleClose = (done) => {
      done();
    };
    const closeDrawer = () => {
      drawer.value = false;
    };
    const changeMosel = (model) => {
      if (model == "4") {
        if (!loginStatus.value) {
          showLoginHandle();
          return;
        }
        if (
          !accountInfo.value.user_account &&
          !accountInfo.value.allowance_num &&
          !accountInfo.value.user_account?.terminable_time &&
          !accountInfo.value.user_account?.un_terminable_time
        ) {
          goSubscribe();
          return;
        }
      }
      store.commit("setUserModel", model);
      localStorage.setItem("userModel", model);
    };
    const subscribeDialog = ref(false);
    const goSubscribe = () => {
      subscribeDialog.value = true;
    };
    const closeSubscribeDialog = () => {
      subscribeDialog.value = false;
    };
    watch(
      () => userPopover.value,
      async (val, old) => {
        const today = new Date();
        const year = today.getFullYear();
        const month = today.getMonth() + 1; // 月份从0开始，所以要加1
        const day = today.getDate();
        expirationTime.value = `${year}.${month}.${day}`;
        if (val == true && loginStatus.value) {
          const result = await payAccount({});
          if (result.code == 200) {
            // accountInfo.value.user_account = null
            // userAccountInfo.value.allowance_num=0
            // userAccountInfo.value.user_account.terminable_time = 0
            // userAccountInfo.value.user_account.un_terminable_time = 0
            accountInfo.value = result.data;

            // if(!result.data.user_account){

            // }
          }
        }
      }
    );
    EventBus.$on("closeDrawer", closeDrawer);
    EventBus.$on("showLoginHandle", showLoginHandle);
    EventBus.$on("goSubscribe", goSubscribe);

    onUnmounted(() => {
      EventBus.$off("showLoginHandle", showLoginHandle);
      EventBus.$off("closeDrawer", closeDrawer);
      EventBus.$off("goSubscribe", goSubscribe);
    });
    return {
      goIndex,
      lang,
      languagePopover,
      userPopover,
      loginShow,
      loginStatus,
      showLoginHandle,
      logout,
      loginSuccess,
      account,
      screenWidth,
      drawer,
      handleClose,
      closeDrawer,
      loginTipMessageBox,
      userModel,
      changeMosel,
      subscribeDialog,
      goSubscribe,
      closeSubscribeDialog,
      accountInfo,
      expirationTime,
      paylist,
      haveCount,
    };
  },
  components: {
    Login,
  },
  watch: {
    loginStatus(val, old) {
      if (val) {
        this.getPayCardInfoList();
      }
    },
  },
  methods: {
    changeLanguage(lang) {
      localStorage.setItem("lang", lang);
      this.$store.commit("setLang", lang);
      this.languagePopover = false;
      this.$i18n.locale = lang;
    },
    closeLogin() {
      this.loginShow = false;
    },
    async getPayCardInfoList() {
      const result = await payCardInfo({});
      if (result.code == 200) {
        this.paylist = result.data;
        this.paylist.forEach((item) => {
          if (item.card_type == "1") {
            item.card_name = this.$t("timeOne");
          } else if (item.card_type == "2") {
            item.card_name = this.$t("nTime", { num: 15 });
          } else if (item.card_type == "3") {
            item.card_name = this.$t("monthlyCard");
          } else if (item.card_type == "4") {
            item.card_name = this.$t("quarterlyCard");
          } else if (item.card_type == "5") {
            item.card_name = this.$t("annualCard");
          }
        });
        //  == '3'? '月卡' :  item.card_type == '4'? '季卡' : '年卡'
        // console.log('paylist.slice(2, 5),,',this.paylist.slice(2, 5))
      }
    },
    //设置cookie
    setCookie(cname, cvalue, exdays) {
      var d = new Date();
      d.setTime(d.getTime() + exdays * 24 * 60 * 60 * 1000);
      var expires = "expires=" + d.toUTCString();
      document.cookie = cname + "=" + cvalue + "; " + expires;
    },
    //获取cookie
    getCookie(cname) {
      var name = cname + "=";
      var ca = document.cookie.split(";");
      for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == " ") c = c.substring(1);
        if (c.indexOf(name) != -1) return c.substring(name.length, c.length);
      }
      return "";
    },
    cutAddress(account) {
      if (account.indexOf(".com") > -1) {
        return account;
      } else {
        const beforeAdr = account.substring(0, 4);
        const afterAdr = account.substring(account.length - 4, account.length);
        return beforeAdr + "..." + afterAdr;
      }
    },
  },
  mounted() {
    // 控制登录弹框是否弹出
    const num = this.getCookie("popUpLogin");
    const loginToken = localStorage.getItem("starloomAI-token");
    if (num) {
      this.setCookie("popUpLogin", Number(num) + 1, 365);
      const time = (Number(num) + 1) % 5;
      if (time == 1) {
        if (!loginToken) {
          this.loginTipMessageBox();
        }
      }
      // else {
      //   this.$refs.advertiseAlert.show = false
      // }
    } else {
      this.setCookie("popUpLogin", 1, 365);
      if (!loginToken) {
        this.loginTipMessageBox();
      }
    }
    this.getPayCardInfoList();
    setTimeout(() => {
      // const lang = localStorage.getItem('lang')
      // this.$store.commit('setLang',lang)
      this.$i18n.locale = "zh";
    }, 500);
  },
  unmounted() {},
};
</script>

<style scoped lang='scss'>
.header {
  background: url(/@/assets/images/header-heng.svg) no-repeat 100% 100%;
  height: 1.2rem;
  opacity: 1;
  display: flex;
  justify-content: space-between;
  align-items: center;
  // border-radius: 30px 30px 0px 0px;
  padding-right: 1rem;
  z-index: 11;
  .left {
    // display: flex;
    // align-items: center;
    cursor: pointer;
    .logo {
      width: 6rem;
      margin-right: 0.1rem;
    }
  }
  .right {
    display: flex;
    align-items: center;
    .func-icon {
      margin-right: 0.4rem;
      font-family: Alimama-DongFangDaKai;
      color: #ded1bb;
      text-align: center;
      .lang,
      .login {
        // margin-right: .4rem;
        border-radius: 10px;
        cursor: pointer;
        // width: 2rem;
        background: #140800;
        height: 0.7rem;
        line-height: 0.7rem;
        padding: 0 0.1rem;
        white-space: nowrap;
      }
      .lang {
        width: 0.7rem;
        // padding: 0 0.15rem;
        border-radius: 50%;
      }
      .login {
        border-radius: 0.5rem;
        padding: 0 0.3rem;
      }
      .signout {
        // margin-right: .4rem;
        cursor: pointer;
        // width: 2rem;
        background: #140800;
        border-radius: 10px;
        height: 0.6rem;
        line-height: 0.6rem;
        padding: 0 0.3rem;
      }
    }
    .chooseModelBox {
      cursor: pointer;
    }
    .typeTab {
      font-size: 0.32rem;
      padding: 0 0.2rem;
      margin-right: 0.3rem;
      line-height: 0.7rem;
      border-radius: 0.2rem;
      font-weight: 400;
    }
    .baseType {
      background: #c0ffd1;
      color: #007636;
      white-space: nowrap;
    }
    .plusType {
      background: linear-gradient(270deg, #fffbf5 0%, #ffe8c4 100%);
      color: #c37600;
      white-space: nowrap;
    }
    .userAccount {
      display: flex;
      // justify-content: space-around;
      align-items: center;
      padding: 0 0.2rem;
      cursor: default;
      img {
        width: 0.6rem;
        height: 0.6rem;
        margin-right: 0.2rem;
      }
    }
    // .user-info{
    //     display: flex;
    //     align-items: center;
    //     .img{
    //         width: .6rem;
    //         height: .6rem;
    //         background: #f39c13;
    //         margin-right: .15rem;
    //         border-radius: 100px;
    //     }
    //     .text{
    //         font-size: .256rem;
    //         color: #FFFFFF;
    //         cursor: pointer;
    //     }
    // }
  }
  &.m {
    height: 1.2rem;
    padding-right: 0.2rem;
    .left {
      // width: 25%;
      img {
        width: 100%;
        height: 1.2rem;
        object-fit: contain;
        object-position: left;
      }
    }
    .func-icon {
      margin-right: 0.2rem;
    }
    .typeTab {
      margin-right: 0.2rem;
    }
  }
}
.mb-header {
  display: flex;
  align-items: center;
  .userimg {
    width: 0.8rem;
    margin-right: 0.5rem;
  }
  .account {
    // color: #FFC772;
    // border-radius: 50%;
  }
}
.mb-menu {
  width: 2rem;
  height: 0.7rem;
  background: linear-gradient(180deg, #ffe2b0 0%, #bf7a00 100%);
  border-radius: 0.8rem;
  display: flex;
  // justify-content: space-between;
  align-items: center;
  img {
    width: 0.8rem;
    margin-right: 0.2rem;
  }
  .menu {
    font-family: Alimama-DongFangDaKai;
    color: #000000;
  }
}

:deep(.el-drawer) {
  background: #29170d !important;
}

.sloganBox {
  padding: 0.2rem 0 0;
  text-align: center;
  .content {
    .zhPart {
      display: flex;
      justify-content: center;
      font-size: 0.45rem;
      align-items: center;
      color: #fff6f1;
      .text_zh {
        font-family: Alimama-DongFangDaKai;
        span {
          color: #ffb840;
        }
      }
    }
    .enPart {
      color: #9c7d6e;
    }
  }
}
</style>