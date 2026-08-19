# 更新原料库原型 - 批量修改
file_path = "/Users/axins/WorkBuddy/2026-06-10-17-12-54/material-center-prototype/原料库/原料库原型.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# === 1. 更新 msMaterials 数据，增加业务归属、渠道、标签字段 ===
old_data = """var msMaterials = [
  {id:1, name:"开场动画A", type:"前贴", optimizer:"崔志恒", date:"2026-06-20", source:"自动入库", folders:[1]},
  {id:2, name:"产品介绍B", type:"中段", optimizer:"黄佩贤", date:"2026-06-19", source:"手动上传", folders:[2,3]},
  {id:3, name:"行动号召C", type:"尾帧", optimizer:"黎舒晴", date:"2026-06-18", source:"自动入库", folders:[3]},
  {id:4, name:"前贴片-夏日版", type:"前贴", optimizer:"李雨航", date:"2026-06-17", source:"手动上传", folders:[1]},
  {id:5, name:"中段-功能演示", type:"中段", optimizer:"谭嘉颖", date:"2026-06-16", source:"自动入库", folders:[2]},
  {id:6, name:"尾帧-下载引导", type:"尾帧", optimizer:"林金维", date:"2026-06-15", source:"自动入库", folders:[3]},
  {id:7, name:"前贴-品牌露出", type:"前贴", optimizer:"陈羽思", date:"2026-06-14", source:"自动入库", folders:[1]},
  {id:8, name:"中段-优惠说明", type:"中段", optimizer:"叶首龙", date:"2026-06-13", source:"手动上传", folders:[]},
  {id:9, name:"尾帧-立即行动", type:"尾帧", optimizer:"赖嘉俊", date:"2026-06-12", source:"自动入库", folders:[]},
  {id:10, name:"前贴-促销快剪", type:"前贴", optimizer:"戚嘉豪", date:"2026-06-11", source:"自动入库", folders:[]},
  {id:11, name:"中段-场景展示", type:"中段", optimizer:"黄雄伟", date:"2026-06-10", source:"自动入库", folders:[]},
  {id:12, name:"尾帧-关注引导", type:"尾帧", optimizer:"姚丰育", date:"2026-06-09", source:"手动上传", folders:[]},
];"""

new_data = """var msMaterials = [
  {id:1, name:"开场动画A", type:"前贴", biz:"存量", channel:"广点通", optimizer:"崔志恒", date:"2026-06-20", source:"自动入库", folders:[1], tags:{user:{region:"一线城市",age:"18-24",gender:"男"},product:"39元",content:{文案:"紧迫性",场景:"营业厅"}}},
  {id:2, name:"产品介绍B", type:"中段", biz:"权益", channel:"头条", optimizer:"黄佩贤", date:"2026-06-19", source:"手动上传", folders:[2,3], tags:{user:{region:"二线城市",age:"25-34",gender:"女"},product:"59元",content:{宣传卖点:"话费",口播:"口播女"}}},
  {id:3, name:"行动号召C", type:"尾帧", biz:"存量", channel:"广点通", optimizer:"黎舒晴", date:"2026-06-18", source:"自动入库", folders:[3], tags:{user:{region:"一线城市",age:"35-44",gender:"男"},product:"39元",content:{文案:"系统通知",对话:"老年男人"}}},
  {id:4, name:"前贴片-夏日版", type:"前贴", biz:"权益", channel:"头条", optimizer:"李雨航", date:"2026-06-17", source:"手动上传", folders:[1], tags:{user:{region:"三四线城市",age:"18-24",gender:"女"},product:"59元",content:{内容:"风景"}}},
  {id:5, name:"中段-功能演示", type:"中段", biz:"存量", channel:"广点通", optimizer:"谭嘉颖", date:"2026-06-16", source:"自动入库", folders:[2], tags:{user:{region:"农村",age:"45+",gender:"男"},product:"39元",content:{场景:"小区",口播:"口播男"}}},
  {id:6, name:"尾帧-下载引导", type:"尾帧", biz:"权益", channel:"头条", optimizer:"林金维", date:"2026-06-15", source:"自动入库", folders:[3], tags:{user:{region:"一线城市",age:"25-34",gender:"女"},product:"59元",content:{宣传卖点:"流量"}}},
  {id:7, name:"前贴-品牌露出", type:"前贴", biz:"存量", channel:"广点通", optimizer:"陈羽思", date:"2026-06-14", source:"自动入库", folders:[1], tags:{user:{region:"二线城市",age:"35-44",gender:"男"},product:"39元",content:{内容:"猛宠"}}},
  {id:8, name:"中段-优惠说明", type:"中段", biz:"权益", channel:"头条", optimizer:"叶首龙", date:"2026-06-13", source:"手动上传", folders:[], tags:{user:{region:"三四线城市",age:"18-24",gender:"女"},product:"59元",content:{场景:"街头"}}},
  {id:9, name:"尾帧-立即行动", type:"尾帧", biz:"存量", channel:"广点通", optimizer:"赖嘉俊", date:"2026-06-12", source:"自动入库", folders:[], tags:{user:{region:"一线城市",age:"45+",gender:"男"},product:"39元",content:{对话:"老年女人"}}},
  {id:10, name:"前贴-促销快剪", type:"前贴", biz:"权益", channel:"头条", optimizer:"戚嘉豪", date:"2026-06-11", source:"自动入库", folders:[], tags:{user:{region:"二线城市",age:"25-34",gender:"女"},product:"59元",content:{内容:"花鸟"}}},
  {id:11, name:"中段-场景展示", type:"中段", biz:"存量", channel:"广点通", optimizer:"黄雄伟", date:"2026-06-10", source:"自动入库", folders:[], tags:{user:{region:"农村",age:"35-44",gender:"男"},product:"39元",content:{场景:"公园"}}},
  {id:12, name:"尾帧-关注引导", type:"尾帧", biz:"权益", channel:"头条", optimizer:"姚丰育", date:"2026-06-09", source:"手动上传", folders:[], tags:{user:{region:"三四线城市",age:"18-24",gender:"女"},product:"59元",content:{口播:"口播女"}}},
];"""

