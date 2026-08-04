(function () {
  'use strict';

  var cfg = window.EREN || {};
  var msgsEl = document.getElementById('assistMessages');
  var formEl = document.getElementById('assistForm');
  var inputEl = document.getElementById('assistInput');
  if (!msgsEl || !formEl || !inputEl) return;

  var isFullPage = msgsEl.classList.contains('assist-page-messages');

  var urls = cfg.urls || {};
  var RUN_LANGS = {
    python: 'python', py: 'python', python3: 'python',
    cpp: 'cpp', c: 'cpp', 'c++': 'cpp', cplusplus: 'cpp',
    java: 'java'
  };
  var STORAGE_KEY = 'cfConvos_' + (cfg.username || 'guest');
  var MAX_CONVOS = 20;
  var MAX_MSGS = 20;

  var store = loadStore();
  if (!Array.isArray(store.convos)) store.convos = [];

  function loadStore() {
    try {
      var d = JSON.parse(localStorage.getItem(STORAGE_KEY) || 'null');
      if (d && typeof d === 'object') return d;
    } catch (e) {}
    return { active: null, convos: [] };
  }

  function saveStore() {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(store)); } catch (e) {}
  }

  function createConvo() {
    var c = {
      id: Date.now().toString(36) + Math.random().toString(36).slice(2, 6),
      title: '',
      messages: [],
      ts: Date.now()
    };
    store.convos.unshift(c);
    if (store.convos.length > MAX_CONVOS) store.convos.pop();
    store.active = c.id;
    saveStore();
    return c;
  }

  function activeConvo() {
    for (var i = 0; i < store.convos.length; i++) {
      if (store.convos[i].id === store.active) return store.convos[i];
    }
    return createConvo();
  }

  function pushMsg(role, content) {
    var c = activeConvo();
    if (!c.title && role === 'user') {
      c.title = (content || '').trim().slice(0, 45);
    }
    c.messages.push({ role: role, content: content });
    if (c.messages.length > MAX_MSGS) c.messages = c.messages.slice(-MAX_MSGS);
    c.ts = Date.now();
    saveStore();
  }

  function appendAssistText(wrapper, txt) {
    var el = document.createElement('div');
    el.className = 'assist-text';
    var html = txt
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');
    html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/`([^`]+)`/g, '<code>$1</code>');
    el.innerHTML = html;
    wrapper.appendChild(el);
  }

  function appendAssistTerm(card, text) {
    var out = card.querySelector('.assist-terminal-out');
    out.textContent = out.textContent ? out.textContent + '\n' + text : text;
    card.querySelector('.assist-terminal').scrollTop = card.querySelector('.assist-terminal').scrollHeight;
  }

  function runAssistCode(card, lang, code) {
    var runBtn = card.querySelector('.assist-code-run');
    var term = card.querySelector('.assist-terminal');
    var status = card.querySelector('.assist-code-status');
    if (!runBtn || runBtn.dataset.running === '1') return;
    runBtn.dataset.running = '1';
    runBtn.disabled = true;
    runBtn.innerHTML = '<span class="spinner-border spinner-border-sm"></span>';
    term.classList.remove('d-none');
    card.querySelector('.assist-terminal-out').textContent = '';
    status.textContent = '';
    var sessionId = null;
    var pollTimer = null;

    function finish(exitCode) {
      if (pollTimer) { clearInterval(pollTimer); pollTimer = null; }
      runBtn.dataset.running = '';
      runBtn.disabled = false;
      runBtn.textContent = 'Run';
      status.textContent = 'Finished (exit ' + exitCode + ')';
    }

    function renderEvents(events) {
      (events || []).forEach(function (item) {
        if (item.type === 'out' || item.type === 'err' || item.type === 'error') {
          appendAssistTerm(card, item.data);
        }
      });
    }

    function poll() {
      pollTimer = setInterval(function () {
        fetch((urls.runPoll || '').replace('SID', sessionId), {
          method: 'POST',
          cache: 'no-store'
        })
          .then(function (res) { return res.json(); })
          .then(function (data) {
            if (!data.ok) {
              appendAssistTerm(card, data.error || 'Session lost.');
              finish(-1);
              return;
            }
            renderEvents(data.events);
            if (data.finished) finish(data.exit_code);
          })
          .catch(function () {});
      }, 400);
    }

    fetch(urls.runStart, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ language: lang, code: code, stdin: '' })
    })
      .then(function (res) { return res.json(); })
      .then(function (data) {
        if (!data.ok) {
          appendAssistTerm(card, data.compile_error || data.error || 'Could not start the program.');
          finish(-1);
          return;
        }
        if (data.finished) {
          renderEvents(data.events);
          finish(data.exit_code);
          return;
        }
        sessionId = data.session_id;
        poll();
      })
      .catch(function () {
        appendAssistTerm(card, 'Could not reach the server. Try again.');
        finish(-1);
      });
  }

  function appendAssistCode(wrapper, lang, code) {
    var langKey = (lang || '').toLowerCase().trim();
    var runLang = RUN_LANGS[langKey] || null;

    var card = document.createElement('div');
    card.className = 'assist-code-card';

    var head = document.createElement('div');
    head.className = 'assist-code-head';
    var label = document.createElement('span');
    label.className = 'assist-code-lang';
    label.textContent = runLang || langKey || 'code';
    head.appendChild(label);

    var actions = document.createElement('div');
    actions.className = 'assist-code-actions';
    if (runLang) {
      var openBtn = document.createElement('button');
      openBtn.type = 'button';
      openBtn.className = 'assist-code-btn';
      openBtn.textContent = 'Open in Compiler';
      openBtn.addEventListener('click', function () {
        try {
          sessionStorage.setItem('cfCompilerCode', JSON.stringify({ lang: runLang, code: code }));
        } catch (e) {}
        window.location.href = urls.compiler;
      });
      actions.appendChild(openBtn);

      var runBtn = document.createElement('button');
      runBtn.type = 'button';
      runBtn.className = 'assist-code-btn assist-code-run';
      runBtn.textContent = 'Run';
      runBtn.addEventListener('click', function () {
        runAssistCode(card, runLang, code);
      });
      actions.appendChild(runBtn);
    }
    head.appendChild(actions);
    card.appendChild(head);

    var pre = document.createElement('pre');
    pre.className = 'assist-code';
    var codeEl = document.createElement('code');
    codeEl.textContent = code.replace(/\n$/, '');
    pre.appendChild(codeEl);
    card.appendChild(pre);

    var term = document.createElement('pre');
    term.className = 'assist-terminal d-none';
    var termOut = document.createElement('code');
    termOut.className = 'assist-terminal-out';
    term.appendChild(termOut);
    card.appendChild(term);

    var status = document.createElement('div');
    status.className = 'assist-code-status';
    card.appendChild(status);

    wrapper.appendChild(card);
  }

  function buildReply(text) {
    var wrapper = document.createElement('div');
    wrapper.className = 'assist-reply';
    var regex = /```([\w-+]*)\s*\n?([\s\S]*?)```/g;
    var last = 0;
    var m;
    while ((m = regex.exec(text)) !== null) {
      if (m.index > last) appendAssistText(wrapper, text.slice(last, m.index));
      appendAssistCode(wrapper, m[1], m[2]);
      last = regex.lastIndex;
    }
    if (last < text.length) appendAssistText(wrapper, text.slice(last));
    return wrapper;
  }

  function renderBotContent(bubble, text) {
    bubble.textContent = '';
    if (/```/.test(text)) {
      bubble.appendChild(buildReply(text));
    } else {
      bubble.textContent = text;
    }
    msgsEl.scrollTop = msgsEl.scrollHeight;
  }

  function addBubble(content, isUser) {
    var bubble = document.createElement('div');
    bubble.className = 'assist-bubble ' + (isUser ? 'assist-user' : 'assist-bot');
    msgsEl.appendChild(bubble);
    if (isUser) {
      bubble.textContent = content;
    } else {
      renderBotContent(bubble, content);
    }
    msgsEl.scrollTop = msgsEl.scrollHeight;
    return bubble;
  }

  function addTypingBubble() {
    var bubble = document.createElement('div');
    bubble.className = 'assist-bubble assist-bot assist-typing';
    bubble.innerHTML = '<span></span><span></span><span></span>';
    msgsEl.appendChild(bubble);
    msgsEl.scrollTop = msgsEl.scrollHeight;
    return bubble;
  }

  function finishTypingBubble(bubble, text) {
    bubble.classList.remove('assist-typing');
    if (/```/.test(text)) {
      renderBotContent(bubble, text);
      return;
    }
    var i = 0;
    var timer = setInterval(function () {
      i += 3;
      if (i >= text.length) {
        clearInterval(timer);
        bubble.textContent = text;
      } else {
        bubble.textContent = text.slice(0, i);
      }
      msgsEl.scrollTop = msgsEl.scrollHeight;
    }, 20);
  }

  function greetingText() {
    if (cfg.greeting) return cfg.greeting;
    var name = cfg.username || 'there';
    return "Hi " + name + "! I'm E.R.E.N \u2014 Educational Response Engine for " +
      "Novices. A long time ago, a frustrated student stayed up until 2 AM to " +
      "build me so no one would get stuck on the same lessons. You've completed " +
      (cfg.userDone || 0) + " of " + (cfg.userTotal || 0) +
      " lessons so far. Ask me anything!";
  }

  function renderMessages(convo) {
    msgsEl.textContent = '';
    var msgs = (convo && convo.messages) || [];
    if (!msgs.length) {
      var g = document.createElement('div');
      g.className = 'assist-bubble assist-bot';
      g.textContent = greetingText();
      msgsEl.appendChild(g);
    } else {
      msgs.forEach(function (m) {
        addBubble(m.content || '', m.role === 'user');
      });
    }
    msgsEl.scrollTop = msgsEl.scrollHeight;
  }

  function newChat() {
    createConvo();
    renderMessages(activeConvo());
    closeSidebarMobile();
    if (inputEl) inputEl.focus();
  }

  function loadConvo(id) {
    for (var i = 0; i < store.convos.length; i++) {
      if (store.convos[i].id === id) {
        store.active = id;
        saveStore();
        renderMessages(store.convos[i]);
        break;
      }
    }
    closeSidebarMobile();
  }

  function deleteConvo(id, evt) {
    if (evt) evt.stopPropagation();
    store.convos = store.convos.filter(function (c) { return c.id !== id; });
    if (store.active === id) store.active = null;
    saveStore();
    renderHistoryList();
    if (store.active === null) renderMessages(activeConvo());
  }

  function timeLabel(ts) {
    try {
      var d = new Date(ts);
      var now = new Date();
      var sameDay = d.toDateString() === now.toDateString();
      var opts = sameDay ? { hour: 'numeric', minute: '2-digit' } : { month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit' };
      return d.toLocaleString(undefined, opts);
    } catch (e) {
      return '';
    }
  }

  function renderHistoryList() {
    var listEl = document.getElementById('assistHistoryList');
    if (!listEl) return;
    listEl.textContent = '';
    if (!store.convos.length) {
      var empty = document.createElement('div');
      empty.className = 'assist-history-empty';
      empty.textContent = 'No conversations yet.';
      listEl.appendChild(empty);
      return;
    }
    store.convos.forEach(function (c) {
      var item = document.createElement('div');
      item.className = 'assist-history-item';
      if (c.id === store.active) item.className += ' assist-history-active';

      var main = document.createElement('button');
      main.type = 'button';
      main.className = 'assist-history-main';
      var title = document.createElement('div');
      title.className = 'assist-history-title';
      title.textContent = c.title || 'New chat';
      var meta = document.createElement('div');
      meta.className = 'assist-history-meta';
      meta.textContent = c.messages.length + ' message(s) · ' + timeLabel(c.ts);
      main.appendChild(title);
      main.appendChild(meta);
      main.addEventListener('click', function () { loadConvo(c.id); });

      var del = document.createElement('button');
      del.type = 'button';
      del.className = 'assist-history-del';
      del.setAttribute('aria-label', 'Delete conversation');
      del.innerHTML = '<i class="bi bi-trash"></i>';
      del.addEventListener('click', function (e) { deleteConvo(c.id, e); });

      item.appendChild(main);
      item.appendChild(del);
      listEl.appendChild(item);
    });
  }

  var sidebarEl = document.getElementById('assistSidebar');
  var sidebarBackdrop = null;

  function openSidebarMobile() {
    if (!sidebarEl) return;
    renderHistoryList();
    sidebarEl.classList.add('open');
    if (!sidebarBackdrop) {
      sidebarBackdrop = document.createElement('div');
      sidebarBackdrop.className = 'assist-sidebar-backdrop';
      sidebarBackdrop.addEventListener('click', closeSidebarMobile);
      sidebarEl.parentNode.insertBefore(sidebarBackdrop, sidebarEl.nextSibling);
    }
    sidebarBackdrop.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeSidebarMobile() {
    if (!sidebarEl) return;
    sidebarEl.classList.remove('open');
    if (sidebarBackdrop) sidebarBackdrop.classList.remove('open');
    document.body.style.overflow = '';
  }

  function sendMessage(message) {
    pushMsg('user', message);
    renderHistoryList();
    if (inputEl) inputEl.value = '';
    addBubble(message, true);

    var started = Date.now();
    var convo = activeConvo();
    var history = (convo.messages || []).slice(0, -1).map(function (m) {
      return { role: m.role === 'user' ? 'user' : 'assistant', content: m.content };
    });

    fetch(urls.assistant, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: message, history: history })
    })
      .then(function (res) { return res.json(); })
      .then(function (data) {
        var reply = data.ok ? data.reply : (data.error || 'Something went wrong.');
        pushMsg('assistant', reply);
        renderHistoryList();
        var elapsed = Date.now() - started;
        setTimeout(function () {
          var typing = addTypingBubble();
          setTimeout(function () { finishTypingBubble(typing, reply); }, 900);
        }, Math.max(0, 450 - elapsed));
      })
      .catch(function () {
        var reply = 'I could not reach the server. Please try again.';
        pushMsg('assistant', reply);
        renderHistoryList();
        var typing = addTypingBubble();
        setTimeout(function () { finishTypingBubble(typing, reply); }, 900);
      });
  }

  if (formEl) {
    formEl.addEventListener('submit', function (e) {
      e.preventDefault();
      var message = (inputEl.value || '').trim();
      if (!message) return;
      sendMessage(message);
    });
  }
  if (inputEl) {
    inputEl.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        formEl.dispatchEvent(new Event('submit', { cancelable: true }));
      }
    });
  }

  var newChatBtn = document.getElementById('assistNewChat');
  if (newChatBtn) newChatBtn.addEventListener('click', newChat);

  var sidebarOpenBtn = document.getElementById('assistSidebarOpen');
  if (sidebarOpenBtn) sidebarOpenBtn.addEventListener('click', openSidebarMobile);

  var sidebarCloseBtn = document.getElementById('assistSidebarClose');
  if (sidebarCloseBtn) sidebarCloseBtn.addEventListener('click', closeSidebarMobile);

  var historyBtn = document.getElementById('assistHistoryBtn');
  var historyPanel = document.getElementById('assistHistoryPanel');
  if (historyBtn && historyPanel) {
    historyBtn.addEventListener('click', function () {
      renderHistoryList();
      historyPanel.classList.toggle('d-none');
    });
  }

  var clearBtn = document.getElementById('assistClearHistory');
  if (clearBtn) {
    clearBtn.addEventListener('click', function () {
      store.convos = [];
      store.active = null;
      saveStore();
      renderHistoryList();
      renderMessages(activeConvo());
      closeSidebarMobile();
    });
  }

  document.querySelectorAll('.assist-chip').forEach(function (chip) {
    chip.addEventListener('click', function () {
      var q = this.dataset.q;
      if (!q) return;
      sendMessage(q);
    });
  });

  var aboutBtn = document.getElementById('assistAbout');
  var aboutModal = document.getElementById('erenModal');
  if (aboutBtn && aboutModal && window.bootstrap) {
    aboutBtn.addEventListener('click', function () {
      new bootstrap.Modal(aboutModal).show();
    });
  }

  if (!isFullPage) {
    var closeBtn = document.getElementById('assistClose');
    var panelEl = document.getElementById('assistPanel');
    if (closeBtn && panelEl) {
      closeBtn.addEventListener('click', function () { panelEl.classList.add('d-none'); });
    }

    var toggleBtn = document.getElementById('assistToggle');
    if (toggleBtn && panelEl) {
      toggleBtn.addEventListener('click', function () {
        panelEl.classList.toggle('d-none');
        if (!panelEl.classList.contains('d-none')) inputEl.focus();
      });
    }
  }

  renderMessages(activeConvo());
})();
