<!-- 星座排行榜 -->
<template>
    <div class="chat-list" :class="screenWidth<=900 ? 'mb' : ''">
      <div class="answer">
            <div class="BotHeader">
              <img class="avatar" :class="screenWidth<=900 ? 'mbImg' : ''" src="/@/assets/images/aibot.png" alt="">
              <div v-if="screenWidth<=900">天机阁</div>
            </div>
            <div class="record-content">   
              <div class="allContent">
                <div class="top" v-if="!presetData.noTab">
                  <div class="rightPart" >
                    <div class="item"  @click="changeTab('')" :class="tab===''? 'active' : ''"> 全部</div>
                    <div class="item"  @click="changeTab(0)" :class="tab===0? 'active' : ''">爱情</div>
                    <div class="item"  @click="changeTab(1)" :class="tab===1? 'active' : ''">个性</div>
                    <div class="item"  @click="changeTab(2)" :class="tab===2? 'active' : ''">钱财</div>
                    <div class="item"  @click="changeTab(3)" :class="tab===3? 'active' : ''">工作</div>
                    <div class="item"  @click="changeTab(4)" :class="tab===4? 'active' : ''">趣味</div>
                  </div>
                </div>
                <div class="question-list">
                  <div class="item-list" v-for='(item, index) in presetData.list' :key="index" @click="xingzuoRanking(item)">
                      <div class="img-box">
                          <img :src="item.imgUrl" alt="">
                      </div>
                      <div>
                          <div class="Q">{{ item.title }}</div>
                          <div>{{ item.content }}</div>
                      </div>
                  </div>
                </div>
                <div class="pagination">
                    <!-- <el-pagination
                        :hide-on-single-page="true"
                          background
                          :current-page="1"
                          :page-size="7"
                          :total="100"
                          :pager-count="5"
                          @current-change="pagechange"
                          layout="pager">
                      </el-pagination> -->
                    <el-pagination 
                      :hide-on-single-page="true"
                      :current-page="page"
                      :page-size="7"
                      :total="presetData.totalCount"
                      :pager-count="5"
                      @current-change="pagechange"
                      layout="pager"
                    />
                </div>
              </div>         
              <div class="xiangyun"></div>
            </div>
        </div>
  </div>
</template>

<script>
import { ref, computed, watch } from 'vue';
import { useStore} from 'vuex'
export default {
name: '',
props:{
  presetData:{
      type: Object,
      default: null
  },
  page:{
      type: Number,
      default: null
  },
  index:{
      type: Number,
      default: null
  },
},
setup(props) {
  const store = useStore()
  //适配
  const screenWidth = computed( () => {
    return store.state.screenWidth
  })
  const presetData = ref(null)
  watch(() => props.presetData, (newValue, oldValue) => {
      presetData.value = newValue
  })
  presetData.value = props.presetData
  const index = ref(null)
  watch(() => props.index, (newValue, oldValue) => {
    index.value = newValue
  })
  index.value = props.index
  const page = ref(1)
  // watch(() => props.page, (newValue, oldValue) => {
  //   page.value = newValue
  // })
  // page.value = props.page
    const tab = ref('')
  // 分割
  // const queList = [
  return {
      presetData,
      tab,
      index,
      page,
      screenWidth,

  } 
},
components: {
},
methods: {
  changeTab(item){
    this.tab = item
    const obj = {
      type: this.tab,
      page: 1,
      pageSize: 7,
      index: this.index,
    }
      this.$emit('chageRankTab', obj)
  },
  pagechange(page){
    console.log(111)
    this.page = page
    const obj = {
      type: this.tab,
      page: this.page,
      pageSize: 7,
      index: this.index,
    }
    this.$emit('chageRankTab', obj)
  },
  xingzuoRanking(item){
    this.$emit('getXingzuoRanking', item)
  }
    
},
mounted() {
  
},
unmounted() {
  
},
}
</script>

<style scoped lang='scss'>
.chat-list{
  text-align: left;
  display: flex;
  margin-top: .3rem;
  &.right-content{
  justify-content: flex-end;
  }
  .question,.answer{
      display: flex;
      width: calc(100% - 1rem);
      img,.img{
          width: .8rem;
          height: .8rem;
      }
      .text-content{
          flex: 1;
          min-height: 1rem;
          box-sizing: border-box;
          display: flex;
          align-items: center;
          .inner{
              padding: .25rem .4rem;
              font-size: 12px;
              line-height: 16px;
              font-family: Poppins-Regular, Poppins;
          }
      }
      .record-content{
          width: 100%;
          padding: 0.6rem .4rem;
          margin-left: .1rem;
          background: linear-gradient(270deg, #341B00 0%, #140B00 100%);
          color: #ffefdd;
          border-radius: 0.1rem 0.25rem 0.25rem 0.25rem;
          position: relative;
          .xiangyun{  
              position: absolute;
              background: url(/@/assets/images/xiangyun.svg) no-repeat 100% 80%;
              top: 0;
              left: 0;
              width: 100%;
              height: 100%;
              background-size: contain;
          }
          .allContent{
            z-index: 1111;
            position: relative;
          }
          .top{
            display: flex;
            justify-content: space-between;
            .rightPart{
              background: #120900;
              display: flex;
              justify-content: space-around;
              align-items: center;
              border-radius: 0.222rem;
              height: .907rem;
              .item{
                color: #ffefdd;
                padding: 0 .3rem;
                text-align: center;
                margin: 0 .2rem;
                border-radius: 0.222rem;
                box-shadow: 0px 4px 20px -6px rgba(0,0,0,0.15);
                // line-height: .685rem;
                height: .685rem;;
                display: flex;
                align-items: center;
                justify-content: center;
                cursor: pointer;
                &.active{
                  background: #894900;
                  color: #FFFFFF;
                }
              }
            }
          }
          .question-list{
             font-size: 0.259rem;
            color: #ffefdd;
            .item-list{
                display: flex;
                justify-content: flex-start;
                margin-top: .685rem;
                cursor: pointer;
                .img-box{
                    width: .8148rem;
                    height: .8148rem;
                    margin-right: .2222rem;
                }
                .Q{
                    color: #FF9900;
                    margin-bottom: .185rem;
                }
            }
          }
          .pagination{
            background: transparent;
            display: flex;
            justify-content: flex-end;
            padding: 0.5rem 0;
            // background: #120900 !important;
            :deep(.el-pagination){
                background: #120900 !important;
                border-radius: .18rem;
                color:  #ffefdd !important;
            }
            :deep(.el-pager li ){
                background: #120900;
                border-radius: .18rem;
                color:  #ffefdd ;
            }
            :deep(.el-pager li.is-active){
                background: #894900;
                box-shadow: 0px 4px 20px -6px rgba(0,0,0,0.15);
                border-radius: .18rem;
                color: #FFFFFF;
            }
          }
      }
  }
  &.mb{
      font-size: .22rem;
      .answer{
        display: block;
        width: 98%;
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
        }
        .record-content{
          margin-top: .2rem;
          .top{
            display: block;
            .rightPart{
              margin-top: .3rem;
              overflow: hidden;
              overflow-x: auto;
              &::-webkit-scrollbar {
                display: none !important;
              }
              .item{
                white-space:nowrap;
                padding: 0;
                width: 20%;
                margin: 0 0.1rem;
              }
            }
          }
        }
      }
    }
}
</style>