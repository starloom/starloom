import { createApp } from 'vue'
import './assets/scss/main.scss'
import App from './App.vue'
import 'lib-flexible'

// 导入 store
import store from './store'
import i18n from './locales'
import router from './route'
const app = createApp(App)
app.config.globalProperties.$formatNumber = (num) => {
    if(!num){
        return 0
      }
      num = Number(num).toFixed(6) - 0
      const parts = num.toString().split('.')
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',')
      return parts.join('.')
}
app.use(store)
app.use(i18n)
app.use(router)
app.mount('#app')
