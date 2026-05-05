import http from './index'
export const loginApi = (data) => http.post('/auth/login', data)
