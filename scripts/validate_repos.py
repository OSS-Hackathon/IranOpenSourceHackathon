#!/usr/bin/env python3
import os
import sys
import urllib.request
from util.github import github_repo_url
from util.repos import load_repos


def check_repo(owner, repo):
    try:
        with urllib.request.urlopen(github_repo_url(owner, repo)) as response:
            if response.status != 200:
                print(f'❌ failed: {owner}/{repo}')
                return False
            else:
                print(f'✅ passed: {owner}/{repo}')
                return True
    except:
        print(f'❌ failed: {owner}/{repo}')
        return False


def check_repos(repos):
    errors = 0
    checked = 0
    for repo in repos:
        checked += 1
        if not check_repo(repo['owner'], repo['slug']):
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
