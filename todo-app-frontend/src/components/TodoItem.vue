<template>
  <li class="todo-item">
    <input
      type="checkbox"
      :id="`todo-${todo.id}`"
      v-model="localCompleted"
      @change="toggle"
      aria-label="Marcar como completada"
    />
    <label
      :for="`todo-${todo.id}`"
      :class="{ completed: localCompleted }"
      @dblclick="enableEdit"
    >
      <span v-if="!isEditing">{{ todo.text }}</span>
      <input
        v-else
        v-model="editedText"
        @keyup.enter="saveEdit"
        @blur="cancelEdit"
        @keyup.esc="cancelEdit"
        aria-label="Editar tarea"
        ref="editInput"
      />
    </label>
    <Button
      variant="secondary"
      @click="remove"
      additionalClasses="delete-btn"
      aria-label="Eliminar tarea"
    >
      Eliminar
    </Button>
  </li>
</template>

<script setup lang="ts">
import { ref, watch, nextTick } from "vue";
import Button from "@/components/common/Button.vue";

// Actualizar la interfaz Todo si se cambió el tipo de id a string
interface Todo {
  id: string;
  text: string;
  completed: boolean;
}

const props = defineProps<{ todo: Todo }>();
const emit = defineEmits<{
  (e: "toggle", id: string, completed: boolean): void;
  (e: "remove", id: string): void;
  (e: "edit", id: string, newText: string): void;
}>();

// Estado local para manejar el checkbox y edición
const localCompleted = ref(props.todo.completed);
const isEditing = ref(false);
const editedText = ref(props.todo.text);

// Referencia al input de edición para enfocarlo al momento de editar
const editInput = ref<HTMLInputElement | null>(null);

// Watcher para emitir el cambio de completado
watch(localCompleted, (newVal) => {
  emit("toggle", props.todo.id, newVal);
});

// Método para eliminar la tarea
const remove = () => {
  emit("remove", props.todo.id);
};

// Método para manejar el cambio de completado
const toggle = () => {
  emit("toggle", props.todo.id, localCompleted.value);
};

// Métodos para manejar la edición
const enableEdit = () => {
  isEditing.value = true;
  // Esperar al siguiente tick para enfocar el input
  nextTick(() => {
    editInput.value?.focus();
  });
};

const saveEdit = () => {
  const trimmedText = editedText.value.trim();
  if (trimmedText && trimmedText !== props.todo.text) {
    emit("edit", props.todo.id, trimmedText);
  } else {
    cancelEdit(); // Cancelar edición si no hay cambios
  }
  isEditing.value = false;
};

const cancelEdit = () => {
  editedText.value = props.todo.text;
  isEditing.value = false;
};
</script>

<style scoped>
.todo-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px;
  border-bottom: 1px solid #ccc;
}

.todo-item input[type="checkbox"] {
  width: 20px;
  height: 20px;
  cursor: pointer;
}

.todo-item label {
  flex: 1;
  display: flex;
  align-items: center;
  cursor: pointer;
}

.todo-item label.completed {
  text-decoration: line-through;
  color: #999;
}

.todo-item label input[type="text"] {
  flex: 1;
  padding: 5px;
  font-size: 1rem;
  border: 2px solid #42b883;
  border-radius: 4px;
  outline: none;
  transition: border-color 0.3s;
}

.todo-item label input[type="text"]:focus {
  border-color: #2c8a6d;
}

.delete-btn {
  background-color: #e74c3c;
}

.delete-btn:hover {
  background-color: #c0392b;
}
</style>
