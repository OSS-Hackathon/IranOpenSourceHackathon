#!/usr/bin/env python3
import os
import sys

from util.markdown import comma_separated, md_link, md_table, NEWLINE
from util.github import github_user_link, github_repo_link
from util.repos import load_repos


def repos_table(repos):
    return md_table({
        'Name': lambda repo: github_repo_link(repo['name'], repo['owner'], repo['slug']),
        'Description': lambda repo: repo['description'],
        'Owner': lambda repo: github_user_link(repo['owner']),
        'Maintainer(s)': lambda repo: comma_separated(map(github_user_link, repo['maintainers'])),
        'Languages': lambda repo: comma_separated(repo['languages']),
    }, repos)


def write_repos(event, table):
    FILE = 'README.md'
    START_MARK = '<!-- Repos Table -->'
    END_MARK = '<!-- /Repos Table -->'

    readme = os.path.join(event, FILE)
    with open(readme, 'r') as f:
        data = f.read()
        pre = data.index(START_MARK) + len(START_MARK)
        post = data.index(END_MARK)

    with open(readme, 'w') as f:
        f.write(data[:pre] + NEWLINE +  table + NEWLINE + data[post:])


def main():
    if len(sys.argv) < 2 or not os.path.isdir(sys.argv[1]):
        print('Invalid argument')
        exit(1)

    event = sys.argv[1]
    repos = load_repos(event, shuffle=True)
    table = repos_table(repos)
    write_repos(event, table)



if __name__ == '__main__':
    main()
