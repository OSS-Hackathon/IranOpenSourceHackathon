from .markdown import md_link


GITHUB_BASE='https://github.com'


def github_user_link(user):
    return md_link(user, f'{GITHUB_BASE}/{user}')


def github_repo_link(title, owner, repo):
    return md_link(title, f'{GITHUB_BASE}/{owner}/{repo}')
