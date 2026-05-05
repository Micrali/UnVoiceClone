# API 接口文档

## 健康检查

`GET /api/health`

## 登录

`POST /api/auth/login`

请求体：`{"username":"admin","password":"admin123"}`

## 音频防御

`POST /api/audio/defend`

表单字段：`file`、`level`

## 视频防御

`POST /api/video/defend`

表单字段：`file`

## 防御测试

`POST /api/test/convert`

`POST /api/test/synthesis`

## 系统统计

`GET /api/system/stats`
