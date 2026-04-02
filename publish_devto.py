#!/usr/bin/env python3
import json, urllib.request

with open('_posts/2026-04-02-github-readme-template-guide.md') as f:
    content = f.read()

end = content.index('---', 3)
body = content[end+3:].strip()

payload = {
    "title": "GitHub README Template: The Complete 2026 Guide to Get More Stars",
    "body_markdown": body,
    "published": True,
    "tag_list": "github, open-source, developer-tools, growth",
    "canonical_url": "https://gingiris.github.io/growth-tools/blog/2026/04/02/github-readme-template-guide/",
    "description": "Learn how to write a GitHub README that gets stars. Based on 60k GitHub stars experience."
}

# Use curl via subprocess to avoid urllib issues
import subprocess, os

cmd = [
    'curl', '-s', '-X', 'POST',
    'https://dev.to/api/articles',
    '-H', 'api-key: JA5tN1koVTn9LNH9oc2HT7sX',
    '-H', 'Content-Type: application/json',
    '-d', json.dumps({"article": payload})
]

result = subprocess.run(cmd, capture_output=True, text=True)
try:
    data = json.loads(result.stdout)
    print("Dev.to:", data.get("url", data.get("errors", data.get("message", ""))))
    if "id" in data:
        print("Article ID:", data["id"])
except:
    print("Raw:", result.stdout[:200])
