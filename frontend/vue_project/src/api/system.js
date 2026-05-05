import http from './index'
export const healthApi = () => http.get('/health')
