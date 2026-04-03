#!/usr/bin/env python3
"""
Gingiris Blog — Batch URL Submission Tool
==========================================
Submits all blog post URLs to:
  1. IndexNow  (Bing / Yandex / Seznam — immediate)
  2. Google Indexing API  (requires one-time Service Account setup)

Usage:
  # Submit all posts
  python3 tools/submit_urls.py

  # IndexNow only (no Google setup needed)
  python3 tools/submit_urls.py --indexnow-only

  # Dry-run: just print URLs
  python3 tools/submit_urls.py --dry-run

Setup (one-time):
  1. Create Google Cloud project → enable "Web Search Indexing API"
  2. Create Service Account → download JSON key → save as tools/google_credentials.json
  3. In Google Search Console → Settings → Users → Add user
     (paste the service account email, role: Owner)
  4. IndexNow key is auto-generated on first run and saved to tools/.indexnow_key
"""

import os, re, sys, json, time, hashlib, argparse
import urllib.request, urllib.error

# ── Config ────────────────────────────────────────────────────────────────────
SITE_URL      = "https://gingiris.github.io/growth-tools"
POSTS_DIR     = os.path.join(os.path.dirname(__file__), "..", "_posts")
CREDS_FILE    = os.path.join(os.path.dirname(__file__), "google_credentials.json")
INDEXNOW_FILE = os.path.join(os.path.dirname(__file__), ".indexnow_key")
INDEXNOW_HOST = "gingiris.github.io"
# Delay between Google API calls (avoid rate limits)
GOOGLE_DELAY_S = 1.0

# ── Helpers ───────────────────────────────────────────────────────────────────

def extract_canonical_urls():
    """Read all _posts/*.md and return a list of unique canonical_url values."""
    urls = []
    seen = set()
    pattern = re.compile(r'^canonical_url:\s*(.+)$', re.MULTILINE)

    for fname in sorted(os.listdir(POSTS_DIR)):
        if not fname.endswith(".md"):
            continue
        with open(os.path.join(POSTS_DIR, fname)) as f:
            content = f.read(3000)  # only need front matter

        m = pattern.search(content)
        if m:
            url = m.group(1).strip().strip('"').strip("'")
            if url not in seen:
                seen.add(url)
                urls.append(url)

    # Filter: only include URLs pointing to this site (skip intentional
    # canonicals to other domains)
    own_urls = [u for u in urls if SITE_URL in u]
    return own_urls


def get_or_create_indexnow_key():
    """Return existing IndexNow key or generate a new one."""
    if os.path.exists(INDEXNOW_FILE):
        with open(INDEXNOW_FILE) as f:
            return f.read().strip()
    key = hashlib.sha256(os.urandom(32)).hexdigest()
    with open(INDEXNOW_FILE, "w") as f:
        f.write(key)
    print(f"[IndexNow] Generated new key: {key}")
    print(f"[IndexNow] ⚠️  You must expose this key at: {SITE_URL}/{key}.txt")
    print(f"           Content of the file: {key}")
    return key


def submit_indexnow(urls, key):
    """Submit URLs to IndexNow (Bing endpoint covers Bing + Yandex + others)."""
    endpoint = "https://api.indexnow.org/indexnow"
    payload = {
        "host": INDEXNOW_HOST,
        "key": key,
        "keyLocation": f"https://{INDEXNOW_HOST}/{key}.txt",
        "urlList": urls,
    }
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        endpoint,
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            status = resp.status
    except urllib.error.HTTPError as e:
        status = e.code
    except Exception as e:
        print(f"[IndexNow] ERROR: {e}")
        return False

    if status in (200, 202):
        print(f"[IndexNow] ✅ Submitted {len(urls)} URLs → status {status}")
        return True
    else:
        print(f"[IndexNow] ⚠️  Unexpected status {status}")
        return False


def submit_google(urls, creds_path):
    """Submit URLs to Google Indexing API using a service account."""
    try:
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
    except ImportError:
        print("[Google] ❌ Missing dependencies. Run:")
        print("         pip install google-auth google-api-python-client")
        return

    SCOPES = ["https://www.googleapis.com/auth/indexing"]
    creds  = service_account.Credentials.from_service_account_file(creds_path, scopes=SCOPES)
    service = build("indexing", "v3", credentials=creds, cache_discovery=False)

    ok = fail = 0
    for url in urls:
        try:
            resp = service.urlNotifications().publish(
                body={"url": url, "type": "URL_UPDATED"}
            ).execute()
            print(f"[Google] ✅ {url}")
            ok += 1
        except Exception as e:
            print(f"[Google] ❌ {url}  →  {e}")
            fail += 1
        time.sleep(GOOGLE_DELAY_S)

    print(f"[Google] Done: {ok} submitted, {fail} failed")


def print_urls(urls):
    print(f"\n{'─'*60}")
    print(f"  {len(urls)} URLs to submit")
    print(f"{'─'*60}")
    for u in urls:
        print(f"  {u}")
    print(f"{'─'*60}\n")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Batch URL submission to search engines")
    parser.add_argument("--dry-run",       action="store_true", help="Print URLs only, don't submit")
    parser.add_argument("--indexnow-only", action="store_true", help="Skip Google Indexing API")
    parser.add_argument("--google-only",   action="store_true", help="Skip IndexNow")
    args = parser.parse_args()

    urls = extract_canonical_urls()
    print_urls(urls)

    if args.dry_run:
        print("Dry-run mode — no submissions made.")
        return

    # ── IndexNow ──────────────────────────────────────────────────────────────
    if not args.google_only:
        key = get_or_create_indexnow_key()
        submit_indexnow(urls, key)

    # ── Google Indexing API ───────────────────────────────────────────────────
    if not args.indexnow_only:
        if os.path.exists(CREDS_FILE):
            print(f"\n[Google] Submitting {len(urls)} URLs via Indexing API…")
            submit_google(urls, CREDS_FILE)
        else:
            print(f"\n[Google] ⚠️  No credentials found at tools/google_credentials.json")
            print("         See setup instructions at the top of this file.")
            print("         To skip Google and use IndexNow only: --indexnow-only")


if __name__ == "__main__":
    main()
