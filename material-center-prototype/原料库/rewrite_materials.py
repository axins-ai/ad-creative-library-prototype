"""
完整重写原料库原型.html - 自包含文件夹功能+标签筛选
"""
import re

file_path = "/Users/axins/WorkBuddy/2026-06-10-17-12-54/material-center-prototype/原料库/原料库原型.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# ===== 1. 添加文件夹栏CSS (在筛选卡片之前) =====
old_filter_card = """/* Filter card style */
.filter-card{background:var(--bg-card);border-radius:var(--radius-l);box-shadow:var(--shadow-s);margin-bottom:16px;overflow:hidden}"""

new_folder_css = """/* 文件夹栏（横向标签） */
.folder-bar{display:flex;align-items:center;gap:4px;margin-bottom:14px;padding:6px 0;flex-wrap:wrap;border-bottom:1px solid var(--border-light)}
.folder-tab{padding:4px 14px;border-radius:14px;font-size:12px;cursor:pointer;transition:all .15s;border:1px solid var(--border-light);background:var(--bg-card);color:var(--text-2);white-space:nowrap}
.folder-tab:hover{border-color:var(--primary);color:var(--primary)}
.folder-tab.active{background:var(--primary);color:#fff;border-color:var(--primary)}
.folder-tab .tab-count{font-size:10px;margin-left:4px;opacity:.7}
.folder-tab.active .tab-count{opacity:.9}
.folder-tab-add{width:26px;height:26px;border-radius:50%;border:1px dashed var(--border);background:transparent;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:14px;color:var(--text-3);transition:all .15s;flex-shrink:0}
.folder-tab-add:hover{border-color:var(--primary);color:var(--primary);background:var(--primary-light)}
.folder-tab-wrap{position:relative}
.folder-tab-mgr{display:none;position:absolute;top:100%;left:0;margin-top:4px;background:#fff;border:1px solid var(--border);border-radius:var(--radius-s);box-shadow:var(--shadow-m);z-index:50;min-width:100px;overflow:hidden}
.folder-tab-mgr.show{display:block}
.folder-tab-mgr .mgr-item{padding:6px 12px;font-size:12px;cursor:pointer;transition:background .1s;white-space:nowrap}
.folder-tab-mgr .mgr-item:hover{background:var(--bg-hover)}
.folder-tab-mgr .mgr-item.danger{color:var(--danger)}
.folder-tab-mgr .mgr-item.danger:hover{background:#fff1f0}

/* Filter card style */
.filter-card{background:var(--bg-card);border-radius:var(--radius-l);box-shadow:var(--shadow-s);margin-bottom:16px;overflow:hidden}"""

content = content.replace(old_filter_card, new_folder_css)
print("✅ 添加文件夹栏CSS")

# ===== 2. 替换文件夹下拉为横向标签 =====
# 找到 <!-- 工具栏 --> 部分并替换文件夹下拉为横向标签
old_toolbar_start = """      <!-- 工具栏 -->
      <div class="toolbar">
        <div class="toolbar-left">
          <div class="filter-group" style="margin-right:8px">
            <label>📁 文件夹</label>
            <select id="folderFilter" onchange="applyMsFilter()" style="min-width:120px">
              <option value="">全部文件夹</option>
              <option value="__uncategorized">未分类</option>
            </select>
          </div>
          <button class="btn btn-primary" onclick="openMsUploadModal()">↑ 上传素材</button>"""

new_toolbar = """      <!-- 文件夹栏 -->
      <div class="folder-bar" id="folderBar">
        <!-- 通过JS渲染 -->
      </div>

      <!-- 工具栏 -->
      <div class="toolbar">
        <div class="toolbar-left">
          <button class="btn btn-primary" onclick="openMsUploadModal()">↑ 上传素材</button>"""

content = content.replace(old_toolbar_start, new_toolbar)
print("✅ 替换文件夹下拉为横向标签栏")

# ===== 3. 移除筛选区的文件夹下拉 =====
old_filter_dropdown = """              <label>文件夹</label>
              <select id="folderFilter2" onchange="syncFolderFilter(this.value)">
                <option value="">全部文件夹</option>
                <option value="__uncategorized">未分类</option>
              </select>
            </div>
            <div class="filter-group">
              <label>类型</label>"""

new_filter_no_folder = """              <label>类型</label>"""

content = content.replace(old_filter_dropdown, new_filter_no_folder)
print("✅ 移除筛选区文件夹下拉")

# ===== 4. 替换JS：populateFolderFilters => renderFolderBar + 移除folderFilter2引用 =====
# 找到整个populateFolderFilters函数
old_ppf = """// ========== 文件夹筛选填充 ==========
function populateFolderFilters() {
  var selects = ['folderFilter', 'folderFilter2'];
  for (var si = 0; si < selects.length; si++) {
    var sel = document.getElementById(selects[si]);
    if (!sel) continue;
    var currentVal = sel.value;
    sel.innerHTML = '<option value="">全部文件夹</option><option value="__uncategorized">未分类</option>';
    for (var i = 0; i < msFolders.length; i++) {
      var opt = document.createElement('option');
      opt.value = msFolders[i].id;
      opt.textContent = msFolders[i].name + ' (' + msFolders[i].materials.length + ')';
      sel.appendChild(opt);
    }
    sel.value = currentVal;
  }
  updateUploadFolderOptions();
}

// 同步两个文件夹筛选下拉
function syncFolderFilter(value) {
  var sel1 = document.getElementById('folderFilter');
  var sel2 = document.getElementById('folderFilter2');
  if (sel1) sel1.value = value;
  if (sel2) sel2.value = value;
  applyMsFilter();
}

function selectFolder(folderId) {
  // 从下拉中选择对应文件夹
  var val = folderId === null ? '' : (folderId === -1 ? '__uncategorized' : String(folderId));
  syncFolderFilter(val);
}"""

