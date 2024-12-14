<template>
  <div class="todo-list">
    <h2>Lista de Tareas</h2>
    <ul>
      <TodoItem
        v-for="todo in filteredTodos"
        :key="todo.id"
        :todo="todo"
        @toggle="toggleTodo"
        @remove="removeTodo"
        @edit="editTodo"
      />
    </ul>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from "vue";
import { useTodoStore } from "@/stores/todoStore";
import TodoItem from "@/components/TodoItem.vue";

// Obtiene el store de Pinia
const todoStore = useTodoStore();

// Computed property que obtiene la lista de tareas
const todos = computed(() => todoStore.todos);

// Computed property que filtra las tareas según el filtro seleccionado
const filter = ref<"all" | "active" | "completed">("all");
const filteredTodos = computed(() => {
  if (filter.value === "active") {
    return todos.value.filter((todo) => !todo.completed);
  } else if (filter.value === "completed") {
    return todos.value.filter((todo) => todo.completed);
  }
  return todos.value;
});

// Métodos para interactuar con el store
const toggleTodo = (id: string) => {
  todoStore.toggleTodo(id);
};

// Método para eliminar una tarea
const removeTodo = (id: string) => {
  todoStore.removeTodo(id);
};

const editTodo = (id: string, newText: string) => {
  todoStore.editTodo(id, newText);
};
</script>

<style scoped>
.todo-list {
  padding: 20px;
}

.todo-list h2 {
  margin-bottom: 10px;
}

.todo-list ul {
  list-style: none;
  padding: 0;
}
</style>
