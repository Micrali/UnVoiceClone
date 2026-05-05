# 用声无恙 - UnVoiceClone

<p align="center">
  <strong>面向生成式伪造语音欺骗的鲁棒主动防御系统</strong>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.8%2B-blue">
  <img alt="Flask" src="https://img.shields.io/badge/Flask-2.3.3-green">
  <img alt="Vue" src="https://img.shields.io/badge/Vue-3.x-42b883">
  <img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-2.0.1-ee4c2c">
  <img alt="License" src="https://img.shields.io/badge/License-Apache%202.0-yellow">
</p>

<p align="center">
  <a href="#-快速开始">快速开始</a> ·
  <a href="#-核心功能">核心功能</a> ·
  <a href="#-系统架构">系统架构</a> ·
  <a href="#-代码结构">代码结构</a> ·
  <a href="#-开源代码与组件使用情况说明">开源说明</a>
</p>

---

## 项目概述

**用声无恙 - UnVoiceClone**，简称 **UnVC**，是一个面向生成式伪造语音欺骗的声纹隐私主动防御系统。

系统不是在伪造语音生成后再进行被动检测，而是在用户发布音频或视频之前，主动对人声进行防克隆处理。处理后的语音在人耳听感上保持自然，但会显著干扰语音克隆模型的声纹提取、身份建模与目标音色复刻，从源头降低声纹泄露、AI 语音诈骗、身份冒充与声音版权侵权风险。

本仓库为根据作品书与任务书构建的完整 GitHub 工程仓库，包含静态前端演示页面、Vue3 开发版前端骨架、Flask 后端 API、核心算法模块、配置文件、文档与测试用例，可用于作品展示、答辩演示、网站截图和后续二次开发。

## 核心技术

- **异性身份替换主动防御**：基于 KL 散度的声纹特征选择策略，最大化克隆语音与原始语音之间的身份差异。
- **高保真防御语音生成**：通过嵌入损失、软约束损失与高斯分布逼近损失，在语音保真与防御强度之间取得平衡。
- **WaveGlow 鲁棒对抗生成**：面向重采样、剪裁、加噪、MP3/AAC 压缩等真实传播场景进行鲁棒扰动优化。
- **动态集成说话人编码器**：融合 ECAPA-TDNN、GE2E、d-vector、Style Encoder 等多类声纹表征，提高未知黑盒模型泛化能力。
- **SAM 扰动优化策略**：引入梯度正则化与锐度感知最小化思想，提升防御扰动在多模型、多平台下的稳定性。
- **Web 端交互闭环**：支持音频防御、视频防御、音频转换测试、音频合成测试、控制台看板与系统配置演示。

## 快速开始

### 环境准备

```bash
# 1. 创建虚拟环境，推荐使用 Python 3.9
python -m venv unvc_env

# 2. 激活虚拟环境
# Windows:
unvc_env\Scripts\activate

# Linux/macOS:
source unvc_env/bin/activate

# 3. 安装依赖包
pip install -r requirements.txt
```

### 方式一：一键启动，推荐

```bash
python start.py
```

支持的启动模式：

#### 1. 传统静态页面模式

- 零配置快速启动
- 适合比赛答辩和作品截图
- 不依赖 Node.js 环境
- 支持完整前端固定输入/输出演示
- 10 秒内即可完成启动

#### 2. Vue 框架开发模式

- Vue3 + Vite 现代化前端工程
- 支持组件化二次开发
- 适合后续扩展为真实产品系统
- 需要 Node.js 18+ 环境

### 方式二：直接启动完整演示系统

```bash
python start_system.py
```

该命令会同时启动：

- 静态前端服务：`http://127.0.0.1:8080`
- Flask 后端服务：`http://127.0.0.1:5000`

### Vue 框架模式详细说明

环境要求：

```bash
node --version  # v18.0.0+
npm --version   # v9.0.0+
```

依赖安装与启动：

```bash
cd frontend/vue_project
npm install
npm run dev
```

Vue 开发版技术栈：

- Vue 3：响应式前端框架
- Vite：现代化构建工具
- Element Plus：企业级 UI 组件库
- Pinia：状态管理
- Vue Router：路由管理
- Axios：HTTP 请求封装
- ECharts：数据可视化

## 系统访问

启动成功后访问以下地址：

