<template>
    <div class="index" :class="screenWidth<=900? 'mb-index' : ''">
        <div class="constellation-box" v-if="(navQueryType.type=='cqsm')&& screenWidth>900">
          <ul class="list" >
            <li v-if="navQueryType.type=='sxxz'" v-for="(item, index) in constellation" :key="index" @click="changeQuetype(item)" :class="item.type== sxxzType.type ? 'active' : ''">{{ item.name }}</li>
            <li v-if="navQueryType.type=='cqsm'" v-for="(item, index) in cqsmSub" :key="index" @click="changeCQSMtype(item)" :class="item.type== cqsmType.type ? 'active' : ''">{{ item.name }}</li>
          </ul>
        </div>
        <div class="mb-constellation-box" v-if="( navQueryType.type=='cqsm') && screenWidth<=900">
          <ul class="list" v-if="!moduletab_mb">
            <li v-if="navQueryType.type=='sxxz'"  v-for="(item1, index1) in constellation.slice(0, 3)" :key="index1"  @click="changeQuetype(item1)" :class="item1.type== sxxzType.type ? 'active' : ''">{{ item1.name }}</li>
            <li v-if="navQueryType.type=='cqsm'"  v-for="(item1, index1) in cqsmSub.slice(0, 3)" :key="index1"  @click="changeCQSMtype(item1)" :class="item1.type== cqsmType.type ? 'active' : ''">{{ item1.name }}</li>
            <li class="btn" @click="moduletab_mb = true">
              <div>展开</div>
              <img src="/@/assets/images/caret-up-square.png" alt="">
            </li>
          </ul>
          <ul class="list" v-if="moduletab_mb">
            <li v-if="navQueryType.type=='sxxz'"  v-for="(item, index) in constellation" :key="index" @click="changeQuetype(item)" :class="item.type== sxxzType.type ? 'active' : ''">{{ item.name }}</li>
            <li v-if="navQueryType.type=='cqsm'"  v-for="(item, index) in cqsmSub" :key="index" @click="changeCQSMtype(item)" :class="item.type== cqsmType.type ? 'active' : ''">{{ item.name }}</li>
            <li class="nostyle">
            </li>
            <li class="btn"  @click="moduletab_mb = false">
              <div>收起</div>
              <img src="/@/assets/images/caret-down-square.png" alt="">
            </li>
          </ul>
        </div>
        <template v-if="false">
          <div class="chatmaxbox" v-if="navQueryType.type=='sxxz'" :class="screenWidth<=900? !moduletab_mb ? 'mb' : 'mb_small' : ''">
            <div class="chat" ref="chatContent">
              <!-- v-if="sxxzType.type === 'xzys'" -->
                <!-- 文字对话 -->
                <!-- v-if="item.type  == 'text' || item.role == 'user'" -->
                <div class="chat-list">
                  <div  class="answer">
                    <div class="BotHeader">
                      <img class="avatar" :class="screenWidth<=900 ? 'mbImg' : ''" src="/@/assets/images/aibot.png" alt="">
                      <div v-if="screenWidth<=900">天机阁</div>
                    </div>
                  
                    <div class="text-content">
                        <div class="inner">
                          <div class="zindex">{{ sxxzType.defaultQue }}</div>
                          <div class="xiangyun"></div>
                        </div>
                    </div>
                  </div>
                </div>
                <!-- <div class="chat-list">
                  <div  class="answer">
                    <div class="BotHeader">
                      <img class="avatar" :class="screenWidth<=900 ? 'mbImg' : ''" src="/@/assets/images/aibot.png" alt="">
                      <div v-if="screenWidth<=900">天机阁</div>
                    </div>
                  
                    <div class="text-content">
                        <div class="inner">
                          <div class="zindex">{{ text }}</div>
                        </div>
                        
                    </div>
                  </div>
                </div> -->
    
                <!-- <template v-if="true">
                    <AstrologicalHouseChart />
                  </template> -->
                  <!-- <template v-if="true">
                    <PlanetInSign />
                  </template> -->
                <template v-if="chatList.length>0">
                  <template v-for="(item,index) in chatList" :key="index">
                    <template v-if="(item.showtype  == 'text' || item.role == 'user') && item.submodel == sxxzType.submodel && !item.islike">
                      <div class="chat-list" :class="item.role == 'user' ? 'right-content' : ''">
                        <div v-if="item.role == 'user'" class="question" @mouseover="onHover(item)" @:mouseleave="onMouseLeave(item)">
                          <div class="text-content" >
                              <div class="inner">
                                  {{item.content}}
                              </div>
                          </div>
                          <img v-if="screenWidth>900" class="avatar" src="/@/assets/images/user.png" alt="">
                        </div>
                        <div v-if="item.role == 'assistant'" class="answer" @mouseover="onHover(item)" @:mouseleave="onMouseLeave(item)">
                          <div class="BotHeader">
                            <img class="avatar" :class="screenWidth<=900 ? 'mbImg' : ''" src="/@/assets/images/aibot.png" alt="">
                            <div v-if="screenWidth<=900">天机阁</div>
                          </div>
                          <div class="text-content">
                              <div class="inner">
                                <div class="zindex" v-html="item.content"></div>
                                <div class="xiangyun"></div>
                              </div>
                          </div>
                        </div>
                    </div>
                    </template>
                  
                    <!-- <div class="chat-list right-content">
                          <div class="question">
                            <div class="text-content">
                                <div class="inner">
                                  射手座
                                </div>
                            </div>
                            <img class="avatar" src="/@/assets/images/user.svg" alt="">
                          </div> -->
                          <!-- <div  class="answer">
                              <img src="/@/assets/images/logo.svg" alt="">
                              <div class="text-content">
                                  <div class="inner">
                                      haha
                                  </div>
                              </div>
                          </div> -->
                      <!-- </div> -->
                  <!-- v-if="item.type == 'tem' && item.type == 'tem'" -->
                    <template v-if="item.role == 'assistant' && item.showtype == 'tem' && item.submodel == sxxzType.submodel && !item.islike">
                      <!-- 生肖查询a-1 -->
                      <template v-if="item.submodel === 'a-1'"> 
                          <ZodiacQuery :presetData="item.content"/>
                      </template>
                      <!-- 生肖运势a-2 -->
                      <template v-if="item.submodel === 'a-2'">
                        <ChineseZodiacFortune :presetData="item.content"/>
                      </template>
                      <!-- 上升星座a-3 -->
                      <template v-if="item.submodel === 'a-3'">
                        <Ascendant :presetData="item.content" />
                      </template>
                      <!-- 下降星座a-4 -->
                      <template v-if="item.submodel === 'a-4'">
                        <DescendingZodiac :presetData="item.content"/>
                      </template>
                      <!-- 星座运势a-5 -->
                      <template v-if="item.submodel === 'a-5'">
                          <Horoscope
                            :presetData="item.content"
                            :index="index"
                            @chageTab="chageTab"
                          />
                      </template>
                      <!-- 星座查询a-6 -->
                      <template v-if="item.submodel ===  'a-6'">
                        <ConstellationInquir :presetData="item.content"/>
                      </template>
                      <!-- 星座排行榜a-7 -->
                      <template v-if="item.submodel ===  'a-7' && item.questionType == 1">
                        <ConstellationRankingList
                        :presetData="item.content"
                        :page="rankPage"
                        :index="index"
                        @chageRankTab="chageRankTab"
                        @getXingzuoRanking="getXingzuoRanking"
                        />
                      </template>
                      <!-- 排行榜详情a-7 -->
                      <template v-if="item.submodel === 'a-7' && item.questionType == 2">
                        <ConstellationRankingItem :presetData="item.content"/>
                      </template>
                      <!-- 生日花a-8 -->
                      <template v-if="item.submodel === 'a-8'">
                        <BirthdayFlower :presetData="item.content" />
                      </template>
                      <!-- 月亮星座a-9 -->
                      <template v-if="item.submodel === 'a-9'">
                        <MoonSign :presetData="item.content"/>
                      </template>
                      <!-- 48星区a-10 -->
                      <template v-if="item.submodel === 'a-10'">
                        <Constellations48 :presetData="item.content"/>
                      </template>
                      <!-- 生日密码a-11 -->
                      <template v-if="item.submodel === 'a-11'">
                        <BirthdatePassword :presetData="item.content" />
                      </template>
                      <!-- 生日书a-12 -->
                      <template v-if="item.submodel === 'a-12'">
                        <BirthdayBook :presetData="item.content"/>
                      </template>
                      <!-- 测试出轨对象a-13 -->
                      <template v-if="item.submodel === 'a-13'">
                        <CheatingPerson :presetData="item.content"/>
                      </template>
                      <!-- 星盘查询a-14 -->
                      <template v-if="item.submodel === 'a-14'">
                        <AstrologicalChart :presetData="item.content" />
                      </template>
                      <!-- 行星落宫位解析a-17 -->
                      <template v-if="item.submodel === 'a-17'">
                        <PlanetInHouse :presetData="item.content" />
                      </template>
                      <!-- 行星落星座解析a-18 -->
                      <template v-if="item.submodel === 'a-18'">
                        <PlanetInSign :presetData="item.content" />
                      </template>
                      <!-- 宫位查询a-15 -->
                      <template v-if="item.submodel === 'a-15'">
                        <AstrologicalHouseChart :presetData="item.content"/>
                      </template>
                      <!-- 星座血型性格a-16 -->
                      <template v-if="item.submodel === 'a-16'">
                        <ConsteBloodPersonality :presetData="item.content"/>
                      </template>
                    </template>
                  </template>
                </template>
              <div class="chat-list"  v-if="loading && loadingmodel == sxxzType.submodel">  <!-- v-if="loading" -->
                  <div class="answer">
                      <div class="BotHeader">
                        <img class="avatar" :class="screenWidth<=900 ? 'mbImg' : ''" src="/@/assets/images/aibot.png" alt="">
                        <div v-if="screenWidth<=900">天机阁</div>
                      </div>
                      <div class="text-content">
                          <div class="inner">
                              <div v-if="step == 1" class="three-bounce"><div class="one"></div><div class="two"></div><div class="three"></div></div>
                              <!-- <TextComponents ref="TextComponents" @onComplete="onComplete"  v-if="step == 2 && chatType  == 'text'" :text="showText" :obj="resObj"/> -->
                              <div class="htmlText" v-if="step == 2" v-html="htmlText">
                            
                              </div>
                              <span class="cursor" v-if="htmlText != ''"></span>
                          </div>
                      </div>
                  </div>
              </div>
              <!-- <div class="bottom-input">
                  <button class="stop" v-if="loading && step == 2" @click="stop">
                      <img src="/@/assets/images/stop.svg" alt="">
                      {{ $t('stopGenerating') }}
                  </button>
                  <button class="regenerateResponse" v-if="!loading && step == 3" @click="regenerateResponse">
                      <img src="/@/assets/images/repeat.svg" alt="">
                      {{ $t('regenerateResponse') }}
                  </button>
              </div> -->
              <!-- <div class="bottom-input">
                  <button class="item">
                      处女座运势
                  </button>
                  <button class="item">
                      金牛座运势
                  </button>
                  <button class="item">
                      天秤座运势
                  </button>
              </div> -->
            </div>
          </div>
        </template>
       
        <div class="chatmaxbox" v-if="navQueryType.type=='cqsm'" :class="screenWidth<=900? !moduletab_mb ? 'mb' : 'mb_small' : ''">
          <div class="chat" ref="chatContent">
            <!-- v-if="sxxzType.type === 'xzys'" -->
              <!-- 文字对话 -->
              <!-- v-if="item.type  == 'text' || item.role == 'user'" -->
              <div class="chat-list">
                <div  class="answer">
                  <div class="BotHeader">
                    <img class="avatar" :class="screenWidth<=900 ? 'mbImg' : ''" src="/@/assets/images/aibot.png" alt="">
                    <div v-if="screenWidth<=900">天机阁</div>
                  </div>
                
                  <div class="text-content">
                      <div class="inner">
                        <div class="zindex">{{ cqsmType.defaultQue }}</div>
                        <div class="xiangyun"></div>
                      </div>
                  </div>
                </div>
              </div>
              <!-- <div class="chat-list">
                <div  class="answer">
                  <div class="BotHeader">
                    <img class="avatar" :class="screenWidth<=900 ? 'mbImg' : ''" src="/@/assets/images/aibot.png" alt="">
                    <div v-if="screenWidth<=900">天机阁</div>
                  </div>
                
                  <div class="text-content">
                      <div class="inner">
                        <div class="zindex">{{ text }}</div>
                      </div>
                      
                  </div>
                </div>
              </div> -->
  
              <!-- <template v-if="true">
                  <AstrologicalHouseChart />
                </template> -->
                <!-- <template v-if="true">
                  <PlanetInSign />
                </template> -->
              <template v-if="chatList_cqsm.length>0">
                <template v-for="(item,index) in chatList_cqsm" :key="index">
                  <template v-if="(item.showtype  == 'text' || item.role == 'user') && item.submodel == cqsmType.submodel && !item.islike">
                    <div class="chat-list" :class="item.role == 'user' ? 'right-content' : ''">
                      <div class="select" v-if="selectStatus" @click="item.choose =!item.choose">
                          <img v-if="!item.choose" src="/@/assets/images/choose.png" alt="" srcset="">
                          <img v-if="item.choose" src="/@/assets/images/choose2.png" alt="">
                        </div>
                      <div v-if="item.role == 'user'" class="question" @mouseover="onHover(item)" @:mouseleave="onMouseLeave(item)">
                        <div class="text-content">
                          <el-popover
                                v-model:visible="item.sharePopover"
                                placement="bottom"
                                trigger="click"
                                :show-arrow="false"
                                popper-class="share-popover"
                                v-if="item.funshow && !selectStatus"
                            >
                                <template #reference>
                                  <img src="/@/assets/images/more.png" alt="">
                                </template>
                                <template #default>
                                  <div class="list" v-if="item.showtype !='tem'" @click="copyHandle(item)"><img src="/@/assets/images/copy.png" alt="" srcset="">复制</div>
                                  <div  class="list" @click="shareHandle(item)"><img src="/@/assets/images/share.png" alt="" srcset="">分享</div>
                                  <div class="list" @click="deleteHandle(item)"><img src="/@/assets/images/deletechat.png" alt="" srcset="">删除</div>
                                </template>
                            </el-popover>
                            <div class="inner">
                                {{item.content}}
                            </div>
                        </div>
                        <img v-if="screenWidth>900" class="avatar" src="/@/assets/images/user.png" alt="">
                      </div>
                      <div v-if="item.role == 'assistant'" class="answer" @mouseover="onHover(item)" @:mouseleave="onMouseLeave(item)">
                        <div class="BotHeader mb">
                          <div class="left">
                            <img class="avatar" :class="screenWidth<=900 ? 'mbImg' : ''" src="/@/assets/images/aibot.png" alt="">
                            <div v-if="screenWidth<=900">天机阁</div>
                          </div>
                          <el-popover
                            v-model:visible="item.sharePopover"
                            placement="bottom"
                            trigger="click"
                            :show-arrow="false"
                            popper-class="share-popover"
                            v-if="item.funshow && !selectStatus && screenWidth<=900"
                          >
                            <template #reference>
                              <img src="/@/assets/images/more.png" alt="">
                            </template>
                            <template #default>
                              <div class="list" v-if="item.showtype !='tem'" @click="copyHandle(item)"><img src="/@/assets/images/copy.png" alt="" srcset="">复制</div>
                              <div  class="list" @click="shareHandle(item)"><img src="/@/assets/images/share.png" alt="" srcset="">分享</div>
                              <div class="list" @click="deleteHandle(item)"><img src="/@/assets/images/deletechat.png" alt="" srcset="">删除</div>
                            </template>
                          </el-popover>
                        </div>
                        <div class="text-content">
                            <div class="inner">
                              <div class="zindex" v-html="item.content"></div>
                              <div class="xiangyun"></div>
                            </div>
                            <el-popover
                                v-model:visible="item.sharePopover"
                                placement="bottom"
                                trigger="click"
                                :show-arrow="false"
                                popper-class="share-popover"
                                v-if="item.funshow && !selectStatus && screenWidth>900"
                            >
                                <template #reference>
                                  <img src="/@/assets/images/more.png" alt="">
                                </template>
                                <template #default>
                                  <div class="list" v-if="item.showtype !='tem'" @click="copyHandle(item)"><img src="/@/assets/images/copy.png" alt="" srcset="">复制</div>
                                  <div  class="list" @click="shareHandle(item)"><img src="/@/assets/images/share.png" alt="" srcset="">分享</div>
                                  <div class="list" @click="deleteHandle(item)"><img src="/@/assets/images/deletechat.png" alt="" srcset="">删除</div>
                                </template>
                            </el-popover>
                        </div>
                      </div>
                  </div>
                  </template>     
                   <!-- <div class="chat-list right-content">
                        <div class="question">
                          <div class="text-content">
                              <div class="inner">
                                射手座
                              </div>
                          </div>
                          <img class="avatar" src="/@/assets/images/user.svg" alt="">
                        </div> -->
                        <!-- <div  class="answer">
                            <img src="/@/assets/images/logo.svg" alt="">
                            <div class="text-content">
                                <div class="inner">
                                    haha
                                </div>
                            </div>
                        </div> -->
                    <!-- </div> -->
                <!-- v-if="item.type == 'tem' && item.type == 'tem'" -->
                  <template v-if="item.role == 'assistant' && item.showtype == 'tem' && item.submodel == cqsmType.submodel && !item.islike">
                    <chouqiansuanming :presetData="item.content"/>    
                  </template>
                  <div class="chatBotton" v-if="index == chatlist_index && !loading && !selectStatus" :class="screenWidth<=900?'mb_chatBotton' : ''">
                    <div class="share" @click="shareHandle(item)">
                      <img src="/@/assets/images/share_yellow.svg" alt="" srcset="">
                      分享
                    </div>
                    <div class="likediv" v-if="!item.likeType" @click="likeHandle(1,item)">
                      <img src="/@/assets/images/like.svg" alt="" srcset="">
                      喜欢
                    </div>
                    <div class="likediv" v-if="!item.likeType" @click="showdislikeDialog(item)">
                      <img src="/@/assets/images/dislike.svg" alt="" srcset="">
                      不喜欢
                    </div>
                    <div class="chooseIsLike" v-if="item.likeType == 1">
                      <img src="/@/assets/images/like2.svg" alt="" srcset="">
                    </div>
                    <div class="chooseIsLike" v-if="item.likeType == 2 || item.likeType == 3 || item.likeType == 4">
                      <img src="/@/assets/images/dislike2.svg" alt="" srcset="">
                    </div>
                  </div>
                </template>
              </template>
            <div class="chat-list"  v-if="loading && loadingmodel == cqsmType.submodel">  <!-- v-if="loading" -->
                <div class="answer">
                    <div class="BotHeader">
                      <img class="avatar" :class="screenWidth<=900 ? 'mbImg' : ''" src="/@/assets/images/aibot.png" alt="">
                      <div v-if="screenWidth<=900">天机阁</div>
                    </div>
                    <div class="text-content">
                        <div class="inner">
                            <div v-if="step == 1" class="three-bounce"><div class="one"></div><div class="two"></div><div class="three"></div></div>
                            <!-- <TextComponents ref="TextComponents" @onComplete="onComplete"  v-if="step == 2 && chatType  == 'text'" :text="showText" :obj="resObj"/> -->
                            <div class="htmlText" v-if="step == 2" v-html="htmlText">
                            
                            </div>
                            <span class="cursor" v-if="htmlText != ''"></span>
                            <!-- v-if="htmlText != ''" -->
                        </div>
                    </div>
                </div>
            </div>
            <!-- <div class="bottom-input">
                <button class="stop" v-if="loading && step == 2" @click="stop">
                    <img src="/@/assets/images/stop.svg" alt="">
                    {{ $t('stopGenerating') }}
                </button>
                <button class="regenerateResponse" v-if="!loading && step == 3" @click="regenerateResponse">
                    <img src="/@/assets/images/repeat.svg" alt="">
                    {{ $t('regenerateResponse') }}
                </button>
            </div> -->
            <!-- <div class="bottom-input">
                <button class="item">
                    处女座运势
                </button>
                <button class="item">
                    金牛座运势
                </button>
                <button class="item">
                    天秤座运势
                </button>
            </div> -->
          </div>
        </div>
        <div class="chatmaxbox-other" v-if="navQueryType.type=='scbz' || 
          navQueryType.type=='sxxz' || 
          navQueryType.type =='zybg'||
          navQueryType.type == 'tlp' ||
          navQueryType.type=='qmcm' || 
          navQueryType.type=='hypd' || 
          navQueryType.type == 'gsqm' || 
          navQueryType.type == 'zgjm' ||
          navQueryType.type == 'fsbj' || 
          navQueryType.type == 'hdnj' ||
          navQueryType.type == 'hljr' ||
          navQueryType.type == 'hmxj'">
          <div class="chat" ref="chatContent">
            <!-- v-if="sxxzType.type === 'xzys'" -->
              <!-- 文字对话 -->
              <!-- v-if="item.type  == 'text' || item.role == 'user'" -->
              <div class="chat-list">
                <div  class="answer">
                  <div class="BotHeader">
                    <img class="avatar"  :class="screenWidth<=900 ? 'mbImg' : ''" src="/@/assets/images/aibot.png" alt="">
                    <div v-if="screenWidth<=900">天机阁</div>
                  </div>
                  <div class="text-content">
                      <div class="inner">
                        <div class="zindex"> {{ navQueryType.defQuestion }} </div>
                        <div class="xiangyun"></div>
                      </div>
                  </div>
                </div>
              </div>
              <template v-if="chatList_scbz.length>0">
                <template v-for="(item,index) in chatList_scbz" :key="index">
                  <template v-if="(item.showtype  == 'text' || item.role == 'user') && item.submodel == navQueryType.module && !item.islike">
                    <div class="chat-list" :class="item.role == 'user' ? 'right-content' : ''">
                      <div class="select" v-if="selectStatus" @click="item.choose =!item.choose">
                          <img v-if="!item.choose" src="/@/assets/images/choose.png" alt="" srcset="">
                          <img v-if="item.choose" src="/@/assets/images/choose2.png" alt="">
                        </div>
                      <div v-if="item.role == 'user'" class="question" @mouseover="onHover(item)" @:mouseleave="onMouseLeave(item)">
                       
                        <div class="text-content">
                          <el-popover
                                v-model:visible="item.sharePopover"
                                placement="bottom"
                                trigger="click"
                                :show-arrow="false"
                                popper-class="share-popover"
                                v-if="item.funshow && !selectStatus"
                            >
                                <template #reference>
                                  <img src="/@/assets/images/more.png" alt="">
                                </template>
                                <template #default>
                                  <div class="list" v-if="item.showtype !='tem'" @click="copyHandle(item)"><img src="/@/assets/images/copy.png" alt="" srcset="">复制</div>
                                  <div  class="list" @click="shareHandle(item)"><img src="/@/assets/images/share.png" alt="" srcset="">分享</div>
                                  <div class="list" @click="deleteHandle(item)"><img src="/@/assets/images/deletechat.png" alt="" srcset="">删除</div>
                                </template>
                            </el-popover>
                          
                            <div class="inner">
                              {{ item.content }}
                            </div>
                            
                        </div>
                        <img v-if="screenWidth>900" class="avatar" src="/@/assets/images/user.png" alt="">
                      </div>
                      <div v-if="item.role == 'assistant'" class="answer" @mouseover="onHover(item)" @:mouseleave="onMouseLeave(item)">
                        <div class="BotHeader mb">
                          <div class="left">
                            <img class="avatar" :class="screenWidth<=900 ? 'mbImg' : ''" src="/@/assets/images/aibot.png" alt="">
                            <div v-if="screenWidth<=900">天机阁</div>
                          </div>
                          <el-popover
                            v-model:visible="item.sharePopover"
                            placement="bottom"
                            trigger="click"
                            :show-arrow="false"
                            popper-class="share-popover"
                            v-if="item.funshow && !selectStatus && screenWidth<=900"
                          >
                            <template #reference>
                              <img src="/@/assets/images/more.png" alt="">
                            </template>
                            <template #default>
                              <div class="list" v-if="item.showtype !='tem'" @click="copyHandle(item)"><img src="/@/assets/images/copy.png" alt="" srcset="">复制</div>
                              <div  class="list" @click="shareHandle(item)"><img src="/@/assets/images/share.png" alt="" srcset="">分享</div>
                              <div class="list" @click="deleteHandle(item)"><img src="/@/assets/images/deletechat.png" alt="" srcset="">删除</div>
                            </template>
                          </el-popover>
                        </div>
                        <div class="text-content">
                            <div class="inner">
                              <div class="zindex" v-html="item.content"></div>
                              <div class="xiangyun"></div>
                            </div>
                            <el-popover
                                v-model:visible="item.sharePopover"
                                placement="bottom"
                                trigger="click"
                                :show-arrow="false"
                                popper-class="share-popover"
                                v-if="item.funshow && !selectStatus  && screenWidth>900"
                            >
                                <template #reference>
                                  <img src="/@/assets/images/more.png" alt="">
                                </template>
                                <template #default>
                                  <div class="list" v-if="item.showtype !='tem'" @click="copyHandle(item)"><img src="/@/assets/images/copy.png" alt="" srcset="">复制</div>
                                  <div  class="list" @click="shareHandle(item)"><img src="/@/assets/images/share.png" alt="" srcset="">分享</div>
                                  <div class="list" @click="deleteHandle(item)"><img src="/@/assets/images/deletechat.png" alt="" srcset="">删除</div>
                                </template>
                            </el-popover>
                          
                        </div>
                      </div>
                     
                  </div>
                  </template>
                  <div class="chatBotton" v-if="index == chatlist_index && !loading && !selectStatus" :class="screenWidth<=900?'mb_chatBotton' : ''">
                    <div class="share" @click="shareHandle(item)">
                      <img src="/@/assets/images/share_yellow.svg" alt="" srcset="">
                      分享
                    </div>
                    <div class="likediv" v-if="!item.likeType" @click="likeHandle(1,item)">
                      <img src="/@/assets/images/like.svg" alt="" srcset="">
                      喜欢
                    </div>
                    <div class="likediv" v-if="!item.likeType" @click="showdislikeDialog(item)">
                      <img src="/@/assets/images/dislike.svg" alt="" srcset="">
                      不喜欢
                    </div>
                    <div class="chooseIsLike" v-if="item.likeType == 1">
                      <img src="/@/assets/images/like2.svg" alt="" srcset="">
                    </div>
                    <div class="chooseIsLike" v-if="item.likeType == 2 || item.likeType == 3 || item.likeType == 4">
                      <img src="/@/assets/images/dislike2.svg" alt="" srcset="">
                    </div>
                  </div>
                </template>
              </template>
            <div class="chat-list"  v-if="loading && loadingmodel == navQueryType.module">  <!-- v-if="loading" -->
                <div class="answer">
                    <div class="BotHeader">
                      <img class="avatar" :class="screenWidth<=900 ? 'mbImg' : ''" src="/@/assets/images/aibot.png" alt="">
                      <div v-if="screenWidth<=900">天机阁</div>
                    </div>
                    <div class="text-content">
                        <div class="inner">
                            <div v-if="step == 1" class="three-bounce"><div class="one"></div><div class="two"></div><div class="three"></div></div>
                            <!-- <TextComponents ref="TextComponents" @onComplete="onComplete"  v-if="step == '2' && chatType  == 'text'" :text="showText" :obj="resObj"/> -->
                            <div class="htmlText" v-if="step == 2" v-html="htmlText"></div>
                            <span class="cursor" v-if="htmlText != ''"></span>
                            <!-- {{ text }} -->
                        </div>
                    </div>
                </div>
            </div>
          </div>
        </div>
      
    
      <div class="bottom-input">
        <!-- v-if="loading && step == 2" -->
          <button class="stop" v-if="loading && step == 2"  @click="stopText">
              <img src="/@/assets/images/stop.svg" alt="">
              {{ $t('stopGenerating') }}
          </button>
          <button class="regenerateResponse" v-if="(!loading && !likeLoading)&& step == 3" @click="regenerateResponse">
              <img src="/@/assets/images/repeat.svg" alt="">
              {{ $t('regenerateResponse') }}
          </button>
      </div>
  </div>
  <DisLikeReason
    :disLikeDialog="disLikeDialog"
    :likeItemObj="likeItemObj"
    @closeDisLike="closeDisLike"
    ref="disLike"
  />
