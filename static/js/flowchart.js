(function () {
  'use strict';

  var svg = document.getElementById('fcCanvas');
  if (!svg) return;
  var SVGNS = 'http://www.w3.org/2000/svg';
  var STORE_KEY = 'cfFlowchart_' + (window.FC_USER || 'guest');

  var NODE_DEFS = {
    start:    { label: 'Start',   w: 150, h: 64, shape: 'oval' },
    process:  { label: 'Process', w: 160, h: 64, shape: 'rect' },
    decision: { label: 'Decision?', w: 170, h: 100, shape: 'diamond' },
    io:       { label: 'Input / Output', w: 180, h: 64, shape: 'parallelo' }
  };

  var nodes = [];
  var edges = [];
  var seq = 1;
  var selectedId = null;
  var connectMode = false;
  var connectFrom = null;
  var dragging = null;
  var editingInput = null;

  // arrow marker
  var defs = document.createElementNS(SVGNS, 'defs');
  defs.innerHTML =
    '<marker id="fcArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">' +
    '<path d="M0,0 L10,5 L0,10 z" fill="#475569"></path></marker>' +
    '<marker id="fcArrowSel" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">' +
    '<path d="M0,0 L10,5 L0,10 z" fill="#e11d48"></path></marker>';
  svg.appendChild(defs);

  function el(name, attrs) {
    var e = document.createElementNS(SVGNS, name);
    for (var k in attrs) { if (attrs.hasOwnProperty(k)) e.setAttribute(k, attrs[k]); }
    return e;
  }

  function center(n) {
    var d = NODE_DEFS[n.type];
    return { cx: n.x + d.w / 2, cy: n.y + d.h / 2 };
  }

  function boundaryPoint(n, tx, ty) {
    var d = NODE_DEFS[n.type];
    var c = center(n);
    var dx = tx - c.cx, dy = ty - c.cy;
    if (dx === 0 && dy === 0) return { x: c.cx, y: c.cy };
    var hw = d.w / 2, hh = d.h / 2;
    var pt;
    if (d.shape === 'diamond') {
      var t = 1 / (Math.abs(dx) / hw + Math.abs(dy) / hh);
      pt = { x: c.cx + dx * t, y: c.cy + dy * t };
    } else {
      var sx = dx !== 0 ? hw / Math.abs(dx) : Infinity;
      var sy = dy !== 0 ? hh / Math.abs(dy) : Infinity;
      var t2 = Math.min(sx, sy);
      pt = { x: c.cx + dx * t2, y: c.cy + dy * t2 };
    }
    return pt;
  }

  function svgPoint(evt) {
    var rect = svg.getBoundingClientRect();
    return { x: evt.clientX - rect.left, y: evt.clientY - rect.top };
  }

  function shapeEl(n) {
    var d = NODE_DEFS[n.type];
    var g = el('g', { 'class': 'fc-node', 'data-id': n.id });
    var shape;
    if (d.shape === 'oval') {
      shape = el('ellipse', { cx: n.x + d.w / 2, cy: n.y + d.h / 2, rx: d.w / 2, ry: d.h / 2 });
    } else if (d.shape === 'rect') {
      shape = el('rect', { x: n.x, y: n.y, width: d.w, height: d.h, rx: 8 });
    } else if (d.shape === 'diamond') {
      var c = center(n);
      shape = el('polygon', {
        points: c.cx + ',' + (n.y) + ' ' + (n.x + d.w) + ',' + c.cy + ' ' + c.cx + ',' + (n.y + d.h) + ' ' + n.x + ',' + c.cy
      });
    } else { // parallelogram
      var sk = 22;
      shape = el('polygon', {
        points: (n.x + sk) + ',' + n.y + ' ' + (n.x + d.w) + ',' + n.y + ' ' + (n.x + d.w - sk) + ',' + (n.y + d.h) + ' ' + n.x + ',' + (n.y + d.h)
      });
    }
    shape.setAttribute('class', 'fc-shape');
    g.appendChild(shape);

    var lines = (n.label || '').split('\n');
    var c2 = center(n);
    var startY = c2.cy - (lines.length - 1) * 9;
    lines.forEach(function (ln, i) {
      var t = el('text', { x: c2.cx, y: startY + i * 18, 'text-anchor': 'middle', 'dominant-baseline': 'middle' });
      t.textContent = ln;
      g.appendChild(t);
    });
    return g;
  }

  function render() {
    while (svg.lastChild && svg.lastChild !== defs) svg.removeChild(svg.lastChild);

    edges.forEach(function (e) {
      var a = nodes.find(function (n) { return n.id === e.from; });
      var b = nodes.find(function (n) { return n.id === e.to; });
      if (!a || !b) return;
      var ca = center(a), cb = center(b);
      var p1 = boundaryPoint(a, cb.cx, cb.cy);
      var p2 = boundaryPoint(b, ca.cx, ca.cy);
      var line = el('line', {
        x1: p1.x, y1: p1.y, x2: p2.x, y2: p2.y,
        'marker-end': 'url(#fcArrow)', 'class': 'fc-edge', 'data-edge': e.id
      });
      svg.appendChild(line);
    });

    nodes.forEach(function (n) {
      var g = shapeEl(n);
      if (n.id === selectedId) g.classList.add('selected');
      if (n.id === connectFrom) g.classList.add('connecting');
      svg.appendChild(g);
    });
  }

  function addNode(type, x, y) {
    var d = NODE_DEFS[type];
    var n = { id: 'n' + (seq++), type: type, x: x, y: y, label: d.label };
    nodes.push(n);
    selectedId = n.id;
    save();
    render();
  }

  function addEdge(from, to) {
    if (from === to) return;
    if (edges.some(function (e) { return e.from === from && e.to === to; })) return;
    edges.push({ id: 'e' + (seq++), from: from, to: to });
    save();
    render();
  }

  function selectNode(id) {
    selectedId = id;
    render();
  }

  function deleteSelected() {
    if (!selectedId) return;
    nodes = nodes.filter(function (n) { return n.id !== selectedId; });
    edges = edges.filter(function (e) { return e.from !== selectedId && e.to !== selectedId; });
    selectedId = null;
    save();
    render();
  }

  function cancelInlineEdit() {
    if (editingInput) {
      if (editingInput.parentNode) editingInput.parentNode.removeChild(editingInput);
      editingInput = null;
    }
  }

  function startInlineEdit(id) {
    var n = nodes.find(function (x) { return x.id === id; });
    if (!n) return;
    cancelInlineEdit();
    selectedId = id;
    render();
    var g = svg.querySelector('[data-id="' + id + '"]');
    var t = g && g.querySelector('text');
    if (!t) return;
    var stageRect = svg.parentElement.getBoundingClientRect();
    var tr = t.getBoundingClientRect();
    var input = document.createElement('input');
    input.type = 'text';
    input.className = 'fc-edit-input';
    input.value = n.label;
    input.style.position = 'absolute';
    input.style.left = (tr.left - stageRect.left) + 'px';
    input.style.top = (tr.top - stageRect.top - 2) + 'px';
    input.style.width = Math.max(Math.round(tr.width) + 16, 80) + 'px';
    input.style.height = (Math.round(tr.height) + 6) + 'px';
    svg.parentElement.appendChild(input);
    editingInput = input;
    input.focus();
    input.select();

    function commit() {
      if (!editingInput) return;
      n.label = input.value;
      cancelInlineEdit();
      save();
      render();
    }
    input.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') { e.preventDefault(); commit(); }
      else if (e.key === 'Escape') { e.preventDefault(); cancelInlineEdit(); }
    });
    input.addEventListener('blur', commit);
  }

  function updateLabel(id) {
    startInlineEdit(id);
  }

  function save() {
    try { localStorage.setItem(STORE_KEY, JSON.stringify({ nodes: nodes, edges: edges, seq: seq })); } catch (e) {}
  }

  function load() {
    try {
      var d = JSON.parse(localStorage.getItem(STORE_KEY) || 'null');
      if (d && Array.isArray(d.nodes)) {
        nodes = d.nodes; edges = d.edges || []; seq = d.seq || (nodes.length + 1);
        render();
        return true;
      }
    } catch (e) {}
    return false;
  }

  function loadExample() {
    nodes = []; edges = []; seq = 1; selectedId = null; connectFrom = null;
    var mk = function (type, x, y, label) { var n = { id: 'n' + (seq++), type: type, x: x, y: y, label: label }; nodes.push(n); return n; };
    var s = mk('start', 60, 30, 'Start');
    var inp = mk('io', 60, 130, 'Input n');
    var dec = mk('decision', 60, 250, 'n % 2 == 0?');
    var even = mk('process', 330, 250, 'Print "Even"');
    var odd = mk('process', 60, 400, 'Print "Odd"');
    var end = mk('start', 60, 510, 'End');
    addEdge(s.id, inp.id);
    addEdge(inp.id, dec.id);
    addEdge(dec.id, even.id);
    addEdge(dec.id, odd.id);
    addEdge(even.id, end.id);
    addEdge(odd.id, end.id);
    render();
    save();
  }

  // ---- events ----
  svg.addEventListener('pointerdown', function (evt) {
    var g = evt.target.closest('[data-id]');
    var p = svgPoint(evt);
    if (g && g.classList.contains('fc-node')) {
      var id = g.getAttribute('data-id');
      if (connectMode) {
        if (!connectFrom) { connectFrom = id; render(); }
        else if (connectFrom !== id) { addEdge(connectFrom, id); connectFrom = null; render(); }
        return;
      }
      selectNode(id);
      var n = nodes.find(function (x) { return x.id === id; });
      var d = NODE_DEFS[n.type];
      dragging = { id: id, offx: n.x - p.x, offy: n.y - p.y };
      svg.setPointerCapture(evt.pointerId);
    } else {
      selectNode(null);
    }
  });

  svg.addEventListener('pointermove', function (evt) {
    if (!dragging) return;
    var p = svgPoint(evt);
    var n = nodes.find(function (x) { return x.id === dragging.id; });
    if (!n) return;
    n.x = Math.max(0, p.x + dragging.offx);
    n.y = Math.max(0, p.y + dragging.offy);
    render();
  });

  svg.addEventListener('pointerup', function (evt) {
    if (dragging) { dragging = null; save(); }
  });

  svg.addEventListener('dblclick', function (evt) {
    var g = evt.target.closest('[data-id]');
    if (g) updateLabel(g.getAttribute('data-id'));
  });

  document.addEventListener('keydown', function (evt) {
    if ((evt.key === 'Delete' || evt.key === 'Backspace') && selectedId) {
      var t = evt.target.tagName;
      if (t === 'INPUT' || t === 'TEXTAREA') return;
      deleteSelected();
      evt.preventDefault();
    }
  });

  // toolbar
  document.querySelectorAll('.fc-shape').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var type = btn.getAttribute('data-type');
      var d = NODE_DEFS[type];
      var svgRect = svg.getBoundingClientRect();
      var x = (svgRect.width - d.w) / 2 + (Math.random() * 40 - 20);
      var y = Math.min(40 + nodes.length * 12, svgRect.height - d.h - 10);
      addNode(type, Math.max(0, x), Math.max(0, y));
    });
  });

  var connectBtn = document.getElementById('fcConnect');
  connectBtn.addEventListener('click', function () {
    connectMode = !connectMode;
    connectFrom = null;
    connectBtn.classList.toggle('active', connectMode);
    document.getElementById('fcHint').textContent = connectMode
      ? 'Connect mode: click the first shape, then the second shape to draw an arrow.'
      : 'Tap a shape above to add it, then drag to move. Double-click a shape — or select it and click Edit Text — to rename it.';
    render();
  });

  document.getElementById('fcDelete').addEventListener('click', deleteSelected);

  document.getElementById('fcEdit').addEventListener('click', function () {
    if (!selectedId) {
      document.getElementById('fcHint').textContent = 'Select a shape first, then click Edit Text (or double-click it).';
      return;
    }
    startInlineEdit(selectedId);
  });

  document.getElementById('fcClear').addEventListener('click', function () {
    if (!confirm('Clear the whole canvas?')) return;
    nodes = []; edges = []; selectedId = null; connectFrom = null;
    save(); render();
  });

  document.getElementById('fcExample').addEventListener('click', loadExample);

  document.getElementById('fcPng').addEventListener('click', function () {
    var rect = svg.getBoundingClientRect();
    var clone = svg.cloneNode(true);
    clone.setAttribute('width', rect.width);
    clone.setAttribute('height', rect.height);
    clone.setAttribute('xmlns', SVGNS);
    var data = new XMLSerializer().serializeToString(clone);
    var url = URL.createObjectURL(new Blob([data], { type: 'image/svg+xml;charset=utf-8' }));
    var img = new Image();
    img.onload = function () {
      var scale = 2;
      var canvas = document.createElement('canvas');
      canvas.width = rect.width * scale; canvas.height = rect.height * scale;
      var ctx = canvas.getContext('2d');
      ctx.fillStyle = '#ffffff';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      URL.revokeObjectURL(url);
      canvas.toBlob(function (blob) {
        var a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = 'flowchart.png';
        a.click();
      });
    };
    img.src = url;
  });

  document.getElementById('fcJson').addEventListener('click', function () {
    var blob = new Blob([JSON.stringify({ nodes: nodes, edges: edges }, null, 2)], { type: 'application/json' });
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'flowchart.json';
    a.click();
  });

  var fileInput = document.getElementById('fcFile');
  document.getElementById('fcLoad').addEventListener('click', function () { fileInput.click(); });
  fileInput.addEventListener('change', function () {
    var f = fileInput.files && fileInput.files[0];
    if (!f) return;
    var reader = new FileReader();
    reader.onload = function () {
      try {
        var d = JSON.parse(reader.result);
        if (Array.isArray(d.nodes)) {
          nodes = d.nodes; edges = d.edges || [];
          seq = (nodes.length + edges.length + 1);
          selectedId = null; connectFrom = null;
          save(); render();
        }
      } catch (e) { alert('Invalid flowchart file.'); }
    };
    reader.readAsText(f);
    fileInput.value = '';
  });

  if (!load()) {
    loadExample();
  }
})();
