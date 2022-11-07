<template>
  <div id="app">
    <h1>{{ message }}</h1>
    <h2>입력된 문자의 길이는 {{ messageLength }}</h2>
    <!-- 1번 helloworld 관련 삭제하고 state 접근 후 서버 켜서 Vuex 확인 -->
    <input
      type="text"
      @keyup.enter="changeMessage"
      v-model="inputData"
    >  
    <!-- 3번 -->
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
        inputData: null
    }
    // 3번
  },
  // 2번 위의 html 직접적인 접근보다는 state message를 갖고 오는 메서드 값 활용  
  computed: {
    message() {
      return this.$store.state.message
    },
    messageLength() { //getters의 계산된 값 가져오기
      return this.$store.getters.messageLength
    },
    doubleLength() {
      return this.$store.getters.doubleLength
    },
  },
  methods: {
    changeMessage() {
      const newMessage = this.inputData
      this.$store.dispatch('changeMessage', newMessage)   //서버 timeline에서 event info확인
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