| 页面 | 地址 | 说明 |
|------|------|------|
| 主页 | `http://127.0.0.1:8080/index.html` | 系统主页与核心指标展示 |
| 登录页 | `http://127.0.0.1:8080/auth.html` | 演示登录入口 |
| 控制台 | `http://127.0.0.1:8080/dashboard.html` | 固定演示数据看板 |
| 功能展示 | `http://127.0.0.1:8080/function.html` | 系统核心功能入口 |
| 音频防御 | `http://127.0.0.1:8080/audio-defend.html` | 音频主动防御演示 |
| 视频防御 | `http://127.0.0.1:8080/video-defend.html` | 视频人声防护演示 |
| 音频转换测试 | `http://127.0.0.1:8080/audio-transform.html` | VC 克隆攻击测试 |
| 音频合成测试 | `http://127.0.0.1:8080/audio-synthesis.html` | TTS 克隆攻击测试 |
| 兼容测试入口 | `http://127.0.0.1:8080/test-defend.html` | 自动跳转到音频转换测试 |
| 系统设置 | `http://127.0.0.1:8080/settings.html` | 模型状态与参数配置 |
| API 健康检查 | `http://127.0.0.1:5000/api/health` | 后端服务健康状态 |
| API 文档 | `http://127.0.0.1:5000/api/docs` | 后端接口列表 |

默认登录：

```text
用户名：admin
密码：admin123
```

## 核心功能

### 音频主动防御

- 支持 MP3、WAV 音频上传
- 提供固定演示输入：`original_voice_demo.wav`
- 输出固定演示结果：`unvc_defended_voice.wav`
- 展示原始音频与防御后音频波形
- 输出防御成功率、语音保真相似度、抗压缩防御能力
- 点击“开始防御”即可展示完整处理结果

### 视频人声防护

- 支持 MP4、AVI 视频文件演示
- 自动模拟视频音轨提取与人声片段定位
- 固定演示输入：`interview_clip_demo.mp4`
- 固定演示输出：`unvc_defended_video.mp4`
- 展示原始视频与防御后视频预览
- 固定结果显示人声片段数量、处理时长与克隆风险下降

### 音频转换测试

- 模拟攻击者基于目标音色进行语音转换克隆
- 固定源音频：`speaker_source_demo.wav`
- 固定目标音色：`defended_target_demo.wav`
- 固定输出：`clone_result_demo.wav`
- 点击“音频转换”后展示克隆前后相似度对比

### 音频合成测试

- 模拟 TTS 模型基于目标音色进行文本到语音合成
- 支持固定演示文本
- 展示合成相似度与目标音色保护结论
- 用于证明防御后音频难以被稳定复刻为原始说话人声音

### 控制台数据看板

- 累计防御文件数
- 今日处理数量
- 平均防御成功率
- 平均处理时长
- 系统可用性
- 克隆风险拦截次数
- 历史处理记录
- 模型运行状态

## 作品效果图

作品效果图可直接使用网页截图。推荐截图顺序如下：

1. 系统主页：`index.html`
2. 功能展示：`function.html`
3. 音频防御：`audio-defend.html`
4. 视频防御：`video-defend.html`
5. 音频转换测试：`audio-transform.html`
6. 音频合成测试：`audio-synthesis.html`
7. 控制台：`dashboard.html`
8. 系统设置：`settings.html`

建议截图规格：

- 浏览器：Chrome / Edge
- 分辨率：1920×1080 或 1440×900
- 浏览器缩放：100%

## 系统架构

```text
用户浏览器
   │
   ├── 静态前端演示页面 frontend/web_static/
   │      ├── 系统主页
   │      ├── 音频防御
   │      ├── 视频防御
   │      ├── 音频转换测试
   │      └── 音频合成测试
   │
   ├── Vue3 开发版前端 frontend/vue_project/
   │      ├── Vue Router
   │      ├── Pinia Store
   │      ├── Axios API
   │      └── Element Plus UI
   │
   └── Flask 后端 API backend/
          ├── 认证接口
          ├── 音频防御接口
          ├── 视频防御接口
          ├── 防御测试接口
          └── 系统管理接口
                 │
                 ▼
          核心算法模块 core_algorithm/
          ├── 动态集成说话人编码器
          ├── KL 散度身份替换
          ├── WaveGlow 对抗语音生成
          ├── 基音可控调节
          ├── SAM 扰动优化
          └── 多损失函数约束
```

## 代码结构

