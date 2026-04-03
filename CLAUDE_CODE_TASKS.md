# Claude Code 任务卡 — Growth Tools Blog SEO 修复

## 当前状态

### ✅ 已完成
- Labnana API 生图 17 张 (2K/16:9)
- 工具站 (growth-tools.github.io) 3 个工具详情页 SEO 完整
- `og:image` + `twitter:image` + `ItemList JSON-LD` + AI bots (GPTBot/ClaudeBot/PerplexityBot)
- `/tools/` 工具索引页 + 3 个工具详情页全部 200
- Blog 33 篇 post，29 篇已有 frontmatter

### ⚠️ 核心问题（需要修复）

#### 1. 9 篇 post 缺 hero image

这些 post 有 frontmatter 但缺 `image:` 字段：
- `2024-09-23-meet-ten-the-worlds-first-truly-realtime-multimodal-agent-framework-for-creating-nextgen-ai-agents.md`
- `2026-03-07-i-led-affine-from-0-to-60k-github-stars-here-are-my-open-source-growth-playbooks.md`
- `2026-03-08-ai-beta.md`
- `2026-03-08-ru-he-li-yong-gong-xian-zhe-ru-men-wen-dang-kuai-su-ti-sheng-kai-yuan-xiang-mu-zeng-chang.md`
- `2026-04-02-best-social-media-listening-tools-startups-2026.md`
- `2026-04-02-best-growth-tools-for-saas-2026.md`
- `2026-04-02-best-kol-marketing-tools-2026.md`
- `2026-04-03-developer-marketing-how-to-reach-technical-audiences.md`
- `2026-04-03-open-source-marketing-the-complete-guide.md`

#### 2. 图片文件不存在
本地缺以下 4 张图（需要重新生成或找现成的）：
```
assets/images/blog-devrel-dashboard.jpg     # 缺
assets/images/blog-growth-tools-saas.jpg    # 缺
assets/images/blog-kol-tools.jpg           # 缺
assets/images/blog-social-media-listening.jpg  # 缺
```
(INDIE HACKER 图缺但 Indie Hacker 文章已删除，不需要)

#### 3. GitHub Pages URL 问题
Auto-generated posts (2026-04-02 批量创建) 的 URL 格式可能是 `blog/2026/04/DD/slug/` 而不是 `blog/YYYY/MM/slug/`，导致 404

## 已生成的图片文件 (21 张)
```
blog-ai-product-launch.jpg
blog-aso-optimization.jpg
blog-community-building.jpg
blog-developer-marketing.jpg
blog-github-history.jpg
blog-github-stars.jpg
blog-growth-hacking.jpg
blog-indie-hacker.jpg
blog-kol-marketing.jpg
blog-open-source-marketing.jpg
blog-ph-comment-generator.jpg
blog-product-hunt-launch.jpg
blog-reddit-marketing.jpg
blog-saas-gtm.jpg
blog-seo-analytics.jpg
blog-startup-launch.jpg
blog-startup-marketing.jpg
blog-user-interview.jpg
og-banner.jpg
github-issue-generator-hero.jpg
github-readme-generator-hero.jpg
ph-comment-generator-hero.jpg
labnana-test.jpg
```

## 工具站 URL 格式
Jekyll permalink: `/:lang/blog/:year/:month/:title/`
实际 URL 格式: `blog/YYYY/MM/slug/` (无日期在 URL 里，slug 不带日期前缀)
sitemap 示例: `blog/2026/03/developer-marketing-101-how-to-grow-your-open-source-project/`

## 需要做的任务

### 任务 1: 补完 9 篇缺图的 post
用 Labnana API 为每篇文章生成对应配图并加入 frontmatter。

**Labnana API**:
- Endpoint: `POST https://api.labnana.com/openapi/v1/images/generation`
- API Key: `lh_sk_69ceb76c8b4aa61b70faf879_ab0779049625e6eac66e7bac583e065b2204a9d392f00c6e`
- 模型: `gemini-3.1-flash-image-preview` (10积分/张，500/月额度)
- 提示词风格参考: Nano Banana Pro prompts (结构化 + 明确布局，如 "dark mode dashboard UI, KPI cards, 16:9"

**每篇文章对应的图主题**:
- AI agent 框架 → `blog-devrel-dashboard.jpg`
- AFFiNE case → `blog-github-stars.jpg`
- AI beta → `blog-ai-product-launch.jpg`
- 贡献者文档 → `blog-community-building.jpg`
- social media listening → `blog-social-media-listening.jpg`
- best growth tools SaaS → `blog-growth-tools-saas.jpg`
- best KOL tools → `blog-kol-tools.jpg`
- developer marketing → `blog-developer-rel-dashboard.jpg`
- open source marketing → `blog-open-source-marketing.jpg`

### 任务 2: 修复 GitHub Pages URL 问题
如果文章 404，检查 `_config.yml` 的 `permalink` 设置和实际 URL 格式。
sitemap 里正确的 URL 格式是 `blog/YYYY/MM/slug/`（无日期在 slug 里）。

### 任务 3: Nano Banana Prompt 学习
参考 `/tmp/nanobananaprompts/` 里的结构，改进生图 prompt：
- Bento grid dashboard 风格
- 明确 dark mode / 16:9 / KPI cards
- 图文布局要求

## Labnana 生图脚本
```bash
./scripts/labnana-img.sh "prompt" "output.jpg" 2K 16:9
```

## API 额度查询
```bash
curl -s "https://api.labnana.com/openapi/v1/user/subscription" \
  -H "Authorization: Bearer lh_sk_69ceb76c8b4aa61b70faf879_ab0779049625e6eac66e7bac583e065b2204a9d392f00c6e"
```

## 提交规范
每次改动后：
1. `git add -A && git commit -m "fix: [brief desc]"`
2. `git push` (可能需要 `git pull --rebase` 解决冲突)
3. 等 2-3 分钟 GitHub Pages rebuild
4. 验证页面 200 + hero image 渲染