</template>

<script>
import TextComponents from '/@/components/ChatComponent/TextComponents.vue'
import DisLikeReason from '/@/components/ChatComponent/DisLikeReason.vue'
import Horoscope from '/@/components/Horoscope.vue'
import ConstellationRankingList from '/@/components/ConstellationRankingList.vue'
import ConstellationRankingItem from '/@/components/common/ConstellationRankingItem.vue'
import ZodiacQuery from '/@/components/ZodiacQuery.vue'
import ConstellationInquir from '/@/components/ConstellationInquir.vue'
import BirthdatePassword from '/@/components/BirthdatePassword.vue'
import ChineseZodiacFortune from '/@/components/ChineseZodiacFortune.vue'
import DescendingZodiac from '/@/components/DescendingZodiac.vue'
import BirthdayFlower from '/@/components/BirthdayFlower.vue'
import BirthdayBook from '/@/components/BirthdayBook.vue'
import ConsteBloodPersonality from '/@/components/ConsteBloodPersonality.vue'
import Ascendant from '/@/components/Ascendant.vue'
import MoonSign from '/@/components/MoonSign.vue'
import Constellations48 from '/@/components/Constellations48.vue'
import CheatingPerson from '/@/components/CheatingPerson.vue'
import AstrologicalChart from '/@/components/AstrologicalChart.vue'
import AstrologicalHouseChart from '/@/components/AstrologicalHouseChart.vue'
import PlanetInHouse from '/@/components/PlanetInHouse.vue'
import PlanetInSign from '/@/components/PlanetInSign.vue'

