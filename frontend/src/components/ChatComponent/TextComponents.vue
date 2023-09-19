<template>
  <div>
    <div class="text" ref="text" style="white-space:pre-line">{{ displayText }}</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      index: 0,
      displayText: "",
      intervalId: null,
      stopStatus: false
    };
  },
  props:['text','obj'],
  mounted() {
    this.startDisplayText();
  },
  beforeDestroy() {
    clearInterval(this.intervalId);
  },
  methods: {
    stop(){
        console.log('stop')
        this.stopStatus = true
    },
    startDisplayText() {
      this.intervalId = setInterval(() => {
        if (this.index < this.text.length && !this.stopStatus) {
          this.displayText += this.text.charAt(this.index);
          this.index++;
        } else {
          clearInterval(this.intervalId);
          // this.obj.displayText = this.displayText
          this.$emit('onComplete',this.displayText, this.obj)
        }
      }, 30);
    }
  }
};
</script>

<style lang="scss" scoped>
.text{
    font-family: Poppins-Regular, Poppins;
    color: #ffefdd;
    line-height: 0.45rem;
    font-size: .24rem;
}
</style>