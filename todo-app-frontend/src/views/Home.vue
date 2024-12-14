<template>
  <div class="home">
    <AddTodo />
    <TodoList />
  </div>
</template>

<script setup lang="ts">
import AddTodo from "@/components/AddTodo.vue";
import TodoList from "@/components/TodoList.vue";
</script>

<style scoped>
.home {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}
</style>
