/* app.js · 追星护卫队前端逻辑 */

// ── 状态 ──────────────────────────────────────────────────────
const state = {
  mode:       'paste',     // 'paste' | 'template'
  attackType: null,
  style:      'mixed',
  field:      'idol',
};

// ── DOM 引用 ───────────────────────────────────────────────────
const $ = id => document.getElementById(id);
const pasteContent  = $('pasteContent');
const charCount     = $('charCount');
const idolName      = $('idolName');
const generateBtn   = $('generateBtn');
const btnText       = $('btnText');
const btnLoading    = $('btnLoading');
const results       = $('results');
const repliesList   = $('repliesList');
const inputSummary  = $('inputSummary');
const historyList   = $('historyList');
const historySection= $('historySection');
const toast         = $('toast');

// ── 字符计数 ───────────────────────────────────────────────────
pasteContent.addEventListener('input', () => {
  charCount.textContent = pasteContent.value.length;
});

// ── 模式切换 ───────────────────────────────────────────────────
function switchMode(mode) {
  state.mode = mode;
  $('panelPaste').classList.toggle('hidden', mode !== 'paste');
  $('panelTemplate').classList.toggle('hidden', mode !== 'template');
  $('btnPaste').classList.toggle('active', mode === 'paste');
  $('btnTemplate').classList.toggle('active', mode === 'template');
}

// ── Pill / Tag 通用激活 ────────────────────────────────────────
function activatePill(group, clicked) {
  group.forEach(el => el.classList.remove('active'));
  clicked.classList.add('active');
}

// 偶像领域
document.querySelectorAll('.pill[data-field]').forEach(btn => {
  btn.addEventListener('click', () => {
    state.field = btn.dataset.field;
    activatePill(document.querySelectorAll('.pill[data-field]'), btn);
  });
});

// 攻击类型
document.querySelectorAll('.attack-tag').forEach(btn => {
  btn.addEventListener('click', () => {
    state.attackType = btn.dataset.type;
    activatePill(document.querySelectorAll('.attack-tag'), btn);
  });
});

// 回复风格
document.querySelectorAll('.style-pill').forEach(btn => {
  btn.addEventListener('click', () => {
    state.style = btn.dataset.style;
    activatePill(document.querySelectorAll('.style-pill'), btn);
  });
});

// ── 生成回复 ───────────────────────────────────────────────────
async function generate() {
  // 验证
  if (state.mode === 'paste' && !pasteContent.value.trim()) {
    showToast('请先粘贴黑粉的话 📋');
    return;
  }
  if (state.mode === 'template' && !state.attackType) {
    showToast('请选择攻击类型 🎯');
    return;
  }

  // UI 进入 loading
  setLoading(true);
  results.classList.add('hidden');

  const body = {
    mode:        state.mode,
    content:     state.mode === 'paste' ? pasteContent.value.trim() : null,
    attack_type: state.mode === 'template' ? state.attackType : null,
    idol_name:   idolName.value.trim() || null,
    idol_field:  state.field,
    style:       state.style,
  };

  try {
    const res = await fetch('/api/generate', {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body:    JSON.stringify(body),
    });

    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      throw new Error(err.detail || `HTTP ${res.status}`);
    }

    const data = await res.json();
    renderReplies(data.replies, data.input_summary);
    saveHistory(data.replies, data.input_summary);

  } catch (e) {
    showToast('生成失败：' + e.message);
  } finally {
    setLoading(false);
  }
}

// ── 渲染结果 ───────────────────────────────────────────────────
function renderReplies(replies, summary) {
  repliesList.innerHTML = '';
  inputSummary.textContent = summary ? `针对：「${summary}」` : '';

  replies.forEach(r => {
    const card = document.createElement('div');
    card.className = 'reply-card';
    card.innerHTML = `
      <div class="reply-meta">
        <span class="reply-style">${r.style}</span>
        <span class="reply-emoji">${r.emoji || '✨'}</span>
      </div>
      <div class="reply-text">${escHtml(r.text)}</div>
      <button class="copy-btn" onclick="copyText(this, ${JSON.stringify(r.text)})">
        📋 复制这条
      </button>`;
    repliesList.appendChild(card);
  });

  results.classList.remove('hidden');
  results.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// ── 复制 ───────────────────────────────────────────────────────
async function copyText(btn, text) {
  try {
    await navigator.clipboard.writeText(text);
    btn.textContent = '✅ 已复制！';
    btn.classList.add('copied');
    setTimeout(() => {
      btn.textContent = '📋 复制这条';
      btn.classList.remove('copied');
    }, 2000);
    showToast('复制成功，去微博战斗吧！⚡');
  } catch {
    showToast('复制失败，请手动长按选取');
  }
}

// ── 历史记录 ───────────────────────────────────────────────────
const HISTORY_KEY = 'fandom_guard_history';

function saveHistory(replies, summary) {
  const raw = localStorage.getItem(HISTORY_KEY);
  const list = raw ? JSON.parse(raw) : [];
  list.unshift({
    summary: summary || '生成结果',
    preview: replies[0]?.text.slice(0, 40) + '…',
    time:    new Date().toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit' }),
    replies,
  });
  const trimmed = list.slice(0, 20);
  localStorage.setItem(HISTORY_KEY, JSON.stringify(trimmed));
  renderHistory();
}

function renderHistory() {
  const raw = localStorage.getItem(HISTORY_KEY);
  const list = raw ? JSON.parse(raw) : [];
  if (!list.length) {
    historyList.innerHTML = '<div class="history-empty">暂无记录</div>';
    return;
  }
  historyList.innerHTML = list.map((item, i) => `
    <div class="history-item" onclick="loadHistory(${i})">
      <div class="history-item-text">
        <span style="color:var(--text3);font-size:10px;">${item.summary}</span><br>
        ${escHtml(item.preview)}
      </div>
      <div class="history-item-time">${item.time}</div>
    </div>`).join('');
}

function loadHistory(i) {
  const raw = localStorage.getItem(HISTORY_KEY);
  const list = raw ? JSON.parse(raw) : [];
  if (!list[i]) return;
  renderReplies(list[i].replies, list[i].summary);
}

function clearHistory() {
  localStorage.removeItem(HISTORY_KEY);
  renderHistory();
  showToast('记录已清除');
}

// ── Loading 状态 ───────────────────────────────────────────────
function setLoading(on) {
  generateBtn.disabled = on;
  btnText.classList.toggle('hidden', on);
  btnLoading.classList.toggle('hidden', !on);
}

// ── Toast ──────────────────────────────────────────────────────
let toastTimer;
function showToast(msg) {
  toast.textContent = msg;
  toast.classList.remove('hidden');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => toast.classList.add('hidden'), 2500);
}

// ── 工具 ───────────────────────────────────────────────────────
function escHtml(s) {
  return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

// ── 初始化 ─────────────────────────────────────────────────────
renderHistory();
