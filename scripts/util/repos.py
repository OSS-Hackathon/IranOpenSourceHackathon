import os
import yaml


def repo_info_from_path(file, dir):
    """
    Extracts repository info from given file and directory address.

    Returns an info object with following format:
    ```python
    {
        'owner': String,
        'repo': String
    }
    ```
    """
    return {
        'owner': os.path.basename(dir),
        'repo': os.path.splitext(file)[0],
    }


def fill_repo_details(repo, dir, file):
    info = repo_info_from_path(file, dir)
    repo['owner'] = info['owner']
    repo['slug'] = info['repo']
    if 'maintainers' not in repo:
        repo['maintainers'] = [repo['owner']]


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
