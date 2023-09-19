<template>
    <div class="login-box" :class="screenWidth<=480 ? 'mb-login-box' : screenWidth<=800 ? 'ipad-login-box' : ''">
      <el-dialog
        v-model="show"
        :show-close="false"
        :before-close="handleClose"
        :width="screenWidth<=480?'350px':screenWidth<=800 ? '470px' :'753px'"
        center
        >
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
                  <div class="text">登录</div>
                  <div class="bg">
                    <img v-if="loginStatus == 'sign-in' || loginStatus == 'forgetpassword' " src="/@/assets/images/LoginBtn_active.png" alt="" srcset="">
                    <img v-else src="/@/assets/images/LoginBtnBg.png" alt="" srcset="">
                  </div>
                </div>
                <div class="signUpBtn" @click="changeLoginTab('sign-up')" :class="loginStatus == 'sign-up' ? 'activeBtn' : '' ">
                  <div class="text" >注册</div>
                  <div class="bg">
                    <img v-if="loginStatus == 'sign-up'" src="/@/assets/images/LoginBtn_active.png" alt="" srcset="">
                    <img v-else src="/@/assets/images/LoginBtnBg.png" alt="" srcset="">
                  </div>
                </div>
              </div>
              <div class="right">
                <!-- 登录 -->
                <div class="login-max" v-if="loginStatus == 'sign-in'">
                  <div class="input-content">
                    <el-form :model="formData" :rules="formRules" ref="form" :hide-required-asterisk="true">
                      <el-form-item prop="email" label="邮箱">
                        <!-- :placeholder="$t('email')"   clearable-->
                        <el-input 
                          class="input"
                          v-model="formData.email"      
                          @input="onInput"
                        />
                      </el-form-item>
                      <el-form-item prop="password" label="密码">
                        <!--  :placeholder="$t('password')"  clearable-->
                        <el-input
                          class="input"
                          v-model="formData.password"
                          type="password"
                          show-password
                        />
                      </el-form-item>
                      <div class="otherfun">
                        <div class="forgetPass" @click="loginStatus = 'forgetpassword'">忘记密码</div>
                      </div>
                      <el-form-item class="btn-group">
                        <el-button :loading="loading" class="submit" type="primary" @click="submitForm('login')">登录</el-button>
                      </el-form-item>
                    </el-form>
                  </div>
                </div>
                 <!-- 注册 -->
                <div class="signUp-max" v-if="loginStatus == 'sign-up'">
                  <div class="step1" v-if="status=='step1'">
                    <div class="input-content">
                      <el-form :model="formData" :rules="formRules" ref="form" :hide-required-asterisk="true">
                        <el-form-item prop="email" label="邮箱">
                          <!-- :placeholder="$t('email')"  clearable-->
                          <el-input 
                            class="input"
                            v-model="formData.email"
                            @input="onInput"
                          />
                        </el-form-item>
                        <el-form-item prop="password" label="密码">
                          <el-input
                            class="input"
                            v-model="formData.password"
                            type="password"
                            show-password
                          />
                        </el-form-item>
                        <!--     :placeholder="$t('password2')"  clearable-->
                        <el-form-item prop="password2" label="确认密码">
                          <el-input
                            class="input"
                            v-model="formData.password2"
                            type="password" 
                            show-password
                          />
                        </el-form-item>
                        <el-form-item class="btn-group">
                          <el-button :loading="loading" class="submit" type="primary" @click="submitForm('sign')">注册</el-button>
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
                        <div class="yzm-text">输入验证码</div>
                        <div class="yzm-text2">请输入我们发送给{{formData.email}}的验证码</div>
                        <!--    :placeholder="$t('VerificationCode')" clearable -->
                        <el-form-item prop="captchaCode" >
                          <el-input
                           class="input mt"
                           v-model="formData.verifyCode"
                          />
                        </el-form-item>
                        <div class="resend">
                          <span @click="sendEmailCode" class="text">{{ $t('Resendcode') }}</span>
                          <span v-if="!sendAgain && time != 0">({{ time }})s</span>
                        </div>
                        <el-form-item class="btn-group">
                          <el-button :loading="sendLoading" class="submit" type="primary" @click="confirm">注册</el-button>
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
                        <div class="resetText steptext">忘记密码</div>
                        <el-form-item prop="email" label="邮箱">
                          <!-- :placeholder="$t('email')"  clearable-->
                          <el-input 
                            class="input"
                            v-model="formData.email"
                            @input="onInput"
                          />
                        </el-form-item>
                        <el-form-item class="btn-group">
                          <el-button :loading="loading" class="submit" type="primary" @click="submitForm('forgetpassword')">下一步</el-button>
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
                        <div class="yzm-text">输入验证码</div>
                        <div class="yzm-text2">请输入我们发送给{{formData.email}}的验证码</div>
                        <!--    :placeholder="$t('VerificationCode')" clearable -->
                        <el-form-item prop="captchaCode" >
                          <el-input
                           class="input mt"
                           v-model="formData.verifyCode"
                          />
                        </el-form-item>
                        <div class="resend">
                          <span @click="sendCodeResetPassword" class="text">{{ $t('Resendcode') }}</span>
                          <span v-if="!sendAgain && time != 0">({{ time }})s</span>
                        </div>
                        <el-form-item class="btn-group">
                          <el-button class="submit" type="primary" @click="goStep4">下一步</el-button>
                        </el-form-item>
                      </el-form>
                    </div>
                  </div>
                  <div class="step2" v-if="status=='step4'">
                    <div class="input-content">
                      <el-form :model="formData" :rules="formRules" ref="form" :hide-required-asterisk="true">
                        <div class="resetText">设置新密码</div>
                        <el-form-item prop="password" label="密码">
                          <el-input
                            class="input"
                            v-model="formData.password"
                            type="password"
                            show-password
                          />
                        </el-form-item>
                        <!--     :placeholder="$t('password2')"  clearable-->
                        <el-form-item prop="password2" label="确认密码">
                          <el-input
                            class="input"
                            v-model="formData.password2"
                            type="password" 
                            show-password
                          />
                        </el-form-item>
                        <el-form-item class="btn-group">
                          <el-button :loading="sendLoading" class="submit" type="primary" @click="confirmReset()">确认</el-button>
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
  import { ref, computed, watch } from 'vue';
  import { useStore} from 'vuex'
  import { useI18n } from 'vue-i18n'
  import { Aim,Back } from '@element-plus/icons-vue'
  import VueHcaptcha from '@hcaptcha/vue3-hcaptcha';
  import EventBus from '/@/utils/EventBus.js'
  import {userLogin,register,sendEmailCode, sendCodeResetPassword, checkEmailCodeResetPassword, resetPassword} from '/@/api/api'
  
  export default {
    name: 'Login',
    props:['loginShow'],
    setup(props) {
      const store = useStore()
      const { t } = useI18n();
      const show = ref(props.loginShow)
      const status = ref('step1') // 状态区分 登录注册和发送验证码
      //适配
      const screenWidth = computed( () => {
        return store.state.screenWidth
      }) 
      // 是否是第一次登录
      const firstLogin = computed( () => {
        return store.state.firstLogin
      })
      const PC = ref('width: 303px;margin:50px auto')
      const MB = ref("margin: 30px 0px 0 30px;")
      const IPAD = ref("margin: 30px 0px 0 50px;")
      const formData = ref({
        email: '',
        password: '',
        password2:'',
        verifyCode:'',
      });
      const lang = computed(() => {
        return store.state.lang
      })

      // const verifyCode = ref('')
      const formRules = ref({
        email: [
          { required: true, message: t('enterEmail'), trigger: 'blur' },
          { type: 'email', message: t('sureEmail'), trigger: 'blur' },
        ],
        password: [
          { required: true, message: t('enterpassword'), trigger: 'blur' },
          { min: 6, max: 20, message: t('passwordLength'), trigger: 'blur' },
        ],
        password2: [
          { required: true, message: t('enterpassword2'), trigger: 'blur' },
        ],
        // verifyCode
        verifyCode: [
          { required: true, message: t('VerificationCode'), trigger: 'blur' },
        ],
      });
      watch(() => store.state.lang,(val) => {
        formRules.value = {
          email: [
            { required: true, message: t('enterEmail'), trigger: 'blur' },
            { type: 'email', message: t('sureEmail'), trigger: 'blur' },
          ],
          password: [
            { required: true, message: t('enterpassword'), trigger: 'blur' },
            { min: 6, max: 20, message: t('passwordLength'), trigger: 'blur' },
          ],
          password2: [
            { required: true, message: t('enterpassword2'), trigger: 'blur' },
          ],
          verifyCode: [
          { required: true, message: t('VerificationCode'), trigger: 'blur' },
        ],
        }
      })
      const loginStatus = ref('sign-in')
      const password = ref('')
      // 请求状态
      const loading = ref(false)
      const sendLoading = ref(false)
      
      // 重新发送验证码倒计时
      const timer = ref(null)
      const time = ref(60)
      const sendAgain = ref(true)
      // watch(loginStatus,(val)=>{
      //   if(val == 'sign-up'){
      //     hcaptchaStatus.value = false
      //   }
      // })
       //人机校验
      const hcaptchaStatus = ref(false)
      const hcaptchaToken = ref('')
      // const verifySuccess = (token, eKey) => {
      //   hcaptchaToken.value = token
      //   hcaptchaStatus.value = true
      //   sendEmailCode()
      // }
      const changeLoginTab = (tab)=>{
        loginStatus.value = tab
        status.value = 'step1'
      }
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
     } 
    },
    components: {
      VueHcaptcha,
    },
    watch: {
      'loginShow'(a){
        this.show = a  
      },
    },
    methods: {
      handleClose(done){
        this.status = 'step1'
        this.loginStatus = 'sign-in'
        this.show = false
        this.$emit('closeLogin','closeLogin')
      },
      onInput() {
        // Replace all spaces with an empty string as the user types
        this.formData.email = this.formData.email.replace(/\s/g, '');
      },
      verifySuccess (token, eKey) {
        this.hcaptchaToken = token
        this.hcaptchaStatus = true
        if(this.loginStatus == "sign-up"){
          this.sendEmailCode()
        }else if(this.loginStatus == "forgetpassword"){
          this.sendCodeResetPassword()
        }  
      },
      submitForm(type){
        const form = this.$refs.form;
        form.validate((valid) => {
          if (valid) {
            //登录
            if(type =='login'){
              this.loginHandle()
            }else if(type == 'sign'){  
              //注册
              this.signnHandle()
            } else if( type == 'forgetpassword'){ // 忘记密码
              this.forgetpasswordHandle()
            }
          } 
        })
      },
      async loginHandle(){
        this.loading = true
        const res = await userLogin({
          email: this.formData.email,
          password: this.formData.password,
        })
        this.loading = false
        if(res.code == 200 && res.data){
            localStorage.setItem('starloomAI-token',res.data.user_token)
            this.$emit('loginSuccess',res.data.account)
            localStorage.setItem('userId',res.data.user_id)
            this.formData.verifyCode = ''
            this.formData.email = ''
            this.formData.password = ''
            this.formData.password2 = ''
            this.show = false
            this.$emit('closeLogin','closeLogin')
            if(!this.firstLogin){
              EventBus.$emit('showModelDialogHandle')
              this.setCookie('firstLogin', 1, 365)
            }  
        }
        else if(res.code == 2002){
          ElMessage({
            message: this.$t('IncorrectLogin'),
            type: 'error',
          })
        }else if(res.code == 2001){
          ElMessage({
            message: this.$t('accountError'),
            type: 'error',
          })
        }
      },
      async signnHandle(){
        if(!this.sendAgain || this.loading){
          return
        }
        //校验第二次呼入密码是否正确
        if(this.formData.password != this.formData.password2){
          ElMessage({
            message: this.$t('passwordNosame'),
            type: 'error',
          })
          return
        }
        this.status = 'step2'
      },
      async sendEmailCode(){
        if(!this.sendAgain || this.loading){
          return
        }
        // 发送邮箱验证码
        this.loading = true
        const res = await sendEmailCode({
          email: this.formData.email,
          'g-recaptcha-response': this.hcaptchaToken,
          language: this.lang
        })
        this.loading = false
        clearInterval(this.timer)
        this.time = 60
        this.Countdown()
        console.log(res)
        if(res.code == 200){
            this.sendAgain = false
            this.$refs.hcaptcha.reset()
            this.status = 'step3'

            ElMessage({
              message: this.$t('sendSuccess'),
              type: 'success',
            })
        }else{
          if(res.code == 2004){
            this.status = 'step2'
            return
          }
          ElMessage({
              message: this.$t(res.code),
              type: 'error',
            })
        }
      },
      //提交注册
      async confirm(){
        if(!this.formData.verifyCode) return
        this.sendLoading = true
        const res = await register({
          email: this.formData.email,
          verifyCode: this.formData.verifyCode,
          password: this.formData.password,
        })
        this.sendLoading = false
        if(res.code == 2009){
          ElMessage({
            message: this.$t('codeError'),
            type: 'error',
          })
          return 
        }
        if(res.code == 200 && res.data){
          ElMessage({
            message: this.$t('signSuccess'),
            type: 'success',
          })
          this.status = 'step1'
          this.loginStatus = 'sign-in'
          this.formData.verifyCode = ''
          this.formData.email = ''
          this.formData.password = ''
          this.formData.password2 = ''
        }
      },
      forgetpasswordHandle(){
        this.status = 'step2'
      },
      async sendCodeResetPassword(){
        if(!this.sendAgain || this.loading){
          return
        }
        // 发送邮箱验证码
        // this.loading = true
        this.sendAgain = false
        const res = await sendCodeResetPassword({
          email: this.formData.email,
          'g-recaptcha-response': this.hcaptchaToken,
          language: this.lang
        })
        // this.loading = false
        clearInterval(this.timer)
        this.time = 60
        this.Countdown()
        console.log(res)
        if(res.code == 200){
            this.sendAgain = false
            this.$refs.hcaptcha.reset()
            this.status = 'step3'

            ElMessage({
              message: this.$t('sendSuccess'),
              type: 'success',
            })
        }else{
          this.sendAgain = true
          if(res.code == 2004){
            this.status = 'step2'
            return
          }
          ElMessage({
              message: this.$t(res.code),
              type: 'error',
            })
        }
      },
      async goStep4() {
        if(!this.formData.verifyCode) return
        const res = await checkEmailCodeResetPassword({
          email: this.formData.email,
          verifyCode: this.formData.verifyCode
        })
        if(res.code == 200 && res.data){
          if( res.data.is_checked == 1 ){
            this.status = 'step4'
          } else if(res.data.is_checked == 0){
            ElMessage({
              message: '验证码不正确',
              type: 'error',
            })
            return 
          }
        }
      },
      //提交注册
      // if(!this.formData.verifyCode) return
      async confirmReset(){
        //密码校验
        if(this.formData.password.length<6 || this.formData.password.length>20 ){
          return
        }
         //校验第二次呼入密码是否正确
         if(this.formData.password != this.formData.password2){
          ElMessage({
            message: this.$t('passwordNosame'),
            type: 'error',
          })
          return
        }
        this.sendLoading = true
        const res = await resetPassword({
          email: this.formData.email,
          verifyCode: this.formData.verifyCode,
          password: this.formData.password,
        })
        this.sendLoading = false
        if(res.code == 2009){
          ElMessage({
            message: this.$t('codeError'),
            type: 'error',
          })
          return 
        }
        if(res.code == 200){
          ElMessage({
            message: '新密码设置成功',
            type: 'success',
          })
          this.status = 'step1'
          this.loginStatus = 'sign-in'
          this.formData.verifyCode = ''
          this.formData.email = ''
          this.formData.password = ''
          this.formData.password2 = ''
        }
      },
      Countdown(){
        const self = this
        clearInterval(self.timer)
        self.timer = setInterval( ()=> {
          if(self.time == 0){
            clearInterval(self.timer)
            this.sendAgain = true
            return
          }
          self.time --
        },1000)
      },
      //设置cookie
      setCookie(cname, cvalue, exdays) {
        var d = new Date()
        d.setTime(d.getTime() + exdays * 24 * 60 * 60 * 1000)
        var expires = 'expires=' + d.toUTCString()
        document.cookie = cname + '=' + cvalue + '; ' + expires
      },
    },
    mounted() {
      
    },
    unmounted() {
      
    },
  }
  </script>
  
  <style scoped lang='scss'>
  
  .login-box{
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
    :deep(.el-overlay-dialog)  {
      backdrop-filter: blur(5px);
    }
    :deep(.el-dialog__header ){
      padding: 0; 
      padding-bottom: 0; 
      margin-right: 0; 
      height: 0;
      position: relative;
    }
    // :deep( .el-dialog--center .el-dialog__body ){ 
    //   padding-top: 0px;
    // }
      .close{
        width: .74rem;
        height: .74rem;
        z-index: 1114;
        position: absolute;
        right: 5px;
        top: 60px;
        cursor: pointer;
      }

    .from{
      padding: 0rem .3rem;
      height: 339px;
      width: 100%;
      .maxBox{
        height: 100%;
        width: 100%;
        display: flex;
        justify-content: space-between;
        .left{
          width: 23%;
          .loginBtn,.signUpBtn{
            width: 80%;
            height: .925rem;
            margin: 0 auto;
            margin-top: .5rem;
            color: #341000;
            position: relative;
            cursor: pointer;
            line-height: 60px;
            text-align: center;
            font-size: .407rem;
            font-family: Alimama-DongFangDaKai;
            &.activeBtn{
              color: #FFFFFF;
              -webkit-text-stroke: 1px #37170D;
              text-stroke: 1px #37170D;
            }
            .text{
              position: absolute;
              z-index: 113;
              width: 100%;
              height: 100%;
            }
            .bg{
              height: 100%;
              position: absolute;
              z-index: 112;
              img{
                height: 100%;
                width: 100%;
              }
            }
          }
          
        }
        .right{
          width: 77%;
          padding: .2rem 1rem;
          color: #462A00;
          .input-content{
            margin-top: .4rem;
            :deep(.el-form-item__label){
              font-family: Alimama-DongFangDaKai;
              font-size: .33rem;
              color: #462A00;
              line-height: .8333rem;
              width: 1.68rem;
              z-index: 1114;
            }
            .yzm-text{
              font-family: Alimama-DongFangDaKai;
              font-size: .33rem;
              line-height: 1rem;
            }
            .yzm-text2{
              font-family: Alimama-DongFangDaKai;
              font-size: .259rem;
              line-height: .5rem;
            }
            .input{
              margin: 0 auto;
              height: .8333rem;
              border-radius: .37rem;
              :deep(.el-input__wrapper){
                border-radius: .222rem;
                background: #F8F6F3;
                box-shadow: inset 1px 1px 5px 1px #906B13;
                &.is-focus{
                  // box-shadow: none;
                }
                .el-input__inner{
                  outline: none;
                  font-size: .259rem;
                  color: #462A00;
                }
                .el-icon {
                  font-size: .4rem;
                }
              }  
            } 
            :deep(.btn-group){
              padding-top: .4rem;
              .submit{
                height: .9rem;
                width: 2.7rem;
                background: url(/@/assets/images/submitBtn.png) no-repeat 100% 100%;
                background-size: cover;
                opacity: 1;
                font-size: .37rem;
                font-family: Alimama-DongFangDaKas;
                color: #341000;
                border: none;
              }
            }
            :deep(.el-form-item__content) {
              justify-content: flex-end;
            }   
            :deep(.el-button>span) {
              margin-bottom: 0.1rem;
            } 
            .resetText{
              font-size: .37rem;
              padding-bottom: 0.4rem;
              margin-left: 0.7rem;
            }
            .steptext{
              margin-bottom: .5rem;
            } 
          }
          .resend{
            display: flex;
            justify-content: flex-end;
            cursor: pointer;
          }
        }
      }
    }
    .otherfun{
      display: flex;
      justify-content: flex-end;
      padding: .2rem 0;
      .forgetPass{
        cursor: pointer;
      }
    }

    &.mb-login-box,&.ipad-login-box{
      font-size: .22rem;
      :deep(.el-dialog) {
        height: 250px;
        // height: 4.63rem;
        background: url(/@/assets/images/LoginBg_zh_mb.png) no-repeat 100% 100%;
        background-size: contain;
      }
      .close{
        width: .54rem;
        height: .54rem;
        position: absolute;
        right: 5px;
        top: 35px;
        cursor: pointer;
      }
      .from{
        padding: 0rem 0rem;
        height: 200px;
        // height: 3.7rem;
        width: 100%;
        .maxBox{
          height: 100%;
          width: 100%;
          display: flex;
          justify-content: space-between;
          .left{  
            .loginBtn,.signUpBtn{
              margin-top: .2rem;
            } 
          }
          .right{
            padding: 0.3rem 0.5rem;
            .input-content{
              margin-top: 0rem;
              :deep(.el-form-item__label){
                width: auto;
                line-height: .73rem;
              }
              // :deep(.el-form-item ){
              //     margin-bottom: 8px;
              // }
              .input{
                margin: 0 auto;
                height: .73rem;
                border-radius: .37rem;
                :deep(.el-input__wrapper){  
                  box-shadow: inset 1px 1px 4px 1px #906B13;
                } 
              } 
              :deep(.btn-group){
                padding-top: 0rem;
              }
              .resetText{
                margin-left: 0rem;
              }
              // .steptext{
              //   margin-bottom: 0rem;
              // } 
            }
            .resend{
              padding: 0.2rem 0;
            }
          }
        }
      }
      .otherfun{
        padding: .2rem 0 0.4rem;
      }

    }
    &.ipad-login-box{
      font-size: .22rem;
      :deep(.el-dialog) {
        height: 320px;
      }
      // .close{
      //   width: .54rem;
      //   height: .54rem;
      //   position: absolute;
      //   right: 5px;
      //   top: 35px;
      //   cursor: pointer;
      // }
      .from{
        // padding: 0rem 0rem;
        height: 270px;
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
        //   .right{
        //     padding: 0.3rem 0.5rem;
        //     .input-content{
        //       margin-top: 0rem;
        //       :deep(.el-form-item__label){
        //         width: auto;
        //         line-height: .73rem;
        //       }
        //       // :deep(.el-form-item ){
        //       //     margin-bottom: 8px;
        //       // }
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
        //   }
        // }
        .left{
          width: 26%;
        }
        .right{
          width: 74%;
        }
        .submit {
          margin-top: .2rem;
        }
      }
      // .otherfun{
      //   padding: .2rem 0 0.4rem;
      // }
    }
  }
  </style>