content = content.replace(old_data, new_data)
print("步骤1 ✅ 更新msMaterials数据（增加业务归属、渠道、标签）")

# === 2. 更新预览弹窗，增加业务归属、渠道、标签字段 ===
old_preview = """      <div class="modal-sidebar">
        <div class="detail-row">
          <div class="detail-label">素材名称</div>
          <div class="detail-value" id="detailName">-</div>
        </div>
        <div class="detail-row">
          <div class="detail-label">素材类型</div>
          <div class="detail-value" id="detailType">-</div>
        </div>
        <div class="detail-row">
          <div class="detail-label">优化师</div>
          <div class="detail-value" id="detailOptimizer">-</div>
        </div>
        <div class="detail-row">
          <div class="detail-label">上传日期</div>
          <div class="detail-value" id="detailDate">-</div>
        </div>
        <div class="detail-row">
          <div class="detail-label">所在文件夹</div>
          <div class="detail-value" id="detailFolder" style="display:flex;flex-wrap:wrap;gap:4px"></div>
        </div>
      </div>"""

new_preview = """      <div class="modal-sidebar">
        <div class="detail-row">
          <div class="detail-label">素材名称</div>
          <div class="detail-value" id="detailName">-</div>
        </div>
        <div class="detail-row">
          <div class="detail-label">素材类型</div>
          <div class="detail-value" id="detailType">-</div>
        </div>
        <div class="detail-row">
          <div class="detail-label">业务归属</div>
          <div class="detail-value" id="detailBiz">-</div>
        </div>
        <div class="detail-row">
          <div class="detail-label">渠道</div>
          <div class="detail-value" id="detailChannel">-</div>
        </div>
        <div class="detail-row">
          <div class="detail-label">优化师</div>
          <div class="detail-value" id="detailOptimizer">-</div>
        </div>
        <div class="detail-row">
          <div class="detail-label">上传日期</div>
          <div class="detail-value" id="detailDate">-</div>
        </div>
        <div class="detail-row">
          <div class="detail-label">所在文件夹</div>
          <div class="detail-value" id="detailFolder" style="display:flex;flex-wrap:wrap;gap:4px"></div>
        </div>
        <div class="detail-row">
          <div class="detail-label">用户标签</div>
          <div class="detail-value" id="detailUserTags" style="font-size:12px">-</div>
        </div>
        <div class="detail-row">
          <div class="detail-label">产品标签</div>
          <div class="detail-value" id="detailProductTag">-</div>
        </div>
        <div class="detail-row">
          <div class="detail-label">内容标签</div>
          <div class="detail-value" id="detailContentTags" style="font-size:12px">-</div>
        </div>
      </div>"""

content = content.replace(old_preview, new_preview)
print("步骤2 ✅ 更新预览弹窗（增加业务归属、渠道、标签字段）")

