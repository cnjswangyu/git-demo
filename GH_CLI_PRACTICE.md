# GitHub CLI 实战指南

用当前的 git-demo 仓库演示 gh 命令的实际用法！

---

## 我们刚才做了什么？

### 1. 创建新分支并添加功能
```bash
# 创建新分支
git checkout -b feature/more-math-functions

# 添加新功能（modulo, absolute, gcd, lcm）
# 修改 calculator.py

# 提交
git add calculator.py
git commit -m "feat: add more math functions"

# 推送到远程
git push -u origin feature/more-math-functions
```

### 2. 分支已推送！
你的分支已经在 GitHub 上了：
**https://github.com/cnjswangyu/git-demo/tree/feature/more-math-functions**

---

## 现在你可以这样操作

### 方式一：在网页上创建 PR（推荐）

1. 访问：https://github.com/cnjswangyu/git-demo/pull/new/feature/more-math-functions
2. 填写 PR 标题和描述
3. 点击 "Create pull request"

### 方式二：用 gh 命令（需要网络稳定）

```bash
# 创建 PR
gh pr create --title "feat: 添加更多数学函数" --body "新增以下数学函数：
- modulo: 模运算
- absolute: 绝对值
- gcd: 最大公约数
- lcm: 最小公倍数"

# 或者打开网页创建
gh pr create --web
```

---

## gh 常用命令完整参考

### 📋 Issue 管理

```bash
# 创建 Issue
gh issue create --title "Issue 标题" --body "Issue 描述"

# 创建 Issue 并添加标签
gh issue create --title "Bug: 登录失败" --body "描述..." --label bug --label "help wanted"

# 查看所有 Issue
gh issue list

# 查看特定 Issue
gh issue view 123

# 查看 Issue 并打开网页
gh issue view 123 --web

# 关闭 Issue
gh issue close 123

# 重新打开 Issue
gh issue reopen 123

# 给 Issue 加标签
gh issue edit 123 --add-label bug --remove-label "help wanted"

# 给 Issue 分配人
gh issue edit 123 --assignee username
```

### 🔀 PR 管理

```bash
# 创建 PR（当前分支）
gh pr create --title "PR 标题" --body "PR 描述"

# 创建 PR 并指定目标分支
gh pr create --title "标题" --body "描述" --base main --head feature-branch

# 打开网页创建 PR
gh pr create --web

# 查看所有 PR
gh pr list

# 查看 PR 状态
gh pr status

# 查看特定 PR
gh pr view 123

# 查看 PR 差异
gh pr diff 123

# 查看 PR 评论
gh pr view 123 --comments

# 查看 PR 并打开网页
gh pr view 123 --web

# 切换到某个 PR 的分支
gh pr checkout 123

# 给 PR 加标签
gh pr edit 123 --add-label "enhancement"

# 给 PR 分配审查者
gh pr edit 123 --reviewer username1,username2

# 合并 PR（三种方式）
gh pr merge 123 --merge    # 创建合并提交
gh pr merge 123 --squash   # 压缩合并（推荐）
gh pr merge 123 --rebase   # 变基合并

# 关闭 PR
gh pr close 123
```

### 🏠 仓库管理

```bash
# 创建新仓库
gh repo create my-repo --public    # 公开仓库
gh repo create my-repo --private   # 私有仓库
gh repo create my-repo --source=. --push  # 用当前目录初始化并推送

# 克隆仓库
gh repo clone owner/repo

# 查看当前仓库信息
gh repo view

# 查看仓库并打开网页
gh repo view --web

# 给仓库加星
gh repo star owner/repo

# 取消星
gh repo unstar owner/repo

# Fork 仓库
gh repo fork owner/repo

# 查看仓库的 Issues
gh issue list --repo owner/repo

# 查看仓库的 PR
gh pr list --repo owner/repo
```

### 🔍 搜索

```bash
# 搜索仓库
gh search repos "git demo in:name language:python"

# 搜索 Issue
gh search issues "bug in:title repo:owner/repo"

# 搜索代码
gh search code "def add repo:owner/repo"
```

### 🔑 认证相关

```bash
# 登录
gh auth login

# 查看登录状态
gh auth status

# 登出
gh auth logout

# 刷新 token
gh auth refresh
```

### ⭐ 其他有用命令

```bash
# 查看 Gists
gh gist list

# 创建 Gist
gh gist create file.txt

# 查看 GitHub 通知
gh notification list

# 运行 GitHub Actions 工作流
gh workflow list
gh workflow run <workflow-name>
```

---

## 完整工作流示例

### 从 Issue 到 PR 的完整流程

```bash
# 1. 创建 Issue
gh issue create --title "需要添加模运算" --body "希望能有模运算功能" --label enhancement

# 2. 查看 Issue 列表
gh issue list

# 3. 创建分支并开发
git checkout main
git pull
git checkout -b feature/modulo-function
# ... 写代码 ...
git add .
git commit -m "feat: add modulo function"
git push -u origin feature/modulo-function

# 4. 创建 PR，关联 Issue
gh pr create --title "feat: 添加模运算" --body "Closes #1

新增模运算功能：
- modulo(a, b): 返回 a % b"

# 5. 查看 PR 状态
gh pr status

# 6. （审查通过后）合并 PR
gh pr merge 1 --squash

# 7. 删除分支
git checkout main
git pull
git branch -d feature/modulo-function
gh repo view --web  # 打开网页确认
```

---

## 常用快捷键/技巧

### 在 PR 描述中关联 Issue

```markdown
Closes #123   # 合并 PR 时自动关闭 Issue #123
Fixes #123    # 同上
Resolves #123  # 同上
```

### PR 模板

创建 `.github/pull_request_template.md`：
```markdown
## 描述
简要描述这个 PR 做了什么

## 关联 Issue
Closes #123

## 测试
- [ ] 测试 A 通过
- [ ] 测试 B 通过

## 截图
如果有界面改动，请放截图
```

---

## 现在去试试吧！

你的分支已经准备好了：
**https://github.com/cnjswangyu/git-demo**

去网页上创建 PR 吧！然后试试上面的各种 gh 命令！
