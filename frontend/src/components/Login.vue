<template>
  <div class="login-box" :class="screenWidth<=480 ? 'mb-login-box' : screenWidth<=800 ? 'ipad-login-box' : ''">
    <el-dialog v-model="show" :show-close="false" :before-close="handleClose" :width="screenWidth<=480?'350px':screenWidth<=800 ? '470px' :'753px'" center>
      <template #header="{ close }">
        <div class="close" @click="close">
          <!-- <img src="/@/assets/imgs/arrow-back-black.svg" alt=""> -->
        </div>
      </template>
      <!-- <div class="maxbg">
          <img src="/@/assets/images/LoginBg_zh.png" alt="" srcset="">
        </div> -->
      <div class="from">
        <div class="maxBox">
          <div class="left">
            <div class="loginBtn" @click="changeLoginTab('sign-in')" :class="loginStatus == 'sign-in' || loginStatus == 'forgetpassword' ? 'activeBtn' : '' ">
              <div class="text">{{ $t('signIn') }}</div>
              <div class="bg">
                <img v-if="loginStatus == 'sign-in' || loginStatus == 'forgetpassword' " src="/@/assets/images/LoginBtn_active.png" alt="" srcset="">
                <img v-else src="/@/assets/images/LoginBtnBg.png" alt="" srcset="">
              </div>
            </div>
            <div class="signUpBtn" @click="changeLoginTab('sign-up')" :class="loginStatus == 'sign-up' ? 'activeBtn' : '' ">
              <div class="text">{{ $t('signUp') }}</div>
              <div class="bg">
                <img v-if="loginStatus == 'sign-up'" src="/@/assets/images/LoginBtn_active.png" alt="" srcset="">
                <img v-else src="/@/assets/images/LoginBtnBg.png" alt="" srcset="">
              </div>
            </div>
          </div>
          <div class="right">
            <div v-if="loginStatus == 'sign-in' && loginType!=='Email'" class="loginType">
              <div class="textType">
                <div>{{$t('loginSocial')}}</div>
              </div>
              <div class="btnEmail" @click="loginType = 'Email'"><img src="/@/assets/images/emailIcon.svg" alt="">{{$t('Emaillogin')}}</div>
              <div class="textType">{{$t('Logwallet')}}</div>
              <div class="walletDiv">
                <div class="walletCont" :class="screenWidth>900?'':'mb'" v-for="item in walletListArr" :key="item" @click="LogWithWallet(item.name)">
                  <img :src="getImg(item.name)" alt="">
                  <div>{{item.name}}</div>
                </div>
              </div>
            </div>
            <!-- 登录 -->
            <div class="login-max" v-if="loginStatus == 'sign-in'&& loginType=='Email'">
              <div class="input-content">
                <el-form :model="formData" :rules="formRules" ref="form" :hide-required-asterisk="true">
                  <el-form-item prop="email" :label="$t('email')">
                    <!-- :placeholder="$t('email')"   clearable-->
                    <el-input class="input" v-model="formData.email" @input="onInput" />
                  </el-form-item>
                  <el-form-item prop="password" :label="$t('password')">
                    <!--  :placeholder="$t('password')"  clearable-->
                    <el-input class="input" v-model="formData.password" type="password" show-password />
                  </el-form-item>
                  <div class="otherfun">
                    <div class="forgetPass" @click.stop="loginType=''">{{ $t('loginSocial') }}</div>
                    <div class="forgetPass" @click="loginStatus = 'forgetpassword'">{{ $t('forgotPassword') }}</div>
                  </div>
                  <el-form-item class="btn-group">
                    <el-button :loading="loading" class="submit" type="primary" @click="submitForm('login')">{{ $t('signIn') }}</el-button>
                  </el-form-item>
                </el-form>
              </div>
            </div>
            <!-- 注册 -->
            <div class="signUp-max" v-if="loginStatus == 'sign-up'">
              <div class="step1" v-if="status=='step1'">
                <div class="input-content">
                  <el-form :model="formData" :rules="formRules" ref="form" :hide-required-asterisk="true">
                    <el-form-item prop="email" :label="$t('email')" class="emailInput">
                      <!-- :placeholder="$t('email')"  clearable-->
                      <el-input class="input" v-model="formData.email" @input="onInput" />
                    </el-form-item>
                    <el-form-item prop="password" :label="$t('password')">
                      <el-input class="input" v-model="formData.password" type="password" show-password />
                    </el-form-item>
                    <!--     :placeholder="$t('password2')"  clearable-->
                    <el-form-item prop="password2" :label="$t('password2')">
                      <el-input class="input" v-model="formData.password2" type="password" show-password />
                    </el-form-item>
                    <el-form-item class="btn-group">
                      <el-button :loading="loading" class="submit" type="primary" @click="submitForm('sign')">{{ $t('signUp') }}</el-button>
                    </el-form-item>
                  </el-form>
                </div>
              </div>
              <div v-show="status=='step2'">
                <vue-hcaptcha sitekey="" :style="screenWidth>800?PC:screenWidth>480?IPAD:MB" :data-size="screenWidth<=800?'compact':''" @verify="verifySuccess" ref="hcaptcha"></vue-hcaptcha>
              </div>
              <div class="step2" v-if="status=='step3'">
                <div class="input-content">
                  <el-form :rules="formRules" ref="form" :hide-required-asterisk="true">
                    <div class="yzm-text">{{ $t('VerificationCode') }}</div>
                    <div class="yzm-text2">{{ $t('sentCode', {email:formData.email}) }}</div>
                    <!--    :placeholder="$t('VerificationCode')" clearable -->
                    <el-form-item prop="captchaCode">
                      <el-input class="input mt" v-model="formData.verifyCode" />
                    </el-form-item>
                    <div class="resend">
                      <span @click="sendEmailCode" class="text">{{ $t('Resendcode') }}</span>
                      <span v-if="!sendAgain && time != 0">({{ time }})s</span>
                    </div>
                    <el-form-item class="btn-group">
                      <el-button :loading="sendLoading" class="submit" type="primary" @click="confirm">{{ $t('signUp') }}</el-button>
                    </el-form-item>
                  </el-form>
                </div>
              </div>
            </div>
            <!-- 忘记密码 -->
            <div class="signUp-max" v-if="loginStatus == 'forgetpassword'">
              <div class="step1" v-if="status=='step1'">
                <div class="input-content">
                  <el-form :model="formData" :rules="formRules" ref="form" :hide-required-asterisk="true">
                    <div class="resetText steptext">{{ $t('forgotPassword') }}</div>
                    <el-form-item prop="email" :label="$t('email')">
                      <!-- :placeholder="$t('email')"  clearable-->
                      <el-input class="input" v-model="formData.email" @input="onInput" />
                    </el-form-item>
                    <el-form-item class="btn-group">
                      <el-button :loading="loading" class="submit" type="primary" @click="submitForm('forgetpassword')">{{ $t('next') }}</el-button>
                    </el-form-item>
                  </el-form>
                </div>
              </div>
              <div v-show="status=='step2'">
                <vue-hcaptcha sitekey="" :style="screenWidth>800?PC:screenWidth>480?IPAD:MB" @verify="verifySuccess" :data-size="screenWidth<=800?'compact':''" ref="hcaptcha"></vue-hcaptcha>
              </div>
              <div class="step2" v-if="status=='step3'">
                <div class="input-content">
                  <el-form :rules="formRules" ref="form" :hide-required-asterisk="true">
                    <div class="yzm-text">{{ $t('VerificationCode') }}</div>
                    <div class="yzm-text2">{{ $t('sentCode', {email:formData.email}) }}</div>
                    <!--    :placeholder="$t('VerificationCode')" clearable -->
                    <el-form-item prop="captchaCode">
                      <el-input class="input mt" v-model="formData.verifyCode" />
                    </el-form-item>
                    <div class="resend">
                      <span @click="sendCodeResetPassword" class="text">{{ $t('Resendcode') }}</span>
                      <span v-if="!sendAgain && time != 0">({{ time }})s</span>
                    </div>
                    <el-form-item class="btn-group">
                      <el-button class="submit" type="primary" @click="goStep4">{{ $t('next') }}</el-button>
                    </el-form-item>
                  </el-form>
                </div>
              </div>
              <div class="step2" v-if="status=='step4'">
                <div class="input-content">
                  <el-form :model="formData" :rules="formRules" ref="form" :hide-required-asterisk="true">
                    <div class="resetText">{{ $t('setNewPassword') }}</div>
                    <el-form-item prop="password" :label="$t('password')">
                      <el-input class="input" v-model="formData.password" type="password" show-password />
                    </el-form-item>
                    <!--     :placeholder="$t('password2')"  clearable-->
                    <el-form-item prop="password2" :label="$t('password2')">
                      <el-input class="input" v-model="formData.password2" type="password" show-password />
                    </el-form-item>
                    <el-form-item class="btn-group">
                      <el-button :loading="sendLoading" class="submit" type="primary" @click="confirmReset()">{{ $t('sure') }}</el-button>
                    </el-form-item>
                  </el-form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </el-dialog>
  </div>
