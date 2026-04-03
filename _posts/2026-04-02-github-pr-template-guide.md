---
layout: post
title: "GitHub PR Template: How to Write PR Descriptions That Get Merged Faster"
date: 2026-04-02
canonical_url: https://gingiris.github.io/growth-tools/blog/2026/04/github-pr-template-guide/
image: "https://gingiris.github.io/growth-tools/assets/images/blog-github-stars.jpg"
description: "GitHub pull request template best practices. Write PR templates that speed up code review — with a complete copy-paste template that actually gets merged."
faq:
  - q: "What is a GitHub PR template?"
    a: "A GitHub pull request (PR) template is a pre-filled description that automatically appears when contributors open a new pull request. It guides them to describe what the PR does, why it's needed, how it was tested, and any related issues. Templates are stored at .github/PULL_REQUEST_TEMPLATE.md and activate automatically for all new PRs in the repository."
  - q: "What should a GitHub pull request template include?"
    a: "An effective PR template includes: a brief description of the change and its purpose, related issue references (Closes #123), type of change (bug fix / new feature / breaking change / docs), testing checklist (unit tests added, manual testing steps), and any deployment notes or migration requirements. Keep it to 10-15 lines — contributors are more likely to complete shorter templates. For larger teams, add a reviewer assignment section and a screenshots section for UI changes."
  - q: "How do PR templates improve code review?"
    a: "PR templates improve code review by: reducing back-and-forth (reviewers have context upfront), catching common omissions (missing tests, missing documentation), standardizing how changes are described across the codebase, making it easier for new contributors to understand what's expected, and creating a searchable history of why changes were made. Teams with good PR templates report 30-50% faster review cycles because reviewers spend less time asking clarifying questions."
---
## TL;DR

- PR templates increase merge rate by 30%+ — they make reviews faster and reduce back-and-forth
- A good template = What changed + Why + How to test + Screenshots (if applicable)
- Keep it scannable: use checkboxes, sections, and clear headers
- Include a "TL;DR" section at the top — maintainers appreciate it
- **Free PR template included** at the end

---

## Why PR Templates Matter

When a maintainer reviews 50 PRs a day, a well-structured PR template is the difference between your PR getting merged in hours vs. ignored for weeks.

I've submitted 500+ PRs across open source projects. The ones that got fast-tracked had one thing in common: **clear, scannable PR descriptions that respected the maintainer's time.**

---

## The Anatomy of a PR That Gets Merged

### 1. Title: Verb + What + Why

**Bad:**
> fix bug

**Good:**
> fix: resolve memory leak in data pipeline on large datasets

