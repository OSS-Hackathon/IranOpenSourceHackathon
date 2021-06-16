import os
from .markdown import md_link


GITHUB_BASE = "https://github.com"


def github_user_link(user):
    """
    Returns a markdown link for given user URL.
    """
    return md_link(user, f"{GITHUB_BASE}/{user}")


def github_repo_link(title, owner, repo):
    """
    Returns a markdown for given repository and with given title.
    """
    return md_link(title, github_repo_url(owner, repo))


def github_repo_pr_search_link(title, repo):
    return md_link(title, f"{GITHUB_BASE}/{repo}")


def github_repo_url(owner, repo):
    """
    Returns the URL for given repository.
    """
    return f"{GITHUB_BASE}/{owner}/{repo}"
