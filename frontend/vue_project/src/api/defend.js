import http from './index'
export const getStatsApi = () => http.get('/system/stats')
