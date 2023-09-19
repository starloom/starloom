const EventBus = {
    events: {},
  
    $on(event, callback) {
      if (!this.events[event]) {
        this.events[event] = []
      }
  
      this.events[event].push(callback)
    },
  
    $off(event, callback) {
      if (this.events[event]) {
        const index = this.events[event].indexOf(callback)
  
        if (index > -1) {
          this.events[event].splice(index, 1)
        }
      }
    },
  
    $emit(event, ...args) {
      if (this.events[event]) {
        this.events[event].forEach(callback => {
          callback(...args)
        })
      }
    }
  }
  
  export default EventBus
  