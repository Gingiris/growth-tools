---
layout: post
title: "GitHub Issue Template: How to Get More Contributions and Build Community"
date: 2026-04-02
canonical_url: https://gingiris.github.io/growth-tools/blog/2026/04/github-issue-template-guide/
image: "https://gingiris.github.io/growth-tools/assets/images/blog-github-stars.jpg"
description: "How to write GitHub issue templates that get better bug reports. Ready-to-use templates for bug reports, feature requests, and questions — copy and paste."
faq:
  - q: "What is a GitHub issue template?"
    a: "A GitHub issue template is a pre-filled form that appears when someone opens a new issue in your repository. Templates guide contributors to provide structured, useful information — eliminating the back-and-forth of asking for reproduction steps, version numbers, and environment details. They're stored in .github/ISSUE_TEMPLATE/ as markdown files and can include required fields, dropdowns, and checkboxes."
  - q: "How do you create a GitHub issue template?"
    a: "Create a GitHub issue template by: (1) Creating the directory .github/ISSUE_TEMPLATE/ in your repository. (2) Adding a markdown file (e.g., bug_report.md) with YAML front matter specifying the template name, description, and labels. (3) Writing the template body with H2 sections for required information (Steps to Reproduce, Expected Behavior, Actual Behavior, Environment). (4) Optionally creating a config.yml in the same folder to control which issue types are available. Push to main and templates appear automatically in the issue creation flow."
  - q: "What should a bug report GitHub issue template include?"
    a: "A bug report template should include: Environment section (OS, browser/runtime version, package version), Steps to Reproduce (numbered list, minimum reproduction steps), Expected Behavior (what should happen), Actual Behavior (what actually happens, including error messages or screenshots), and Additional Context (logs, related issues, workarounds tried). Keep it short enough that reporters actually fill it out — the most useful templates take under 3 minutes to complete. Long templates lead to reporters deleting sections entirely."
---
## TL;DR

- Good issue templates increase contributor activity by 40%+
- Bug report template → better bugs, faster fixes
- Feature request template → clearer roadmap
- Pull request template → higher merge rate
- **Free templates included** — copy and use today

---

## Why Issue Templates Matter

When developers file issues without guidance, you get:

- Vague bug reports: "it doesn't work"
- Duplicate requests: "I already built this in #123"
- Missing context: no steps to reproduce

With templates, you get actionable information that moves your project forward.

---

## The 4 Essential Templates

### 1. Bug Report Template

```markdown
---
name: 🐛 Bug Report
about: Report something that isn't working
labels: bug
---

**Description**
A clear description of the bug.

**Steps to Reproduce**
1. Go to '...'
2. Click on '...'
3. See error

**Expected Behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment**
- OS: [e.g. macOS 14.0]
- Version: [e.g. 1.0.0]

**Additional Context**
Any other context about the problem.
```

### 2. Feature Request Template

```markdown
---
name: ✨ Feature Request
about: Suggest an idea for this project
labels: enhancement
---

**Problem**
What problem does this solve?

**Solution**
Describe your proposed solution.

**Alternatives**
Any alternative solutions you've considered.

**Additional Context**
Mockups, examples, references.
```

### 3. Pull Request Template

```markdown
## TL;DR
<!-- 1-3 sentences: what changed -->

## Changes
<!-- Added / Changed / Fixed -->

## Testing
<!-- How did you test this? -->

## Screenshots (if UI change)
<!-- Before → After -->

## Checklist
- [ ] Tests pass
- [ ] Documentation updated
- [ ] No console.log
```

### 4. Custom Issue Template (config.yml)

```yaml
blank_issues_enabled: false
contact_links:
  - name: ❓ Questions
    url: https://github.com/YOUR_REPO/discussions
    about: Ask questions here
  - name: 💬 Discord
    url: YOUR_DISCORD_LINK
    about: Chat with the community
```

---

## Pro Tips

### Make Templates Discoverable

Add a `ISSUE_TEMPLATE.md` at repo root:

```markdown
# Contributing

Before opening an issue:

- 🔍 Search existing issues first
- 📖 Check the FAQ in discussions
- 🐛 For bugs: use the Bug Report template
- ✨ For features: use the Feature Request template
```

### Use Labels Strategically

| Label | When to Use |
|-------|-------------|
| bug | Something is broken |
| enhancement | New feature request |
| good first issue | Easy wins for new contributors |
| documentation | Docs improvements |
| question | User questions |
| wontfix | Won't address, explain why |

### Respond to Issues Fast

- First response within 48 hours → 3x more likely to get contributions
- Label "good first issue" → attracts new contributors
- Close duplicates politely with a link to the original

---

## TL;DR Summary

- **Bug template**: Steps to reproduce + expected vs actual
- **Feature template**: Problem + solution + alternatives
- **PR template**: TL;DR + changes + testing checklist
- **Config**: Disable blank issues, add links
- **Labels**: Make them actionable
- **Speed**: Respond within 48 hours

For more open source growth strategies, see [github.com/Gingiris/gingiris-opensource](https://github.com/Gingiris/gingiris-opensource) — the complete playbook from 0 to 60k stars.

*Part of the [Gingiris Open Source Growth Playbook](https://github.com/Gingiris/gingiris-opensource) — helping developers build open source communities.*
