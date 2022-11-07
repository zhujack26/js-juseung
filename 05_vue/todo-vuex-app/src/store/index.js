import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [],
      // {
      //   title: '할 일 1',
      //   isCompleted: false,
      // },
      // {
      //   title: '할 일 2',
      //   isCompleted: false,
      // }, mutation 만들고 필요없다
  },
  getters: {
  },
  mutations: {
    CREATE_TODO(state, todoItem) {
      state.todos.push(todoItem)
    },
    DELETE_TODO(state, todoItem){
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index)
    }
  },
  actions: {
    createTodo(context, todoTitle){
      // Todo 객체 만들기
      const todoItem = {
        title: todoTitle,
        isCompleted: false,
      }
      context.commit('CREATE_TODO', todoItem)
    },
    deleteTodo(context, todoItem) {
      context.commit('DELETE_TODO', todoItem)
    }
  },
  // actions 에서 보통 비동기 관련 작업이 진행되지만 현재는 불필요하기 때문에 이렇게 진행
  modules: {
  }
})
