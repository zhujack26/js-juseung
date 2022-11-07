<template>
  <div>
    <TodoListItem
      v-for="(todo, index) in todos"
      :key="index"
      :todo="todo"
    />
    <!-- v-for의 key는 배열의 각 요소 간의 유일한 식별자 값을 사용해야 하지만
    vuex 흐름에 집중하기 위해 indx를 key로 사용하도록 함 -->
  </div>  
</template>

<script>
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  computed: {
    todos() {
      return this.$store.state.todos
    }
  }
}
</script>

<style>

</style>