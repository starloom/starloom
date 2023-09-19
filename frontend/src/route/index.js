import { createRouter, createWebHashHistory } from "vue-router"

const Index = () => import("../page/Index.vue")
const Crypto = () => import("../page/Crypto.vue")
const Chat = () => import("../page/Chat.vue")
const AskDivination = () => import("../page/AskDivination.vue")
const Success = () => import("../components/ChatComponent/Success.vue")
const Cancel = () => import("../components/ChatComponent/Cancel.vue")

const routes = [
  {
    path: "/",
    name: "index",
    component: Index
  },
  // {
  //   path: "/crypto",
  //   name: "crypto",
  //   component: Crypto
  // },
  {
    path: "/askDivination/:id",
    name: "askDivination",
    component: AskDivination
  },
  {
    path: "/chat/:shareKey",
    name: "chat",
    component: Chat
  },
  // {
  //   path: "/success",
  //   name: "success",
  //   component: Success
  // },
  // {
  //   path: "/cancel",
  //   name: "cancel",
  //   component: Cancel
  // },
]
const router = createRouter({
    history: createWebHashHistory(),
    routes: routes
  })
  export default router