#!/bin/bash
# Add related posts section to each markdown file
# Usage: ./add_related_posts.sh

POSTS_DIR="_posts"

# Related posts mapping (topic clusters)
declare -A LINKS
LINKS["2026-03-30-reddit-marketing-guide-how-to-promote-without-getting-banned.md"]="| Reddit Marketing | [Product Hunt Launch: 30x #1 Guide](/blog/2026/03/25/product-hunt-launch-playbook-the-definitive-guide-30x-1-winner/) | [SaaS Go-to-Market](/blog/2026/03/27/saas-gotomarket-strategy-the-complete-framework-from-0-to-10m-arr/) |"
LINKS["2026-03-25-product-hunt-launch-playbook-the-definitive-guide-30x-1-winner.md"]="| Product Hunt | [Reddit Marketing Without Bans](/blog/2026/03/30/reddit-marketing-guide-how-to-promote-without-getting-banned/) | [Startup Launch Checklist](/blog/2026/03/25/startup-launch-checklist-47-tasks-before-during-after-launch-day/) |"
LINKS["2026-03-29-how-to-launch-on-product-hunt-stepbystep-guide-30x-1-winner.md"]="| Product Hunt | [PH Launch Checklist](/blog/2026/03/31/product-hunt-launch-checklist-30time-1-winners-playbook/) | [Startup Marketing](/blog/2026/04/01/startup-marketing-strategy-from-zero-to-first-1000-users/) |"
LINKS["2026-03-31-product-hunt-launch-checklist-30time-1-winners-playbook.md"]="| Product Hunt | [How to Launch on PH](/blog/2026/03/29/how-to-launch-on-product-hunt-stepbystep-guide-30x-1-winner/) | [Reddit Marketing](/blog/2026/03/30/reddit-marketing-guide-how-to-promote-without-getting-banned/) |"
LINKS["2026-03-29-product-hunt-launch-checklist-the-complete-2026-guide-from-30x-daily-1-experience.md"]="| Product Hunt | [How to Launch on PH](/blog/2026/03/29/how-to-launch-on-product-hunt-stepbystep-guide-30x-1-winner/) | [PH Playbook](/blog/2026/03/25/product-hunt-launch-playbook-the-definitive-guide-30x-1-winner/) |"
LINKS["2026-03-25-how-to-get-more-github-stars-the-definitive-guide-33k-stars-case-study.md"]="| GitHub Stars | [Star Growth Tactics](/blog/2026/03/27/github-star-growth-10-proven-tactics-that-got-us-33k-stars/) | [GitHub Stars History](/blog/2026/03/30/github-stars-history-how-to-track-and-analyze-repository-growth/) |"
LINKS["2026-03-27-github-star-growth-10-proven-tactics-that-got-us-33k-stars.md"]="| GitHub Stars | [How to Get Stars](/blog/2026/03/25/how-to-get-more-github-stars-the-definitive-guide-33k-stars-case-study/) | [Developer Marketing](/blog/2026/03/25/developer-marketing-101-how-to-grow-your-open-source-project/) |"
LINKS["2026-03-29-github-readme-best-practices-how-to-write-a-readme-that-gets-stars.md"]="| GitHub Stars | [How to Get Stars](/blog/2026/03/25/how-to-get-more-github-stars-the-definitive-guide-33k-stars-case-study/) | [Developer Marketing](/blog/2026/03/24/developer-marketing-playbook-how-to-reach-technical-audiences-in-2026/) |"
LINKS["2026-03-30-github-stars-history-how-to-track-and-analyze-repository-growth.md"]="| GitHub Stars | [Star Growth](/blog/2026/03/27/github-star-growth-10-proven-tactics-that-got-us-33k-stars/) | [How to Get Stars](/blog/2026/03/25/how-to-get-more-github-stars-the-definitive-guide-33k-stars-case-study/) |"
LINKS["2026-03-31-github-stars-history.md"]="| GitHub Stars | [GitHub README Guide](/blog/2026/03/29/github-readme-best-practices-how-to-write-a-readme-that-gets-stars/) | [Star Growth](/blog/2026/03/27/github-star-growth-10-proven-tactics-that-got-us-33k-stars/) |"
LINKS["2026-03-25-developer-marketing-101-how-to-grow-your-open-source-project.md"]="| Developer | [Dev Marketing Playbook](/blog/2026/03/24/developer-marketing-playbook-how-to-reach-technical-audiences-in-2026/) | [GitHub README](/blog/2026/03/29/github-readme-best-practices-how-to-write-a-readme-that-gets-stars/) |"
LINKS["2026-03-24-developer-marketing-playbook-how-to-reach-technical-audiences-in-2026.md"]="| Developer | [Dev Marketing 101](/blog/2026/03/25/developer-marketing-101-how-to-grow-your-open-source-project/) | [GitHub Stars](/blog/2026/03/25/how-to-get-more-github-stars-the-definitive-guide-33k-stars-case-study/) |"
LINKS["2026-03-15-aso-app-store-optimization-complete-2026-playbook.md"]="| ASO | [ASO Guide 2026](/blog/2026/03/29/aso-guide-app-store-optimization-complete-guide-2026/) | [Startup Marketing](/blog/2026/04/01/startup-marketing-strategy-from-zero-to-first-1000-users/) |"
LINKS["2026-03-29-aso-guide-app-store-optimization-complete-guide-2026.md"]="| ASO | [ASO Playbook](/blog/2026/03/15/aso-app-store-optimization-complete-2026-playbook/) | [SaaS Growth](/blog/2026/03/29/saas-growth-strategy-complete-framework-from-0-to-10m-arr/) |"
LINKS["2026-03-27-saas-gotomarket-strategy-the-complete-framework-from-0-to-10m-arr.md"]="| SaaS | [SaaS Growth](/blog/2026/03/29/saas-growth-strategy-complete-framework-from-0-to-10m-arr/) | [Startup Marketing](/blog/2026/04/01/startup-marketing-strategy-from-zero-to-first-1000-users/) |"
LINKS["2026-03-29-saas-growth-strategy-complete-framework-from-0-to-10m-arr.md"]="| SaaS | [SaaS GTM](/blog/2026/03/27/saas-gotomarket-strategy-the-complete-framework-from-0-to-10m-arr/) | [Product Hunt](/blog/2026/03/25/product-hunt-launch-playbook-the-definitive-guide-30x-1-winner/) |"
LINKS["2026-04-01-startup-marketing-strategy-from-zero-to-first-1000-users.md"]="| Startup | [Product Hunt Launch](/blog/2026/03/18/product-hunt-launch-the-2026-playbook-for-winning-1/) | [SaaS GTM](/blog/2026/03/27/saas-gotomarket-strategy-the-complete-framework-from-0-to-10m-arr/) |"
LINKS["2026-03-25-startup-launch-checklist-47-tasks-before-during-after-launch-day.md"]="| Startup | [PH Launch](/blog/2026/03/25/product-hunt-launch-playbook-the-definitive-guide-30x-1-winner/) | [Startup Marketing](/blog/2026/04/01/startup-marketing-strategy-from-zero-to-first-1000-users/) |"
LINKS["2026-03-25-how-to-conduct-user-interviews-the-937interview-framework-that-found-pmf.md"]="| User Research | [Startup Marketing](/blog/2026/04/01/startup-marketing-strategy-from-zero-to-first-1000-users/) | [SaaS Growth](/blog/2026/03/29/saas-growth-strategy-complete-framework-from-0-to-10m-arr/) |"
LINKS["2026-03-30-geo-optimization-guide.md"]="| SEO/GEO | [Startup Marketing](/blog/2026/04/01/startup-marketing-strategy-from-zero-to-first-1000-users/) | [Growth Tools](/blog/2026/03/30/100-growth-tools-for-startups-going-global-2026-edition/) |"
LINKS["2026-03-30-100-growth-tools-for-startups-going-global-2026-edition.md"]="| Growth | [Startup Marketing](/blog/2026/04/01/startup-marketing-strategy-from-zero-to-first-1000-users/) | [Reddit Marketing](/blog/2026/03/30/reddit-marketing-guide-how-to-promote-without-getting-banned/) |"