</template>
  
  <script>
import { ref, computed, watch } from "vue";
import { useStore } from "vuex";
import { useI18n } from "vue-i18n";
import { Aim, Back } from "@element-plus/icons-vue";
import VueHcaptcha from "@hcaptcha/vue3-hcaptcha";
import EventBus from "/@/utils/EventBus.js";
import walletList from "/@/utils/walletConfig.js";
import {
  userLogin,
  register,
  sendEmailCode,
  sendCodeResetPassword,
  checkEmailCodeResetPassword,
  resetPassword,
} from "/@/api/api";
import Web3 from "web3";
export default {
  name: "Login",
  props: ["loginShow"],
  setup(props) {
    const store = useStore();
    const { t } = useI18n();
    const show = ref(props.loginShow);
    const status = ref("step1"); // 状态区分 登录注册和发送验证码
    //适配
    const screenWidth = computed(() => {
      return store.state.screenWidth;
    });
    // 是否是第一次登录
    const firstLogin = computed(() => {
      return store.state.firstLogin;
    });
    const PC = ref("width: 303px;margin:50px auto");
    const MB = ref("margin: 30px 0px 0 30px;");
    const IPAD = ref("margin: 30px 0px 0 50px;");
    const formData = ref({
      email: "",
      password: "",
      password2: "",
      verifyCode: "",
    });
    const lang = computed(() => {
      return store.state.lang;
    });

    // const verifyCode = ref('')
    const formRules = ref({
      email: [
        { required: true, message: t("enterEmail"), trigger: "blur" },
        { type: "email", message: t("sureEmail"), trigger: "blur" },
      ],
      password: [
        { required: true, message: t("enterpassword"), trigger: "blur" },
        { min: 6, max: 20, message: t("passwordLength"), trigger: "blur" },
      ],
      password2: [
        { required: true, message: t("enterpassword2"), trigger: "blur" },
      ],
      // verifyCode
      verifyCode: [
        { required: true, message: t("VerificationCode"), trigger: "blur" },
      ],
    });
    watch(
      () => store.state.lang,
      (val) => {
        formRules.value = {
          email: [
            { required: true, message: t("enterEmail"), trigger: "blur" },
            { type: "email", message: t("sureEmail"), trigger: "blur" },
          ],
          password: [
            { required: true, message: t("enterpassword"), trigger: "blur" },
            { min: 6, max: 20, message: t("passwordLength"), trigger: "blur" },
          ],
          password2: [
            { required: true, message: t("enterpassword2"), trigger: "blur" },
          ],
          verifyCode: [
            { required: true, message: t("VerificationCode"), trigger: "blur" },
          ],
        };
      }
    );
    const loginStatus = ref("sign-in");
    const password = ref("");
    // 请求状态
    const loading = ref(false);
    const sendLoading = ref(false);

    // 重新发送验证码倒计时
    const timer = ref(null);
    const time = ref(60);
    const sendAgain = ref(true);
    // watch(loginStatus,(val)=>{
    //   if(val == 'sign-up'){
    //     hcaptchaStatus.value = false
    //   }
    // })
    //人机校验
    const hcaptchaStatus = ref(false);
    const hcaptchaToken = ref("");
    // const verifySuccess = (token, eKey) => {
    //   hcaptchaToken.value = token
    //   hcaptchaStatus.value = true
    //   sendEmailCode()
    // }
    const changeLoginTab = (tab) => {
      loginStatus.value = tab;
      status.value = "step1";
    };
    const loginType = ref("");
    const walletListArr = ref(walletList);
    const walletProvider = ref(null);
    return {
      show: show,
      status,
      formData,
      // verifyCode,
      formRules,
      loginStatus,
      password,
      loading,
      sendLoading,
      timer,
      time,
      sendAgain,
      hcaptchaStatus,
      hcaptchaToken,
      screenWidth,
      // verifySuccess,
      lang,
      changeLoginTab,
      PC,
      MB,
      IPAD,
      firstLogin,
      loginType,
      walletListArr,
      walletProvider,
    };
  },
  components: {
    VueHcaptcha,
  },
  watch: {
    loginShow(a) {
      this.show = a;
    },
  },
  methods: {
    handleClose(done) {
      this.status = "step1";
      this.loginStatus = "sign-in";
      this.show = false;
      this.$emit("closeLogin", "closeLogin");
    },
    onInput() {
      // Replace all spaces with an empty string as the user types
      this.formData.email = this.formData.email.replace(/\s/g, "");
    },
    verifySuccess(token, eKey) {
      this.hcaptchaToken = token;
      this.hcaptchaStatus = true;
      if (this.loginStatus == "sign-up") {
        this.sendEmailCode();
      } else if (this.loginStatus == "forgetpassword") {
        this.sendCodeResetPassword();
      }
    },
    submitForm(type) {
      const form = this.$refs.form;
      form.validate((valid) => {
        if (valid) {
          //登录
          if (type == "login") {
            this.loginHandle();
          } else if (type == "sign") {
            //注册
            this.signnHandle();
          } else if (type == "forgetpassword") {
            // 忘记密码
            this.forgetpasswordHandle();
          }
        }
      });
    },
    async loginHandle(signature, account, timestamp) {
      this.loading = true;
      let loginParams = {
        email: this.formData.email,
        password: this.formData.password,
      };
      if (this.loginType != "Email" && this.loginType != "") {
        loginParams = {
          signature: signature,
          wallet_address: account,
          type: 1,
          timestamp: timestamp.toString(),
        };
      }
      const res = await userLogin(loginParams);
      this.loading = false;
      if (res.code == 200 && res.data) {
        localStorage.setItem("starloomAI-token", res.data.user_token);
        this.$emit("loginSuccess", res.data.account);
        localStorage.setItem("userId", res.data.user_id);
        this.$store.commit("setUserModel", "4");
        this.formData.verifyCode = "";
        this.formData.email = "";
        this.formData.password = "";
        this.formData.password2 = "";
        this.show = false;
        this.$emit("closeLogin", "closeLogin");
        // if(!this.firstLogin){
        //   EventBus.$emit('showModelDialogHandle')
        //   this.setCookie('firstLogin', 1, 365)
        // }
      } else if (res.code == 2002) {
        ElMessage({
          message: this.$t("IncorrectLogin"),
          type: "error",
        });
      } else if (res.code == 2001) {
        ElMessage({
          message: this.$t("accountError"),
          type: "error",
        });
      }
    },
    async signnHandle() {
      if (!this.sendAgain || this.loading) {
        return;
      }
      //校验第二次呼入密码是否正确
      if (this.formData.password != this.formData.password2) {
        ElMessage({
          message: this.$t("passwordNosame"),
          type: "error",
        });
        return;
      }
      this.status = "step2";
    },
    async sendEmailCode() {
      if (!this.sendAgain || this.loading) {
        return;
      }
      // 发送邮箱验证码
      this.loading = true;
      const res = await sendEmailCode({
        email: this.formData.email,
        "g-recaptcha-response": this.hcaptchaToken,
        language: this.lang,
      });
      this.loading = false;
      clearInterval(this.timer);
      this.time = 60;
      this.Countdown();
      console.log(res);
      if (res.code == 200) {
        this.sendAgain = false;
        this.$refs.hcaptcha.reset();
        this.status = "step3";

        ElMessage({
          message: this.$t("sendSuccess"),
          type: "success",
        });
      } else {
        if (res.code == 2004) {
          this.status = "step2";
          return;
        }
        ElMessage({
          message: this.$t(res.code),
          type: "error",
        });
      }
    },
    //提交注册
    async confirm() {
      if (!this.formData.verifyCode) return;
      this.sendLoading = true;
      const res = await register({
        email: this.formData.email,
        verifyCode: this.formData.verifyCode,
        password: this.formData.password,
      });
      this.sendLoading = false;
      if (res.code == 2009) {
        ElMessage({
          message: this.$t("codeError"),
          type: "error",
        });
        return;
      }
      if (res.code == 200 && res.data) {
        ElMessage({
          message: this.$t("signSuccess"),
          type: "success",
        });
        this.status = "step1";
        this.loginStatus = "sign-in";
        this.formData.verifyCode = "";
        this.formData.email = "";
        this.formData.password = "";
        this.formData.password2 = "";
      }
    },
    forgetpasswordHandle() {
      this.status = "step2";
    },
    async sendCodeResetPassword() {
      if (!this.sendAgain || this.loading) {
        return;
      }
      // 发送邮箱验证码
      // this.loading = true
      this.sendAgain = false;
      const res = await sendCodeResetPassword({
        email: this.formData.email,
        "g-recaptcha-response": this.hcaptchaToken,
        language: this.lang,
      });
      // this.loading = false
      clearInterval(this.timer);
      this.time = 60;
      this.Countdown();
      console.log(res);
      if (res.code == 200) {
        this.sendAgain = false;
        this.$refs.hcaptcha.reset();
        this.status = "step3";

        ElMessage({
          message: this.$t("sendSuccess"),
          type: "success",
        });
      } else {
        this.sendAgain = true;
        if (res.code == 2004) {
          this.status = "step2";
          return;
        }
        ElMessage({
          message: this.$t(res.code),
          type: "error",
        });
      }
    },
    async goStep4() {
      if (!this.formData.verifyCode) return;
      const res = await checkEmailCodeResetPassword({
        email: this.formData.email,
        verifyCode: this.formData.verifyCode,
      });
      if (res.code == 200 && res.data) {
        if (res.data.is_checked == 1) {
          this.status = "step4";
        } else if (res.data.is_checked == 0) {
          ElMessage({
            message: "验证码不正确",
            type: "error",
          });
          return;
        }
      }
    },
    //提交注册
    // if(!this.formData.verifyCode) return
    async confirmReset() {
      //密码校验
      if (
        this.formData.password.length < 6 ||
        this.formData.password.length > 20
      ) {
        return;
      }
      //校验第二次呼入密码是否正确
      if (this.formData.password != this.formData.password2) {
        ElMessage({
          message: this.$t("passwordNosame"),
          type: "error",
        });
        return;
      }
      this.sendLoading = true;
      const res = await resetPassword({
        email: this.formData.email,
        verifyCode: this.formData.verifyCode,
        password: this.formData.password,
      });
      this.sendLoading = false;
      if (res.code == 2009) {
        ElMessage({
          message: this.$t("codeError"),
          type: "error",
        });
        return;
      }
      if (res.code == 200) {
        ElMessage({
          message: "新密码设置成功",
          type: "success",
        });
        this.status = "step1";
        this.loginStatus = "sign-in";
        this.formData.verifyCode = "";
        this.formData.email = "";
        this.formData.password = "";
        this.formData.password2 = "";
      }
    },
    Countdown() {
      const self = this;
      clearInterval(self.timer);
      self.timer = setInterval(() => {
        if (self.time == 0) {
          clearInterval(self.timer);
          this.sendAgain = true;
          return;
        }
        self.time--;
      }, 1000);
    },
    //设置cookie
    setCookie(cname, cvalue, exdays) {
      var d = new Date();
      d.setTime(d.getTime() + exdays * 24 * 60 * 60 * 1000);
      var expires = "expires=" + d.toUTCString();
      document.cookie = cname + "=" + cvalue + "; " + expires;
    },

    async web3Sign(message, account, timestamp) {
      var web3 = new Web3(this.walletProvider);
      try {
        web3.eth.personal
          .sign(message, account, "")
          .then((signature) => {
            this.loginHandle(signature, account, timestamp);
            setTimeout(() => {
              ElMessage({
                message: this.$t("AuthorizationSuccessful"),
                type: "success",
              });
            }, 500);
          })
          .catch((error) => {
            console.log(error.code);
            if (error.code == 100) {
              ElMessage({
                message: this.$t("cancleSign"),
                type: "error",
              });
            }
          });
      } catch (e) {
        return { error: e.message };
      }
    },
    async LogWithWallet(type) {
      this.loginType = type;
      if (type == "OKX Wallet") {
        if (!window.okexchain) {
          return ElMessage({
            message: this.$t("notInstallMetamask", { wallet: type }),
            type: "error",
          });
        }
        this.walletProvider = okexchain;
      } else if (type == "Bitget") {
        if (!window.bitkeep) {
          return ElMessage({
            message: this.$t("notInstallMetamask", { wallet: type }),
            type: "error",
          });
        }
        this.walletProvider = window.bitkeep.ethereum;
      } else {
        if (!window.ethereum) {
          return ElMessage({
            message: this.$t("notInstallMetamask", { wallet: type }),
            type: "error",
          });
        }
        this.walletProvider = window.ethereum;
      }

      const walletRes = await this.walletProvider.request({
        method: "eth_requestAccounts",
        params: [],
      });
      if (walletRes) {
        this.walletProvider.request({ method: "eth_chainId" }).then((res) => {
          this.$store.commit("setWalltChainId", parseInt(res) + "");
        });
        this.$store.commit("setWalletType", "MetaMask");
        this.$store.commit("setWalltAddress", walletRes[0]);

        let timestamp = parseInt(new Date().getTime() / 1000);
        var message =
          "Welcome. Login Starloom. This is completely secure and doesn't cost anything!" +
          " " +
          timestamp;
        const signature = await this.web3Sign(message, walletRes[0], timestamp);
      }
    },
    getImg(name) {
      return new URL(`../assets/images/${name}.svg`, import.meta.url).href;
    },
  },
  mounted() {},
  unmounted() {},
};
</script>
  
  <style scoped lang='scss'>