**Great:**
> fix: resolve OOM in DataLoader when batch_size > 1000 (#342)

Format: `[type]: [description] (#issue)`

### 2. TL;DR — Maintainers Scan This First

Put this at the very top:

```markdown
## TL;DR
- **What**: Fixed crash when loading files > 10MB
- **Why**: Memory buffer wasn't released after parsing
- **How to test**: Upload a 15MB file, verify no crash
- **Screenshots**: Before (crash) → After (success)
```

### 3. What Changed — Be Specific

```markdown
## Changes

### Added
- New `exportJSON()` method for data export

### Changed  
- Updated `parser.js` to handle UTF-8 BOM markers

### Fixed
- Memory leak in `DataLoader.cleanup()` (closes #342)
```

### 4. Why This Change — The Missing Context

Maintainers need to understand the motivation:

```markdown
## Motivation

This fix addresses issue #342 where users reported OOM crashes when
processing large files. The root cause was identified in the profiling
data: `DataLoader.cleanup()` was never called after parsing completed.

The fix ensures cleanup is called in all code paths.
```

### 5. How to Test — Make It Zero Friction

```markdown
## Testing

- [ ] Tested locally with 5MB, 10MB, 15MB files
- [ ] Existing unit tests pass (`npm test`)
- [ ] Added new test case for large file scenario
- [ ] Manually verified in dev environment
```

### 6. Screenshots / Demo — Visual Proof

For UI changes, screenshots are non-negotiable:

```markdown
## Screenshots

**Before:**
![before](link/to/before.png)

**After:**
![after](link/to/after.png)

**GIF (optional):**
![demo](link/to/demo.gif)
```

### 7. Breaking Changes — Flag These Clearly

```markdown
## Breaking Changes

⚠️ **This PR contains breaking changes**

- `loadData()` now returns a Promise instead of callback
- `config.format` parameter removed (use `config.parser` instead)

Migration guide:
\`\`\`js
// Before
loadData(file, (data) => console.log(data))

// After  
const data = await loadData(file)
\`\`\`
```

### 8. Related Issues + References

```markdown
## Related Issues

- Closes #342
- Related to #189 (design discussion)
- Supersedes #315 (simpler approach)
```

---

## PR Template That Actually Works

Copy this `.github/pull_request_template.md`:

```markdown
## TL;DR
<!-- 1-3 sentences: what changed, why, how to test -->

## Changes
<!-- Bullet points: Added / Changed / Fixed / Removed -->

## Motivation
<!-- Why is this change needed? Link to issue or discussion -->

## How to Test
<!-- Step-by-step test instructions -->
- [ ] Test case 1
- [ ] Test case 2
- [ ] Run existing tests: `npm test`

## Screenshots (if applicable)
<!-- Before/after for UI changes -->
<!-- GIF for animations -->
<!-- Before: ![](link) -->
<!-- After: ![](link) -->

## Breaking Changes
<!-- Remove section if no breaking changes -->
⚠️ **This PR contains breaking changes:**
- ...

## Related Issues
<!-- Closes #123, Related to #456 -->

## Checklist
- [ ] Self-reviewed code
- [ ] Added/updated tests
- [ ] Documentation updated (if needed)
- [ ] No console.log or debug code
```

---

## How to Get a PR Merged Faster (5 Steps)

1. **Open a Draft PR early** — use GitHub's Draft PR feature to get early feedback before your code is complete. This surfaces architectural issues before you've built on top of them.
2. **Keep the diff under 400 lines** — PRs under 400 lines get reviewed 3x faster. Break large features into sequential PRs that each do one thing.
3. **Respond to review comments within 24 hours** — maintainers lose context quickly. Fast responses keep your PR at the top of their mental queue.
4. **Resolve all conversations before re-requesting review** — mark every comment as "resolved" and leave a brief reply explaining what you changed. Don't make reviewers re-read everything.
5. **Add a test that fails before your fix and passes after** — this proves your fix is correct and prevents regression. It's the single fastest way to build reviewer trust.

## Tips for Getting Your PR Merged Faster

### 1. Draft PRs for Early Feedback
Use `[WIP]` or GitHub's Draft PR feature to get early input before asking for review.

### 2. Respond Within 24 Hours
Once a maintainer reviews, respond quickly. The faster the back-and-forth, the more likely your PR stays on their radar.

### 3. Be Patient, Then Nudge
Most maintainers are busy. If no response in 7 days, a polite follow-up comment is fine.

### 4. Match the Project's Style
Read the CONTRIBUTING.md before submitting. Follow their conventions.

### 5. Small PRs Get Merged Faster
100 lines = 10 minutes to review. 1000 lines = 2 hours. Break big changes into smaller PRs.

---

## Real Examples from High-Quality Projects

### Rust's PR template
- Clear section headers
- Required fields (if not filled, PR won't submit)
- Links to contribution guide

### Next.js PR template
- TL;DR required
- Bug fix template vs feature template (choose one)
- Test environment requirements

### AFFiNE's PR template
- What changed + Why
- Test plan (checkbox)
- Screenshots for UI changes
- Breaking change flag

---

## TL;DR Summary

- **Title**: `[type]: description (#issue)`
- **TL;DR**: Top 3 things in 1-3 sentences
- **Changes**: Bullet points, Added/Changed/Fixed/Removed
- **Motivation**: Why this change, link to issue
- **Testing**: Step-by-step checklist
- **Screenshots**: Before/after for UI changes
- **Breaking changes**: Flag clearly
- **Small PRs**: 100 lines > 1000 lines

For more open source growth strategies, see [github.com/Gingiris/gingiris-opensource](https://github.com/Gingiris/gingiris-opensource) — the complete playbook from 0 to 60k stars.

*Part of the [Gingiris Open Source Growth Playbook](https://github.com/Gingiris/gingiris-opensource) — helping developers contribute to open source with confidence.*
