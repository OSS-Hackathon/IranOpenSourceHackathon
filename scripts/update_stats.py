import sys
import os
import urllib.request
import urllib.error
import json
import time

from util import repos

IDENTIFIER = "%23iosh"
STATS_FILE = "stats.json"
PER_PAGE = 100


def fetch_repo_prs(owner, repo):
    access_token = os.getenv("GH_ACCESS_TOKEN")
    result = []
    page = 1
    next_page_available = True
    while next_page_available:
        for _try in range(3):
            try:
                api_addr = f"https://api.github.com/search/issues?q={IDENTIFIER}+repo:{owner}/{repo}+is:pr+is:merged+in:title,body,comments+merged:2021-07-06+merged:2021-09-06&per_page={PER_PAGE}&page={page}"
                req = urllib.request.Request(api_addr)
                if access_token:
                    req.add_header("Authorization", f"token {access_token}")
                with urllib.request.urlopen(req) as response:
                    data = json.load(response)
                    result.extend(data["items"])
                    if data["total_count"] / PER_PAGE < page:
                        next_page_available = False
                    break
            except urllib.error.HTTPError as e:
                if e.code == 403:
                    remaining = e.headers.get("X-RateLimit-Remaining")
                    reset_timestamp = e.headers.get("X-RateLimit-Reset")
                    if int(remaining) == 0:
                        wait_time = int(int(reset_timestamp) - time.time()) + 1
                        print(f"Rate-Limiter: Waiting for {wait_time}s ...")
                        time.sleep(wait_time)
                        continue
                print(f"❌ fetching {owner}/{repo} PRs failed: {e.code}")
            except Exception as e:
                print(f"❌ fetching {owner}/{repo} PRs failed: {e}")
                return None
        page += 1
    return result


def write_prs(event, prs):
    with open(os.path.join(event, STATS_FILE), "w") as f:
        json.dump(prs, f)


def main():
    if len(sys.argv) < 2 or not os.path.isdir(sys.argv[1]):
        print("Invalid argument")
        exit(1)

    event = sys.argv[1]
    prs = dict()
    for r in repos.load_repos(event):
        items = fetch_repo_prs(r["owner"], r["slug"])
        if items is not None:
            prs[f"{r['owner']}/{r['slug']}"] = items
            print(f"fetched successfully: {r['owner']}/{r['slug']}")

    write_prs(event, prs)


if __name__ == "__main__":
    main()
