(function () {
  'use strict';

  var STORAGE_KEY = 'cfMusicPrefs';

  var STATIONS = [
    { id: 'jfKfPfyJRdk', name: 'Lo-Fi Beats', icon: 'bi-music-note-beamed', hint: 'lofi hip hop · study' },
    { id: 'E2vONfzoyRI', name: 'Jazz Lo-Fi', icon: 'bi-soundwave', hint: 'jazzy lofi · chill' },
    { id: '4xDzrJKXOOY', name: 'Synthwave', icon: 'bi-stars', hint: 'synthwave · focus' },
    { id: '4oStw0r33so', name: 'Peaceful Piano', icon: 'bi-brightness-high', hint: 'piano · calm' },
    { id: 'SKhpl1OMqEY', name: 'Dark Ambient', icon: 'bi-moon', hint: 'ambient · deep' },
    { id: 'JD-kMIpDfnY', name: 'Sleep / Chill', icon: 'bi-moon-stars', hint: 'lofi · sleep' },
    { id: '5yx6BWlEVcY', name: 'Chillhop Radio', icon: 'bi-headphones', hint: 'jazzy hip hop' },
    { id: 'g5rOZm3pvs4', name: 'OPM Love Songs', icon: 'bi-heart', hint: 'OPM relax · sleep' },
    { id: 'J3m6Jk5wVo8', name: 'OPM Tagalog Hits', icon: 'bi-mic', hint: 'OPM pop · trending' }
  ];

  var BENBEN_SONGS = [
    { id: 'nh1gNhLWYuI', name: 'Pagtingin' },
    { id: '7n4isX-yh3Y', name: 'Araw-Araw' },
    { id: 'nGwqqGGbrww', name: 'Sa Susunod Na Habang Buhay' },
    { id: '2gVl2Lwr8_E', name: 'Kathang Isip' },
    { id: 'Zoo1nBRaN9Y', name: 'Leaves (feat. Young K)' },
    { id: 'kL7rhQQQNz0', name: 'Lunod (feat. Zild & juan karlos)' },
    { id: 'hHIcsFEoyrw', name: 'Paninindigan Kita' }
  ];

  var OPM_SONGS = BENBEN_SONGS.concat([
    { id: 'iGHVjTEaNIM', name: 'Esremborak — Mahal Magmahal' },
    { id: '4x45qKtxUB0', name: 'Zack Tabudlo — Pano' },
    { id: 'LiTbbZua-F0', name: 'Moira — Paubaya' },
    { id: 'C2zyYjC_-co', name: 'WRIVE — Hakbang' },
    { id: 'XsJa7VV-DRA', name: 'dwta — Tabi!' }
  ]);

  var PLAYLISTS = [
    { key: 'opm', name: 'OPM Hits', icon: 'bi-flag', hint: 'Ben&Ben & new Pinoy hits', songs: OPM_SONGS },
    { key: 'benben', name: 'Ben&Ben', icon: 'bi-music-note-list', hint: 'Ben&Ben favorites', songs: BENBEN_SONGS }
  ];

  var els = {
    toggle: document.getElementById('musicToggle'),
    panel: document.getElementById('musicPanel'),
    close: document.getElementById('musicClose'),
    station: document.getElementById('musicStation'),
    title: document.getElementById('musicTitle'),
    eq: document.getElementById('musicEq'),
    play: document.getElementById('musicPlay'),
    prev: document.getElementById('musicPrev'),
    next: document.getElementById('musicNext'),
    volume: document.getElementById('musicVolume'),
    stations: document.getElementById('musicStations'),
    custom: document.getElementById('musicCustom'),
    url: document.getElementById('musicUrl'),
    searchForm: document.getElementById('musicSearchForm'),
    searchInput: document.getElementById('musicSearchInput'),
    fallback: document.getElementById('musicFallback'),
    embedWrap: document.getElementById('musicEmbedWrap'),
    embed: document.getElementById('musicEmbed'),
    playerWrap: document.getElementById('musicPlayer')
  };

  if (!els.toggle || !els.panel || !els.playerWrap) return;

  var player = null;
  var embedPlayer = null;
  var embedMode = false;
  var ready = false;
  var currentId = null;
  var currentName = '';
  var currentPlaylist = null;
  var playlistIndex = 0;
  var activeKey = null;
  var isPlaying = false;
  var lastError = false;
  var retryCount = 0;
  var viewKey = null;
  var currentResults = null;
  var currentResultIndex = -1;
  var resumeId = null;
  var resumeTime = 0;
  var prefs = loadPrefs();

  function loadPrefs() {
    try {
      var d = JSON.parse(localStorage.getItem(STORAGE_KEY) || 'null');
      if (d && typeof d === 'object') return d;
    } catch (e) {}
    return {};
  }

  function savePrefs() {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(prefs)); } catch (e) {}
  }

  function stationById(id) {
    for (var i = 0; i < STATIONS.length; i++) {
      if (STATIONS[i].id === id) return STATIONS[i];
    }
    return null;
  }

  function playlistByKey(key) {
    for (var i = 0; i < PLAYLISTS.length; i++) {
      if (PLAYLISTS[i].key === key) return PLAYLISTS[i];
    }
    return null;
  }

  function setActiveKey(key) {
    activeKey = key;
    var btns = els.stations.querySelectorAll('.music-station-btn');
    for (var i = 0; i < btns.length; i++) {
      btns[i].classList.toggle('active', btns[i].dataset.key === key);
    }
  }

  function renderStations() {
    viewKey = null;
    els.stations.innerHTML = '';
    STATIONS.forEach(function (s) {
      var btn = makeStationBtn(s.icon, s.name, s.hint, s.id);
      btn.addEventListener('click', function () {
        playStation(s.id);
      });
      els.stations.appendChild(btn);
    });
    PLAYLISTS.forEach(function (p) {
      var btn = makeStationBtn(p.icon, p.name, p.hint, p.key);
      btn.addEventListener('click', function () {
        renderPlaylistTracks(p.key);
        if (currentPlaylist && currentPlaylist.key === p.key) {
          playPlaylist(p.key, playlistIndex);
        } else {
          playPlaylist(p.key, 0);
        }
      });
      els.stations.appendChild(btn);
    });
  }

  function renderPlaylistTracks(key) {
    var p = playlistByKey(key);
    if (!p) return;
    viewKey = key;
    els.stations.innerHTML = '';
    var back = document.createElement('button');
    back.type = 'button';
    back.className = 'music-station-btn music-back';
    back.innerHTML = '<i class="bi bi-arrow-left-short"></i><span>' + p.name + '</span>';
    back.addEventListener('click', function () {
      renderStations();
    });
    els.stations.appendChild(back);
    p.songs.forEach(function (s, i) {
      var btn = makeStationBtn('bi-music-note', s.name, '', s.id);
      btn.classList.add('music-track');
      btn.dataset.index = String(i);
      if (currentPlaylist && currentPlaylist.key === key && i === playlistIndex) {
        btn.classList.add('active');
      }
      btn.addEventListener('click', function () {
        playPlaylist(key, i);
      });
      els.stations.appendChild(btn);
    });
    setActiveKey(key);
  }

  function markActiveTrack() {
    var btns = els.stations.querySelectorAll('.music-track');
    for (var i = 0; i < btns.length; i++) {
      btns[i].classList.toggle('active', !!currentPlaylist && btns[i].dataset.index === String(playlistIndex));
    }
  }

  function makeStationBtn(icon, name, hint, key) {
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'music-station-btn';
    btn.dataset.key = key;
    btn.innerHTML =
      '<i class="bi ' + icon + '"></i>' +
      '<span class="flex-grow-1"><span class="d-block">' + name + '</span>' +
      '<span class="music-station-hint">' + hint + '</span></span>';
    return btn;
  }

  function setTitle(text) {
    els.title.textContent = text || 'Select a station to start';
    els.title.title = text || '';
  }

  function setStationLabel(text) {
    els.station.textContent = text || '';
  }

  function updatePlayIcon() {
    els.play.innerHTML = isPlaying
      ? '<i class="bi bi-pause-fill"></i>'
      : '<i class="bi bi-play-fill"></i>';
    els.play.setAttribute('aria-label', isPlaying ? 'Pause' : 'Play');
    els.eq.classList.toggle('playing', isPlaying);
    els.toggle.classList.toggle('playing', isPlaying);
  }

  function updateTitleFromPlayer() {
    try {
      var d = player.getVideoData();
      var t = d && d.title ? d.title : currentName;
      setTitle(t);
    } catch (e) {
      setTitle(currentName);
    }
  }

  function doPlay() {
    if (embedMode && embedPlayer) {
      try { embedPlayer.unMute(); embedPlayer.playVideo(); } catch (e) {}
      return;
    }
    if (!ready || !player) return;
    try {
      player.unMute();
      player.playVideo();
    } catch (e) {}
  }

  function doPause() {
    if (embedMode && embedPlayer) {
      try { embedPlayer.pauseVideo(); } catch (e) {}
      return;
    }
    if (!ready || !player) return;
    try { player.pauseVideo(); } catch (e) {}
  }

  function loadVideo(id, name, opts) {
    currentId = id;
    currentName = name;
    if (els.fallback) els.fallback.classList.add('d-none');
    destroyEmbedPlayer();
    prefs.currentId = id;
    savePrefs();
    if (!ready || !player) return;
    lastError = false;
    retryCount = 0;
    try { player.loadVideoById(id); } catch (e) {}
    if (opts && opts.play) doPlay();
  }

  function playStation(id) {
    var s = stationById(id);
    prefs.station = id;
    prefs.playlistKey = null;
    prefs.playlistIndex = null;
    prefs.custom = null;
    savePrefs();
    currentPlaylist = null;
    setActiveKey(id);
    if (s) {
      setStationLabel(s.name);
      setTitle(s.name);
    }
    loadVideo(id, s ? s.name : 'Custom video', { play: true });
  }

  function playPlaylist(key, index) {
    var p = playlistByKey(key);
    if (!p) return;
    var songs = p.songs;
    index = ((index % songs.length) + songs.length) % songs.length;
    prefs.station = null;
    prefs.playlistKey = p.key;
    prefs.playlistIndex = index;
    prefs.custom = null;
    savePrefs();
    currentPlaylist = p;
    playlistIndex = index;
    setActiveKey(p.key);
    setStationLabel(p.name);
    setTitle(songs[index].name);
    markActiveTrack();
    loadVideo(songs[index].id, songs[index].name, { play: true });
  }

  function nextTrack() {
    if (prefs.custom && currentResults && currentResults.length) {
      if (playNextSearchResult()) return;
    }
    if (currentPlaylist) {
      playPlaylist(currentPlaylist.key, playlistIndex + 1);
      return;
    }
    var order = STATIONS.map(function (s) { return s.id; });
    var idx = order.indexOf(currentId);
    var nextId = idx === -1 ? order[0] : order[(idx + 1) % order.length];
    playStation(nextId);
  }

  function prevTrack() {
    if (prefs.custom && currentResults && currentResults.length) {
      if (playPrevSearchResult()) return;
    }
    if (currentPlaylist) {
      playPlaylist(currentPlaylist.key, playlistIndex - 1);
      return;
    }
    var order = STATIONS.map(function (s) { return s.id; });
    var idx = order.indexOf(currentId);
    var prevId = idx <= 0 ? order[order.length - 1] : order[idx - 1];
    playStation(prevId);
  }

  function togglePlay() {
    if (isPlaying) {
      isPlaying = false;
      doPause();
    } else {
      isPlaying = true;
      if (!currentId) {
        if (prefs.playlistKey) {
          playPlaylist(prefs.playlistKey, prefs.playlistIndex || 0);
        } else {
          playStation(prefs.station || STATIONS[0].id);
        }
        return;
      }
      if (lastError) {
        lastError = false;
        loadVideo(currentId, currentName, { play: true });
      } else {
        doPlay();
      }
    }
    updatePlayIcon();
  }

  function extractVideoId(url) {
    url = (url || '').trim();
    if (!url) return null;
    if (/^[A-Za-z0-9_-]{11}$/.test(url)) return url;
    if (!/youtube\.com|youtu\.be/i.test(url)) return null;
    var m = url.match(/(?:[?&]v=|\/embed\/|\/shorts\/|\/live\/|\/v\/|youtu\.be\/)([A-Za-z0-9_-]{11})/);
    return m ? m[1] : null;
  }

  function playCustom() {
    var id = extractVideoId(els.url.value);
    if (!id) {
      els.url.classList.add('is-invalid');
      return;
    }
    els.url.classList.remove('is-invalid');
    prefs.station = null;
    prefs.playlistKey = null;
    prefs.playlistIndex = null;
    prefs.custom = id;
    prefs.customTitle = null;
    savePrefs();
    currentPlaylist = null;
    setActiveKey(null);
    setStationLabel('Custom video');
    loadVideo(id, 'Custom video', { play: true });
    els.url.value = '';
  }

  function onReady() {
    ready = true;
    var vol = typeof prefs.volume === 'number' ? prefs.volume : 70;
    try { player.setVolume(vol); } catch (e) {}
    els.volume.value = vol;

    if (prefs.custom) {
      var cTitle = prefs.customTitle || 'Custom video';
      setActiveKey(null);
      setStationLabel(prefs.customTitle ? 'YouTube search' : 'Custom video');
      setTitle(cTitle);
      loadVideo(prefs.custom, cTitle);
    } else if (prefs.playlistKey) {
      var p = playlistByKey(prefs.playlistKey);
      if (p) {
        var idx = ((prefs.playlistIndex || 0) % p.songs.length + p.songs.length) % p.songs.length;
        currentPlaylist = p;
        playlistIndex = idx;
        setActiveKey(p.key);
        setStationLabel(p.name);
        setTitle(p.songs[idx].name);
        loadVideo(p.songs[idx].id, p.songs[idx].name);
      } else {
        restoreStation();
      }
    } else {
      restoreStation();
    }
    if (prefs.playing) {
      resumeId = prefs.currentId || currentId;
      resumeTime = typeof prefs.currentTime === 'number' ? prefs.currentTime : 0;
      doPlay();
    }
  }

  function restoreStation() {
    if (prefs.station) {
      var s = stationById(prefs.station);
      setActiveKey(s ? s.id : null);
      setStationLabel(s ? s.name : '');
      setTitle(s ? s.name : '');
      loadVideo(prefs.station, s ? s.name : '');
    } else {
      var first = STATIONS[0];
      setActiveKey(first.id);
      setStationLabel(first.name);
      setTitle(first.name);
      loadVideo(first.id, first.name);
    }
  }

  function onStateChange(ev) {
    if (!ev || ev.data === undefined) return;
    if (ev.data === 1) {
      isPlaying = true;
      lastError = false;
      retryCount = 0;
      if (els.fallback) els.fallback.classList.add('d-none');
      prefs.playing = true;
      prefs.currentId = currentId;
      savePrefs();
      if (resumeId && resumeId === currentId && resumeTime > 0) {
        try { player.seekTo(resumeTime, true); } catch (e) {}
      }
      resumeId = null;
      resumeTime = 0;
      updateTitleFromPlayer();
      updatePlayIcon();
    } else if (ev.data === 2) {
      isPlaying = false;
      prefs.playing = false;
      savePrefs();
      updatePlayIcon();
    } else if (ev.data === 0) {
      isPlaying = false;
      prefs.playing = false;
      savePrefs();
      updatePlayIcon();
      nextTrack();
    }
  }

  function onError(ev) {
    var code = ev && ev.data;
    isPlaying = false;
    lastError = true;
    prefs.playing = false;
    savePrefs();
    updatePlayIcon();
    try {
      if (window.console && window.console.warn) {
        window.console.warn('[music-floater] player error code ' + code + ' for ' + currentId);
      }
    } catch (e) {}
    retryCount += 1;
    var curId = currentId;
    if (els.fallback && currentId) {
      els.fallback.href = 'https://www.youtube.com/watch?v=' + currentId;
    }
    var permanent = (code === 100 || code === 101 || code === 150);
    if (permanent) {
      setTitle(currentName || 'Trying embedded player...');
      setStationLabel('Embedded player');
      if (els.fallback) els.fallback.classList.remove('d-none');
      initEmbedPlayer(currentId);
      return;
    }
    if (retryCount === 1) {
      setTitle('Playback hiccup — retrying...');
      setTimeout(function () {
        if (currentId === curId) loadVideo(curId, currentName, { play: true });
      }, 700);
    } else if (retryCount === 2) {
      setTitle('Still struggling — trying next...');
      setTimeout(function () {
        if (currentId === curId) nextTrack();
      }, 700);
    } else {
      setTitle('Playback error (code ' + code + ')');
      if (els.fallback) els.fallback.classList.remove('d-none');
    }
  }

  function initPlayer() {
    player = new YT.Player(els.playerWrap.id, {
      width: '200',
      height: '200',
      videoId: '',
      playerVars: {
        autoplay: 0,
        controls: 0,
        disablekb: 1,
        fs: 0,
        iv_load_policy: 3,
        rel: 0,
        playsinline: 1,
        modestbranding: 1,
        origin: window.location.origin
      },
      events: {
        onReady: onReady,
        onStateChange: onStateChange,
        onError: onError
      }
    });
  }

  function loadPlayerApi() {
    if (window.YT && window.YT.Player) {
      initPlayer();
      return;
    }
    window.onYouTubeIframeAPIReady = initPlayer;
    var tag = document.createElement('script');
    tag.src = 'https://www.youtube.com/iframe_api';
    var first = document.getElementsByTagName('script')[0];
    first.parentNode.insertBefore(tag, first);
  }

  els.toggle.addEventListener('click', function () {
    els.panel.classList.toggle('d-none');
  });
  els.close.addEventListener('click', function () {
    els.panel.classList.add('d-none');
  });
  els.play.addEventListener('click', togglePlay);
  els.prev.addEventListener('click', prevTrack);
  els.next.addEventListener('click', nextTrack);
  els.volume.addEventListener('input', function () {
    var v = parseInt(els.volume.value, 10) || 0;
    prefs.volume = v;
    savePrefs();
    if (ready && player) {
      try { player.setVolume(v); } catch (e) {}
    }
  });
  els.custom.addEventListener('submit', function (ev) {
    ev.preventDefault();
    playCustom();
  });
  els.url.addEventListener('input', function () {
    els.url.classList.remove('is-invalid');
  });

  setInterval(function () {
    if (!ready || !player || !isPlaying || embedMode) return;
    try {
      var d = player.getDuration();
      if (d && isFinite(d)) {
        prefs.currentTime = player.getCurrentTime();
        prefs.currentId = currentId;
        savePrefs();
      }
    } catch (e) {}
  }, 5000);

  function escapeHtml(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function makeSearchBack() {
    var back = document.createElement('button');
    back.type = 'button';
    back.className = 'music-station-btn music-back';
    back.innerHTML = '<i class="bi bi-arrow-left-short"></i><span>Back to stations</span>';
    back.addEventListener('click', function () {
      renderStations();
    });
    return back;
  }

  function renderSearchResults(results) {
    viewKey = '__search__';
    currentResults = results || [];
    currentResultIndex = -1;
    els.stations.innerHTML = '';
    els.stations.appendChild(makeSearchBack());
    if (!results.length) {
      var none = makeStationBtn('bi-music-note', 'No results found', '', '');
      none.classList.add('music-search-status');
      els.stations.appendChild(none);
      return;
    }
    results.forEach(function (r) {
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'music-station-btn music-result';
      btn.dataset.key = r.id;
      btn.innerHTML =
        (r.thumb
          ? '<img src="' + r.thumb + '" alt="" loading="lazy" class="music-result-thumb">'
          : '<i class="bi bi-music-note"></i>') +
        '<span class="flex-grow-1"><span class="d-block music-result-title">' + escapeHtml(r.title) + '</span>' +
        '<span class="music-station-hint">' + escapeHtml(r.channel) + '</span></span>';
      btn.addEventListener('click', function () {
        playSearchResult(r.id, r.title);
      });
      els.stations.appendChild(btn);
    });
  }

  function renderSearchError(msg) {
    viewKey = '__search__';
    els.stations.innerHTML = '';
    els.stations.appendChild(makeSearchBack());
    var row = makeStationBtn('bi-exclamation-circle', msg || 'Search failed. Please try again.', '', '');
    row.classList.add('music-search-status');
    els.stations.appendChild(row);
  }

  function searchYouTube(q) {
    q = (q || '').trim();
    if (!q) {
      els.searchInput.classList.add('is-invalid');
      return;
    }
    viewKey = '__search__';
    currentResults = null;
    currentResultIndex = -1;
    els.stations.innerHTML = '';
    var loading = makeStationBtn('bi-search', 'Searching for "' + q + '"...', '', '');
    loading.classList.add('music-search-status');
    els.stations.appendChild(loading);

    fetch('/api/youtube/search?q=' + encodeURIComponent(q), { credentials: 'same-origin' })
      .then(function (r) { return r.json(); })
      .then(function (data) {
        if (data.error) {
          renderSearchError(data.message || data.error);
          return;
        }
        renderSearchResults(data.results || []);
      })
      .catch(function () {
        renderSearchError('Search failed. Please try again.');
      });
  }

  function destroyEmbedPlayer() {
    embedMode = false;
    if (embedPlayer) {
      try { embedPlayer.destroy(); } catch (e) {}
      embedPlayer = null;
    }
    hideEmbed();
  }

  function skipDeadVideo() {
    destroyEmbedPlayer();
    if (els.fallback) els.fallback.classList.add('d-none');
    if (currentResults && currentResults.length) {
      if (playNextSearchResult()) return;
    }
    nextTrack();
  }

  function initEmbedPlayer(vid) {
    if (!els.embedWrap || !window.YT || !window.YT.Player) return;
    hideEmbed();
    if (embedPlayer) {
      try { embedPlayer.destroy(); } catch (e) {}
      embedPlayer = null;
    }
    els.embedWrap.classList.remove('d-none');
    try {
      embedPlayer = new YT.Player('musicEmbed', {
        videoId: vid,
        width: '100%',
        height: '100%',
        playerVars: { autoplay: 1, playsinline: 1, rel: 0, modestbranding: 1 },
        events: {
          onStateChange: function (ev) {
            if (!ev || ev.data === undefined) return;
            if (ev.data === 1) {
              embedMode = true;
              isPlaying = true;
              lastError = false;
              prefs.playing = true;
              prefs.currentId = currentId;
              savePrefs();
              updatePlayIcon();
              if (els.fallback) els.fallback.classList.add('d-none');
            } else if (ev.data === 2) {
              isPlaying = false;
              prefs.playing = false;
              savePrefs();
              updatePlayIcon();
            } else if (ev.data === 0) {
              isPlaying = false;
              prefs.playing = false;
              savePrefs();
              updatePlayIcon();
              setTimeout(skipDeadVideo, 0);
            }
          },
          onError: function (ev) {
            try {
              if (window.console && window.console.warn) {
                window.console.warn('[music-floater] embed fallback error ' + (ev && ev.data) + ' for ' + currentId);
              }
            } catch (e) {}
            setTimeout(skipDeadVideo, 0);
          }
        }
      });
    } catch (e) {
      try {
        if (window.console && window.console.warn) {
          window.console.warn('[music-floater] embed init failed: ' + (e && e.message));
        }
      } catch (e2) {}
      setTimeout(skipDeadVideo, 0);
    }
  }

  function hideEmbed() {
    if (!els.embedWrap) return;
    els.embedWrap.classList.add('d-none');
  }

  function playSearchResult(vid, title) {
    if (currentResults) {
      for (var i = 0; i < currentResults.length; i++) {
        if (currentResults[i].id === vid) {
          currentResultIndex = i;
          break;
        }
      }
    }
    prefs.station = null;
    prefs.playlistKey = null;
    prefs.playlistIndex = null;
    prefs.custom = vid;
    prefs.customTitle = title;
    savePrefs();
    currentPlaylist = null;
    setActiveKey(null);
    setStationLabel('YouTube search');
    loadVideo(vid, title, { play: true });
  }

  function playNextSearchResult() {
    if (!currentResults || !currentResults.length) return false;
    var next = currentResultIndex + 1;
    if (next >= currentResults.length) return false;
    var r = currentResults[next];
    currentResultIndex = next;
    playSearchResult(r.id, r.title);
    return true;
  }

  function playPrevSearchResult() {
    if (!currentResults || !currentResults.length) return false;
    var prev = currentResultIndex - 1;
    if (prev < 0) return false;
    var r = currentResults[prev];
    currentResultIndex = prev;
    playSearchResult(r.id, r.title);
    return true;
  }

  if (els.searchForm && els.searchInput) {
    els.searchForm.addEventListener('submit', function (ev) {
      ev.preventDefault();
      searchYouTube(els.searchInput.value);
    });
    els.searchInput.addEventListener('input', function () {
      els.searchInput.classList.remove('is-invalid');
    });
  }

  renderStations();
  if (prefs.playlistKey) {
    renderPlaylistTracks(prefs.playlistKey);
  }
  setActiveKey(prefs.playlistKey || prefs.station || null);
  loadPlayerApi();
})();
