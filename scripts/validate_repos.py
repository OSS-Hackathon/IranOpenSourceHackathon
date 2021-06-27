#!/usr/bin/env python3
import os
import sys
import urllib.request
from util.github import github_repo_url, GITHUB_BASE
from util.repos import load_repos

owners_check = []

def make_request(url) -> bool:
    try:
        with urllib.request.urlopen(url) as response:
            if response.status != 200:
                return False
            else:
                return True
    except:
        return False

def check_maintainers_name(owner):
    if [owner, True] in owners_check:
        print(f'✅ already passed: {owner}')
        return True

    if make_request(f"{GITHUB_BASE}/{owner}"):
        owners_check.append([owner, True])
        print(f'✅ passed: {owner}')
        return True
    else:
        print(f'❌ failed: {owner}')
        return False

def check_repo(owner, repo):
    if make_request(github_repo_url(owner, repo)):
        print(f'✅ passed: {owner}/{repo}')
        return True
    else:
        print(f'❌ failed: {owner}/{repo}')
        return False


def check_repos(repos):
    errors = 0
    checked = 0
    for repo in repos:
        checked += 1
        if not check_repo(repo['owner'], repo['slug']):
            errors += 1
        if not check_maintainers_name(repo['owner']):
            errors += 1

    return checked, errors


def main():
    if len(sys.argv) < 2 or not os.path.isdir(sys.argv[1]):
        print('Invalid argument')
        exit(1)

    event = sys.argv[1]
    repos = load_repos(event)
    checked, errors = check_repos(repos)

    print(f'{checked} checked, {errors} failed')
    if errors > 0:
        exit(1)


if __name__ == '__main__':
    main()
