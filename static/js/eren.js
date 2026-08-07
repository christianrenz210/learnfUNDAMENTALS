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

  function pushMsg(role, content, extra) {
    var c = activeConvo();
    if (!c.title && role === 'user') {
      c.title = (content || '').trim().slice(0, 45);
    }
    var msg = { role: role, content: content };
    if (extra) {
      for (var k in extra) { if (Object.prototype.hasOwnProperty.call(extra, k)) msg[k] = extra[k]; }
    }
    c.messages.push(msg);
    if (c.messages.length > MAX_MSGS) c.messages = c.messages.slice(-MAX_MSGS);
    c.ts = Date.now();
    saveStore();
  }

  function processVideoEmbeds(text) {
    var tokens = [];

    // 1. YouTube iframe elements
    text = text.replace(/<iframe[^>]*src=["'](?:https?:)?\/\/(?:www\.)?youtube\.com\/embed\/([a-zA-Z0-9_-]+)["'][^>]*>(?:<\/iframe>)?/gi, function(match, id) {
      var token = '___VIDEO_EMBED_' + tokens.length + '___';
      var titleMatch = match.match(/title=["']([^"']+)["']/i);
      tokens.push({ id: id, title: titleMatch ? titleMatch[1] : 'Video Lesson' });
      return token;
    });

    // 2. Custom [video:ID:TITLE] or [video:ID] markers
    text = text.replace(/\[video:([a-zA-Z0-9_-]+)(?::([^\]]+))?\]/gi, function(match, id, title) {
      var token = '___VIDEO_EMBED_' + tokens.length + '___';
      tokens.push({ id: id, title: title || 'Video Lesson' });
      return token;
    });

    // 3. YouTube Embed or Watch or Short URLs
    text = text.replace(/https?:\/\/(?:www\.)?youtube\.com\/embed\/([a-zA-Z0-9_-]+)[^\s<]*/gi, function(match, id) {
      var token = '___VIDEO_EMBED_' + tokens.length + '___';
      tokens.push({ id: id, title: 'Video Lesson' });
      return token;
    });

    text = text.replace(/https?:\/\/(?:www\.)?youtube\.com\/watch\?v=([a-zA-Z0-9_-]+)[^\s<]*/gi, function(match, id) {
      var token = '___VIDEO_EMBED_' + tokens.length + '___';
      tokens.push({ id: id, title: 'Video Lesson' });
      return token;
    });

    text = text.replace(/https?:\/\/youtu\.be\/([a-zA-Z0-9_-]+)[^\s<]*/gi, function(match, id) {
      var token = '___VIDEO_EMBED_' + tokens.length + '___';
      tokens.push({ id: id, title: 'Video Lesson' });
      return token;
    });

    return { text: text, tokens: tokens };
  }

  function assistInline(s) {
    return s
      .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
      .replace(/`([^`]+)`/g, '<code>$1</code>');
  }

  function layoutAssistText(escaped) {
    var lines = escaped.split('\n');
    var out = [];
    var inList = false;
    function closeList() {
      if (inList) { out.push('</ul>'); inList = false; }
    }
    for (var i = 0; i < lines.length; i++) {
      var raw = lines[i];
      var trimmed = raw.trim();
      if (!trimmed) {
        closeList();
        out.push('<div class="assist-gap"></div>');
        continue;
      }
      var heading = trimmed.match(/^(#{1,6})\s+(.+)$/);
      if (heading) {
        closeList();
        var level = Math.min(heading[1].length + 3, 6);
        var hTitle = heading[2]
          .replace(/^Slide\s*\d+\s*[:.\u2013-]*\s*/i, '')
          .replace(/^Title\s*:\s*/i, '')
          .replace(/^\*+\s*/, '');
        out.push('<h' + level + ' class="assist-heading">' + assistInline(hTitle) + '</h' + level + '>');
        continue;
      }
      var slideNoHash = trimmed.match(/^Slide\s*\d+\s*[:\-.]\s+(.+)$/i);
      if (slideNoHash) {
        closeList();
        out.push('<h6 class="assist-heading">' + assistInline(slideNoHash[1]) + '</h6>');
        continue;
      }
      var bullet = trimmed.match(/^([\-\*\+])\s+(.+)$/);
      if (bullet) {
        if (!inList) { out.push('<ul class="assist-list">'); inList = true; }
        var itemText = bullet[2]
          .replace(/^Title\s*:\s*/i, '')
          .replace(/^Bullets?\s*:\s*/i, '');
        if (!itemText.trim()) continue;
        var indent = raw.length - raw.replace(/^\s+/, '').length;
        if (indent > 0) {
          out.push('<li class="assist-li-sub">' + assistInline(itemText) + '</li>');
        } else {
          out.push('<li>' + assistInline(itemText) + '</li>');
        }
        continue;
      }
      var numbered = trimmed.match(/^(\d+)[\.\)]\s+(.+)$/);
      if (numbered) {
        if (!inList) { out.push('<ul class="assist-list">'); inList = true; }
        out.push('<li><span class="assist-num">' + numbered[1] + '.</span> ' + assistInline(numbered[2]) + '</li>');
        continue;
      }
      closeList();
      out.push('<div class="assist-line">' + assistInline(trimmed) + '</div>');
    }
    closeList();
    return out.join('\n');
  }

  function appendAssistText(wrapper, txt) {
    var el = document.createElement('div');
    el.className = 'assist-text';

    var res = processVideoEmbeds(txt);
    var textWithTokens = res.text;
    var tokens = res.tokens;

    var html = textWithTokens
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');

    el.innerHTML = layoutAssistText(html);

    tokens.forEach(function(item, idx) {
      var token = '___VIDEO_EMBED_' + idx + '___';
      var embedHtml = '<div class="ratio ratio-16x9 my-2 rounded overflow-hidden shadow-sm">' +
        '<iframe src="https://www.youtube.com/embed/' + item.id + '" title="' + (item.title || 'Video Lesson') + '" allowfullscreen frameborder="0" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"></iframe>' +
        '</div>';
      el.innerHTML = el.innerHTML.replace(token, embedHtml);
    });

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
    var isOutput = langKey === 'output' || langKey === 'sample output';

    var card = document.createElement('div');
    card.className = 'assist-code-card' + (isOutput ? ' assist-code-output' : '');

    var head = document.createElement('div');
    head.className = 'assist-code-head';
    var label = document.createElement('span');
    label.className = 'assist-code-lang';
    label.textContent = isOutput ? 'Sample Output' : (runLang || langKey || 'code');
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

  function looksLikeSlides(text) {
    return /(^|\n)\s*#{1,6}\s+\S/.test(text) ||
      /\bSlide\s*\d+\s*[:.\-]?\s*\S+/i.test(text) ||
      /(^|\n)\s*Title\s*:/i.test(text);
  }

  function pptFileName(text) {
    var m = text.match(/^#{1,6}\s+(?:Slide\s*\d+\s*[:\-.\u2013]?\s*)?([^\n]+)/im) ||
      text.match(/\bSlide\s*\d+\s*[:\-.\u2013]\s*([^\n]+)/i) ||
      text.match(/^Title\s*:\s*(.+)$/im);
    var t = m ? m[1] : '';
    t = t.replace(/\*\*/g, '').replace(/`/g, '').replace(/[^\w\- ]+/g, '').trim();
    t = t.replace(/\s+/g, '-');
    return (t || 'presentation').slice(0, 60) + '.pptx';
  }

  function addPptButton(bubble, text) {
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'assist-ppt-btn';
    btn.innerHTML = '<i class="bi bi-file-ppt"></i> Download PPT';
    btn.addEventListener('click', function () {
      if (btn.dataset.busy === '1') return;
      btn.dataset.busy = '1';
      btn.disabled = true;
      btn.innerHTML = '<span class="spinner-border spinner-border-sm"></span>';
      fetch(urls.assistantPpt, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text })
      })
        .then(function (res) {
          if (!res.ok) return res.json().then(function (d) { throw new Error(d.error || 'Could not create the file.'); });
          return res.blob();
        })
        .then(function (blob) {
          var a = document.createElement('a');
          var objUrl = URL.createObjectURL(blob);
          a.href = objUrl;
          a.download = pptFileName(text);
          document.body.appendChild(a);
          a.click();
          document.body.removeChild(a);
          setTimeout(function () { URL.revokeObjectURL(objUrl); }, 2000);
          btn.dataset.busy = '';
          btn.disabled = false;
          btn.innerHTML = '<i class="bi bi-file-ppt"></i> Download PPT';
        })
        .catch(function (err) {
          btn.dataset.busy = '';
          btn.disabled = false;
          btn.innerHTML = '<i class="bi bi-file-ppt"></i> Download PPT';
          alert(err.message);
        });
    });
    return btn;
  }

  function addTxtButton(bubble, text) {
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'assist-ppt-btn';
    btn.innerHTML = '<i class="bi bi-file-earmark-text"></i> Download Summary (TXT)';
    btn.addEventListener('click', function () {
      var blob = new Blob([text], { type: 'text/plain;charset=utf-8' });
      var a = document.createElement('a');
      var objUrl = URL.createObjectURL(blob);
      a.href = objUrl;
      a.download = 'video-summary.txt';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      setTimeout(function () { URL.revokeObjectURL(objUrl); }, 2000);
    });
    return btn;
  }

  function renderBotContent(bubble, text, opts) {
    bubble.textContent = '';
    if (/```|<iframe|youtube\.com|youtu\.be|\[video:/.test(text)) {
      bubble.appendChild(buildReply(text));
    } else {
      var w = document.createElement('div');
      w.className = 'assist-reply';
      appendAssistText(w, text);
      bubble.appendChild(w);
    }
    if (opts && opts.yt) {
      var bar = document.createElement('div');
      bar.className = 'assist-ppt-bar';
      bar.appendChild(addTxtButton(bubble, text));
      bubble.appendChild(bar);
    } else if (urls.assistantPpt && looksLikeSlides(text)) {
      var bar2 = document.createElement('div');
      bar2.className = 'assist-ppt-bar';
      bar2.appendChild(addPptButton(bubble, text));
      bubble.appendChild(bar2);
    }
    msgsEl.scrollTop = msgsEl.scrollHeight;
  }

  function addBubble(content, isUser, opts) {
    var bubble = document.createElement('div');
    bubble.className = 'assist-bubble ' + (isUser ? 'assist-user' : 'assist-bot');
    msgsEl.appendChild(bubble);
    if (isUser) {
      if (opts && opts.image) {
        var img = document.createElement('img');
        img.className = 'assist-user-img';
        img.src = opts.image;
        img.alt = 'Attached image';
        bubble.appendChild(img);
      }
      if (content) bubble.appendChild(document.createTextNode(content));
    } else {
      renderBotContent(bubble, content, opts);
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

  function finishTypingBubble(bubble, text, opts) {
    bubble.classList.remove('assist-typing');
    if (/```|<iframe|youtube\.com|youtu\.be|\[video:/.test(text)) {
      renderBotContent(bubble, text, opts);
      return;
    }
    var i = 0;
    var timer = setInterval(function () {
      i += 3;
      if (i >= text.length) {
        clearInterval(timer);
        renderBotContent(bubble, text, opts);
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
        addBubble(m.content || '', m.role === 'user', m);
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

  var pendingImage = null;
  var imageInputEl = document.getElementById('assistImageInput');
  var imageBtn = document.getElementById('assistImageBtn');
  var imagePreview = document.getElementById('assistImagePreview');
  var imageThumb = document.getElementById('assistImageThumb');
  var imageClear = document.getElementById('assistImageClear');

  function clearPendingImage() {
    pendingImage = null;
    if (imagePreview) imagePreview.classList.add('d-none');
    if (imageInputEl) imageInputEl.value = '';
  }

  function setPendingImage(dataUrl) {
    pendingImage = dataUrl;
    if (imagePreview && imageThumb) {
      imageThumb.src = dataUrl;
      imagePreview.classList.remove('d-none');
    }
  }

  function handleImageFile(file) {
    if (!file || !/^image\/(png|jpe?g|webp|gif)$/i.test(file.type)) {
      alert('Please attach a PNG, JPEG, WEBP, or GIF image.');
      return;
    }
    if (file.size > 6 * 1024 * 1024) {
      alert('Image is too large. Please use one under 6 MB.');
      return;
    }
    var reader = new FileReader();
    reader.onload = function () { downscaleImage(reader.result, setPendingImage); };
    reader.onerror = function () { alert('Could not read that image.'); };
    reader.readAsDataURL(file);
  }

  function downscaleImage(dataUrl, done) {
    var img = new Image();
    img.onload = function () {
      var MAX = 1400;
      var scale = Math.min(1, MAX / Math.max(img.width, img.height));
      if (scale >= 1) { done(dataUrl); return; }
      var canvas = document.createElement('canvas');
      canvas.width = Math.round(img.width * scale);
      canvas.height = Math.round(img.height * scale);
      var ctx = canvas.getContext('2d');
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      done(canvas.toDataURL('image/jpeg', 0.85));
    };
    img.onerror = function () { done(dataUrl); };
    img.src = dataUrl;
  }

  if (imageBtn && imageInputEl) {
    imageBtn.addEventListener('click', function () {
      var proModalEl = document.getElementById('proModal');
      if (proModalEl && window.bootstrap) {
        new bootstrap.Modal(proModalEl).show();
      } else {
        imageInputEl.click();
      }
    });
    imageBtn.addEventListener('mouseenter', function () {
      imageBtn.setAttribute('title', 'Pro feature (locked)');
    });
    imageInputEl.addEventListener('change', function () { handleImageFile(imageInputEl.files && imageInputEl.files[0]); });
  }
  if (imageClear) imageClear.addEventListener('click', clearPendingImage);

  var proUpgradeBtn = document.getElementById('proUpgradeBtn');
  if (proUpgradeBtn) {
    proUpgradeBtn.addEventListener('click', function () {
      var proModalEl = document.getElementById('proModal');
      if (proModalEl && window.bootstrap) {
        bootstrap.Modal.getOrCreateInstance(proModalEl).hide();
      }
      if (imageInputEl) imageInputEl.click();
    });
  }

  function sendMessage(message) {
    var image = pendingImage;
    clearPendingImage();
    pushMsg('user', message, image ? { image: image } : null);
    renderHistoryList();
    if (inputEl) inputEl.value = '';

    var userExtra = image ? { image: image } : null;
    addBubble(message, true, userExtra);

    var started = Date.now();
    var convo = activeConvo();
    var history = (convo.messages || []).slice(0, -1).map(function (m) {
      return { role: m.role === 'user' ? 'user' : 'assistant', content: m.content };
    });

    fetch(urls.assistant, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: message, history: history, image: image })
    })
      .then(function (res) { return res.json(); })
      .then(function (data) {
        var reply = data.ok ? data.reply : (data.error || 'Something went wrong.');
        var opts = (data.ok && data.yt_summary) ? { yt: true } : null;
        pushMsg('assistant', reply, opts);
        renderHistoryList();
        var elapsed = Date.now() - started;
        setTimeout(function () {
          var typing = addTypingBubble();
          setTimeout(function () { finishTypingBubble(typing, reply, opts); }, 900);
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

  if (window.visualViewport && document.querySelector('.assist-layout')) {
    var layoutEl = document.querySelector('.assist-layout');
    var lastLayoutH = 0;
    function syncLayoutHeight() {
      var h = window.visualViewport.height;
      if (Math.abs(h - lastLayoutH) > 1) {
        lastLayoutH = h;
        layoutEl.style.height = h + 'px';
      }
    }
    window.visualViewport.addEventListener('resize', syncLayoutHeight);
    window.visualViewport.addEventListener('scroll', syncLayoutHeight);
    syncLayoutHeight();
  }

  renderMessages(activeConvo());
})();
