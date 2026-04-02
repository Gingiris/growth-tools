#!/usr/bin/env python3
import json, subprocess

with open('_posts/2026-04-02-github-issue-template-guide.md') as f:
    content = f.read()

end = content.index('---', 3)
body = content[end+3:].strip()

payload = {
    'title': 'GitHub Issue Template: How to Get More Contributions and Build Community',
    'body_markdown': body,
    'published': True,
    'tag_list': 'github, open-source, community, developer-tools, contributions',
    'canonical_url': 'https://gingiris.github.io/growth-tools/blog/2026/04/02/github-issue-template-guide/',
    'description': 'Learn how to write GitHub issue templates that get better bug reports.'
}

cmd = [
    'curl', '-s', '-X', 'POST', 'https://dev.to/api/articles',
    '-H', 'api-key: JA5tN1koVTn9LNH9oc2HT7sX',
    '-H', 'Content-Type: application/json',
    '-d', json.dumps({'article': payload})
]

result = subprocess.run(cmd, capture_output=True, text=True)
data = json.loads(result.stdout)
url = data.get('url') or str(data.get('errors')) or str(data.get('message')) or 'unknown'
print('Dev.to:', url)
if 'id' in data:
    print('ID:', data['id'])
