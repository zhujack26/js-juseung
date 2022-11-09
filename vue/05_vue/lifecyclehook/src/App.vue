<template>
  <div id="app">
    <button @click="toggle">toggle</button>
    <ChildComponent
      v-if="flag"
    />
    <hr>
    <DogComponent/>
  </div>
</template>

<script>
import ChildComponent from '@/components/ChildComponent'
import DogComponent from '@/components/DogComponent'

export default {
  name: 'App',
  data() {
    return {
      flag: true
    }
  },
  methods: {
    toggle() {
      this.flag = !this.flag
    }
  },
  components: {
    ChildComponent,
    DogComponent,
  },
  created() {
    console.log('App created!')
  },
  mounted() {
    console.log('App mounted!')
  },
}
</script>

<!-- App.vue 생성 -> ChildComponent 생성 -> ChildComponent 부착
-> App.vue 부착 -> ChildComponent 업데이트 순으로 동작한 것 -->