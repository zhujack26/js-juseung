import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    message: 'message in store'
  },
/* state : $store.state로 state 데이터에 접근*/
  getters: {
    messageLength(state) {
      return state.message.length
    },
    // return this.$store.getters.messageLength
    doubleLength(state, getters) {
      return getters.messageLengh *2
    },
  },
/*state를 활용하여 계산된 값을 얻고자 할 때 사용
결과는 캐시되며, 종속된 값이 변경된 경우에만 재계산
계산된 값은 state에 영향 x
첫번째 인자로 state, 두번째 인자로 getter를 받음*/
  mutations: {
    CHANGE_MESSAGE(state, newMessage) {
      // 대문자로 강조하여 actions와 구별
      // console.log(state)
      // console.log(newMessage)
      state.message = newMessage
    }
  },
/* Mutations
실제로 state를 변경하는 유일한 방법
여기서 호출되는 핸들러 함수는 반드시 동기적, state의 변화 시기를 특정할 수 없기 때문
첫 번째 인자로 state를 받으며, component 혹은 Actions에서 commit()메서드로 호출됨*/
  actions: {
    changeMessage(context, newMessage) {
      // console.log(context)
      // console.log(newMessage)
      context.commit('CHANGE_MESSAGE', newMessage)
    }
  },
/* 비동기 작업이 포함될 수 있는(외부 API와의 소통 등) methods
station 직접 변경하지 않고 commit()메서드로 mutations를 호출해서 state를 변경
context 객체를 인자로 받으면, 이 객체를 통해 store.js의 모든 요소와 메서드에 접근 가능
(== 즉 state를 직접 변경할 수 있지만 하지 않아야 함)
component 에서 dispatch()메서드에 의해 호출됨
첫 번째 인자는 context, 두 번째 인자는 payloda */
  modules: {
  }
})


/* component에서 데이터를 조작하기 위한 데이터의 흐름
component => (actions) => mutations => state

component에서 데이터를 사용하기 위한 데이터의의 흐름
state => (getters) => component 

이제부터는 객체 메서드 축양형 사용
*/

