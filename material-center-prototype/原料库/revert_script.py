file_path = "/Users/axins/WorkBuddy/2026-06-10-17-12-54/material-center-prototype/原料库/原料库原型.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# === HTML替换 ===

# 1. 替换文件夹标签为下拉筛选（工具栏）
old_tabs = """      <!-- 文件夹标签 -->
      <div class="folder-tabs" id="folderTabs">
        <!-- 通过JS渲染 -->
      </div>

      <!-- 工具栏 -->
      <div class="toolbar">
        <div class="toolbar-left">"""

new_dropdown = """      <!-- 工具栏 -->
      <div class="toolbar">
        <div class="toolbar-left">
          <div class="filter-group" style="margin-right:8px">
            <label>📁 文件夹</label>
            <select id="folderFilter" onchange="applyMsFilter()" style="min-width:120px">
              <option value="">全部文件夹</option>
              <option value="__uncategorized">未分类</option>
            </select>
          </div>"""

content = content.replace(old_tabs, new_dropdown)
print("步骤1 ✅ 替换文件夹标签为下拉")

# 2. 在筛选区添加文件夹下拉
old_filter = """              <label>类型</label>
              <select id="typeFilter" onchange="applyMsFilter()">"""

new_filter = """              <label>文件夹</label>
              <select id="folderFilter2" onchange="syncFolderFilter(this.value)">
                <option value="">全部文件夹</option>
                <option value="__uncategorized">未分类</option>
              </select>
            </div>
            <div class="filter-group">
              <label>类型</label>
              <select id="typeFilter" onchange="applyMsFilter()">"""

content = content.replace(old_filter, new_filter)
print("步骤2 ✅ 恢复筛选区文件夹下拉")

# === JS替换 ===

# 3. 替换 renderFolderTabs 函数 + selectedFolder 变量
# 找到从 "var selectedFolder" 到 "function renderFolderTabs()" 之间
old_js1 = "var selectedFolder = null; // null=全部, "
new_js1 = "var selectedFolder = null; // 已废弃（使用下拉筛选）\nvar renderedFolderTabs = null; // "

content = content.replace(old_js1, new_js1)

# 替换 renderFolderTabs 函数体 - 简单方式：替换掉整个函数
old_rf = """function renderFolderTabs() {"""

# 找到renderFolderTabs函数结束位置
idx = content.find(old_rf)
if idx > 0:
    # 找到下一个function的开始
    next_func = content.find("\nfunction ", idx + 30)
    if next_func > 0:
        # 提取整个函数并替换
        old_func = content[idx:next_func]
        new_func = "function renderFolderTabs() {\n  // 已迁移到 populateFolderFilters\n  populateFolderFilters();\n}\n"
        content = content.replace(old_func, new_func)
        print("步骤3 ✅ 替换 renderFolderTabs -> populateFolderFilters")
    else:
        print("❌ 未找到下一个函数")
else:
    print("❌ 未找到 renderFolderTabs")

# 4. 替换 selectFolderTab 函数
old_sel = """function selectFolderTab(folderId) {"""
idx2 = content.find(old_sel)
if idx2 > 0:
    next_func2 = content.find("\nfunction ", idx2 + 25)
    if next_func2 > 0:
        old_sel_func = content[idx2:next_func2]
        new_sel_func = "function selectFolderTab(folderId) {\n  // 通过下拉选择文件夹\n  var val = folderId === null ? '' : (folderId === -1 || folderId === '__uncategorized' ? '__uncategorized' : String(folderId));\n  document.getElementById('folderFilter').value = val;\n  document.getElementById('folderFilter2').value = val;\n  applyMsFilter();\n}\n"
        content = content.replace(old_sel_func, new_sel_func)
        print("步骤4 ✅ 替换 selectFolderTab -> 下拉方式")
    else:
        print("❌ 未找到下一个函数(select)")
else:
    print("❌ 未找到 selectFolderTab")

# 5. 替换 getFilteredMsMaterials 中的文件夹筛选逻辑
old_get = "    if (selectedFolder === '__uncategorized') {"
new_get = "    var folderVal = document.getElementById('folderFilter') ? document.getElementById('folderFilter').value : '';\n    if (folderVal === '__uncategorized') {"

content = content.replace(old_get, new_get)

old_get2 = "    } else if (selectedFolder !== null) {"
new_get2 = "    } else if (folderVal !== '') {"

content = content.replace(old_get2, new_get2)

old_get3 = "      if (!m.folders || m.folders.indexOf(selectedFolder) === -1) continue;"
new_get3 = "      var fid = parseInt(folderVal);\n      if (!m.folders || m.folders.indexOf(fid) === -1) continue;"

content = content.replace(old_get3, new_get3)
print("步骤5 ✅ 恢复 getFilteredMsMaterials 的文件夹筛选逻辑")

# 6. 添加 populateFolderFilters + syncFolderFilter + selectFolder 函数
# 在 renderFolderTabs 之前添加
new_functions = """// ========== 文件夹筛选填充 ==========
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
}
"""

# 添加到 renderFolderTabs 函数之前
rf_pos = content.find("function renderFolderTabs() {")
if rf_pos > 0:
    # 找到前面的换行
    content = content[:rf_pos] + new_functions + "\n\n" + content[rf_pos:]
    print("步骤6 ✅ 添加 populateFolderFilters 函数")
else:
    print("❌ 未找到 renderFolderTabs 插入点")

# 7. 替换所有 renderFolderTabs() 调用（除了函数定义本身）
# 需要小心：只替换调用，不替换定义
content = content.replace("\nrenderFolderTabs();", "\npopulateFolderFilters();")
print("步骤7 ✅ 替换 renderFolderTabs() 调用为 populateFolderFilters()")

# 8. 删除 folder-tabs CSS
old_css = """/* 文件夹标签 */
.folder-tabs{display:flex;gap:4px;margin-bottom:12px;flex-wrap:wrap;padding:8px 0;border-bottom:1px solid var(--border-light);flex-shrink:0}
.folder-tab{padding:5px 14px;border-radius:var(--radius-s);font-size:12px;cursor:pointer;transition:all .15s;border:1px solid transparent;background:transparent;color:var(--text-2);white-space:nowrap}
.folder-tab:hover{background:var(--bg-hover);color:var(--text-1)}
.folder-tab.active{background:var(--primary-light);color:var(--primary);border-color:var(--primary);font-weight:500}
.folder-tab .tab-count{font-size:10px;color:var(--text-3);margin-left:3px}
.folder-tab.active .tab-count{color:var(--primary)}
"""

content = content.replace(old_css, "")
print("步骤8 ✅ 移除文件夹标签CSS")

# 保存
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"\n✅ 完成！文件大小: {len(content)} 字节")
