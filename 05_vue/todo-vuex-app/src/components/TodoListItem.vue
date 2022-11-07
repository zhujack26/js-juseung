<template>
  <div> 
    {{ todo.title }}
    <button @click="deleteTodo"> Delete</button>
  </div>
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: Object,
  },
  methods: {
    deleteTodo() {
      // console.log('삭제 메서드 호출!!')
      this.$store.dispatch('deleteTodo', this.todo)
      // this.$store.commit('DELETE_TODO', this.todo)
    }
  }
}
</script>

<style>

</style>