```text
UnVoiceClone-System/
├── start.py                         # 系统启动选择器
├── start_system.py                  # 静态前端 + Flask 后端启动器
├── README.md                        # 项目说明文档
├── LICENSE                          # Apache 2.0 开源协议
├── requirements.txt                 # Python 依赖包清单
│
├── frontend/                        # 前端工程
│   ├── web_static/                  # 静态 HTML 演示版
│   │   ├── index.html               # 系统主页
│   │   ├── auth.html                # 登录页面
│   │   ├── dashboard.html           # 控制台数据看板
│   │   ├── function.html            # 功能展示页
│   │   ├── audio-defend.html        # 音频防御页面
│   │   ├── video-defend.html        # 视频防御页面
│   │   ├── audio-transform.html     # 音频转换测试页面
│   │   ├── audio-synthesis.html     # 音频合成测试页面
│   │   ├── test-defend.html         # 兼容跳转页面
│   │   ├── settings.html            # 系统设置页面
│   │   ├── styles.css               # 全局样式
│   │   ├── app.js                   # 演示交互逻辑
│   │   └── components.js            # 公共导航组件
│   │
│   └── vue_project/                 # Vue3 开发版前端
│       ├── src/
│       │   ├── main.js              # Vue 应用入口
│       │   ├── App.vue              # 根组件
│       │   ├── components/          # 页面组件
│       │   ├── router/              # Vue Router
│       │   ├── store/               # Pinia 状态管理
│       │   ├── api/                 # API 接口封装
│       │   └── styles/              # 全局样式
│       ├── package.json             # 前端依赖配置
│       └── vite.config.js           # Vite 构建配置
│
├── backend/                         # Flask 后端服务
│   ├── app.py                       # Flask 应用入口
│   ├── model_client.py              # 算法模型客户端
│   ├── api/                         # API 蓝图模块
│   │   ├── auth_api.py              # 认证接口
│   │   ├── audio_defend_api.py      # 音频防御接口
│   │   ├── video_defend_api.py      # 视频防御接口
│   │   ├── test_api.py              # 防御测试接口
│   │   └── system_api.py            # 系统管理接口
│   ├── utils/                       # 后端工具
│   │   ├── audio_processor.py       # 音频预处理工具
│   │   ├── video_processor.py       # 视频处理工具
│   │   ├── file_handler.py          # 文件上传与输出处理
│   │   └── auth_handler.py          # 权限认证工具
│   └── config/                      # 后端配置
│       ├── app_config.py            # 应用配置
│       └── model_config.py          # 模型配置
│
├── core_algorithm/                  # 核心算法模块
│   ├── model_server.py              # 算法推理服务
│   ├── modules/
│   │   ├── speaker_encoder_integration.py
│   │   ├── kl_divergence_identity_swap.py
│   │   ├── waveglow_adversarial_generator.py
│   │   ├── pitch_controllable_adjust.py
│   │   └── perturbation_optimizer.py
│   └── loss/
│       ├── embedding_loss.py
│       ├── soft_constraint_loss.py
│       └── gaussian_approximation_loss.py
│
├── models/                          # 预训练模型目录
│   ├── pretrained/                  # 预训练权重存放位置
│   └── model_loader.py              # 模型加载工具
│
├── utils/                           # 全局工具脚本
│   ├── ina_speech_segmenter_wrapper.py
│   ├── metrics_calculator.py
│   └── multi_thread_processor.py
│
├── configs/                         # 全局配置
│   ├── integration_config.py
│   ├── algorithm_params.yaml
│   └── server_config.yaml
│
├── docs/                            # 项目文档
│   ├── 作品安装说明.md
│   ├── 作品效果图说明.md
│   ├── API接口文档.md
│   ├── 部署文档.md
│   ├── 技术白皮书.md
│   └── 开源代码与组件使用情况说明.md
│
└── tests/                           # 测试用例
    ├── api_test.py
    ├── algorithm_test.py
    └── performance_test.py
```

## API 接口体系

### 认证管理

- `POST /api/auth/login`：用户登录
- `POST /api/auth/logout`：用户退出
- `GET /api/auth/profile`：用户信息查询

### 音频防御服务

- `POST /api/audio/defend`：上传音频并执行 UnVC 防御
- `GET /api/audio/status/<task_id>`：查询音频防御任务状态
- `GET /api/audio/download/<file_id>`：下载防御后音频

### 视频防御服务

- `POST /api/video/defend`：上传视频并执行人声防护
- `GET /api/video/status/<task_id>`：查询视频防御任务状态
- `GET /api/video/download/<file_id>`：下载防御后视频

### 防御测试服务

- `POST /api/test/convert`：音频转换克隆测试
- `POST /api/test/synthesis`：音频合成克隆测试
- `GET /api/test/report/<task_id>`：获取测试报告

### 系统管理服务

- `GET /api/health`：系统健康检查
- `GET /api/docs`：API 列表
- `GET /api/system/stats`：系统统计数据
- `GET /api/system/status`：模型与服务状态

