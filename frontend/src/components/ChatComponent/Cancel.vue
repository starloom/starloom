<template>
    <div class="successMaxBox">
      <div class="text" ref="text" style="white-space:pre-line">支付成功，感谢您的订单</div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        // index: 0,
        // displayText: "",
        // intervalId: null,
        // stopStatus: false
      };
    },
    props:['text','obj'],
    mounted() {
    //   this.startDisplayText();
    },
    beforeDestroy() {
    //   clearInterval(this.intervalId);
    },
    methods: {
    //   stop(){
    //       console.log('stop')
    //       this.stopStatus = true
    //   },
    //   startDisplayText() {
    //     this.intervalId = setInterval(() => {
    //       if (this.index < this.text.length && !this.stopStatus) {
    //         this.displayText += this.text.charAt(this.index);
    //         this.index++;
    //       } else {
    //         clearInterval(this.intervalId);
    //         // this.obj.displayText = this.displayText
    //         this.$emit('onComplete',this.displayText, this.obj)
    //       }
    //     }, 30);
    //   }
    }
  };
  </script>
  
  <style lang="scss" scoped>
  .successMaxBox{
    padding: 1rem 6%;
    height: 100%;
    display: flex;
    align-items: center;
  }
  .text{
      font-family: Poppins-Regular, Poppins;
      color: #ffefdd;
    //   line-height: 0.45rem;
      font-size: .43rem;
      color: #000;
      margin: 0 auto;
        // line-height: 100%;
        // height: 100%; 
        // padding-top: 40%;
  }
  </style>