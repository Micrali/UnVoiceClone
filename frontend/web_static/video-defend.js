const demoVideo = {
  name: 'interview_clip_demo.mp4',
  duration: '15s',
  size: '18.6 MB',
  type: 'MP4',
  originalUrl: 'interview_clip_demo.mp4',
  defendedUrl: 'interview_clip_demo.mp4'
}

const state = { fileLoaded: true, processing: false, completed: false, currentFileName: demoVideo.name, customUrl: '' }

function $(selector) {
  return document.querySelector(selector)
}

function showToast(message, type = 'success') {
  const toast = $('#toast')
  if (!toast) return
  toast.textContent = message
  toast.className = `toast show ${type}`
  setTimeout(() => { toast.className = 'toast' }, 2200)
}

function hideDefenseResults() {
  $('#timelinePanel')?.classList.add('hidden')
  $('#metricGrid')?.classList.add('hidden')
  $('#result')?.classList.add('hidden')
}

function showDefenseResults() {
  $('#timelinePanel')?.classList.remove('hidden')
  $('#metricGrid')?.classList.remove('hidden')
  $('#result')?.classList.remove('hidden')
}

function updateFileInfo(name, duration, format, size) {
  const info = $('#fileInfo')
  if (!info) return
  info.textContent = `当前文件：${name}　输入视频总时长：${duration}　格式：${format}　大小：${size}`
}

function resetProcessingState() {
  state.processing = false
  state.completed = false
  hideDefenseResults()
  $('#downloadVideo').disabled = true
  $('#startDefense').classList.remove('loading')
  $('#startDefense').textContent = '开始防御'
  $('#progressBar').style.width = '0%'
  $('#processText').textContent = '视频已加载，可开始防御。防御完成后会展示人声时间轴、核心指标卡和风险下降结果。'
}

function loadPresetVideo() {
  const original = $('#originalVideo')
  const defended = $('#defendedVideo')
  state.fileLoaded = true
  state.currentFileName = demoVideo.name
  updateFileInfo(demoVideo.name, demoVideo.duration, demoVideo.type, demoVideo.size)
  resetProcessingState()

  if (original) {
    original.classList.add('is-visible')
    original.src = demoVideo.originalUrl
    original.load()
  }
  if (defended) {
    defended.classList.remove('is-visible')
    defended.removeAttribute('src')
    defended.load()
  }
  showToast('预设视频已加载，可直接预览')
}

function handleUpload(event) {
  const file = event.target.files && event.target.files[0]
  if (!file) return
  if (!file.type.startsWith('video/')) {
    showToast('请上传 MP4/WebM/Ogg 视频文件', 'error')
    return
  }
  if (state.customUrl) URL.revokeObjectURL(state.customUrl)
  state.customUrl = URL.createObjectURL(file)
  const original = $('#originalVideo')
  state.fileLoaded = true
  state.currentFileName = file.name
  updateFileInfo(file.name, '待识别', (file.type || 'video/mp4').split('/').pop().toUpperCase(), `${(file.size / 1024 / 1024).toFixed(1)} MB`)
  resetProcessingState()

  if (original) {
    original.classList.add('is-visible')
    original.src = state.customUrl
    original.load()
  }
  const defended = $('#defendedVideo')
  if (defended) {
    defended.classList.remove('is-visible')
    defended.removeAttribute('src')
    defended.load()
  }
  showToast('文件上传成功，已加载到原始视频播放器')
}

function completeDefense() {
  state.processing = false
  state.completed = true
  const start = $('#startDefense')
  const download = $('#downloadVideo')
  const text = $('#processText')
  const result = $('#result')
  start.classList.remove('loading')
  start.textContent = '防御完成'
  download.disabled = false
  text.textContent = '视频防御完成，已生成人声识别时间轴和风险对比结果。'
  showDefenseResults()
  if (result) {
    result.innerHTML = '<div class="result-kicker">视频防御结果</div><h3>已完成 15 秒演示视频声纹防护</h3><p>系统完成 3 段人声定位与 8.7s 定向处理，克隆风险已从 98% 明显压降至 21.8%。</p>'
  }
  const defended = $('#defendedVideo')
  const original = $('#originalVideo')
  if (defended) {
    defended.classList.add('is-visible')
    defended.src = state.customUrl || demoVideo.originalUrl
    defended.load()
    if (original) defended.currentTime = original.currentTime
  }
  showToast('防御处理完成，可预览并下载结果')
}

function startDefense() {
  if (!state.fileLoaded) {
    showToast('请先上传或加载 15 秒演示视频', 'error')
    return
  }
  if (state.processing) return
  state.processing = true
  state.completed = false
  hideDefenseResults()
  const start = $('#startDefense')
  const download = $('#downloadVideo')
  const bar = $('#progressBar')
  const text = $('#processText')
  start.classList.add('loading')
  start.textContent = '防御处理中...'
  download.disabled = true
  bar.style.width = '0%'
  text.textContent = '正在执行人声定位、匿名化扰动与风险抑制，结果卡片将在处理完成后展示...'
  let progress = 0
  const timer = setInterval(() => {
    progress += 5
    bar.style.width = `${Math.min(progress, 100)}%`
    if (progress >= 100) {
      clearInterval(timer)
      completeDefense()
    }
  }, 435)
}

function downloadDefendedVideo() {
  if (!state.completed) {
    showToast('请先完成防御处理', 'error')
    return
  }
  const link = document.createElement('a')
  link.href = demoVideo.defendedUrl
  link.download = 'unvc_defended_interview_clip_demo.mp4'
  link.click()
  showToast('已开始下载防御后视频')
}

function oneClickDemo() {
  loadPresetVideo()
  showToast('一键演示已启动：加载素材 → 启动防御 → 展示结果')
  setTimeout(startDefense, 700)
}

function syncPlayers() {
  const original = $('#originalVideo')
  const defended = $('#defendedVideo')
  if (!original || !defended) return
  original.addEventListener('play', () => { if (defended.src) defended.play().catch(() => {}) })
  original.addEventListener('pause', () => defended.pause())
  original.addEventListener('seeked', () => { defended.currentTime = original.currentTime })
}

document.addEventListener('DOMContentLoaded', () => {
  $('#uploadBtn')?.addEventListener('click', () => $('#videoInput').click())
  $('#videoInput')?.addEventListener('change', handleUpload)
  $('#loadPresetBtn')?.addEventListener('click', loadPresetVideo)
  $('#startDefense')?.addEventListener('click', startDefense)
  $('#downloadVideo')?.addEventListener('click', downloadDefendedVideo)
  $('#oneClickDemo')?.addEventListener('click', oneClickDemo)
  syncPlayers()
  hideDefenseResults()
})