# === 3. 更新 openMsPreview 函数，填充新字段 ===
old_preview_func = """function openMsPreview(id) {
  var m = null;
  for (var i = 0; i < msMaterials.length; i++) {
    if (msMaterials[i].id === id) { m = msMaterials[i]; break; }
  }
  if (!m) return;
  
  document.getElementById("msPreviewTitle").textContent = "预览：" + m.name;
  document.getElementById("detailName").textContent = m.name;
  document.getElementById("detailType").textContent = m.type;
  document.getElementById("detailOptimizer").textContent = m.optimizer;
  document.getElementById("detailDate").textContent = m.date;
  
  // 显示所在文件夹
  var folderNames = [];
  if (m.folders && m.folders.length > 0) {
    for (var j = 0; j < m.folders.length; j++) {
      for (var k = 0; k < msFolders.length; k++) {
        if (msFolders[k].id === m.folders[j]) {
          folderNames.push(msFolders[k].name);
          break;
        }
      }
    }
  }
  document.getElementById("detailFolder").innerHTML = folderNames.length > 0 
    ? folderNames.map(function(n) { return '<span class=\"tag-pill\">' + n + '</span>'; }).join('')
    : '<span style=\"color:var(--text-3);font-size:12px\">未分类</span>';
  
  document.getElementById("msPreviewModal").classList.add("active");
  document.body.style.overflow = "hidden";
}"""

new_preview_func = """function openMsPreview(id) {
  var m = null;
  for (var i = 0; i < msMaterials.length; i++) {
    if (msMaterials[i].id === id) { m = msMaterials[i]; break; }
  }
  if (!m) return;
  
  document.getElementById("msPreviewTitle").textContent = "预览：" + m.name;
  document.getElementById("detailName").textContent = m.name;
  document.getElementById("detailType").textContent = m.type;
  document.getElementById("detailBiz").textContent = m.biz || '-';
  document.getElementById("detailChannel").textContent = m.channel || '-';
  document.getElementById("detailOptimizer").textContent = m.optimizer;
  document.getElementById("detailDate").textContent = m.date;
  
  // 显示所在文件夹
  var folderNames = [];
  if (m.folders && m.folders.length > 0) {
    for (var j = 0; j < m.folders.length; j++) {
      for (var k = 0; k < msFolders.length; k++) {
        if (msFolders[k].id === m.folders[j]) {
          folderNames.push(msFolders[k].name);
          break;
        }
      }
    }
  }
  document.getElementById("detailFolder").innerHTML = folderNames.length > 0 
    ? folderNames.map(function(n) { return '<span class="tag-pill">' + n + '</span>'; }).join('')
    : '<span style="color:var(--text-3);font-size:12px">未分类</span>';
  
  // 用户标签
  var userTags = '-';
  if (m.tags && m.tags.user) {
    var parts = [];
    if (m.tags.user.region) parts.push('地区:' + m.tags.user.region);
    if (m.tags.user.age) parts.push('年龄:' + m.tags.user.age);
    if (m.tags.user.gender) parts.push('性别:' + m.tags.user.gender);
    if (parts.length > 0) userTags = parts.join(' | ');
  }
  document.getElementById("detailUserTags").textContent = userTags;
  
  // 产品标签
  document.getElementById("detailProductTag").textContent = (m.tags && m.tags.product) || '-';
  
  // 内容标签
  var contentTags = '-';
  if (m.tags && m.tags.content) {
    var cparts = [];
    for (var k in m.tags.content) {
      if (m.tags.content.hasOwnProperty(k)) {
        cparts.push(k + ':' + m.tags.content[k]);
      }
    }
    if (cparts.length > 0) contentTags = cparts.join(' | ');
  }
  document.getElementById("detailContentTags").textContent = contentTags;
  
  document.getElementById("msPreviewModal").classList.add("active");
  document.body.style.overflow = "hidden";
}"""

content = content.replace(old_preview_func, new_preview_func)
print("步骤3 ✅ 更新 openMsPreview 函数填充新字段")

# === 4. 添加 filterByFolder 函数供父页面调用 ===
old_init_end = "// ========== 初始化"
new_before_init = """// ========== 供父页面调用的函数 ==========
function filterByFolder(folderId) {
  // 从父页面菜单点击文件夹时调用
  if (folderId === null) {
    // 全部
    document.getElementById('folderFilter').value = '';
    document.getElementById('folderFilter2').value = '';
  } else if (folderId === '__uncategorized') {
    document.getElementById('folderFilter').value = '__uncategorized';
    document.getElementById('folderFilter2').value = '__uncategorized';
  } else {
    document.getElementById('folderFilter').value = String(folderId);
    document.getElementById('folderFilter2').value = String(folderId);
  }
  applyMsFilter();
}

function getFoldersData() {
  // 返回文件夹数据供父页面使用
  return JSON.parse(JSON.stringify(msFolders));
}

// ========== 初始化
"""

content = content.replace(old_init_end, new_before_init)
print("步骤4 ✅ 添加 filterByFolder 和 getFoldersData 函数")

# 保存
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"\n✅ 全部完成！文件大小: {len(content)} 字节")
