const pageConfigs = {
  'audio-defend': {
    presetName: 'original_voice_12s_demo.wav',
    outputName: 'original_voice_12s_demo.wav',
    duration: '12.4s',
    actionText: '开始防御',
    loadingText: '防御处理中...',
    doneText: '防御完成',
    resultTitle: '音频防御完成',
    resultDesc: '系统已生成防克隆音频：语音保真度 84.73%，黑盒模型防御成功率 66.29%，抗压缩防御成功率 60.04%。',
    presetUrl: 'original_voice_12s_demo.wav',
    outputUrl: 'original_voice_12s_demo.wav'
  },
  transform: {
    presetName: 'original_voice_12s_demo.wav',
    outputName: 'original_voice_12s_demo.wav',
    duration: '12.4s',
    actionText: '开始转换',
    loadingText: '转换测试中...',
    doneText: '转换完成',
    resultTitle: '音频转换测试完成',
    resultDesc: '转换攻击结果已生成：原始目标音色相似度 92%，防御后相似度降至 17%，攻击效果明显失效。',
    presetUrl: 'original_voice_12s_demo.wav',
    outputUrl: 'original_voice_12s_demo.wav'
  },
  synthesis: {
    presetName: 'original_voice_12s_demo.wav',
    outputName: 'original_voice_12s_demo.wav',
    duration: '12.4s',
    actionText: '开始合成',
    loadingText: '合成测试中...',
    doneText: '合成完成',
    resultTitle: '音频合成测试完成',
    resultDesc: 'TTS 克隆合成完成：防御后合成相似度降至 19%，系统判定目标音色提取失败。',
    presetUrl: 'original_voice_12s_demo.wav',
    outputUrl: 'original_voice_12s_demo.wav'
  }
}

function qs(selector) { return document.querySelector(selector) }

function getConfig() {
  const demoBtn = document.querySelector('[data-demo]')
  return pageConfigs[demoBtn?.dataset.demo] || pageConfigs['audio-defend']
}

const cfg = getConfig()
const demoState = { loaded: false, processing: false, completed: false, objectUrl: '' }

function toast(message, type = 'success') {
  const el = qs('#toast')
  if (!el) return
  el.textContent = message
  el.className = `toast show ${type}`
  setTimeout(() => { el.className = 'toast' }, 2200)
}

function hideResults() {
  qs('#metricGrid')?.classList.add('hidden')
  qs('#visualPanel')?.classList.add('hidden')
  qs('#result')?.classList.add('hidden')
}

function showResults() {
  qs('#metricGrid')?.classList.remove('hidden')
  qs('#visualPanel')?.classList.remove('hidden')
  qs('#result')?.classList.remove('hidden')
}

function setAudioSources(inputUrl, outputUrl = '') {
  const original = qs('#originalAudio')
  const output = qs('#defendedAudio')
  if (original) original.src = inputUrl
  if (output && outputUrl) output.src = outputUrl
}

function resetState() {
  demoState.processing = false
  demoState.completed = false
  hideResults()
  qs('#downloadAction').disabled = true
  qs('#startAction').textContent = cfg.actionText
  qs('#startAction').classList.remove('loading')
  qs('#progressBar').style.width = '0%'
  qs('#processText').textContent = '素材已加载，可以开始处理。核心结果会在完成后醒目展示。'
}

function loadPreset() {
  demoState.loaded = true
  qs('#audioInfo').textContent = `当前文件：${cfg.presetName}　时长：${cfg.duration}　格式：WAV　大小：3.8 MB`
  setAudioSources(cfg.presetUrl)
  const output = qs('#defendedAudio')
  if (output) output.removeAttribute('src')
  resetState()
  toast('预设素材已加载，可直接预览')
}

function uploadAudio(event) {
  const file = event.target.files && event.target.files[0]
  if (!file) return
  if (!file.type.startsWith('audio/')) {
    toast('请上传音频文件', 'error')
    return
  }
  if (demoState.objectUrl) URL.revokeObjectURL(demoState.objectUrl)
  demoState.objectUrl = URL.createObjectURL(file)
  demoState.loaded = true
  qs('#audioInfo').textContent = `当前文件：${file.name}　时长：待识别　格式：${(file.type || 'audio/wav').split('/').pop().toUpperCase()}　大小：${(file.size / 1024 / 1024).toFixed(1)} MB`
  setAudioSources(demoState.objectUrl)
  resetState()
  toast('音频文件上传成功')
}

function completeAction() {
  demoState.processing = false
  demoState.completed = true
  qs('#startAction').classList.remove('loading')
  qs('#startAction').textContent = cfg.doneText
  qs('#downloadAction').disabled = false
  qs('#processText').textContent = '处理完成，结果播放器、指标卡与评估报告已解锁。'
  const output = qs('#defendedAudio')
  if (output) output.src = cfg.outputUrl
  const result = qs('#result')
  if (result) result.innerHTML = `<div class="result-kicker">评估报告</div><h3>${cfg.resultTitle}</h3><p>${cfg.resultDesc}</p>`
  showResults()
  toast('处理完成，可直接播放对比结果')
}

function startAction() {
  if (!demoState.loaded) {
    toast('请先上传或加载预设素材', 'error')
    return
  }
  if (demoState.processing) return
  demoState.processing = true
  hideResults()
  qs('#downloadAction').disabled = true
  qs('#startAction').classList.add('loading')
  qs('#startAction').textContent = cfg.loadingText
  qs('#processText').textContent = '正在处理音频并生成对比结果，完成后再展示核心指标...'
  let progress = 0
  const timer = setInterval(() => {
    progress += 6
    qs('#progressBar').style.width = `${Math.min(progress, 100)}%`
    if (progress >= 100) {
      clearInterval(timer)
      completeAction()
    }
  }, 210)
}

function downloadAction() {
  if (!demoState.completed) {
    toast('请先完成处理', 'error')
    return
  }
  const link = document.createElement('a')
  link.href = cfg.outputUrl
  link.download = cfg.outputName
  link.click()
  toast('已开始下载结果文件')
}

function oneClick() {
  loadPreset()
  setTimeout(startAction, 600)
}

document.addEventListener('DOMContentLoaded', () => {
  hideResults()
  qs('#uploadAudio')?.addEventListener('click', () => qs('#audioInput').click())
  qs('#audioInput')?.addEventListener('change', uploadAudio)
  qs('#presetAudio')?.addEventListener('click', loadPreset)
  qs('#startAction')?.addEventListener('click', startAction)
  qs('#downloadAction')?.addEventListener('click', downloadAction)
  document.querySelector('[data-demo]')?.addEventListener('click', oneClick)
})
