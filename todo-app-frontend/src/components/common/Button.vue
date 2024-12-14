<template>
  <button
    :type="type"
    :disabled="disabled"
    :aria-disabled="disabled"
    class="btn"
    :class="[variantClass, additionalClasses]"
  >
    <slot />
  </button>
</template>

<script setup lang="ts">
import { computed } from "vue";

// Define los props que el componente puede recibir
interface ButtonProps {
  type?: "button" | "submit" | "reset";
  disabled?: boolean;
  variant?: "primary" | "secondary";
  // Permite recibir clases adicionales
  additionalClasses?: string;
}

// Define los props con tipado estricto
const props = defineProps<ButtonProps>();

// Computed para manejar clases adicionales de manera condicional
const variantClass = computed(() => {
  switch (props.variant) {
    case "primary":
      return "btn-secondary";
    case "primary":
    default:
      return "btn-primary";
  }
});
</script>

<style scoped>
.btn {
  padding: 10px 20px;
  color: white;
  border: none;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s;
  border-radius: 4px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.btn-primary {
  background-color: #42b883;
}

.btn-secondary {
  background-color: #1e90ff;
}

.btn:disabled,
.btn[aria-disabled="true"] {
  background-color: #ccc;
  cursor: not-allowed;
}

.btn:not(:disabled):hover {
  filter: brightness(0.9);
}
</style>