import { SuccessFilled } from '@element-plus/icons-vue'
import { ref, computed, watch, markRaw } from 'vue';
import { useStore} from 'vuex'
import { GPTChat, xingzuoYunshi, shengxiaoYunshi, shengxiaoQuery, xingzuoChaxun, xingzuoShengrishu,
   xingzuoShengrimima, xingzuoShengrihua, xingzuoRankingList, xingzuoRankingGet, xingzuoRankingQuestion,
  xingzuoChugui, xingzuoXuexing, queryConstellations48, xingzuoXiajiang, xingzuoYueliang, setUserSharechat, usermsgDelete} from  '/@/api/api.js'
import EventBus from '/@/utils/EventBus.js'
import objKeySort from '/@/utils/hexmd5.js'
import useClipboard from 'vue-clipboard3'
import { MD5 } from 'crypto-js';
// import  from 'js-md5';
import { marked } from 'marked'
const url_pro = 'https://starloom.mpcbot.ai/chat';
const url_test = 'https://testastroai.mpcbot.ai/chat';

export default {
  name: '',
  setup() {
    const chatList = ref([])
    const chatList_cqsm = ref([])
    const chatList_scbz = ref([])
    const loading = ref(false) //加载状态
    const loadingmodel = ref('') //加载显示的模块
    const chatType = ref('') // 接口返回的 对话类型
    const step =  ref('1') //加载过程中的状态， 1 代表正在跟后台请求中， 2 代表 正在显示文字中 3 代表文字显示完毕或者用户中断回答
    const showText = ref('') // 回答的文本
    const resObj = ref(null)  //接口返回数据 模版类型，子模版位置等
    const chatContent = ref(null)
    const rankPage = ref(1)
    const modelChatList = ref([])
    const sxxzType = ref({type:'xzys', submodel:'a-5', name:'星座运势', defaultQue:'您好，请输入您的星座，获取您的星座运势。例如：狮子座。'})
    const cqsmType = ref({type:'gylq', submodel:'k-1', name:'观音灵签', defaultQue:'亲爱的众生，欢迎来到观音灵签的神圣空间。在此，我们先与救苦救难的观音菩萨建立心灵的连接。请您合十，默念三遍[救苦救难观音菩萨]，然后默念您的姓名、出生时辰、年龄与地址。请心中默念您的请求，无论是关于婚姻、事业还是财运。当您准备好后，请告诉我开始抽签，我们将一同寻找观音菩萨为您指点的答案。'})
    const time = ref(new Date().getTime() + localStorage.getItem('userId'))
    const store = useStore()
    const text = ref('')
    const htmlText = ref('') // 回答的文本
    const disLikeDialog = ref(false)   // 不喜欢弹窗是否展示
    const selectStatus = computed(() => store.state.selectStatus)
    const selectType = computed(() => store.state.selectType)
    const apiurl = computed(() => store.state.apiurl)
    const userModel = computed(() => store.state.userModel)
    // const likeType = ref('')   // 是否喜欢类型  1喜欢 2不准确 3无益 4攻击性
    const sharelink = computed(() => store.state.sharelink)//分享链接 
    const haveCount =computed( () => store.state.haveCount) // 是否有条数
    const list_current = ref('')
    const likeItemObj = ref('')
    const likeLoading = ref(false)

    const chatlist_index = computed(() => {   //当前模块list
      if(navQueryType.value.type=='cqsm'){
        list_current.value = chatList_cqsm.value.filter(item =>item.submodel == cqsmType.value.submodel && item.role == 'assistant' && !item.islike  )
        const leng = list_current.value.length-1
        for(var i=0;i<chatList_cqsm.value.length;i++){
          if(chatList_cqsm.value[i]== list_current.value[leng]){
              return i
          }
        } 
      }else{
        list_current.value = chatList_scbz.value.filter(item =>item.submodel == navQueryType.value.module && item.role == 'assistant' && !item.islike)
        const leng = list_current.value.length-1
        for(var i=0;i<chatList_scbz.value.length;i++){
          if(chatList_scbz.value[i]== list_current.value[leng]){
              return i
          }
        } 
      }
    })
    let eventSource
    // 登录状态
    const loginStatus = computed( () => {
      return store.state.loginStatus
    }) 
    //适配
    const screenWidth = computed( () => {
      return store.state.screenWidth
    })
    const scrollToBottom = ()=> { // 保持滚动条在最底部
        var element = chatContent.value
        element.scrollTop = element.scrollHeight
    }
    const moduletab_mb = ref(false)
    const navQueryType = computed(() => store.state.navQueryType)
    //监听导航tab模块
    watch(() => navQueryType.value,(val,old) => {
      if(old){
          if(loading.value){
            loading.value = false
            eventSource.close()
            const chat = {
                role: 'assistant',
                copyText: text.value,
                content: marked(text.value),
                showtype: 'text',
                submodel: resObj.value.modelType,  //a-1
                msggroup:time.value,
                msgId: resObj.value.msgIds[1],
                islike: false,
              }
              text.value = ''
              htmlText.value = ''
            // if(old.type=='sxxz'){
            //   chatList.value.push(chat)
            // }else
             if (old.type == 'cqsm'){
              chatList_cqsm.value.push(chat)
            }else{
              chatList_scbz.value.push(chat)
            }
          }
        }
        // if(old){
        //   if(loading.value){
        //     loading.value = false
        //     eventSource.close()
        //     const chat = {
        //         role: 'assistant',
        //         copyText: text.value,
        //         content: marked(text.value),
        //         showtype: 'text',
        //         submodel: resObj.value.modelType,  //a-1
        //         msggroup:time.value,
        //       }
        //       text.value = ''
        //     if(old.type=='sxxz'){
        //       chatList.value.push(chat)
        //     }else if(old.type == 'cqsm'){
        //       chatList_cqsm.value.push(chat)
        //     }else{
        //       chatList_scbz.value.push(chat)
        //     }
        //   }
        // }
        if(val){
          const list = chatList_scbz.value.filter(item => item.submodel == val.module && item.msggroup)
          if(list.length>0){
            time.value = list[0].msggroup
            step.value = 3
          }else{
            time.value = new Date().getTime() + localStorage.getItem('userId') 
            step.value = 1
          }
        }
    })
    const sendMessage = async (questionText, tabIndex, index) => {
        console.log('问题内容：：：', questionText)
        if(loading.value || questionText == ''){
                return
        } 
          //  || navQueryType.value.type == 'sxxz'
        if(navQueryType.value.type == 'cqsm'){
          if(!tabIndex && tabIndex !=0 ){
            const chat = {
              role: 'user',
              content:questionText,
              copyText:questionText,
              showtype:'text',
              submodel: navQueryType.value.type == 'sxxz'?sxxzType.value.submodel:cqsmType.value.submodel,
              msggroup: time.value,
              islike: false,
            }
            chatList.value.push(chat)
            chatList_cqsm.value.push(chat)
            loading.value = true
            // likeType.value = ""
            loadingmodel.value = navQueryType.value.type == 'sxxz'?sxxzType.value.submodel:cqsmType.value.submodel
            step.value = 1
          }
          setTimeout(() => {
              scrollToBottom() 
              store.commit('setQuestion', '')
          },50)
          let userQueList = []
          const model1 = navQueryType.value.type == 'sxxz'?sxxzType.value.submodel:cqsmType.value.submodel
          const chat1 = navQueryType.value.type == 'sxxz'?chatList:chatList_cqsm
          chat1.value.forEach(item =>  {
            if(item.submodel == model1){
                userQueList.push({ 
                  "type": item.role == 'user'? 'user' : item.showtype,
                  "content": item.content
                })
            }
          })
          const requestData =  {
                "module":navQueryType.value.type == 'sxxz'?'a':'k',
                "sub_module":navQueryType.value.type == 'sxxz'?sxxzType.value.submodel:cqsmType.value.submodel,
                "messages":userQueList,
                "msggroup": time.value,
                "gpt_mode": userModel.value == '3.5'? 1 : 2,
                islike:false,
              }
          try{

            eventSource = new SSE(apiurl.value, {
              headers: {
                'Content-Type': 'application/json', 
                'Authorization': localStorage.getItem('starloomAI-token'),
              },
              payload: JSON.stringify(requestData),
              method: "POST"
            });
            console.info(eventSource)
            eventSource.onopen = () => {
                console.log('open')
            }
            let n = 0
            let chat
            eventSource.onmessage = function(event) {
              // 第一次返回： text|tem
            // 如果 是tem ，第二次返回整个json字符串；如果是text，第二次，到第N次按照流输出一个字一个字的，遇到[DONE]结束
              console.log('1111,',event.data)
              if(n==2) return
              if(n==0){
              const obj = JSON.parse(event.data)
                chat = {
                  role: 'assistant',
                  // content:result.data.data,
                  showtype: obj.type,
                  submodel: obj.modelType,  //a-1
                  msggroup:time.value,
                  msgId: obj.msgIds[1],
                  islike:false,
                }
                resObj.value = JSON.parse(event.data)
                const lengthnum = chatList_cqsm.value.length
                chatList_cqsm.value[lengthnum-1].msgId =  obj.msgIds[0]
                n = 1
              }else {
                if(chat.showtype == 'tem'){
                  eventSource.close()
                  if(sxxzType.value.submodel == 'a-7'){
                    if(event.data.totalCount){
                      chat.questionType = 1
                      event.data.data.noTab = true
                    } else {
                      chat.questionType = 2
                    }
                  }
                  chat.content = JSON.parse(event.data) 
                  chat.copyText = JSON.parse(event.data)
                  loading.value = false
                  loadingmodel.value = ''
                  chatList.value.push(chat)
                  chatList_cqsm.value.push(chat)
                  console.log('对话list：：：', chatList.value)
                } else if (chat.showtype == 'text'){
                  if (event.data === '[DONE]') {
                    console.info('结束')
                    loading.value = false
                    chat.content = marked(text.value)
                    chat.copyText = text.value
                    htmlText.value = marked(text.value);
                    chatList.value.push(chat)
                    chatList_cqsm.value.push(chat)
                    text.value = ''
                    htmlText.value = ''
                    step.value = 3
                    n=2
                    eventSource.close()
                  } else {
                      step.value = 2
                      console.log('event.data,,,',event.data)
                      // if (event.data.indexOf('<br><br>') != -1) {
                      //     event.data = event.data.replace('<br><br>', '\n\n')
                      // }
                      // if(event.data.indexOf('<br>') != -1){
                      //   event.data = event.data.replace('<br>','\n')
                      // }
                     
                      text.value += event.data
                      htmlText.value = marked(text.value);
                      console.log('text.value,,,',text.value)
                      setTimeout(() => {
                          scrollToBottom() 
                          store.commit('setQuestion', '')
                      },50)
                  }
                }
              }
            };
            eventSource.onerror = (error) => {
                console.error('EventSource failed:', error)
                loading.value = false
                loadingmodel.value = ''
                step.value = 3
                eventSource.close()
            };
            eventSource.stream();
              // const result = await GPTChat({
              //   "module":"a",
              //   "sub_module":sxxzType.value.submodel,
              //   "messages":userQueList,
              //   "msggroup": time.value,
              // })
              // if(result.code == 200){
              //     const chat = {
              //         role: 'assistant',
              //         content:result.data.data,
              //         showtype:result.data.type,
              //         submodel: result.data.modelType,  //a-1
              //         msggroup: time.value,
              //     }
              //     if(sxxzType.value.submodel == 'a-7'){
              //       if(result.data.data.totalCount){
              //         chat.questionType = 1
              //         result.data.data.noTab = true
              //       } else {
              //         chat.questionType = 2
              //       }
              //     }
              //     if(result.data.type == 'text'){
              //       showText.value = result.data.data
              //       resObj.value = result.data
              //       resObj.value.msggroup = time.value
              //       step.value = 2
              //       chatType.value = 'text'
              //     }else{
              //       loading.value = false
              //       loadingmodel.value = ''
              //       chatList.value.push(chat)
              //     }
              // }else{
              //   loading.value = false
              //   loadingmodel.value = ''
              //   step.value = 3
              // }
          }catch(error){
            console.log('error',error)
          }
        } else if(navQueryType.value.type == 'scbz' ||
          navQueryType.value.type=='sxxz' || 
          navQueryType.value.type == 'tlp' || 
          navQueryType.value.type == 'qmcm' ||
          navQueryType.value.type == 'zybg' ||
          navQueryType.value.type == 'hypd' ||
          navQueryType.value.type == 'gsqm' ||
          navQueryType.value.type == 'zgjm' ||
          navQueryType.value.type == 'fsbj' ||
          navQueryType.value.type == 'hdnj' ||
          navQueryType.value.type == 'hljr' ||
          navQueryType.value.type == 'hmxj'
        ) {
            const chat = {
              role: 'user',
              content:questionText,
              copyText: questionText,
              showtype:'text',
              submodel: navQueryType.value.module,
              msggroup: time.value,
              islike: false,
            }
            chatList_scbz.value.push(chat)
            loading.value = true
            // likeType.value = ""
            loadingmodel.value = navQueryType.value.module
            step.value = 1
            setTimeout(() => {
                scrollToBottom() 
                store.commit('setQuestion', '')
            },50)
            let userQueList = []
            chatList_scbz.value.forEach(item =>  {
              if(item.submodel == navQueryType.value.module){
                userQueList.push({ 
                  "type": item.role == 'user'? 'user' : item.showtype,
                  "content": item.content
                })
              }
            })
            const requestData =  {
                "module":navQueryType.value.module,
               // "sub_module":sxxzType.value.submodel,
                "messages":userQueList,
                "msggroup": time.value,
                "gpt_mode": userModel.value == '3.5'? 1 : 2,
                islike: false,
              }
              if( navQueryType.value.type == 'sxxz'){
                requestData.sub_module = 'a-1'
              }
          try{
            eventSource = new SSE(apiurl.value, {
              headers: {
                'Content-Type': 'application/json', 
                'Authorization': localStorage.getItem('starloomAI-token'),
              },
              payload: JSON.stringify(requestData),
              method: "POST"
            });
            console.info(eventSource)
            eventSource.onopen = () => {
                console.log('open')
            }
            let n = 0
            let chat
            eventSource.onmessage = function(event) {
              // 第一次返回： text|tem
            // 如果 是tem ，第二次返回整个json字符串；如果是text，第二次，到第N次按照流输出一个字一个字的，遇到[DONE]结束
              console.log('1111,',event.data)
              if(n==2) return
              if(n==0){
                const obj = JSON.parse(event.data)
                chat = {
                  role: 'assistant',
                  // content:result.data.data,
                  showtype: obj.type,
                  submodel: obj.modelType,  //a-1
                  msggroup:time.value,
                  msgId: obj.msgIds[1],
                  islike: obj.islike,
                }
                resObj.value = JSON.parse(event.data)
                const lengthnum = chatList_scbz.value.length
                chatList_scbz.value[lengthnum-1].msgId =  obj.msgIds[0]
                n = 1
              }else {
                if(chat.showtype == 'tem'){
                  eventSource.close()
                  if(sxxzType.value.submodel == 'a-7'){
                    if(event.data.totalCount){
                      chat.questionType = 1
                      event.data.data.noTab = true
                    } else {
                      chat.questionType = 2
                    }
                  }
                  chat.content = JSON.parse(event.data)
                  chat.copyText = JSON.parse(event.data)
                  loading.value = false
                  loadingmodel.value = ''
                  chatList_scbz.value.push(chat)
                  console.log('对话list：：：', chatList_scbz.value)
                } else if (chat.showtype == 'text'){
                  if (event.data === '[DONE]') {
                    console.info('结束')
                    loading.value = false
                    chat.copyText = text.value
                    chat.content = marked(text.value)
                    chatList_scbz.value.push(chat)
                    text.value = ''
                    htmlText.value = ''
                    step.value = 3
                    n=2
                    eventSource.close()
                  } else {
                      step.value = 2
                      console.log('event.data,,,',event.data)
                      // if (event.data.indexOf('<br><br>') != -1) {
                      //     event.data = event.data.replace('<br><br>', '\n\n')
                      // }
                      // if(event.data.indexOf('<br>') != -1){
                      //   event.data = event.data.replace('<br>','\n')
                      // }
                      text.value += event.data
                      htmlText.value = marked(text.value);
                      console.log('text.value,,,',text.value)
                      setTimeout(() => {
                          scrollToBottom() 
                          store.commit('setQuestion', '')
                      },50)
                  }
                }
              }
              
            };
            eventSource.onerror = (error) => {
                console.error('EventSource failed:', error)
                loading.value = false
                loadingmodel.value = ''
                step.value = 3
                eventSource.close()
            };
            eventSource.stream();
              // const result = await GPTChat({
              //   "module":navQueryType.value.module,
              //   // "sub_module":sxxzType.value.submodel,
              //   "messages":userQueList,
              //   "msggroup": time.value,
              // })
              // if(result.code == 200){
              //     const chat = {
              //         role: 'assistant',
              //         content:result.data.data,
              //         showtype:result.data.type,
              //         submodel: result.data.modelType,  //a-1
              //         msggroup: time.value,
              //     }
              //     if(sxxzType.value.submodel == 'a-7'){
              //       chat.questionType = 1
              //     }
              //     if(result.data.type == 'text'){
              //       showText.value = result.data.data
              //       resObj.value = result.data
              //       step.value = 2
              //       chatType.value = 'text'
              //     }else{
              //       loading.value = false
              //       loadingmodel.value = ''
              //       chatList_scbz.value.push(chat)
              //     }
              // }else{
              //   loading.value = false
              //   loadingmodel.value = ''
              //   step.value = 3
              // }
          }catch(error){

          }
        }
    }

    const stopText = () =>{
      eventSource.close()
     const chat = {
        role: 'assistant',
        copyText: text.value,
        content: marked(text.value),
        showtype: 'text',
        submodel: resObj.value.modelType,  //a-1
        msggroup:time.value,
        msgId: resObj.value.msgIds[1], 
        islike: false,
      }
      // if(navQueryType.value.type == 'sxxz'){
      //   chatList.value.push(chat)
      // }else 
      if(navQueryType.value.type == 'cqsm'){
        chatList_cqsm.value.push(chat)
      }else{
        chatList_scbz.value.push(chat)
      }
      text.value = ""
      htmlText.value = ''
      step.value = 3
      loading.value = false
    }

    const getMessageTem = async (questionText, tabIndex, index) => {
      // 监听对话的回调 目前分为预设1,2,3 以及文本对话
      console.log('问题内容：：：', questionText)
      if(loading.value || questionText == ''){
              return
      }
      if(!tabIndex && tabIndex !=0){
        const chat = {
          role: 'user',
          content: questionText,
          copyText: questionText,
          showtype:'text',
          submodel: navQueryType.value.type == 'sxxz'?sxxzType.value.submodel:cqsmType.value.submodel,
          islike: false,
        }
        chatList.value.push(chat)
        chatList_cqsm.value.push(chat)
        loading.value = true
        loadingmodel.value = navQueryType.value.type == 'sxxz'?sxxzType.value.submodel:cqsmType.value.submodel
        step.value = 1
      }
      setTimeout(() => {
          // scrollToBottom() 
          store.commit('setQuestion', '')
      },50)
      if(navQueryType.value.type == 'sxxz'||navQueryType.value.type=='cqsm'){
        if(sxxzType.value.submodel == 'a-1'){
              console.log('shengxiaoQuery')
              try{
                  const result = await shengxiaoQuery({
                    query: questionText
                  })
                  if(result.code == 200){
                      const chat = {
                          role: 'assistant',
                          content:result.data.data,
                          copyText: result.data.data,
                          showtype:result.data.type,
                          submodel: result.data.modelType,  //a-1
                          islike: false,
                      }
                      if(result.data.type == 'text'){
                        showText.value = result.data.data
                        resObj.value = result.data
                        step.value = 2
                        chatType.value = 'text'
                      }else{
                        loading.value = false
                        chatList.value.push(chat)
                        console.log('对话list：：：', chatList.value)
                      }
                  }else{
                    loading.value = false
                    step.value = 3
                  }
              }catch(error){

              }
          } else if(sxxzType.value.submodel == 'a-2'){
            console.log('shengxiaoYunshi')
            try{
                const result = await shengxiaoYunshi({
                  query: questionText,
                })
                if(result.code == 200){
                    const chat = {
                        role: 'assistant',
                        content: result.data.data,
                        copyText: result.data.data,
                        showtype: result.data.type,
                        submodel: result.data.modelType,
                        islike: false,
                    }
                    if(result.data.type == 'text'){
                      showText.value = result.data.data
                      resObj.value = result.data
                      step.value = 2
                      chatType.value = 'text'
                    }else{
                      chatList.value.push(chat)
                      loading.value = false
                      console.log('对话list：：：', chatList.value)
                    }            
                    // chatList.value.push(chat)
                }else{
                  loading.value = false
                  step.value = 3
                }
            }catch(error){

            }
          } else if(sxxzType.value.submodel == 'a-4'){
            console.log('xingzuoXiajiang')
            try{
                const result = await xingzuoXiajiang({
                  query: questionText,
                })
                if(result.code == 200){
                    const chat = {
                        role: 'assistant',
                        content: result.data.data,
                        copyText: result.data.data,
                        showtype: result.data.type,
                        submodel: result.data.modelType,
                        islike: false,
                    }
                    if(result.data.type == 'text'){
                      showText.value = result.data.data
                      resObj.value = result.data
                      step.value = 2
                      chatType.value = 'text'
                    }else{
                      chatList.value.push(chat)
                      loading.value = false
                      console.log('对话list：：：', chatList.value)
                    }            
                    // chatList.value.push(chat)
                }else{
                  loading.value = false
                  step.value = 3
                }
            }catch(error){

            }
          } else if(sxxzType.value.submodel == 'a-5'){
            console.log('xingzuoyunshi')
            try{
                const result = await xingzuoYunshi({
                  query: questionText,
                  index: tabIndex ? tabIndex : 0,
                })
                if(result.code == 200){
                    const chat = {
                        role: 'assistant',
                        content: result.data.data,
                        copyText: result.data.data,
                        showtype: result.data.type,
                        submodel: result.data.modelType,
                        islike: false,
                    }
                    if(result.data.type == 'text'){
                      showText.value = result.data.data
                      resObj.value = result.data
                      step.value = 2
                      chatType.value = 'text'
                    }else{
                      if(tabIndex || tabIndex==0){
                        chatList.value[index] = chat
                      } else{
                        chatList.value.push(chat)
                      }
                      loading.value = false
                      loadingmodel.value = ''
                      console.log('对话list：：：', chatList.value)
                    }
                    // chatList.value.push(chat)
                }else{
                  loading.value = false
                  loadingmodel.value = ''
                  step.value = 3
                }
            }catch(error){

            }
          } else if(sxxzType.value.submodel == 'a-6'){
              console.log('xingzuoChaxun')
              try{
                  const result = await xingzuoChaxun({
                    query: questionText
                  })
                  if(result.code == 200){
                      const chat = {
                          role: 'assistant',
                          content:result.data.data,
                          copyText: result.data.data,
                          showtype:result.data.type,
                          submodel: result.data.modelType,  //a-1
                          islike: false,
                      }
                      if(result.data.type == 'text'){
                        showText.value = result.data.data
                        resObj.value = result.data
                        step.value = 2
                        chatType.value = 'text'
                      }else{
                        chatList.value.push(chat)
                        loading.value = false
                        console.log('对话list：：：', chatList.value)
                      }
                  }else{
                    loading.value = false
                    step.value = 3
                  }
              }catch(error){

              }
          } else if(sxxzType.value.submodel == 'a-7'){
              console.log('xingzuoRankingQuestion')
              try{
                  const result = await xingzuoRankingQuestion({
                    query: questionText
                  })
                  if(result.code == 200){
                      const chat = {
                          role: 'assistant',
                          content:result.data.data,
                          copyText: result.data.data,
                          showtype:result.data.type,
                          submodel: result.data.modelType,
                          islike: false,
                          questionType: 2,
                      }
                      if(result.data.type == 'text'){
                        showText.value = result.data.data
                        resObj.value = result.data
                        step.value = 2
                        chatType.value = 'text'
                      }else{
                        chatList.value.push(chat)
                        loading.value = false
                        console.log('对话list：：：', chatList.value)
                      }
                  }else{
                    loading.value = false
                    step.value = 3
                  }
              }catch(error){

              }
          } else if(sxxzType.value.submodel == 'a-8'){
              console.log('xingzuoShengrihua')
              try{
                  const result = await xingzuoShengrihua({
                    query: questionText
                  })
                  if(result.code == 200){
                      const chat = {
                          role: 'assistant',
                          content:result.data.data,
                          copyText: result.data.data,
                          showtype:result.data.type,
                          submodel: result.data.modelType,
                          islike: false,
                      }
                      if(result.data.type == 'text'){
                        showText.value = result.data.data
                        resObj.value = result.data
                        step.value = 2
                        chatType.value = 'text'
                      }else{
                        chatList.value.push(chat)
                        loading.value = false
                        console.log('对话list：：：', chatList.value)
                      }
                  }else{
                    loading.value = false
                    step.value = 3
                  }
              }catch(error){

              }
          } else if(sxxzType.value.submodel == 'a-9'){
              console.log('xingzuoYueliang')
              try{
                  const result = await xingzuoYueliang({
                    query: questionText
                  })
                  if(result.code == 200){
                      const chat = {
                          role: 'assistant',
                          content:result.data.data,
                          copyText: result.data.data,
                          showtype:result.data.type,
                          submodel: result.data.modelType,
                          islike: false,
                      }
                      if(result.data.type == 'text'){
                        showText.value = result.data.data
                        resObj.value = result.data
                        step.value = 2
                        chatType.value = 'text'
                      }else{
                        chatList.value.push(chat)
                        loading.value = false
                        console.log('对话list：：：', chatList.value)
                      }
                  }else{
                    loading.value = false
                    step.value = 3
                  }
              }catch(error){

              }
              chatList.value.push(chat)
              loading.value = true
              loadingmodel.value = navQueryType.value.type == "sxxz"?sxxzType.value.submodel:cqsmType.value.submodel
              step.value = 1
            }
            setTimeout(() => {
                scrollToBottom() 
                store.commit('setQuestion', '')
            },50)
            let userQueList = []
            const submodel1=navQueryType.value.type == "sxxz"?sxxzType.value.submodel:cqsmType.value.submodel
            const chat2 = navQueryType.value.type == "sxxz"?chatList:chatList_cqsm
            chat2.value.forEach(item =>  {
              if(item.submodel == submodel1){
                  userQueList.push({ 
                    "type": item.role == 'user'? 'user' : item.showtype,
                    "content": item.content
                  })
              }
            })
            const requestData =  {
                  "module":navQueryType.value.type == "sxxz" ? "a" : "k",
                  "sub_module":navQueryType.value.type == "sxxz"?sxxzType.value.submodel:cqsmType.value.submodel,
                  "messages":userQueList,
                  "msggroup": time.value,
                  "gpt_mode": userModel.value == '3.5'? 1 : 2,
                  islike: false,
                }
            try{
  
              eventSource = new SSE(apiurl.value, {
                headers: {
                  'Content-Type': 'application/json', 
                  'Authorization': localStorage.getItem('starloomAI-token'),
                },
                payload: JSON.stringify(requestData),
                method: "POST"
              });
              console.info(eventSource)
              eventSource.onopen = () => {
                  console.log('open')
              }
              let n = 0
              let chat
              eventSource.onmessage = function(event) {
                // 第一次返回： text|tem
              // 如果 是tem ，第二次返回整个json字符串；如果是text，第二次，到第N次按照流输出一个字一个字的，遇到[DONE]结束
                console.log('1111,',event.data)
                if(n==2) return
                if(n==0){
                const obj = JSON.parse(event.data)
                  chat = {
                    role: 'assistant',
                    // content:result.data.data,
                    showtype: obj.type,
                    submodel: obj.modelType,  //a-1
                    msggroup:time.value,
                  }
                  resObj.value = JSON.parse(event.data)
                  n = 1
                }else {
                  if(chat.showtype == 'tem'){
                    eventSource.close()
                    if(sxxzType.value.submodel == 'a-7'){
                      if(event.data.totalCount){
                        chat.questionType = 1
                        event.data.data.noTab = true
                      } else {
                        chat.questionType = 2
                      }
                    }
                    chat.content = JSON.parse(event.data)  
                    chat.copyText = JSON.parse(event.data) 
                    loading.value = false
                    loadingmodel.value = ''
                    chatList.value.push(chat)
                    chatList_cqsm.value.push(chat)
                    console.log('对话list：：：', chatList.value)
                  } else if (chat.showtype == 'text'){
                    if (event.data === '[DONE]') {
                      console.info('结束')
                      loading.value = false
                      chat.content = marked(text.value)
                      chat.copyText = text.value
                      htmlText.value = marked(text.value);
                      chatList.value.push(chat)
                      chatList_cqsm.value.push(chat)
                      text.value = ''
                      htmlText.value = ''
                      step.value = 3
                      n=2
                      eventSource.close()
                    } else {
                        step.value = 2
                        console.log('event.data,,,',event.data)
                        // if (event.data.indexOf('<br><br>') != -1) {
                        //     event.data = event.data.replace('<br><br>', '\n\n')
                        // }
                        // if(event.data.indexOf('<br>') != -1){
                        //   event.data = event.data.replace('<br>','\n')
                        // }
                       
                        text.value += event.data
                        htmlText.value = marked(text.value);
                        console.log('text.value,,,',text.value)
                    }
                  }
                }
              };
              eventSource.onerror = (error) => {
                  console.error('EventSource failed:', error)
                  loading.value = false
                  loadingmodel.value = ''
                  step.value = 3
                  eventSource.close()
              };
              eventSource.stream();
                // const result = await GPTChat({
                //   "module":"a",
                //   "sub_module":sxxzType.value.submodel,
                //   "messages":userQueList,
                //   "msggroup": time.value,
                // })
                // if(result.code == 200){
                //     const chat = {
                //         role: 'assistant',
                //         content:result.data.data,
                //         showtype:result.data.type,
                //         submodel: result.data.modelType,  //a-1
                //         msggroup: time.value,
                //     }
                //     if(sxxzType.value.submodel == 'a-7'){
                //       if(result.data.data.totalCount){
                //         chat.questionType = 1
                //         result.data.data.noTab = true
                //       } else {
                //         chat.questionType = 2
                //       }
                //     }
                //     if(result.data.type == 'text'){
                //       showText.value = result.data.data
                //       resObj.value = result.data
                //       resObj.value.msggroup = time.value
                //       step.value = 2
                //       chatType.value = 'text'
                //     }else{
                //       loading.value = false
                //       loadingmodel.value = ''
                //       chatList.value.push(chat)
                //     }
                // }else{
                //   loading.value = false
                //   loadingmodel.value = ''
                //   step.value = 3
                // }
            }catch(error){
              console.log('error',error)
            }
          } else if(navQueryType.value.type == 'scbz' || 
            navQueryType.value.type == 'qmcm' ||
            navQueryType.value.type == 'tlp' || 
            navQueryType.value.type == 'zybg' ||
            navQueryType.value.type == 'hypd' ||
            navQueryType.value.type == 'gsqm' ||
            navQueryType.value.type == 'zgjm' ||
            navQueryType.value.type == 'fsbj' ||
            navQueryType.value.type == 'hdnj' ||
            navQueryType.value.type == 'hljr' ||
            navQueryType.value.type == 'hmxj'
          ) {
              const chat = {
                role: 'user',
                content:questionText,
                copyText: questionText,
                showtype:'text',
                submodel: navQueryType.value.module,
                msggroup: time.value,
                islike: false,
              }
              chatList_scbz.value.push(chat)
              loading.value = true
              loadingmodel.value = navQueryType.value.module
              step.value = 1
              setTimeout(() => {
                  scrollToBottom() 
                  store.commit('setQuestion', '')
              },50)
              let userQueList = []
              chatList_scbz.value.forEach(item =>  {
                if(item.submodel == navQueryType.value.module){
                  userQueList.push({ 
                    "type": item.role == 'user'? 'user' : item.showtype,
                    "content": item.content
                  })
                }
              })
              const requestData =  {
                  "module":navQueryType.value.module,
                 // "sub_module":sxxzType.value.submodel,
                  "messages":userQueList,
                  "msggroup": time.value,
                  "gpt_mode": userModel.value == '3.5'? 1 : 2,
                  islike: false,
                }
            try{
              eventSource = new SSE(apiurl.value, {
                headers: {
                  'Content-Type': 'application/json', 
                  'Authorization': localStorage.getItem('starloomAI-token'),
                },
                payload: JSON.stringify(requestData),
                method: "POST"
              });
              console.info(eventSource)
              eventSource.onopen = () => {
                  console.log('open')
              }
              let n = 0
              let chat
              eventSource.onmessage = function(event) {
                // 第一次返回： text|tem
              // 如果 是tem ，第二次返回整个json字符串；如果是text，第二次，到第N次按照流输出一个字一个字的，遇到[DONE]结束
                console.log('1111,',event.data)
                if(n==2) return
                if(n==0){
                  const obj = JSON.parse(event.data)
                  chat = {
                    role: 'assistant',
                    // content:result.data.data,
                    showtype: obj.type,
                    submodel: obj.modelType,  //a-1
                    msggroup:time.value,
                    msgId: obj.msgIds[1],
                    islike: false,
                  }
                  resObj.value = JSON.parse(event.data)
                  const lengthnum = chatList_scbz.value.length
                  chatList_scbz.value[lengthnum-1].msgId =  obj.msgIds[0]
                  n = 1
                }else {
                  if(chat.showtype == 'tem'){
                    eventSource.close()
                    if(sxxzType.value.submodel == 'a-7'){
                      if(event.data.totalCount){
                        chat.questionType = 1
                        event.data.data.noTab = true
                      } else {
                        chat.questionType = 2
                      }
                    }
                    chat.content = JSON.parse(event.data)
                    chat.copyText = JSON.parse(event.data)
                    loading.value = false
                    loadingmodel.value = ''
                    chatList_scbz.value.push(chat)
                    console.log('对话list：：：', chatList_scbz.value)
                  } else if (chat.showtype == 'text'){
                    if (event.data === '[DONE]') {
                      console.info('结束')
                      loading.value = false
                      chat.content = marked(text.value)
                      chat.copyText = text.value
                      chatList_scbz.value.push(chat)
                      text.value = ''
                      htmlText.value = ''
                      step.value = 3
                      n=2
                      eventSource.close()
                    } else {
                        step.value = 2
                        console.log('event.data,,,',event.data)
                        // if (event.data.indexOf('<br><br>') != -1) {
                        //     event.data = event.data.replace('<br><br>', '\n\n')
                        // }
                        // if(event.data.indexOf('<br>') != -1){
                        //   event.data = event.data.replace('<br>','\n')
                        // }
                        text.value += event.data
                        htmlText.value = marked(text.value);
                        console.log('text.value,,,',text.value)
                    }
                  }
                }
                
              };
              eventSource.onerror = (error) => {
                  console.error('EventSource failed:', error)
                  loading.value = false
                  loadingmodel.value = ''
                  step.value = 3
                  eventSource.close()
              };
              eventSource.stream();
                // const result = await GPTChat({
                //   "module":navQueryType.value.module,
                //   // "sub_module":sxxzType.value.submodel,
                //   "messages":userQueList,
                //   "msggroup": time.value,
                // })
                // if(result.code == 200){
                //     const chat = {
                //         role: 'assistant',
                //         content:result.data.data,
                //         showtype:result.data.type,
                //         submodel: result.data.modelType,  //a-1
                //         msggroup: time.value,
                //     }
                //     if(sxxzType.value.submodel == 'a-7'){
                //       chat.questionType = 1
                //     }
                //     if(result.data.type == 'text'){
                //       showText.value = result.data.data
                //       resObj.value = result.data
                //       step.value = 2
                //       chatType.value = 'text'
                //     }else{
                //       loading.value = false
                //       loadingmodel.value = ''
                //       chatList_scbz.value.push(chat)
                //     }
                // }else{
                //   loading.value = false
                //   loadingmodel.value = ''
                //   step.value = 3
                // }
            }catch(error){
  
            }
          }
      }
      // 生肖星座切换模块
      const changeQuetype = (item) => {
        if(sxxzType.value.submodel !=  item.submodel && item.submodel == 'a-7'){
          sxxzType.value = item
          const list = chatList.value.filter(item => item.submodel == sxxzType.value.submodel && item.msggroup)
          if(list.length>0){
            time.value = list[0].msggroup
          }else{
            time.value = new Date().getTime() + localStorage.getItem('userId') 
          }
           // 是否已经有问题 
          const list_model = chatList.value.filter(item => item.role == 'user' && item.submodel == sxxzType.value.submodel)
          if(list_model.length>0){
            step.value = 3
          }else{
            step.value = 1
          }
          // chatList.value = []
          // modelChatList.value = chatList.value.filter(item => item.submodel == sxxzType.value.submodel )
          getRankingList('', 1, 7)   // {"type": "4", "page": 1, "pageSize": 10}
          // sendMessage('星座排行榜',100)
          console.log(sxxzType.value.submodel)
          return
        }
        console.log(sxxzType.value.submodel)
        sxxzType.value = item
        // 是否已经有问题 
        const list_model = chatList.value.filter(item => item.role == 'user' && item.submodel == sxxzType.value.submodel)
        if(list_model.length>0){
          step.value = 3
        }else{
          step.value = 1
        }
        const list = chatList.value.filter(item => item.submodel == sxxzType.value.submodel && item.msggroup)
        if(list.length>0){
          time.value = list[0].msggroup
        }else{
          time.value = new Date().getTime() + localStorage.getItem('userId') 
        }
        console.log(sxxzType.value.submodel)
        // modelChatList.value = chatList.value.filter(item => item.submodel == sxxzType.value.submodel )
        // chatList.value = []
      }
      //  星座运势查询更改tab调用
      const chageTab = (obj) => { 
        getMessageTem(obj.que, obj.tab, obj.index)
      }
      
      const chageRankTab = (obj) => {
        rankPage.value = obj.page
        getRankingList(obj.type, obj.page, obj.pageSize, obj.index)
      }
  
    const getRankingList = async (type, page, pageSize, index) =>{
        console.log('xingzuoRankingList')
        // if(!index && index !=0){
        //     const chat = {
        //       role: 'user',
        //       content:questionText,
        //       showtype:'text',
        //       submodel: sxxzType.value.submodel
        //     }
        //     chatList.value.push(chat)
        //     loading.value = true
        //     step.value = 1
        //   }
          // setTimeout(() => {
          //     scrollToBottom() 
          //     store.commit('setQuestion', '')
          // },50)
        try{
            const result = await xingzuoRankingList({
              type: type, 
              page: page, 
              pageSize: pageSize,
            })
            if(result.code == 200){
                const chat = {
                    role: 'assistant',
                    content:result.data.data,
                    copyText: result.data.data,
                    showtype:result.data.type,
                    submodel: result.data.modelType,  //a-7
                    islike: false,
                    questionType: 1,
                }
                if(result.data.type == 'text'){
                  showText.value = result.data.data
                  resObj.value = result.data
                  step.value = 2
                  chatType.value = 'text'
                }else{  
                  if(index || index==0){
                    chatList.value[index] = chat
                    return
                  }
                  //  let a7Index 
                  const list = chatList.value.filter(item => item.showtype=='tem' && item.submodel == 'a-7' &&  item.questionType == 1)
                  if(list.length<=0){
                    chatList.value.push(chat)
                    loading.value = false
                    console.log('对话list：：：', chatList.value)
                    return
                  } else {
                    for(var i=0;i<chatList.value.length;i++){
                      if(chatList.value[i].showtype== list[0].showtype && chatList.value[i].submodel== list[0].submodel && chatList.value[i].questionType == list[0].questionType){
                          chatList.value[i] = chat
                      }
                    } 
                  }
  
                  // let a7Index 
                  // if(chatList.value.length>0){
                  //   for(var i=0;i<chatList.value.length;i++){
                  //     if(chatList.value[i].showtype=='tem' && chatList.value[i].submodel=='a-7' && chatList.value[i].questionType == 1){
                  //       a7Index = i
                  //       if(a7Index == 0 || a7Index){
                  //         chatList.value[a7Index] = chat
                  //       }else{
                  //         chatList.value.push(chat)
                  //       }
                  //       loading.value = false
                  //       break
                  //     }
                  //   } 
                  // }else{
                  //   chatList.value.push(chat)
                  //   loading.value = false
                  // } 
                }  
            }else{
            loading.value = false
            step.value = 3
          }
      }catch(error){

      }
    }

    const getXingzuoRanking = async (item) =>{
      console.log('xingzuoRankingGet')
      const chat = {
            role: 'user',
            content: item.title,
            copyText: item.title,
            showtype:'text',
            submodel: sxxzType.value.submodel,
            islike: false,
          }
      chatList.value.push(chat)
      loading.value = true
      step.value = 1
      try{
        const result = await xingzuoRankingGet({
          id: item.id,
          title: item.title,
          msggroup: time.value,
        })
        if(result.code == 200){
            const chat = {
                role: 'assistant',
                content:result.data.data,
                copyText: result.data.data,
                showtype:result.data.type,
                submodel: result.data.modelType,  //a-7
                islike: false,
                questionType: 2,
            }
            if(result.data.type == 'text'){
              showText.value = result.data.data
              resObj.value = result.data
              step.value = 2
              chatType.value = 'text'
            }else{
              result.data.data.sort((a, b) => a.votesNum - b.votesNum);
              chatList.value.push(chat)
              setTimeout(() => {
                  scrollToBottom() 
              },50)
              loading.value = false
              console.log('对话list：：：', chatList.value)
            }
        }else{
          loading.value = false
          step.value = 3
        }
      }catch(error){

      }
    }
    // 生肖星座切换模块
    const changeCQSMtype = (item) => {
       
        console.log(cqsmType.value.submodel)
        cqsmType.value = item
        // 是否已经有问题 
        const list_model = chatList_cqsm.value.filter(item => item.role == 'user' && item.submodel == cqsmType.value.submodel)
        if(list_model.length>0){
          step.value = 3
        }else{
          step.value = 1
        }
        const list = chatList_cqsm.value.filter(item => item.submodel == cqsmType.value.submodel && item.msggroup)
        if(list.length>0){
          time.value = list[0].msggroup
        }else{
          time.value = new Date().getTime() + localStorage.getItem('userId') 
        }
        console.log(cqsmType.value.submodel)
        
      }
    const shareLinkHandle =  async(mul) =>{ //md5Handle
      // const { MD5 } = require('crypto-js');
      
      const time = new Date().getTime()
      var privateKey = 'Gxo2lx^2(oBl3cx92(ixvG4Vy32g4'; 
      let list
      if(navQueryType.value.type == 'cqsm'){
        list = chatList_cqsm.value.filter(item => item.choose)
      }else{
        list = chatList_scbz.value.filter(item => item.choose)
      }
      if(list.length==0){
        ElMessage({
            message: '您必须至少选择一条要分享的消息。',
            type: 'error',
          })
          return
       }
      console.log(list)
      // const messagesList1 = md5(list.toString()) 
      // const messagesList = md5Handle(list.toString(), time) 
      var dex_str = objKeySort(list, time);
      const md5Hash = MD5(dex_str + privateKey)
      const md5Hex = md5Hash.toString();
      console.log('md5Hex,,,',md5Hex)
      let url
          if(location.href.indexOf('defi.swftcoin.com') != -1){
            url = 'https://defi.swftcoin.com/view/astroai_web-test/index.html#/'
          } else if(location.href.indexOf('starloom.ai') != -1 || location.href.indexOf('tianjige') != -1 ){
            url = 'https://starloom.ai//#/'
          } else{
            url = 'http://192.168.124.3:5173/#/'
          }
      const link = `${url}chat/${md5Hex}`
      if(mul == 'link'){
        const { toClipboard } = useClipboard()
        try {
            // 复制
            await toClipboard(link)
            // ElMessage({
            //   message: '复制链接成功',
            //   type: 'success',
            // })
            // 复制成功
          } catch (e) {
            // 复制失败
          }
      }
      
      const result = await setUserSharechat({
        code: md5Hex,
        t:time,
        contents:list,
      })
      if(result.code == 200){
        store.commit('setSelectStatus', false)
        store.commit('setSelectType', '')
        // let url
        //   if(location.href.indexOf('defi.swftcoin.com') != -1){
        //     url = 'https://defi.swftcoin.com/view/astroai_web-test/index.html#/'
        //   } else if(location.href.indexOf('starloom.ai') != -1 || location.href.indexOf('tianjige') != -1 ){
        //     url = 'https://starloom.ai//#/'
        //   } else{
        //     url = 'http://192.168.124.3:5173/#/'
        //   }
          // const link = `${url}chat/${md5Hex}`
          store.commit('setSharelink',link)
          console.log('sharelink,,,',link)
          if(mul == 'link'){
            // const { toClipboard } = useClipboard()
            // try {
            //   // 复制
            //   await toClipboard(link)
            //   // ElNotification({
            //   //   duration: 5000,
            //   //   message: '复制链接成功',
            //   //   customClass: 'notify',
            //   //   'show-close': false,
            //   // })
              ElMessage({
                message: '复制链接成功',
                type: 'success',
              })
            //   // 复制成功
            // } catch (e) {
            //   // 复制失败
            // }
          }else{
            EventBus.$emit('shareMultimedia', mul)
          }
        chatList.value.forEach(item =>{
          item.choose = false
          item.funshow = false
          item.sharePopover = false
        })
        chatList_cqsm.value.forEach(item =>{
          item.choose = false
          item.funshow = false
          item.sharePopover = false
        })
        chatList_scbz.value.forEach(item =>{
          item.choose = false
          item.funshow = false
          item.sharePopover = false
        })
      }else{
        // toClipboard.clearSelection();
        window.clipboardData.setData("Text","")
      }
    }
    const deleteChat =  async() =>{ //md5Handle
      let arr
      let a //最后一条是否选中
      if(navQueryType.value.type == 'cqsm'){
        arr = chatList_cqsm.value.filter(item => item.choose)
        // chatList_cqsm.value = chatList_scbz.value.filter(item => !arr.includes(item));
      }else{
        arr = chatList_scbz.value.filter(item => item.choose)
        // chatList_scbz.value = chatList_scbz.value.filter(item => !arr.includes(item));
      }
      const num =  list_current.value.length-1
      if(list_current.value[num].choose){
        a = "Y"
      }
      console.log(arr)
      let list = []
      arr.forEach(item => {
        list.push(item.msgId)
      })
      if(list.length==0){
          ElMessage({
              message: '您必须至少选择一条要删除的消息。',
              type: 'error',
            })
            return
        }
       console.log('list,,,',list)
       if(navQueryType.value.type == 'cqsm'){
          chatList_cqsm.value = chatList_cqsm.value.filter(item => !arr.includes(item));
          // if(a=="Y") likeType.value = ''
        }else{
          chatList_scbz.value = chatList_scbz.value.filter(item => !arr.includes(item));
          // if(a=="Y") likeType.value = ''
        }
      if(!loginStatus.value){
        store.commit('setSelectStatus', false)
        store.commit('setSelectType', '') 
        ElMessage({
          message: '删除成功',
          type: 'success',
        })
        return
      }
      const result = await usermsgDelete({
        "msgIds": list,
      })
      if(result.code == 200){
        // ElNotification({
        //   duration: 5000,
        //   message: '删除成功',
        //   customClass: 'notify',
        //   'show-close': false,
        // })
        ElMessage({
          message: '删除成功',
          type: 'success',
        })
        store.commit('setSelectStatus', false)
        store.commit('setSelectType', '') 
        chatList.value.forEach(item =>{
          item.choose = false
          item.funshow = false
          item.sharePopover = false
        })
        chatList_cqsm.value.forEach(item =>{
          item.choose = false
          item.funshow = false
          item.sharePopover = false
        })
        chatList_scbz.value.forEach(item =>{
          item.choose = false
          item.funshow = false
          item.sharePopover = false
        })
      }
    }
    const copyHandle =  async(item) => {
      const { toClipboard } = useClipboard()
      try {
        // 复制
        await toClipboard(item.copyText)
        console.log('success', ElMessage)
        // ElNotification({
        //   duration: 5000,
        //   message: '复制成功',
        //   customClass: 'notify',
        //   'show-close': false,
        // })
        ElMessage({
          message: '复制成功',
          type: 'success',
        })
        // 复制成功
      } catch (e) {
        // 复制失败
      }
    }
    const likeHandle = (liketype, obj)=>{
      obj.likeType = liketype
      let questionText
      if(liketype == 1){ // 喜欢
        questionText ='我非常赞同你上述回答，回复我“明白”即可！无需再回复任何信息。'
      } else if(liketype == 2){  //不准确
        questionText ='你的上述回答不准确。回复我“明白”即可！无需再回复任何信息。'
      } else if(liketype == 3){ //无益
        questionText ='你的上述回答对我没有什么帮助。回复我“明白”即可！无需再回复任何信息。'
      } else if(liketype == 4){ //攻击性
        questionText ='你的上述回答带有攻击性。回复我“明白”即可！无需再回复任何信息。'
      }
      let list_notlike
      let userchat
      if(navQueryType.value.type == 'cqsm'){
        list_notlike =  chatList_cqsm.value.filter(item=>!item.islike)
        userchat = {
          role: 'user',
          content:questionText,
          copyText: questionText,
          showtype:'text',
          submodel: cqsmType.value.submodel,
          msggroup: time.value,
          islike: true,
        }
      }else{
        list_notlike =  chatList_scbz.value.filter(item=>!item.islike)
        userchat = {
          role: 'user',
          content:questionText,
          copyText: questionText,
          showtype:'text',
          submodel: navQueryType.value.module,
          msggroup: time.value,
          islike: true,
        }
      }
      // likeType.value = liketype
      let userQueList = []
     
      if(navQueryType.value.type == 'cqsm'){
        chatList_cqsm.value.push(userchat)
        list_notlike.push(userchat)
        list_notlike.forEach(item =>  {
          if(item.submodel == cqsmType.value.submodel){
            userQueList.push({ 
              "type": item.role == 'user'? 'user' : item.showtype,
              "content": item.content
            })
          }
        })
      }else{
        chatList_scbz.value.push(userchat)
        list_notlike.push(userchat)
        list_notlike.forEach(item =>  {
          if(item.submodel == navQueryType.value.module){
            userQueList.push({ 
              "type": item.role == 'user'? 'user' : item.showtype,
              "content": item.content
            })
          }
        })
      }
      likeLoading.value = true
        const requestData =  {
            "module":navQueryType.value.module,
            // "sub_module":sxxzType.value.submodel,
            "messages":userQueList,
            "msggroup": time.value,
            "gpt_mode": userModel.value == '3.5'? 1 : 2,
            islike: true,
          }
          if(navQueryType.value.module=='a'){
            requestData.sub_module = 'a-1'
          }
      try{
        eventSource = new SSE(apiurl.value, {
          headers: {
            'Content-Type': 'application/json', 
            'Authorization': localStorage.getItem('starloomAI-token'),
          },
          payload: JSON.stringify(requestData),
          method: "POST"
        });
        console.info(eventSource)
        eventSource.onopen = () => {
            console.log('open')
        }
        let n = 0
        let chat
        eventSource.onmessage = function(event) {
          // 第一次返回： text|tem
        // 如果 是tem ，第二次返回整个json字符串；如果是text，第二次，到第N次按照流输出一个字一个字的，遇到[DONE]结束
          console.log('1111,',event.data)
          if(n==2) return
          if(n==0){
            const obj = JSON.parse(event.data)
            chat = {
              role: 'assistant',
              // content:result.data.data,
              showtype: obj.type,
              submodel: obj.modelType,  //a-1
              msggroup:time.value,
              msgId: obj.msgIds[1],
              islike: obj.islike,
            }
            resObj.value = JSON.parse(event.data)
          
            if(navQueryType.value.type == 'cqsm'){
              const lengthnum = chatList_cqsm.value.length
              chatList_cqsm.value[lengthnum-1].msgId =  obj.msgIds[0]
            }else{
              const lengthnum = chatList_scbz.value.length
              chatList_scbz.value[lengthnum-1].msgId =  obj.msgIds[0]
            }
            n = 1
          }else {
            if(chat.showtype == 'tem'){
              eventSource.close()
              if(sxxzType.value.submodel == 'a-7'){
                if(event.data.totalCount){
                  chat.questionType = 1
                  event.data.data.noTab = true
                } else {
                  chat.questionType = 2
                }
              }
              chat.content = JSON.parse(event.data)
              chat.copyText = JSON.parse(event.data)
              if( navQueryType.value.type == 'cqsm'){
                //navQueryType.value.type == 'sxxz' ||
                chatList_cqsm.value.push(chat)
              } else{
                chatList_scbz.value.push(chat)
              }  
              console.log('对话list：：：', chatList_scbz.value)
            } else if (chat.showtype == 'text'){
              if (event.data === '[DONE]') {
                console.info('结束')
                chat.content = marked(text.value)
                chat.copyText = text.value
                if( navQueryType.value.type == 'cqsm'){
                  //navQueryType.value.type == 'sxxz' ||
                  chatList_cqsm.value.push(chat)
                } else{
                  chatList_scbz.value.push(chat)
                }  
                text.value = ""
                n=2
                eventSource.close()
                likeLoading.value = false
              } else {
                  console.log('event.data,,,',event.data)
                  text.value += event.data
                  console.log('text.value,,,',text.value)
              }
            }
          }
          
        };
        eventSource.onerror = (error) => {
            console.error('EventSource failed:', error)
            loading.value = false
            loadingmodel.value = ''
            step.value = 3
            eventSource.close()
        };
        eventSource.stream();
      }catch(error){

      }
          
    }
    const showdislikeDialog = (item) => {
      likeItemObj.value = item
      disLikeDialog.value = true
    }
    const closeDisLike = () => {
      disLikeDialog.value = false
    }

   return {
      constellation: [
        {type:'sxcx', submodel:'a-1', name:'生肖查询',defaultQue:'您好，请输入您的公历出生年份，获取您的查询结果。例如：1980年10月5日'},
        {type:'sxys', submodel:'a-2', name:'生肖运势',defaultQue:'您好，请输入您的属相和要查询运势的年份(仅允许查询当年运势和下一年的运势)。例如：属相龙 2023年。'},
        {type:'ssxz', submodel:'a-3', name:'上升星座',defaultQue:'您好，请输入您的公历出生年月日以及出生时辰和性别。例如：公历1980年10月22日，00:00，女。'},
        {type:'xjxz', submodel:'a-4', name:'下降星座',defaultQue:'您好，请输入你的公历出生年月日以及时辰性别，例如：公历 1990年10月22日，00:00，女。'},
        {type:'xzys', submodel:'a-5', name:'星座运势', defaultQue:'您好，请输入您的星座，获取您的星座运势。例如：狮子座。'},
        {type:'zxcx', submodel:'a-6', name:'星座查询',defaultQue:'您好，请输入您的公历出生年月日。例：1980年10月22日。'},
        {type:'xzphb', submodel:'a-7', name:'星座排行榜',defaultQue:'您好，请点击下方列表中的问题来获取您想要查询星座排行。'},
        {type:'srh', submodel:'a-8', name:'生日花',defaultQue:'您好，请输入您的公历出生年月日。例：1980年10月22日。'},
        {type:'ylxz', submodel:'a-9', name:'月亮星座',defaultQue:'您好，请输入你的公历出生年月日以及时辰性别，例如：公历 1990年10月22日，00:00，女。'},
        {type:'48xq', submodel:'a-10', name:'48星区',defaultQue:'您好，请输入您的公历出生年月日。例：1980年10月22日。'},
        {type:'srmm', submodel:'a-11', name:'生日密码',defaultQue:'您好，请输入您的公历出生年月日。例：1980年10月22日。'},
        {type:'srs', submodel:'a-12', name:'生日书',defaultQue:'您好，请输入您的公历出生年月日。例：1980年10月22日。'},
        {type:'cscgdx', submodel:'a-13', name:'测试出轨对象',defaultQue:'您好，请输入测试对象的公历出生年月日以及性别，例如：1990年10月22日，女。'},
        {type:'xpcx', submodel:'a-14', name:'星盘查询',defaultQue:'您好，请输入您的公历出生年月日、出生地以及出生时辰和性别。例如：1990年10月22日，河北石家庄，00:00，女。'},
        {type:'xxlgwjx', submodel:'a-17', name:'行星落宫位解析',defaultQue:'您好，请输入您的行星和落在的宫位。例如：太阳落在第一宫位。'},
        {type:'xxlxzjx', submodel:'a-18', name:'行星落星座解析',defaultQue:'您好，请输入您的行星和落在的星座。例如：太阳落在白羊座。'},
        {type:'gwcx', submodel:'a-15', name:'宫位查询',defaultQue:'您好，请输入您的公历出生年月日、出生地以及出生时辰和性别。例如：1990年10月22日，河北石家庄，00:00，女。'},
        {type:'xzxxxg', submodel:'a-16', name:'星座血型性格',defaultQue:'您好，请输入您的公历出生年月日以及血型。例如：1990年10月22日，A型。'},     
      ],
      cqsmSub: [
        {
          type: "gylq",
          submodel: "k-1",
          name: "观音灵签",
          defaultQue:
            "亲爱的众生，欢迎来到观音灵签的神圣空间。在此，我们先与救苦救难的观音菩萨建立心灵的连接。请您合十，默念三遍[救苦救难观音菩萨]，然后默念您的姓名、出生时辰、年龄与地址。请心中默念您的请求，无论是关于婚姻、事业还是财运。当您准备好后，请告诉我开始抽签，我们将一同寻找观音菩萨为您指点的答案。",
        },
        {
          type: "gdlq",
          submodel: "k-2",
          name: "关帝灵签",
          defaultQue:
            "各位信众，欢迎来到关帝灵签的神秘殿堂。在开始之前，让我们首先向威武的关帝老爷致以三拜，以示诚挚的敬意。请您在默念自己的姓名、出生时辰、年龄及地址后，心中思索您所寻求的指引，无论是关于婚姻、事业或财运。当您的意念明确，告诉我开始抽签，关帝老爷将为您指明前路。",
        },
        {
          type: "lzlq",
          submodel: "k-3",
          name: "吕祖灵签",
          defaultQue:
            "亲爱的信徒，欢迎您来到吕祖灵签的神圣领域。在我们揭晓天命之前，请向仁慈的吕祖恭敬地拜上三拜，并默念您的姓名、出生资讯和地址。当您的内心诉求—无论是关于婚姻、事业还是财运—都已经凝结，告诉我开始抽签，我们将跟随吕祖的指引，走向命运的答案。",
        },
        {
          type: "yllq",
          submodel: "k-4",
          name: "月老灵签",
          defaultQue:
            "亲爱的寻缘者，欢迎来到月下老人的神秘之地。在我们揭晓您的姻缘之前，请向月老恭敬地拜三拜，并默念您的姓名与出生信息。心中的疑虑和期望，清晰地呈现。当您心意已决，告诉我开始抽签，我们一同看月老如何为您指点前程。",
        },
        {
          type: "hdxlq",
          submodel: "k-5",
          name: "黄大仙灵签",
          defaultQue:
            "各位信士，在黄大仙的庇佑之下，我们先行三拜，默念个人的姓名、时辰、年龄和地址，寻求对于婚姻、事业、财运等方面的神示。现在请告诉我开始抽签！",
        },
        {
          type: "fzlq",
          submodel: "k-6",
          name: "佛祖灵签",
          defaultQue:
            "亲爱的佛友。在这神圣的一刹，让我们合十，三遍默诵“佛祖慈悲，指点迷津”，心中默念自己姓名，出生时辰，年龄，地址，请求佛祖对我们的婚姻、事业、财运给予明确的指示。准备好了请告诉我开始抽签！",
        },
        {
          type: "mzlq",
          submodel: "k-7",
          name: "妈祖灵签",
          defaultQue:
            "各位敬仰妈祖的信徒，在这特殊的时刻，双手合十，默念“妈祖娘娘，指点迷津”三遍，，然后默念自己的姓名、生辰、年龄和地址，请求娘娘关于婚姻、事业、财运的启示。当您准备好后，请告诉我开始抽签！",
        },
        {
          type: "cslq",
          submodel: "k-8",
          name: "财神灵签",
          defaultQue:
            "各位求财者，在这充满变数的世界里，您双手合十，诚心地默念：“财神驾到，指点迷津”三次。然后，为让财神更了解您，您默念自己的详细信息：姓名、出生时辰、年龄和地址。在此基础上，您真诚地希望财神能为您在婚姻、事业和财运上给予建议。当您准备好后，请告诉我开始抽签！",
        },
        {
          type: "dzwlq",
          submodel: "k-9",
          name: "地藏王灵签",
          defaultQue:
            "亲爱的信徒，欢迎来到地藏王灵签的神秘空间，在面对生活中的疑惑与迷茫的时候，您静心地双手合十，全神贯注地默念：“地藏王驾到，指点迷津”三遍。仔细地默念自己的姓名、出生的具体时辰、年龄和住址，请求关于婚姻、事业和财运的答案，当您已经准备好了，请告诉我开始抽签！",
        },
        {
          type: "tsljlq",
          submodel: "k-10",
          name: "太上老君灵签",
          defaultQue:
            "各位道教的信徒，在太上老君的庇佑下，双手合十，您默默地默念：“太上老君，指点迷津”三次，仔细地默念自己的姓名、出生时辰、年龄和地址。心中对于婚姻、事业和财运的不确定，您请求老君的指引，如果您已经准备好了，请告诉我开始抽签！",
        },
        {
          type: "yj64glq",
          submodel: "k-11",
          name: "易经64卦灵签",
          defaultQue:
            "各位虔诚的信徒，在生活的波涛中，双手合十，深情地默念：“周文易经，指点迷津”三次。为了与易经的智慧更加贴近，您仔细地默念自己的姓名、出生的具体时辰、年龄和住址。对于未来的各种问题，如婚姻、事业和财运，您恳求易经给予您明确的建议，您准备好后，告诉我开始抽签！",
        },
        {
          type: "lhlq",
          submodel: "k-12",
          name: "罗汉灵签",
          defaultQue:
            "亲爱的罗汉的信徒，生活的道路上，五百罗汉的智慧与指引常被视为宝贵的财富。因此，您深情地双手合十，默念：“五百罗汉，指点迷津”三遍，心中默念自己的姓名、出生的时辰、年龄和地址。心中充满了对未来婚姻、事业和财运的疑虑，准备好后，请告诉我开始抽签！",
        },
        {
          type: "wspslq",
          submodel: "k-13",
          name: "文殊菩萨灵签",
          defaultQue:
            "亲爱的信徒，在人生的旅途中，文殊菩萨的智慧经常为迷茫者提供方向。双手合十，全心全意地默念：“文殊菩萨，指点迷津”三次。认真地默念您的姓名、出生时辰、年龄和地址。对于未来的婚姻、事业、财运等重要命题，对于未来的婚姻、事业和财运，您带着旺盛的好奇和期待请求指点，如果准备好了，请告诉我开始抽签！",
        },
        {
          type: "ltylq",
          submodel: "k-14",
          name: "老天爷灵签",
          defaultQue:
            "亲爱的大运之人，在无数次的选择与机遇中，有时我们希望得到超越凡人的指示，向老天爷拜下三拜，默念了自己的姓名、出生时辰、年龄和住址，好让老天爷明确地了解您的身份，带着这种心情，准备好请告诉我开始抽签！",
        },
        {
          type: "jglq",
          submodel: "k-15",
          name: "济公灵签",
          defaultQue:
            "虔诚的信徒，在人生旅途的某个交叉点，向济公深深地三拜，希望他能指引您走出人生的迷雾，默念自己姓名，出生时辰，年龄，地址还有那未知的缘分和姻缘，如果准备好了，请告诉我开始抽签！",
        },
        {
          type: "qtdslq",
          submodel: "k-16",
          name: "齐天大圣灵签",
          defaultQue:
            "愤愤天道不公的信徒，当命运之网似乎将您困于纷繁的尘埃中时，虔诚的先向齐天大圣拜三拜，诚求指示，向大圣娓娓道来自己的姓名，出生时辰，年龄，地址，关于那未知的缘分，关于那悬而未决的姻缘，如果您住备好了，请告诉我开始抽签！",
        },
        {
          type: "txdyq",
          submodel: "k-17",
          name: "天下第一签",
          defaultQue:
            "亲爱的众生，向那位气度非凡，神态慈悲的观音菩萨深深地躬身，拜上三拜，心中默诵着自己的名字、生辰、年龄与住址，无论是关于婚姻、事业还是财运。当您准备好后，请告诉我开始抽签，我们将一同寻找观音菩萨为您指点的答案。",
        },
      ],
      chatList,
      chatList_cqsm,
      chatList_scbz,
      loading,
      loadingmodel,
      step,
      showText,
      chatContent,
      sendMessage,
      scrollToBottom,
      chatType,
      navQueryType,
      sxxzType,
      changeQuetype,
      chageTab,
      chageRankTab,
      rankPage,
      getXingzuoRanking,
      resObj,
      getMessageTem,
      modelChatList,
      time,
      screenWidth,
      moduletab_mb,
      text,
      stopText,
      htmlText,
      cqsmType,
      changeCQSMtype,
      selectStatus,
      shareLinkHandle,
      selectType,
      deleteChat,
      copyHandle,
      likeHandle,
      disLikeDialog,
      showdislikeDialog,
      closeDisLike,
      chatlist_index,
      loginStatus,
      // likeType,
      apiurl,
      sharelink,
      list_current,
      likeItemObj,
      likeLoading,
      haveCount,
      // RelatedQuestions,
   } 
  },
  components: {
    Horoscope,
    ConstellationRankingList,
    ConstellationRankingItem,
    ZodiacQuery,
    ConstellationInquir,
    BirthdatePassword,
    ChineseZodiacFortune,
    DescendingZodiac,
    BirthdayFlower,
    BirthdayBook,
    ConsteBloodPersonality,
    Ascendant,
    MoonSign,
    Constellations48,
    CheatingPerson,
    AstrologicalChart,
    AstrologicalHouseChart,
    TextComponents,
    PlanetInHouse,
    PlanetInSign,
    DisLikeReason,
  },
  watch:{
    // chatList(val, old){
    //   this.modelChatList = val.filter(item => item.submodel == this.sxxzType.submodel )
    // }
    navQueryType(val,old){
      let userList_module
      // if(val.module == 'a'){
      //   userList_module = this.chatList.filter( item => item.role == 'user' && item.submodel == this.sxxzType.submodel)
      // } else
       if(val.module == 'k'){
        userList_module = this.chatList_cqsm.filter( item => item.role == 'user' && item.submodel == this.cqsmType.submodel)
      }else {
        userList_module = this.chatList_scbz.filter( item => item.role == 'user' && item.submodel == this.navQueryType.module)
      }
      if(userList_module.length>0){
        this.step = 3
      }else{
        this.step = 1
      }
    },
    selectStatus(val,old){
      if(val == false){
        this.chatList.forEach(item =>{
          item.choose = false
          item.funshow = false
          item.sharePopover = false
        })
        this.chatList_cqsm.forEach(item =>{
          item.choose = false
          item.funshow = false
          item.sharePopover = false
        })
        this.chatList_scbz.forEach(item =>{
          item.choose = false
          item.funshow = false
          item.sharePopover = false
        })
      }
    }
  },
  methods: {
    //文字展示完成的回调
    onComplete(text, obj){
      const self = this
      const chat = {
          role: 'assistant',
          content: text,
          copyText: text,
          showtype: obj.type,
          submodel: obj.modelType,  //a-7
          msggroup: obj.msggroup,
      }
      if(self.navQueryType.module == 'a'){
        self.chatList.push(chat)
      }else if(self.navQueryType.module == 'k'){
        self.chatList_cqsm.push(chat)
      } else{
        self.chatList_scbz.push(chat)
      }  
      self.loading = false
      setTimeout(() => {
          self.step = 3
      },100)
    },
    // 重新响应
    regenerateResponse(){
      if(!this.haveCount){
        EventBus.$emit('goSubscribe')
        return
      }
      let userList
      // if(this.navQueryType.type=='sxxz'){
      // userList = this.chatList.filter( item => item.role == 'user' && item.submodel == this.sxxzType.submodel)     
      // } else 
      if(this.navQueryType.type=='cqsm'){
        userList = this.chatList_cqsm.filter( item => item.role == 'user' && item.submodel == this.cqsmType.submodel && !item.islike) 
      } else{
        userList = this.chatList_scbz.filter( item => item.role == 'user' && item.submodel == this.navQueryType.module  && !item.islike)
      }
      this.sendMessage(userList[userList.length - 1].content)
      const self = this
      setTimeout(() => {
          self.scrollToBottom() 
      },500)
   },
    //停止响应
    stop(){
        // this.$refs.TextComponents.stop()
    },
    onHover(item){  //鼠标经过展示三点 其他功能
      item.funshow =  true
    },
    onMouseLeave(item){
      if(item.sharePopover) return
      item.funshow= false
    },
    getUrlParams(){
      var sHref = window.location.href
      var args = sHref.split('?')
      if (args[0] == sHref) {
        return ''
      }
      var arr = args[1].split('&')
      var obj = {}
      for (var i = 0; i < arr.length; i++) {
        var arg = arr[i].split('=')
        obj[arg[0]] = arg[1]
      }
      const paystatus = obj['paystatus']
      console.log('paystatus::::',paystatus)
      if(paystatus=='success'){
        ElMessageBox.confirm(
          "<img style='width: 0.6rem !important;margin-right: 0.1rem !important;margin-bottom: 0.05rem !important;' src='https://images.swft.pro/astroAI/pay/paySucc.svg' />订单支付成功",
            {
              showCancelButton:false,
              dangerouslyUseHTMLString: true,
              confirmButtonText: '确定',
              // cancelButtonText: t('cancel'),
              // cancelButtonClass: 'cancel',
              confirmButtonClass:'ok',
              // beforeClose: (action, instance, done) => {
              //   // if (action === 'confirm') {
              //   //   // 执行删除操作
              //   //   this.deleteRecord()
              //   //     .then(() => {
              //   //       done(); // 关闭消息框
              //   //     })
              //   //     .catch(() => {
              //   //       done(); // 阻止关闭消息框
              //   //     });
              //   // } else 
              //   if (action === 'close') {
              //     // 用户点击了关闭按钮或遮罩层
              //     console.log('用户关闭了消息框');
              //     const currentUrlWithoutParams = window.location.origin + window.location.pathname;
              //     history.replaceState({}, '',currentUrlWithoutParams )
              //   } else {
              //     done(); // 关闭消息框
              //   }
              // },
            },
        )
        .then(() => {
          const currentUrlWithoutParams = window.location.origin + window.location.pathname;
          history.replaceState({}, '',currentUrlWithoutParams )
        })
        .catch(() => {
          const currentUrlWithoutParams = window.location.origin + window.location.pathname;
          history.replaceState({}, '',currentUrlWithoutParams )
        })
      }else if(paystatus=='fail'){
        ElMessageBox.confirm(
          "<img style='width: 0.6rem !important;margin-right: 0.1rem !important;margin-bottom: 0.05rem !important;' src='https://images.swft.pro/astroAI/pay/payFail.svg' />订单支付失败",
            {
              showCancelButton:false,
              dangerouslyUseHTMLString: true,
              confirmButtonText: '确定',
              // cancelButtonText: t('cancel'),
              // cancelButtonClass: 'cancel',
              confirmButtonClass:'ok',
            },
        )
        .then(() => {
          const currentUrlWithoutParams = window.location.origin + window.location.pathname;
          history.replaceState({}, '',currentUrlWithoutParams )
        })
        .catch(() => {
          const currentUrlWithoutParams = window.location.origin + window.location.pathname;
          history.replaceState({}, '',currentUrlWithoutParams )
        })
      }
    },
    // copyHandle(){

    // },
    shareHandle(item){
      item.choose =true
      this.$store.commit('setSelectStatus', true)
      this.$store.commit('setSelectType', 'share')
    },
    deleteHandle(item){
      item.choose =true
      this.$store.commit('setSelectStatus', true)
      this.$store.commit('setSelectType', 'delete')
    }

  },
  mounted() {
    this.getUrlParams()
    EventBus.$on('sendMessage', this.sendMessage)
    EventBus.$on('shareLinkHandle', this.shareLinkHandle)
    EventBus.$on('deleteChat', this.deleteChat)
    EventBus.$on('likeHandle', (type,obj) => {
      this.likeHandle(type,obj)
    })
  },
  unmounted() {
    EventBus.$off('sendMessage', this.sendMessage)
    EventBus.$off('shareLinkHandle', this.shareLinkHandle)
    EventBus.$off('deleteChat', this.deleteChat)
    EventBus.$off('likeHandle', (type,obj) => {
      this.likeHandle(type,obj)
    })
  },
}
</script>

