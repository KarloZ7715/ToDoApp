import { defineStore } from 'pinia';
import { v4 as uuidv4 } from 'uuid';

interface Todo {
  id: string;
  text: string;
  completed: boolean;
}

export const useTodoStore = defineStore('todo', {
  state: () => ({
    todos: [] as Todo[],
  }),
  actions: {
    addTodo(text: string) {
      this.todos.push({
        id: uuidv4(),
        text,
        completed: false,
      });
    },
    toggleTodo(id: string) {
      const todo = this.todos.find((todo) => todo.id === id);
      if (todo) {
        todo.completed = !todo.completed;
      }
    },
    removeTodo(id: string) {
      this.todos = this.todos.filter((todo) => todo.id !== id);
    },
    editTodo(id: string, newText: string) {
      const todo = this.todos.find((todo) => todo.id === id);
      if (todo && newText.trim().length > 0) {
        todo.text = newText.trim();
      }
    },
  },
});