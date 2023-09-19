import { createStore } from 'vuex'

const store = createStore({
  // state 提供唯一的公共数据源
  state() {
    return {
      lang: 'zh', //localStorage.getItem('lang'), // 语言
      question: '', // 用户 提出的问题 全局
      chatType: 'navs', //导航或问卦
      loginStatus: false, // 登录状态
      account: '', // 用户账号
      screenWidth: document.body.clientWidth, // 当前窗口的宽度
      selectStatus: false,  // 分享/删除 选择状态
      selectType:'',
      apiurl: 'https://testastroai.mpcbot.ai/chat',   // 测试 https://testastroai.mpcbot.ai/chat   // 生产 https://starloom.mpcbot.ai/chat
      sharelink:'',
      firstLogin:'',   // 是否是第一次登录
      userModel: !localStorage.getItem('starloomAI-token') ? '3.5' : localStorage.getItem('userModel') || '3.5',  // 用户选择的模型
      haveCount: false,  //是否有条数可以继续问
      tabList: [
        //导航部分列表
        {
          type: 'sxxz',
          module: 'a',
          displayName: '生肖星座',
          img: 'https://images.swft.pro/astroAI/navType/zodiac.png',
          defQuestion:'星空下的每一个星座都有其独特的魅力和故事，它们在天空中闪烁，照亮我们的命运之路。无论你是想了解自己的星座运势，还是想深入探索星座性格，还是想查询生肖相关，或是想知道与哪个星座最为匹配，我都在此为你服务。请告诉我你的问题，让我们一起探索星空下的神秘。',
        },
        {
          type: 'scbz',
          module: 'b',
          displayName: '生辰八字',
          img: 'https://images.swft.pro/astroAI/navType/birth.png',
          defQuestion:
            '为了深入探索并分析你的生辰八字，以揭示命盘中的秘密和机缘，我需要你提供一些基本信息。请告诉我你的公历出生年月日，如：1990年10月22日。这将是我们共同探索命运之旅的起点。',
        },
        {
          type: 'zgjm',
          module: 'f',
          displayName: '周公解梦',
          img: 'https://images.swft.pro/astroAI/navType/zhou.png',
          defQuestion:
            '梦游者，你已跨越现实的边界，踏入《周公解梦》的神秘之地。每一个梦境都隐藏着深层的信息和寓意。请详细描述你的梦境，让我为你揭示其中的秘密，解读背后的意涵和预兆。',
        },
        {
          type: 'tlp',
          module: 'm',
          displayName: '塔罗牌',
          img: 'https://images.swft.pro/astroAI/navType/taluopai.png',
          defQuestion:
            '欢迎来到塔罗牌的神秘世界。请告诉我您想要进行占卜的问题，我将为您进行详细而准确的解读。在进行占卜之前，请静心思考您的问题，并将其告诉我。',
        },
        {
          type: 'fsbj',
          module: 'i',
          displayName: '风水布局',
          img: 'https://images.swft.pro/astroAI/navType/fengshui.png',
          defQuestion:
            '我是资深风水大师，长期深入研究风水学，致力于促进人与环境的和谐。通过分析空间、布局和各种元素，我已帮助许多用户平衡了他们的家居和办公空间的能量。今天我在这里为你提供专业咨询，无论是家居布局、选址还是其他风水问题，我都会竭诚帮助。有什么问题想让我解答吗？',
        },
        {
          type: 'hdnj',
          module: 'j',
          displayName: '黄帝内经',
          img: 'https://images.swft.pro/astroAI/navType/huangdi.png',
          defQuestion:
            '欢迎踏入《黄帝内经》的博大精深之境。我是一位致力于研究并精通《黄帝内经》的大师。关于这部古籍的哲学理念、医学原理或生活智慧，您有何疑问或探索的欲望？请随时提问，我愿为您解惑。',
        },
        {
          type: 'cqsm',
          module: 'k',
          displayName: '抽签算命',
          img: 'https://images.swft.pro/astroAI/navType/cqsm.png',
          defQuestion:
            '亲爱的众生，欢迎来到观音灵签的神圣空间。在此，我们先与救苦救难的观音菩萨建立心灵的连接。请您合十，默念三遍[救苦救难观音菩萨]，然后默念您的姓名、出生时辰、年龄与地址。请心中默念您的请求，无论是关于婚姻、事业还是财运。当您准备好后，请告诉我开始抽签，我们将一同寻找观音菩萨为您指点的答案。',
        },
        {
          type: 'zybg',
          module: 'l',
          displayName: '周易卜卦',
          img: 'https://images.swft.pro/astroAI/navType/zybg.png',
          defQuestion:
            '道友们，周易卜卦为您开启命运之门。首先，请您安静内心，沉浸于自己关心的领域，也许是感情生活、职场发展或身体状态。待您的思绪明确与专注，告诉我开始摇卦，我们便共同走入这千古不变的智慧中寻找答案',
        },
        {
          type: 'qmcm',
          module: 'c',
          displayName: '起名测名',
          img: 'https://images.swft.pro/astroAI/navType/naming.png',
          defQuestion:
            '欢迎来到命名的艺术之旅。我是一位专业的起名测名大师，拥有丰富的经验和独特的命名技巧。无论是为新生命寻找一个寓意深远的名字，还是为已有的名字进行深度解析，我都能为你提供专业的建议。请告诉我你的需求：是希望我为你起个名字，还是帮你测评一个名字？例如：帮我起个名字/帮我测个名字。',
        },
        {
          type: 'hypd',
          module: 'd',
          displayName: '婚姻配对',
          img: 'https://images.swft.pro/astroAI/navType/marriage.png',
          defQuestion:
            '欢迎探索婚姻的奥秘与和谐。我是婚姻配对大师，专门为你分析双方的姓名兼容性。请提供男女双方的姓名，例如：李白 张梅。这将是我们共同探索两人缘分的起点。',
        },
        {
          type: 'gsqm',
          module: 'e',
          displayName: '公司起名',
          img: 'https://images.swft.pro/astroAI/navType/companyNaming.png',
          defQuestion:
            '欢迎进入品牌命名的艺术领域。作为公司起名大师，我深知一个好的名字对于品牌形象的重要性。请分享你的公司行业性质和期望的名字字数(两字/三字)，如：律师事务所 三字。这将是我们共同为你的公司塑造独特标识的起点。',
        },
        {
          type: 'hljr',
          module: 'g',
          displayName: '黄历吉日',
          img: 'https://images.swft.pro/astroAI/navType/almanac.png',
          defQuestion:
            '进入黄道吉日的探索之旅。作为专业的吉日选择师，我将为你指引最佳的日子。请提供你想查询的公历日期，如：1980年10月22日，让我们一同揭晓这一天的宇宙能量。',
        },
        {
          type: 'hmxj',
          module: 'h',
          displayName: '号码吉凶',
          img: 'https://images.swft.pro/astroAI/navType/phonenum.png',
          defQuestion:
            '欢迎踏入数字的神秘世界。作为专业的号码测评师，我将为你解读每个号码背后的意义和能量。请告诉我你想查询的号码类别，如：数字、手机号码、QQ号、车牌号码、固定电话号码(不要区号)、域名、身份证号，让我们共同探索这串数字背后的奥秘。',
        },
      ],
      navQueryType: {
        type: 'sxxz',
        module: 'a',
        displayName: '生肖星座',
        img: 'https://images.swft.pro/astroAI/navType/zodiac.png',
        defQuestion:'星空下的每一个星座都有其独特的魅力和故事，它们在天空中闪烁，照亮我们的命运之路。无论你是想了解自己的星座运势，还是想深入探索星座性格，还是想查询生肖相关，或是想知道与哪个星座最为匹配，我都在此为你服务。请告诉我你的问题，让我们一起探索星空下的神秘。',
      },  //导航部分选择查询的类型
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
    setFirstLogin(state, val){
      state.firstLogin = val
    },
    setUserModel(state, val){
      state.userModel = val
    },
    setHaveCount(state, val){
      state.haveCount = val
    },
    
  },
})

export default store