## 技术栈

### 前端技术

- HTML5 / CSS3 / JavaScript：静态演示页面
- Vue 3：开发版前端框架
- Vite：前端构建工具
- Element Plus：UI 组件库
- Pinia：状态管理
- Vue Router：路由管理
- Axios：API 请求封装
- ECharts：图表可视化

### 后端技术

- Flask：轻量级 Web 服务框架
- Flask-CORS：跨域访问支持
- Python 多线程：批量任务处理
- REST API：前后端接口通信
- 文件处理模块：上传、保存、输出管理

### 算法与音视频技术

- PyTorch：深度学习模型推理与算法实现
- torchaudio：音频张量与深度学习音频处理
- librosa：音频特征提取与预处理
- pydub：音频切片、拼接与格式转换
- ffmpeg-python：音视频编解码与格式转换
- moviepy：视频重封装与音视频合成
- opencv-python：视频元信息读取与校验
- numpy / scipy / scikit-learn：数值计算、统计分析与聚类处理

## 系统要求

### 最低配置

- Python：3.8+
- 内存：8GB RAM
- 存储：10GB 可用空间
- 浏览器：Chrome 90+ / Edge 90+ / Firefox 88+
- 操作系统：Windows 10、Ubuntu 18.04+、macOS

### 推荐配置

- Python：3.9
- 内存：16GB+ RAM
- GPU：NVIDIA GPU，CUDA 11.7+，显存 16GB+
- 存储：20GB+ SSD
- Node.js：18+ LTS，用于 Vue 开发版

## 使用指南

### 1. 音频防御演示

1. 打开 `audio-defend.html`。
2. 查看固定演示输入 `original_voice_demo.wav`。
3. 点击“开始防御”。
4. 页面展示防御后文件、处理耗时、防御成功率与保真度结果。

### 2. 视频防御演示

1. 打开 `video-defend.html`。
2. 查看原始视频演示画面。
3. 点击“开始防御”。
4. 页面展示防御后视频、人声片段数量与克隆风险下降结果。

### 3. 音频转换测试

1. 打开 `audio-transform.html`。
2. 查看原始音频与目标音色音频。
3. 点击“音频转换”。
4. 页面展示克隆前后相似度对比与防御结论。

### 4. 音频合成测试

1. 打开 `audio-synthesis.html`。
2. 查看固定测试文本与目标音色。
3. 点击“开始合成”。
4. 页面展示合成相似度与声纹保护结论。

## 开源代码与组件使用情况说明

本项目以前后端工程与算法模块化封装为主体，界面设计、交互逻辑、接口组织、配置管理与业务流程均围绕“声纹隐私主动保护”需求完成。项目使用 Flask、Vue、PyTorch、ECharts、librosa、ffmpeg-python、moviepy 等开源组件作为基础开发工具和底层支撑，所有组件均在其开源协议允许范围内使用。

项目核心创新点包括 KL 散度身份替换、防御扰动优化、动态集成说话人编码器、多损失约束与音视频主动防御流程。第三方开源组件主要承担框架、音视频处理、可视化和基础计算能力，不构成对核心业务创新的替代。

详细说明见：

```text
docs/开源代码与组件使用情况说明.md
```

## 测试验证

```bash
python -m pytest tests/api_test.py tests/algorithm_test.py tests/performance_test.py
```

当前测试覆盖：

- API 健康检查
- KL 身份替换模块输出形状
- 核心指标计算结果

## 常见问题

### 启动后无法访问页面

请检查 `8080` 和 `5000` 端口是否被占用。若端口被占用，可关闭对应进程或修改 `configs/server_config.yaml`。

### Vue 前端启动失败

请确认 Node.js 版本为 18+，进入 `frontend/vue_project/` 后执行：

```bash
npm install
npm run dev
```

### 上传后没有真实生成模型结果

当前仓库为作品展示与工程骨架版本，前端页面内置固定演示输入输出，后端保留真实模型接入接口。接入完整预训练权重后，可替换 `core_algorithm/` 中的模拟流程。

### 模型权重应放在哪里

预训练模型权重建议放入：

```text
models/pretrained/
```

并在 `backend/config/model_config.py` 与 `configs/algorithm_params.yaml` 中配置路径和推理参数。

## 项目文档

- `docs/作品安装说明.md`
- `docs/作品效果图说明.md`
- `docs/API接口文档.md`
- `docs/部署文档.md`
- `docs/技术白皮书.md`
- `docs/开源代码与组件使用情况说明.md`

## 开源协议

本项目采用 Apache 2.0 开源协议，详见 `LICENSE` 文件。
