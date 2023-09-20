[![Starloom](./images/mainpage2.jpg)](https://starloom.ai)

# StarLoom:基于AI的算命与占卜系统

欢迎来到StarLoom，一个由数据驱动的前沿占卜系统。深入探索宇宙的奥秘，探索您的星座，并揭开命运的秘密，所有这些都得益于人工智能的帮助。  
Starloom涵盖从远古龟卜、蓍占；到汉唐以来的周易八卦、八字算命、六爻算卦、梅花数；以及民间流传的称骨算命、抽签、测名、解梦等，同时亦有从西方传入的星座运程、塔罗牌占卜等，一个博古今，占未来的AI助手。

[传送门:starloom.ai](https://starloom.ai/#/)
## ⚾主要特点
- 古典的用户界面
- 适配移动端
- 支持历史记录查看以及搜索
- 自动生成命令历史记录
- 支持Finetune
- 支持流式传输
- 支持本地部署
## 🎈系统功能
- starloom助理：从星座到解梦，StarLoom涵盖了占卜的各个方面
- 在线搜索: LLM数据陈旧，通过API和爬虫实现最新的数据访问的功能
- 知识库：加载使用文档和文件，进行embeding
- 本地部署：一键部署属于你的语言模型
- 提示功能：支持导入和修改prompt
## 🎱系统说明
- 支持中英双语切换
- 支持基于界面的模型切换
- 支持用户登录
- 输入框支持换行，聊天支持停止生成
- 支持聊天内容的复制
- 支持对聊天评论以及分享
- 对话记录自动保存，自动生成记录名
- 支持重命名历史记录
- 支持历史记录的搜索
- 界面适配PC，MAC以及移动端
## ⚒️安装
1. Clone项目目录到本地
```
$ git clone https://github.com/starloom/starloom.git
```
2. 安装依赖关系
```
$ cd starloom
$ npm install
$ pip install -r requirements.txt
```
3. 在项目根目录下创建.env.local文件，然后增加该行
```
OPENAI_API_KEY=your_openai_api_key
```
4. 运行本地部署服务
```
$ npm run serve
```
5. 在浏览器中访问你的本地应用
```
http://localhost:3000
```
6. 使用界面内的发送框进行聊天  
   🍺享受属于您的旅程吧！

