---
layout: post
title: "GitHub README Best Practices: How to Write a README That Gets Stars"
date: 2026-03-29
canonical_url: https://gingiris.github.io/growth-tools/blog/2026/03/29/github-readme-best-practices-how-to-write-a-readme-that-gets-stars/
image: "https://gingiris.github.io/growth-tools/assets/images/blog-github-stars.jpg"
---
---

## Why Your README Matters

Your README is your project's landing page. It's often the difference between someone starring your repo or bouncing in 3 seconds.

I'm Iris, former cofounder & COO of [AFFiNE](https://github.com/toeverything/AFFiNE) (60k+ GitHub stars). After helping grow multiple open source projects, I've learned that **README quality directly correlates with star growth**.

| Project | Stars | README Quality |
|---------|-------|----------------|
| AFFiNE | 60k+ | Optimized |
| Average OSS | <100 | Minimal |

---

## GitHub README Best Practices

### 1. Start With a Clear Value Proposition

The first 2 lines should answer: **What is this? Why should I care?**

```markdown
# ProjectName

> One-line description of what it does and why it matters
```

❌ Bad: "A tool for developers"
✅ Good: "Open-source Notion alternative with real-time collaboration — 60k+ stars"

### 2. Add Visual Proof Immediately

After the title, show don't tell:

- **GIF demo** (15-30 seconds max)
- **Screenshot** of the main interface
- **Architecture diagram** for technical projects

```markdown
<div align="center">
  <img src="demo.gif" alt="Product Demo" width="600" />
</div>
```

### 3. Badges That Matter

Only include badges that build trust:

| Badge Type | Why Include |
|:-----------|:------------|
| Stars | Social proof |
| License | Legal clarity |
| Build status | Quality signal |
| Last commit | Active maintenance |

Skip: Download counts, coverage %, and vanity metrics.

### 4. Quick Start in 30 Seconds

Users want to try before they commit. Make it copy-paste simple:

```markdown
## Quick Start

```bash
npm install your-package
your-package init
```

That's it! Open http://localhost:3000 to see it running.
```markdown

### 5. Feature List as a Table

Tables are scannable. Bullet lists are not.

```markdown
## Features

| Feature | Description |
|:--------|:------------|
| Real-time sync | Collaborate with your team instantly |
| Offline mode | Works without internet |
| Self-hosted | Your data, your servers |
```

### 6. The "Why" Section

Explain the problem you're solving. This builds emotional connection:

```markdown
## Why ProjectName?

Existing tools are either:
- Too expensive for indie developers
- Too complex for simple use cases
- Not open source

We built ProjectName because [personal story].
```

### 7. Clear Documentation Links

Don't dump everything in the README. Link out:

```markdown
## Documentation

- [Getting Started](docs/getting-started.md)
- [API Reference](docs/api.md)
- [Contributing](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)
```

### 8. Contribution Invitation

Make it welcoming:

```markdown
## Contributing

We love contributions! See our [Contributing Guide](CONTRIBUTING.md) to get started.

Not sure where to start? Check issues labeled `good first issue`.
```

---

## README Template

Here's a battle-tested template:

```markdown
<div align="center">
  <img src="logo.png" width="120" />
  <h1>Project Name</h1>
  <p>One-line value proposition</p>
  
  <!-- Badges -->
  [![Stars](badge)](link)
  [![License](badge)](link)
</div>

<div align="center">
  <img src="demo.gif" width="600" />
</div>

## Quick Start
[30-second setup]

## Features
[Table format]

## Why This Project?
[Problem + Story]

## Documentation
[Links]

## Contributing
[Invitation]

## License
[MIT/Apache/etc]
```

---

## FAQ: GitHub README

### How long should a README be?

**500-1500 words** is the sweet spot. Long enough to be comprehensive, short enough to be read. Use documentation links for details.

### Should I include installation for every platform?

No. Include the most common method (usually npm/pip/brew), then link to detailed installation docs.

### What's the best format for images?

- **GIFs** for demos (< 5MB)
- **PNGs** for screenshots
- **SVGs** for diagrams and logos

Host images in the repo's `/assets` folder or use a CDN.

### Should I translate my README?

For global reach, yes. Use language links at the top:

```markdown
**[English](README.md) | [中文](README-zh.md) | [日本語](README-ja.md)**
```

---

## Common README Mistakes

| Mistake | Fix |
|:--------|:----|
| Wall of text | Use headers, tables, and whitespace |
| No visuals | Add GIF demo or screenshot |
| Complex setup | Simplify to 2-3 commands |
| Missing "why" | Add motivation section |
| Outdated info | Set up CI to check links |
| No contribution guide | Add CONTRIBUTING.md |

---

## README Checklist

```markdown
□ Clear one-line description
□ Visual demo (GIF/screenshot)
□ Essential badges only
□ Quick start (< 30 seconds)
□ Features table
□ "Why" section with story
□ Documentation links
□ Contributing invitation
□ License
```

---

## Real Examples

Projects with excellent READMEs:

| Project | Stars | Why It Works |
|:--------|:------|:-------------|
| [AFFiNE](https://github.com/toeverything/AFFiNE) | 60k+ | Clear value prop, visual demo, feature table |
| [Supabase](https://github.com/supabase/supabase) | 70k+ | Instant demo, comparison table |
| [Excalidraw](https://github.com/excalidraw/excalidraw) | 80k+ | Interactive demo link, minimal text |

---

## Summary

Your README is your project's first impression. Invest time in:

1. **Clear value proposition** — What and why in 2 lines
2. **Visual proof** — GIF or screenshot immediately
3. **30-second quick start** — Copy-paste simple
4. **Scannable structure** — Tables over bullet lists
5. **Emotional connection** — Tell your "why"

A great README doesn't just document — it sells.

---

## Free Resources

- 📚 [Open Source Marketing Playbook](https://github.com/Gingiris/gingiris-opensource) — How to grow GitHub stars
- 📚 [Product Hunt Launch Guide](https://github.com/Gingiris/gingiris-launch) — Launch strategy from 30x #1 winner

---

**Questions?** Drop a comment or reach out on [Twitter @WeiYipei](https://x.com/WeiYipei).

*This guide is part of the [Gingiris Open Source Playbook](https://github.com/Gingiris/gingiris-opensource) — battle-tested strategies from 60k+ GitHub stars.*

---

## 📚 Related Reading

| Category | Article |
|----------|---------|
| 📖 | [How to Get GitHub Stars](https://gingiris.github.io/growth-tools/blog/2026/03/25/how-to-get-more-github-stars-the-definitive-guide-33k-stars-case-study/) |
| 📖 | [Developer Marketing Playbook](https://gingiris.github.io/growth-tools/blog/2026/03/24/developer-marketing-playbook-how-to-reach-technical-audiences-in-2026/) |

*More tools → [Growth Tools Directory](https://gingiris.github.io/growth-tools/)*

