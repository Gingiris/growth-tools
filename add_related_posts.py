#!/usr/bin/env python3
"""Add related posts section to each blog post for internal linking SEO boost."""

import os
import re

POSTS_DIR = "_posts"

# Related posts mapping
RELATED = {
    "2026-03-30-reddit-marketing-guide-how-to-promote-without-getting-banned.md": [
        ("Product Hunt Launch: 30x #1 Winner's Guide", "/blog/2026/03/25/product-hunt-launch-playbook-the-definitive-guide-30x-1-winner/"),
        ("SaaS Go-to-Market Strategy", "/blog/2026/03/27/saas-gotomarket-strategy-the-complete-framework-from-0-to-10m-arr/"),
    ],
    "2026-03-25-product-hunt-launch-playbook-the-definitive-guide-30x-1-winner.md": [
        ("How to Launch on Product Hunt", "/blog/2026/03/29/how-to-launch-on-product-hunt-stepbystep-guide-30x-1-winner/"),
        ("Reddit Marketing Without Getting Banned", "/blog/2026/03/30/reddit-marketing-guide-how-to-promote-without-getting-banned/"),
    ],
    "2026-03-29-how-to-launch-on-product-hunt-stepbystep-guide-30x-1-winner.md": [
        ("PH Launch Checklist", "/blog/2026/03/31/product-hunt-launch-checklist-30time-1-winners-playbook/"),
        ("Startup Marketing Strategy", "/blog/2026/04/01/startup-marketing-strategy-from-zero-to-first-1000-users/"),
    ],
    "2026-03-31-product-hunt-launch-checklist-30time-1-winners-playbook.md": [
        ("How to Launch on Product Hunt", "/blog/2026/03/29/how-to-launch-on-product-hunt-stepbystep-guide-30x-1-winner/"),
        ("Reddit Marketing Guide", "/blog/2026/03/30/reddit-marketing-guide-how-to-promote-without-getting-banned/"),
    ],
    "2026-03-29-product-hunt-launch-checklist-the-complete-2026-guide-from-30x-daily-1-experience.md": [
        ("PH Playbook", "/blog/2026/03/25/product-hunt-launch-playbook-the-definitive-guide-30x-1-winner/"),
        ("How to Launch", "/blog/2026/03/29/how-to-launch-on-product-hunt-stepbystep-guide-30x-1-winner/"),
    ],
    "2026-03-18-product-hunt-launch-the-2026-playbook-for-winning-1.md": [
        ("PH Launch Checklist", "/blog/2026/03/31/product-hunt-launch-checklist-30time-1-winners-playbook/"),
        ("Startup Marketing", "/blog/2026/04/01/startup-marketing-strategy-from-zero-to-first-1000-users/"),
    ],
    "2026-03-25-how-to-get-more-github-stars-the-definitive-guide-33k-stars-case-study.md": [
        ("Star Growth Tactics: 10 Proven Ways", "/blog/2026/03/27/github-star-growth-10-proven-tactics-that-got-us-33k-stars/"),
        ("GitHub Stars History", "/blog/2026/03/30/github-stars-history-how-to-track-and-analyze-repository-growth/"),
    ],
    "2026-03-27-github-star-growth-10-proven-tactics-that-got-us-33k-stars.md": [
        ("How to Get More GitHub Stars", "/blog/2026/03/25/how-to-get-more-github-stars-the-definitive-guide-33k-stars-case-study/"),
        ("Developer Marketing 101", "/blog/2026/03/25/developer-marketing-101-how-to-grow-your-open-source-project/"),
    ],
    "2026-03-29-github-readme-best-practices-how-to-write-a-readme-that-gets-stars.md": [
        ("How to Get GitHub Stars", "/blog/2026/03/25/how-to-get-more-github-stars-the-definitive-guide-33k-stars-case-study/"),
        ("Developer Marketing Playbook", "/blog/2026/03/24/developer-marketing-playbook-how-to-reach-technical-audiences-in-2026/"),
    ],
    "2026-03-30-github-stars-history-how-to-track-and-analyze-repository-growth.md": [
        ("Star Growth Tactics", "/blog/2026/03/27/github-star-growth-10-proven-tactics-that-got-us-33k-stars/"),
        ("How to Get GitHub Stars", "/blog/2026/03/25/how-to-get-more-github-stars-the-definitive-guide-33k-stars-case-study/"),
    ],
    "2026-03-31-github-stars-history.md": [
        ("GitHub README Best Practices", "/blog/2026/03/29/github-readme-best-practices-how-to-write-a-readme-that-gets-stars/"),
        ("Star Growth Tactics", "/blog/2026/03/27/github-star-growth-10-proven-tactics-that-got-us-33k-stars/"),
    ],
    "2026-03-25-developer-marketing-101-how-to-grow-your-open-source-project.md": [
        ("Developer Marketing Playbook", "/blog/2026/03/24/developer-marketing-playbook-how-to-reach-technical-audiences-in-2026/"),
        ("GitHub README Best Practices", "/blog/2026/03/29/github-readme-best-practices-how-to-write-a-readme-that-gets-stars/"),
    ],
    "2026-03-24-developer-marketing-playbook-how-to-reach-technical-audiences-in-2026.md": [
        ("Developer Marketing 101", "/blog/2026/03/25/developer-marketing-101-how-to-grow-your-open-source-project/"),
        ("How to Get GitHub Stars", "/blog/2026/03/25/how-to-get-more-github-stars-the-definitive-guide-33k-stars-case-study/"),
    ],
    "2026-03-15-aso-app-store-optimization-complete-2026-playbook.md": [
        ("ASO Complete Guide 2026", "/blog/2026/03/29/aso-guide-app-store-optimization-complete-guide-2026/"),
        ("Startup Marketing Strategy", "/blog/2026/04/01/startup-marketing-strategy-from-zero-to-first-1000-users/"),
    ],
    "2026-03-29-aso-guide-app-store-optimization-complete-guide-2026.md": [
        ("ASO Playbook", "/blog/2026/03/15/aso-app-store-optimization-complete-2026-playbook/"),
        ("SaaS Growth Strategy", "/blog/2026/03/29/saas-growth-strategy-complete-framework-from-0-to-10m-arr/"),
    ],
    "2026-03-27-saas-gotomarket-strategy-the-complete-framework-from-0-to-10m-arr.md": [
        ("SaaS Growth Strategy", "/blog/2026/03/29/saas-growth-strategy-complete-framework-from-0-to-10m-arr/"),
        ("Startup Marketing Strategy", "/blog/2026/04/01/startup-marketing-strategy-from-zero-to-first-1000-users/"),
    ],
    "2026-03-29-saas-growth-strategy-complete-framework-from-0-to-10m-arr.md": [
        ("SaaS Go-to-Market", "/blog/2026/03/27/saas-gotomarket-strategy-the-complete-framework-from-0-to-10m-arr/"),
        ("Product Hunt Launch Playbook", "/blog/2026/03/25/product-hunt-launch-playbook-the-definitive-guide-30x-1-winner/"),
    ],
    "2026-04-01-startup-marketing-strategy-from-zero-to-first-1000-users.md": [
        ("Product Hunt Launch Playbook", "/blog/2026/03/18/product-hunt-launch-the-2026-playbook-for-winning-1/"),
        ("SaaS Go-to-Market Strategy", "/blog/2026/03/27/saas-gotomarket-strategy-the-complete-framework-from-0-to-10m-arr/"),
    ],
    "2026-03-25-startup-launch-checklist-47-tasks-before-during-after-launch-day.md": [
        ("Product Hunt Launch Playbook", "/blog/2026/03/25/product-hunt-launch-playbook-the-definitive-guide-30x-1-winner/"),
        ("Startup Marketing Strategy", "/blog/2026/04/01/startup-marketing-strategy-from-zero-to-first-1000-users/"),
    ],
    "2026-03-25-how-to-conduct-user-interviews-the-937interview-framework-that-found-pmf.md": [
        ("Startup Marketing Strategy", "/blog/2026/04/01/startup-marketing-strategy-from-zero-to-first-1000-users/"),
        ("SaaS Growth Strategy", "/blog/2026/03/29/saas-growth-strategy-complete-framework-from-0-to-10m-arr/"),
    ],
    "2026-03-30-geo-optimization-guide.md": [
        ("Startup Marketing Strategy", "/blog/2026/04/01/startup-marketing-strategy-from-zero-to-first-1000-users/"),
        ("100+ Growth Tools for Startups", "/blog/2026/03/30/100-growth-tools-for-startups-going-global-2026-edition/"),
    ],
    "2026-03-30-100-growth-tools-for-startups-going-global-2026-edition.md": [
        ("Startup Marketing Strategy", "/blog/2026/04/01/startup-marketing-strategy-from-zero-to-first-1000-users/"),
        ("Reddit Marketing Guide", "/blog/2026/03/30/reddit-marketing-guide-how-to-promote-without-getting-banned/"),
    ],
}

