import { defineStore } from 'pinia'

export const useSystemStore = defineStore('system', {
  state: () => ({ cpu: 42, memory: 58, gpu: 36, modelReady: true })
})