RELATED_TEMPLATE='
---

## 📚 Related Reading

%LINKS%

*More tools → [Growth Tools Directory](https://gingiris.github.io/growth-tools/)*
'

count=0
for file in "$POSTS_DIR"/*.md; do
  filename=$(basename "$file")
  
  # Check if already has Related Reading section
  if grep -q "Related Reading\|## 📚 Related\|## Related" "$file"; then
    echo "SKIP: $filename (already has related section)"
    continue
  fi
  
  if [[ -n "${LINKS[$filename]}" ]]; then
    # Build the section
    links_formatted=$(echo "${LINKS[$filename]}" | sed 's/|/\n|/g' | head -4)
    section=$(echo "$RELATED_TEMPLATE" | sed "s|%LINKS%|${LINKS[$filename]}|")
    
    # Append before final ---
    # Check if file ends with ---
    if tail -5 "$file" | grep -q "---"; then
      # Remove trailing --- and add section
      head -n -1 "$file" > /tmp/temp_post.md
      echo "$section" >> /tmp/temp_post.md
      echo "---" >> /tmp/temp_post.md
      mv /tmp/temp_post.md "$file"
      echo "ADDED: $filename"
      ((count++))
    else
      echo "$section" >> "$file"
      echo "ADDED (no trailing ---): $filename"
      ((count++))
    fi
  fi
done

echo ""
echo "Done: added related posts to $count articles"
