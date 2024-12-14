<template>
  <div class="add-todo">
    <form @submit.prevent="submitTodo" class="add-todo-form">
      <input
        type="text"
        v-model="newTodo"
        placeholder="Añadir nueva tarea"
        @keyup.enter="submitTodo"
        aria-label="Nueva Tarea"
        :aria-invalid="!isValid"
        :class="{ 'input-error': !isValid && hasAttemptedSubmit }"
      />
      <Button
        type="submit"
        :disabled="!isValid"
        variant="primary"
        additionalClasses="add-btn"
      >
        Añadir
      </Button>
    </form>
    <p v-if="!isValid && hasAttemptedSubmit" class="error-message">
      Por favor, introduce una tarea válida.
    </p>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from "vue";
import { useTodoStore } from "@/stores/todoStore";
import Button from "@/components/common/Button.vue";

// Referencia para la nueva tarea
const newTodo = ref("");

// Bandera para saber si se ha intentado enviar el formulario
const hasAttemptedSubmit = ref(false);

// Accede al store de Pinia
const todoStore = useTodoStore();

// Computed property para validar la nueva tarea
const isValid = computed(() => newTodo.value.trim().length > 0);

// Método para añadir una nueva tarea
const submitTodo = () => {
  hasAttemptedSubmit.value = true;
  if (isValid.value) {
    todoStore.addTodo(newTodo.value.trim());
    newTodo.value = "";
    hasAttemptedSubmit.value = false;
  }
};
</script>

<style scoped>
.add-todo {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
}

.add-todo-form {
  display: flex;
  width: 100%;
  max-width: 600px;
  gap: 10px;
}

.add-todo input {
  flex: 1;
  padding: 10px;
  font-size: 1rem;
  border: 2px solid #ccc;
  border-radius: 4px;
  outline: none;
  transition: border-color 0.3s;
}

.add-todo input:focus {
  border-color: #42b883;
}

.input-error {
  border-color: #e74c3c;
}

.error-message {
  color: #e74c3c;
  margin-top: 5px;
  font-size: 0.9rem;
}

.add-btn {
  padding: 10px 20px;
}
</style>
