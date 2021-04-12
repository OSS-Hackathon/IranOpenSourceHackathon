import os
import sys
import yaml

from util.markdown import comma_separated, md_link, md_table, NEWLINE
from util.github import github_user_link, github_repo_link


def fill_repo_details(repo, dir, file):
    repo['owner'] = os.path.basename(dir)
    repo['slug'] = os.path.splitext(file)[0]
    if 'maintainers' not in repo:
        repo['maintainers'] = [repo['owner']]


def repos_table(repos):
    return md_table({
        'Name': lambda repo: github_repo_link(repo['name'], repo['owner'], repo['slug']),
        'Description': lambda repo: repo['description'],
        'Owner': lambda repo: github_user_link(repo['owner']),
        'Maintainer(s)': lambda repo: comma_separated(map(github_user_link, repo['maintainers'])),
        'Languages': lambda repo: comma_separated(repo['languages']),
    }, repos)


def load_repos(event):
    FOLDER = 'repos'
    repos = []
    for current_path, _, files in os.walk(os.path.join(event, FOLDER)):
        for file in files:
            with open(os.path.join(current_path, file)) as f:
                repo = yaml.full_load(f)
                fill_repo_details(repo, current_path, file)
            repos.append(repo)

    return repos


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
    repos = load_repos(event)
    table = repos_table(repos)
    write_repos(event, table)



if __name__ == '__main__':
    main()
