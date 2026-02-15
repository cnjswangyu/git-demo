# Git + AI 超实用技巧

## 1. AI 生成 Commit Message（最常用！）

**传统方式（头疼）**：
```bash
# 想半天不知道写什么 commit message
git commit -m "update stuff"  # 糟糕的信息
```

**AI 方式（推荐）**：
使用 GitHub Copilot CLI 或类似工具：
```bash
# 先暂存更改
git add .

# 让 AI 分析差异并生成 commit message
git diff --staged | ai "生成一个规范的 git commit message，遵循 Conventional Commits 规范"
```

**Conventional Commits 规范**：
```
<type>(<scope>): <description>

类型：
- feat: 新功能
- fix: 修复 bug
- docs: 文档更新
- style: 代码格式调整
- refactor: 重构
- test: 测试相关
- chore: 构建/工具链相关
```

示例：
- `feat(auth): add JWT token refresh`
- `fix(checkout): resolve race condition in payment processing`
- `docs: update API documentation for v2 endpoints`

---

## 2. AI 解释代码变更

```bash
# 让 AI 解释某次提交改了什么
git show <commit-hash> | ai "解释这次代码变更的目的和影响"
```

---

## 3. AI 辅助 Code Review

```bash
# 查看差异并让 AI 做初步审查
git diff main...feature-branch | ai "审查这个 PR 的代码，找出潜在问题：
1. 逻辑错误
2. 性能问题
3. 安全隐患
4. 代码风格问题
5. 测试缺失"
```

---

## 4. AI 生成 Git 命令

```bash
# 忘了怎么操作？问 AI！
ai "我想撤销最后一次 commit 但保留代码更改，git 命令是什么？"
# 答案：git reset --soft HEAD~1
```

---

## 5. AI 解决合并冲突

当遇到冲突时：
```bash
# 1. 查看冲突
git status

# 2. 让 AI 帮忙分析冲突
git diff | ai "分析这个 git 合并冲突，建议如何解决"

# 3. 手动编辑后标记解决
git add <conflicted-file>
git commit
```

---

## 6. 实用 Git Aliases（配合 AI 更香）

在 `~/.gitconfig` 中添加：
```ini
[alias]
    # 好看的 log
    lg = log --graph --pretty=format:'%C(auto)%h%d %s %C(green)(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
    
    # 查看当前状态
    s = status -sb
    
    # 快速提交
    c = commit -m
    
    # 撤销最后一次 commit（保留代码）
    undo = reset --soft HEAD~1
    
    # 查看最近的提交
    last = log -1 HEAD
    
    # 查看某个文件的历史
    hist = log --follow -p
```

使用：
```bash
git lg      # 漂亮的历史图
git s       # 简洁状态
git c "feat: add new feature"
git undo    # 撤销最后一次 commit
```

---

## 7. AI 辅助编写 `.gitignore`

```bash
ai "为 Python + Node.js 项目生成一个 .gitignore 文件"
```

---

## 8. 实际工作流示例

### 场景：开发一个新功能

1. **创建分支**
   ```bash
   git checkout -b feat/user-profile
   ```

2. **写代码**
   ```python
   # ... 写了一堆代码 ...
   ```

3. **查看变更**
   ```bash
   git diff
   ```

4. **AI 生成 commit message**
   ```bash
   git add .
   git diff --staged | ai "生成 Conventional Commits 规范的 commit message"
   # AI 返回：feat(profile): add user profile editing with validation
   git commit -m "feat(profile): add user profile editing with validation"
   ```

5. **推送并创建 PR**
   ```bash
   git push origin feat/user-profile
   ```

6. **AI 辅助写 PR 描述**
   ```bash
   git log main..feat/user-profile --oneline | ai "基于这些 commit 写一个 PR 描述"
   ```

---

## 推荐工具

- **GitHub Copilot** - IDE 内实时辅助
- **GitHub Copilot CLI** - 命令行 AI 助手
- **Cursor / Windsurf** - AI 优先的代码编辑器
- **GitButler** - AI 驱动的 Git 客户端
- **Sourcegraph Cody** - 代码理解 AI
