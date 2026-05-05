function renderHeader(active){
  document.write(`<header class="site-header"><div class="header-inner"><a class="brand" href="index.html"><span class="accent">Un</span>VoiceClone</a><nav class="main-nav"><a class="${active==='index'?'active':''}" href="index.html">主页</a><a class="${active==='function'?'active':''}" href="function.html">功能展示</a><a class="${active==='audio'?'active':''}" href="audio-defend.html">音频防御</a><a class="${active==='video'?'active':''}" href="video-defend.html">视频防御</a><a class="${active==='transform'?'active':''}" href="audio-transform.html">音频转换测试</a><a class="${active==='synthesis'?'active':''}" href="audio-synthesis.html">音频合成测试</a></nav></div></header>`)
}
function breadcrumb(current){
  document.write(`<div class="breadcrumb"><a href="index.html">主页</a> / ${current}</div>`)
}