<style scoped lang='scss'>
.index{
  padding: .5rem 5.5% 0 5.3%;
  height: 100%;
}
.constellation-box,.mb-constellation-box{
  ul{
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;
    li{
      width: 9%;
      margin: 0 0.5%;
      margin-bottom: .2rem;
      text-align: center;
      height: .907rem;
      background: linear-gradient(180deg, #4B3628 0%, #130A00 100%);
      border-radius:0.259rem;;
      opacity: 1;
      border-image: linear-gradient(180deg, rgba(255, 255, 255, 1), rgba(255, 184, 0, 1)) 1 1;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-family: Alimama-DongFangDaKai;
      &.active{
        background: linear-gradient(180deg, #FFECAA 0%, #DE9932 100%);
        color: #000000;
      }
    }
  }
  &.mb-box{
    width: 90%;
    margin: 0 auto;
    overflow: hidden;
    overflow-x: auto;
    &::-webkit-scrollbar {
       display: none;
    }
    ul{
      flex-wrap: nowrap;
      width: 2550px;
    } 
      width: 90%;
      margin: 0 auto;
      overflow-x: auto;
      li{
        width: 120px;
        padding: 0 .2rem;
        // width: auto;
        margin: 0 .2rem;
      }
    }
}
.mb-constellation-box{
  ul{
    display: flex;
    li{
      width: 23%;
      margin: .2rem 1%;
      font-size: .259rem;
    }
    .nostyle{
      background: transparent;
    }
    .btn{
      display: flex;
      background: #FFFFFF;
      color: #000000;
      border-radius: .6rem;
    }
  }
}
.chatmaxbox{
  width: 98%;
  height: calc(100% - 2.148rem);
  margin: 0 auto;
  &.mb{
    height: calc(100% - 1.148rem);
  }
  &.mb_small{
    height: calc(100% - 5.478rem);
  }
}
.chatmaxbox-other{
  width: 98%;
  // height: calc(100% - 1rem);
  height: 100%;
  margin: 0 auto;
}
.chat{
  width: 100%;
  // height: 100%;
  // height: calc(100% - 3.548rem);
  height: 100%;
  overflow: hidden;
  overflow-y: auto;
  padding-bottom: 1rem;
  // padding: 0 1.5rem;
  // padding-bottom: 1.2rem;
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
  .chat-list{
    text-align: left;
    display: flex;
    margin-top: .3rem;
    .select{
      margin-right: .2rem;
      img{
        width: .4rem;
      }
    }
    &:last-child{
      padding-bottom: 1.2rem; 
    }
    &.right-content{
      justify-content: flex-end;
      .select{
        display: flex;
        justify-content: flex-start;
        align-items: center;
        flex: 1;
      }
    }
    .question,.answer{
      width: 100%;
      display: flex;
      .avatar{
          width: .8rem;
          height: .8rem;
      }
      .text-content{
        flex: 1;
        min-height: 1rem;
        box-sizing: border-box;
        display: flex;
        align-items:flex-start;
        .inner{
            padding: .25rem .4rem;
            font-size: .259rem;
            line-height: 16px;
            font-family: Poppins-Regular, Poppins;
            max-width: calc(100% - 1rem);
        }
        // .cursorafter{
        //   display: flex;
        //   // justify-content: flex-start;
        //   &:after {
        //     content: '';
        //     display: inline-block;
        //     height: 15px;
        //     width: 3px;
        //     vertical-align: baseline;
        //     background-color: currentcolor;
        //     animation: cursor 1s infinite;
        //   }
        // }
      }
      .record-content{
        width: 100%;
        margin-left: .1rem;
      }
    }
    .question{
      .text-content{
        justify-content: flex-end;
        .inner{
          margin-right: .1rem; 
          background: #FFECBD;
          border-radius: .3rem .1rem  .3rem  .3rem;
          color: #000000;
          word-break: break-all;
        }
      }         
    }
    .answer{
      .text-content{
        .inner{
          margin-left: .1rem;
          background: linear-gradient(270deg, #341B00 0%, #140B00 100%);
          border-radius: 0.1rem 0.3rem 0.3rem 0.3rem;
          position: relative;
          color: #ffefdd;
          line-height: 0.45rem;
          // font-size: .24rem;
          font-size: .259rem;
          // padding: .6rem .4rem;
          .zindex{
            z-index: 1111;
            position: relative;
          }
          .xiangyun{  
            position: absolute;
            background: url(/@/assets/images/xiangyun.svg) no-repeat 100% 80%;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-size: contain;
          }
        }
      }
    }
  }
  .chatBotton{
    display: flex;
    margin-left: 1.1rem;
    margin-top: 0.1rem;
    font-size: .259rem;
    .share{
      background: #FFF5E5;
      border-radius: .55rem;   
      color: #FF870F;
      display: flex;
      align-items: center;
      height: .7rem;
      padding: 0 .3rem;
      cursor: pointer;
      margin-right: .2rem;
      img{
        margin-right: .1rem;
      }
    }
    .likediv{
      width: 1.81rem;
      border-radius: .55rem;   
      color: #2C2216;
      display: flex;
      align-items: center;
      justify-content: center;
      height: .7rem;
      // padding: 0 .3rem;
      border: 1px solid #130A00;
      cursor: pointer; 
      margin-right: .2rem;
      img{
        margin-right: .1rem;
      }
    }
    .chooseIsLike{
      width: 1rem;
      border-radius: .55rem;   
      display: flex;
      align-items: center;
      justify-content: center;
      height: .7rem;
      // padding: 0 .3rem;
      border: 1px solid #FF3D00;
      cursor: pointer; 
      margin-right: .2rem;
    }
     &.mb_chatBotton{
        margin-left: .1rem;
      }

  }
}
.bottom-input{
        position: absolute;
        bottom: .3rem; 
        width: 100%;
        left: 0;
        display: flex;
        justify-content: center;
        .item{
            border-radius: .185rem;
            background: #A98F6E;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            height: .7rem;
            font-size: .26rem;
            font-family: Poppins-Regular, Poppins;
            color: #2D1800;
            margin: 0 0.361rem;
            width: 2.3888rem;
            border: none;
        }
    }
.normal-box,.vip-box{
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  .list{
    width: 30%;
    margin-bottom: .3rem;
  }
}
.line{
  font-size: .3333rem;
  font-family: Poppins-Bold, Poppins;
  color: #FFFFFF;
  text-align: center;
  padding: .8rem 0;
}
.mb-index{
  .chat-list{
    .select{
      margin-right: .3rem;
      img{
        width: .4rem;
      }
    }
    .answer{
      display: block;
      width: 99%;
      .BotHeader{
        display: flex;
        align-items: center;
        color: #000000;
        img{
          margin-right: .2rem;
          &.mbImg{
            width: .5rem;
            height: .5rem;
          }
        }
        &.mb{
          justify-content: space-between;
          .left{
            display: flex;
            align-items: center;
          }
        }
      }
      .text-content{
        margin-top: .2rem;
        .inner{
          max-width: 100%;
        }
      }
    }
  }
}
</style>
<style>
.three-bounce {
  text-align: left;
  display: flex;
  align-items: center;
}
.three-bounce .one {
  -webkit-animation-delay: -.32s;
  animation-delay: -.32s;
}
.three-bounce .two {
  -webkit-animation-delay: -.16s;
  animation-delay: -.16s;
}
.three-bounce>div {
  display: inline-block;
  width: 14px;
  height: 14px;
  border-radius: 100%;
  top: 50%;
  background: #aeadba;
  -webkit-animation: bouncedelay 1.4s infinite ease-in-out;
  animation: bouncedelay 1.4s infinite ease-in-out;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
}

@keyframes bouncedelay {
  0%,100%,80% {
      transform: scale(0);
      -webkit-transform: scale(0)
  }

  40% {
      transform: scale(1);
      -webkit-transform: scale(1)
  }
}
</style>