new_ppf = """// ========== 文件夹标签栏 ==========
var msSelectedFolder = null; // null=全部, '__uncategorized'=未分类, number=具体文件夹

function renderFolderBar() {
  var bar = document.getElementById('folderBar');
  if (!bar) return;
  var html = '';
  
  // 全部
  html += '<span class="folder-tab' + (msSelectedFolder === null ? ' active' : '') + '" onclick="selectFolderTab(null)">全部</span>';
  
  // 未分类
  var uncatCount = 0;
  for (var i = 0; i < msMaterials.length; i++) {
    if (!msMaterials[i].folders || msMaterials[i].folders.length === 0) uncatCount++;
  }
  html += '<span class="folder-tab' + (msSelectedFolder === '__uncategorized' ? ' active' : '') + '" onclick="selectFolderTab(\'__uncategorized\')">未分类<span class="tab-count">' + uncatCount + '</span></span>';
  
  // 各文件夹
  for (var i = 0; i < msFolders.length; i++) {
    var f = msFolders[i];
    var active = msSelectedFolder === f.id;
    var isOwner = f.creator === CURRENT_USER;
    html += '<span class="folder-tab-wrap"><span class="folder-tab' + (active ? ' active' : '') + '" onclick="selectFolderTab(' + f.id + ')" oncontextmenu="event.preventDefault();showFolderMenu(' + f.id + ', event)">' + f.name + '<span class="tab-count">' + f.materials.length + '</span></span></span>';
  }
  
  // + 新建按钮
  html += '<button class="folder-tab-add" onclick="openNewFolderModal()" title="新建文件夹">+</button>';
  
  bar.innerHTML = html;
  updateUploadFolderOptions();
}

function selectFolderTab(folderId) {
  msSelectedFolder = folderId;
  renderFolderBar();
  applyMsFilter();
}"""

content = content.replace(old_ppf, new_ppf)
print("✅ 替换文件夹筛选逻辑为标签栏")

# ===== 5. 更新 getFilteredMsMaterials 使用 msSelectedFolder =====
old_filter_get = """    // 文件夹筛选（从下拉获取）
    var folderVal = document.getElementById('folderFilter') ? document.getElementById('folderFilter').value : '';
    if (folderVal === '__uncategorized') {"""

new_filter_get = """    // 文件夹筛选（从标签栏获取）
    if (msSelectedFolder === '__uncategorized') {"""

content = content.replace(old_filter_get, new_filter_get)

old_filter_get2 = """    } else if (folderVal !== '') {
      // 特定文件夹
      var fid = parseInt(folderVal);
      if (!m.folders || m.folders.indexOf(fid) === -1) continue;
    }"""
new_filter_get2 = """    } else if (msSelectedFolder !== null) {
      if (!m.folders || m.folders.indexOf(msSelectedFolder) === -1) continue;
    }"""
content = content.replace(old_filter_get2, new_filter_get2)
print("✅ 更新筛选逻辑使用 msSelectedFolder")

# ===== 6. 更新提交上传/删除/移动后的调用 =====
content = content.replace('populateFolderFilters();', 'renderFolderBar();')
print("✅ 更新调用名为 renderFolderBar")

# ===== 7. 替换初始化中的调用 =====
old_init = """// ========== 初始化 ==========
populateFolderFilters();
initTagFilters();
renderMsGrid();

// 从URL读取folder参数（父页面菜单传过来的）
function readFolderFromUrl() {
  var match = location.search.match(/folder=(\d+)/);
  if (match) {
    var folderId = parseInt(match[1]);
    document.getElementById('folderFilter').value = String(folderId);
    document.getElementById('folderFilter2').value = String(folderId);
    applyMsFilter();
  }
}
readFolderFromUrl();"""

new_init = """// ========== 初始化 ==========
renderFolderBar();
initTagFilters();
renderMsGrid();"""

content = content.replace(old_init, new_init)
print("✅ 更新初始化调用")

# ===== 8. 删除 renderFolderTabs 函数（已废弃） =====
old_rft = """// 已迁移到 populateFolderFilters
  populateFolderFilters();"""
# 这个函数会被renderFolderBar替代，直接删除其内容
content = content.replace('function renderFolderTabs() {\n  // 已迁移到 populateFolderFilters\n  populateFolderFilters();\n}', 
                         'function renderFolderTabs() { renderFolderBar(); }')
print("✅ 清理遗留函数")

# 保存
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"\n✅ 全部完成！文件大小: {len(content)} 字节")