RELATED_SECTION = '''
---

## 📚 Related Reading

| Category | Article |
|----------|---------|
{rows}

*More tools → [Growth Tools Directory](https://gingiris.github.io/growth-tools/)*

'''

def make_row(title, url):
    base = "https://gingiris.github.io/growth-tools"
    full_url = f"{base}{url}" if url.startswith("/") else url
    return f"| 📖 | [{title}]({full_url}) |"

def add_related_posts(filepath):
    filename = os.path.basename(filepath)
    if filename not in RELATED:
        return False
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Skip if already has related section
    if "## 📚 Related Reading" in content or "## Related Reading" in content:
        print(f"SKIP: {filename} (already has related)")
        return False
    
    rows = "\n".join(make_row(t, u) for t, u in RELATED[filename])
    section = RELATED_SECTION.format(rows=rows)
    
    # Append before trailing ---
    if content.rstrip().endswith("---"):
        content = content.rstrip()[:-3] + section + "\n---\n"
    else:
        content = content.rstrip() + "\n" + section
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"ADDED: {filename}")
    return True

def main():
    count = 0
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith('.md'):
            filepath = os.path.join(POSTS_DIR, filename)
            if add_related_posts(filepath):
                count += 1
    print(f"\nDone: added related posts to {count} articles")

if __name__ == "__main__":
    main()
