import { defineStore } from 'pinia'

export const useDefendStore = defineStore('defend', {
  state: () => ({ tasks: [], level: 'standard' }),
  actions: { addTask(task) { this.tasks.unshift(task) } }
})