.login-box {
  font-family: Alimama-DongFangDaKai;
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
    background-color: transparent !important;
    background: url();
    background: url(/@/assets/images/LoginBg_zh.png) no-repeat 100% 100%;
    height: 389px;
    background-size: contain;
    box-shadow: none;
    border-radius: 30px;
  }
  :deep(.el-overlay-dialog) {
    backdrop-filter: blur(5px);
  }
  :deep(.el-dialog__header) {
    padding: 0;
    padding-bottom: 0;
    margin-right: 0;
    height: 0;
    position: relative;
  }
  // :deep( .el-dialog--center .el-dialog__body ){
  //   padding-top: 0px;
  // }
  .close {
    width: 0.74rem;
    height: 0.74rem;
    z-index: 1114;
    position: absolute;
    right: 5px;
    top: 60px;
    cursor: pointer;
  }

  .from {
    padding: 0rem 0.3rem;
    height: 339px;
    width: 100%;
    .maxBox {
      height: 100%;
      width: 100%;
      display: flex;
      justify-content: space-between;
      .left {
        width: 23%;
        .loginBtn,
        .signUpBtn {
          width: 80%;
          height: 0.925rem;
          margin: 0 auto;
          margin-top: 0.5rem;
          color: #341000;
          position: relative;
          cursor: pointer;
          line-height: 60px;
          text-align: center;
          font-size: 0.407rem;
          font-family: Alimama-DongFangDaKai;
          &.activeBtn {
            color: #ffffff;
            -webkit-text-stroke: 1px #37170d;
            text-stroke: 1px #37170d;
          }
          .text {
            position: absolute;
            z-index: 113;
            width: 100%;
            height: 100%;
          }
          .bg {
            height: 100%;
            position: absolute;
            z-index: 112;
            img {
              height: 100%;
              width: 100%;
            }
          }
        }
      }
      .right {
        width: 77%;
        padding: 0.2rem 1rem;
        color: #462a00;
        .input-content {
          margin-top: 0.4rem;
          :deep(.el-form-item) {
            margin-bottom: 26px;
            align-items: center;
          }
          :deep(.el-form-item__label) {
            font-family: Alimama-DongFangDaKai;
            font-size: 0.33rem;
            color: #462a00;
            line-height: 0.3rem;
            width: 1.68rem;
            z-index: 1114;
            display: flex;
            align-items: center;
          }
          .yzm-text {
            font-family: Alimama-DongFangDaKai;
            font-size: 0.33rem;
            line-height: 1rem;
          }
          .yzm-text2 {
            font-family: Alimama-DongFangDaKai;
            font-size: 0.259rem;
            line-height: 0.5rem;
          }
          .input {
            margin: 0 auto;
            height: 0.8333rem;
            border-radius: 0.37rem;
            :deep(.el-input__wrapper) {
              border-radius: 0.222rem;
              background: #f8f6f3;
              box-shadow: inset 1px 1px 5px 1px #906b13;
              &.is-focus {
                // box-shadow: none;
              }
              .el-input__inner {
                outline: none;
                font-size: 0.259rem;
                color: #462a00;
              }
              .el-icon {
                font-size: 0.4rem;
              }
            }
          }
          :deep(.btn-group) {
            padding-top: 0.4rem;
            .submit {
              height: 0.9rem;
              width: 2.7rem;
              background: url(/@/assets/images/submitBtn.png) no-repeat 100%
                100%;
              background-size: cover;
              opacity: 1;
              font-size: 0.37rem;
              font-family: Alimama-DongFangDaKas;
              color: #341000;
              border: none;
            }
          }
          :deep(.el-form-item__content) {
            justify-content: flex-end;
          }
          :deep(.el-button > span) {
            margin-bottom: 0.1rem;
          }
          .resetText {
            font-size: 0.37rem;
            padding-bottom: 0.4rem;
            margin-left: 0.7rem;
          }
          .steptext {
            margin-bottom: 0.5rem;
          }
        }
        .resend {
          display: flex;
          justify-content: flex-end;
          cursor: pointer;
        }
        .loginType {
          width: 100%;
          height: auto;
          margin-top: 50px;
          .textType {
            font-size: 0.22rem;
            font-family: Poppins, Poppins;
            font-weight: bold;
            color: #482b01;
            margin-top: 20px;
            margin-bottom: 10px;
            display: flex;
            justify-content: space-between;
            cursor: pointer;
            span {
              text-decoration: underline;
            }
          }
          .btnEmail {
            width: 100%;
            height: 1rem;
            line-height: 1rem;
            background: #4b3628;
            box-shadow: 0px 4px 20px -6px rgba(0, 0, 0, 0.15);
            border-radius: 10px;
            opacity: 1;
            border: 1px solid #a57521;
            font-size: 0.37rem;
            font-family: Poppins-Regular, Poppins;
            font-weight: 400;
            color: #ffe3a3;
            text-align: center;
            margin-bottom: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;

            img {
              margin-right: 5px;
            }
          }
          .walletDiv {
            width: 100%;
            // height: 2rem;
            border-radius: 20px;
            display: flex;
            justify-content: space-between;
            justify-items: center;
            align-items: center;
            .walletCont {
              width: 24%;
              height: 2rem;
              font-size: 12px;
              background-color: #edc996;
              margin-right: 5px;
              text-align: center;
              padding: 0.2rem 0;
              border-radius: 5px;
              color: #482b01;
              flex: 1;
              border: 1px solid #a57521;
              img {
                width: 1rem;
                height: 1rem;
                margin-bottom: 10px;
              }
              &.mb {
                padding: 5px 0;
                height: 1.5rem;
                font-size: 50%;
                margin-right: 2px;
                img {
                  width: 20px;
                  height: 20px;
                  margin-bottom: 10px;
                }
              }
            }
          }
        }
      }
    }
  }
  .otherfun {
    display: flex;
    justify-content: space-between;
    padding: 0.2rem 0;
    padding-left: 1.68rem;
    .forgetPass {
      cursor: pointer;
    }
  }

  &.mb-login-box,
  &.ipad-login-box {
    font-size: 0.22rem;
    :deep(.el-dialog) {
      height: 290px;
      // height: 4.63rem;
      background: url(/@/assets/images/LoginBg_zh_mb.png) no-repeat 100% 100%;
      background-size: contain;
    }
    .close {
      width: 0.54rem;
      height: 0.54rem;
      position: absolute;
      right: 5px;
      top: 35px;
      cursor: pointer;
    }
    .from {
      padding: 0rem 0rem;
      height: 200px;
      // height: 3.7rem;
      width: 100%;
      .maxBox {
        height: 100%;
        width: 100%;
        display: flex;
        justify-content: space-between;
        .left {
          .loginBtn,
          .signUpBtn {
            margin-top: 0.2rem;
            .text {
              font-size: 0.3rem;
            }
          }
        }
        .right {
          padding: 0.3rem 0.5rem;
          .input-content {
            margin-top: 0rem;
            :deep(.el-form-item__label) {
              // width: 1.4rem;
              line-height: 0.3rem;
              white-space: normal;
              word-wrap: break-word;
            }
            :deep(.el-form-item) {
              margin-bottom: 36px;
              align-items: center;
            }
            .emailInput {
              margin-bottom: 20px;
            }

            .input {
              margin: 0 auto;
              height: 0.73rem;
              border-radius: 0.37rem;
              :deep(.el-input__wrapper) {
                box-shadow: inset 1px 1px 4px 1px #906b13;
              }
            }
            :deep(.btn-group) {
              padding-top: 0rem;
            }
            .resetText {
              margin-left: 0rem;
            }
            // .steptext{
            //   margin-bottom: 0rem;
            // }
          }
          .resend {
            padding: 0.2rem 0;
          }
        }
      }
    }
    .otherfun {
      padding: 0.2rem 0 0.4rem;
    }
  }
  &.ipad-login-box {
    font-size: 0.22rem;
    :deep(.el-dialog) {
      height: 370px;
    }
    // .close{
    //   width: .54rem;
    //   height: .54rem;
    //   position: absolute;
    //   right: 5px;
    //   top: 35px;
    //   cursor: pointer;
    // }
    .from {
      // padding: 0rem 0rem;
      height: 320px;
      // height: 3.7rem;
      // width: 100%;
      // .maxBox{
      //   height: 100%;
      //   width: 100%;
      //   display: flex;
      //   justify-content: space-between;
      //   .left{
      //     width: 23%;
      //     .loginBtn,.signUpBtn{
      //       margin-top: .2rem;
      //     }
      //   }
      .right {
        //     padding: 0.3rem 0.5rem;
        .input-content {
          //       margin-top: 0rem;
          :deep(.el-form-item__label) {
            width: 1.5rem !important;
            line-height: 0.3rem !important;
            white-space: normal;
            word-wrap: break-word;
          }
          :deep(.el-form-item) {
            margin-bottom: 30px !important;
            align-items: center;
          }
          //       .input{
          //         margin: 0 auto;
          //         height: .73rem;
          //         border-radius: .37rem;
          //         :deep(.el-input__wrapper){
          //           box-shadow: inset 1px 1px 4px 1px #906B13;
          //         }
          //       }
          //       :deep(.btn-group){
          //         padding-top: 0rem;
          //       }
          //       .resetText{
          //         margin-left: 0rem;
          //       }
          //       // .steptext{
          //       //   margin-bottom: 0rem;
          //       // }
          //     }
          //     // .resend{
          //     //   display: flex;
          //     //   justify-content: flex-end;
          //     //   cursor: pointer;
          //     // }
        }
      }
      .left {
        width: 26%;
      }
      .right {
        width: 74%;
      }
      .submit {
        margin-top: 0.2rem;
      }
    }
    // .otherfun{
    //   padding: .2rem 0 0.4rem;
    // }
  }
}
</style>
