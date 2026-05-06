function renderHeader(active){
  document.write(`<header class="site-header"><div class="header-inner"><a class="brand macaron-brand" href="index.html">用声无恙<span class="sound-mark">≋</span></a><nav class="main-nav"><a class="${active==='index'?'active':''}" href="index.html">首页</a><a href="index.html#tech">核心技术</a><a href="index.html#features">系统功能</a><a href="index.html#results">测试成果</a><a href="index.html#future">应用前景</a></nav><a class="nav-cta" href="auth.html">立即体验</a></div></header>`)
}
function breadcrumb(current){
  document.write(`<div class="breadcrumb"><a href="index.html">首页</a> / ${current}</div>`)
}
