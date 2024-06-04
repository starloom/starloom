import { createStore } from 'vuex'
// import { i18n } from '/@/locales/index.js'
// const { t } = i18n.global;

const store = createStore({
  // state 提供唯一的公共数据源
  state() {
    return {
      lang: 'zh', // 语言 localStorage.getItem('lang')
      question: '', // 用户 提出的问题 全局
      imgBase64: '',   // 图片base64
      audioBase64: '', // 音频base64
      chatType: 'navs', //导航或问卦
      loginStatus: true, // 登录状态
      account: '', // 用户账号
      screenWidth: document.body.clientWidth, // 当前窗口的宽度
      selectStatus: false,  // 分享/删除 选择状态
      selectType: '',
      apiurl: 'https://service-prod.starloom.ai/chat',   // 测试 https://service-test.starloom.ai/chat   // 生产 https://service-prod.starloom.ai/chat
      v1chatUrl: 'https://service-prod.starloom.ai/v1/chat',   // 测试 https://service-test.starloom.ai/v1/chat   // 生产 https://service-prod.starloom.ai/v1/chat
      sharelink: '',
      firstLogin: '',   // 是否是第一次登录
      userModel: '4',      //localStorage.getItem('userModel') && localStorage.getItem('userModel') != '' ? localStorage.getItem('userModel') : '3.5',// 用户选择的模型  !localStorage.getItem('starloomAI-token') ? '3.5' : localStorage.getItem('userModel') || '3.5',
      haveCount: false,  //是否有条数可以继续问
      receiveType: 'audio',    // 接收音频还是文本  audio是音频   text是文本
      gptAudio: '',
      gptAudioLoading: false,
      tabList: [
        //导航部分列表
        {
          type: 'tlp',
          module: 'm',
          displayName: 'tlp',  // 塔罗牌
          img: 'https://images.swft.pro/astroAI/navType/taluopai.png',
          defQuestion:
            'tlp_openremarks'
        },
        {
          type: 'sxxz',
          module: 'a',
          displayName: 'sxxz',  // 生肖星座
          img: 'https://images.swft.pro/astroAI/navType/zodiac.png',
          defQuestion: 'sxxz_openremarks',
        },
        {
          type: 'scbz',
          module: 'b',
          displayName: 'scbz',  // 生辰八字
          img: 'https://images.swft.pro/astroAI/navType/birth.png',
          defQuestion:
            'scbz_openremarks'
        },
        {
          type: 'zgjm',
          module: 'f',
          displayName: 'zgjm',  // 周公解梦
          img: 'https://images.swft.pro/astroAI/navType/zhou.png',
          defQuestion:
            'zgjm_openremarks'
        },
        {
          type: 'fsbj',
          module: 'i',
          displayName: 'fsbj',  // 风水布局
          img: 'https://images.swft.pro/astroAI/navType/fengshui.png',
          defQuestion:
            'fsbj_openremarks'
        },
        {
          type: 'hdnj',
          module: 'j',
          displayName: 'hdnj',  // 黄帝内经
          img: 'https://images.swft.pro/astroAI/navType/huangdi.png',
          defQuestion:
            'hdnj_openremarks'
        },
        {
          type: 'cqsm',
          module: 'k',
          displayName: 'cqsm',  // 抽签算命
          img: 'https://images.swft.pro/astroAI/navType/cqsm.png',
          defQuestion:
            'gylq_openremarks'
        },
        {
          type: 'sxjm',
          module: 'q',
          displayName: 'sxjm',  // 手相揭秘
          img: 'https://images.swft.pro/astroAI/navType/sxjm.png',
          defQuestion:
            'sxjm_openremarks'
        },
        {
          type: 'rgcs',
          module: 'o',
          displayName: 'rgcs',  // '人格测试'
          img: 'https://images.swft.pro/astroAI/navType/rgcs.png',
          defQuestion:
            'jxrg_openremarks'
        },
        {
          type: 'smsz',
          module: 'p',
          displayName: 'smsz',  // '生命数字'
          img: 'https://images.swft.pro/astroAI/navType/smsz.png',
          defQuestion:
            'smsz_openremarks'
        },
        {
          type: 'zwds',
          module: 'n',
          displayName: 'zwds',  // '紫微斗数'
          img: 'https://images.swft.pro/astroAI/navType/zwds.png',
          defQuestion:
            'zwds_openremarks'
        },
        {
          type: 'zybg',
          module: 'l',
          displayName: 'zybg',  // 周易卜卦
          img: 'https://images.swft.pro/astroAI/navType/zybg.png',
          defQuestion:
            'zybg_openremarks'
        },
        {
          type: 'qmcm',
          module: 'c',
          displayName: 'qmcm',  // 起名测名
          img: 'https://images.swft.pro/astroAI/navType/naming.png',
          defQuestion:
            'qmcm_openremarks'
        },
        {
          type: 'hypd',
          module: 'd',
          displayName: 'hypd',  // '婚姻配对'
          img: 'https://images.swft.pro/astroAI/navType/marriage.png',
          defQuestion:
            'hypd_openremarks'
        },
        {
          type: 'gsqm',
          module: 'e',
          displayName: 'gsqm',  // '公司起名'
          img: 'https://images.swft.pro/astroAI/navType/companyNaming.png',
          defQuestion:
            'gsqm_openremarks'
        },
        {
          type: 'hljr',
          module: 'g',
          displayName: 'hljr',  // '黄历吉日'
          img: 'https://images.swft.pro/astroAI/navType/almanac.png',
          defQuestion:
            'hljr_openremarks'
        },
        {
          type: 'hmxj',
          module: 'h',
          displayName: 'hmjx',  // '号码吉凶'
          img: 'https://images.swft.pro/astroAI/navType/phonenum.png',
          defQuestion:
            'hmjx_openremarks'
        },
      ],
      navQueryType: {
        type: 'tlp',
        module: 'm',
        displayName: 'tlp',  // 塔罗牌
        img: 'https://images.swft.pro/astroAI/navType/taluopai.png',
        defQuestion:
          'tlp_openremarks'
      },  //导航部分选择查询的类型
      wallet: {
        address: '',
        chainId: '',
        type: ''
      }
    }
  },
  mutations: {
    setLang(state, lang) {
      state.lang = lang
    },
    setQuestion(state, question) {
      state.question = question
    },
    setNavQueryType(state, type) {
      state.navQueryType = type
    },
    setChatType(state, str) {
      state.chatType = str
    },
    setTabList(state, list) {
      state.tabList = list
    },
    setLoginStatus(state, loginStatus) {
      state.loginStatus = loginStatus
    },
    setAccount(state, account) {
      state.account = account
    },
    setScreenWidth(state, val) {
      state.screenWidth = val
    },
    setSelectStatus(state, val) {
      state.selectStatus = val
    },
    setSelectType(state, val) {
      state.selectType = val
    },
    setSharelink(state, val) {
      state.sharelink = val
    },
    setFirstLogin(state, val) {
      state.firstLogin = val
    },
    setUserModel(state, val) {
      state.userModel = val
    },
    setHaveCount(state, val) {
      state.haveCount = val
    },
    setImgBase64(state, str) {
      state.imgBase64 = str
    },
    setAudioBase64(state, str) {
      state.audioBase64 = str
    },
    setReceiveType(state, type) {
      state.receiveType = type
    },
    setGptAudio(state, type) {
      state.gptAudio = type
    },
    setGptAudioLoading(state, val) {
      state.gptAudioLoading = val
    },
    setWalletType(state, val) {
      state.wallet.type = val
    },
    setWalltAddress(state, val) {
      state.wallet.address = val
    },
    setWalltChainId(state, val) {
      state.wallet.chainId = val
    }
  },
})

export default store
