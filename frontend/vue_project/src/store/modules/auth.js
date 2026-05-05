import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({ token: localStorage.getItem('unvc_token') || '', user: null }),
  actions: { setToken(token) { this.token = token; localStorage.setItem('unvc_token', token) } }
})
