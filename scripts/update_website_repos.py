#!/usr/bin/env python3
import os
import re
import sys

from util.markdown import comma_separated
from util.github import github_repo_url
from util.repos import load_repos


def update_website(event, repos):
    html_path = os.path.join("docs", "index.html")
    with open(html_path, "r") as f: content = f.read()

    content = re.sub(
        r"(?<=<!-- Repos Count -->).*?(?=<!-- /Repos Count -->)",
        str(len(repos)),
        content
    )

    template = re.findall(
        r"(?<=<!-- Repo Item Template -->)[\s\S]*?(?=<!-- /Repo Item Template -->)",
        content
    )
    if len(template) != 1: exit("docs/index.html isn't usable anymore.")
    template = template[0].replace("<!--", "").replace("-->", "")

    repos_html = "".join(
        template
            .replace("{{link}}", github_repo_url(repo["owner"], repo["slug"]))
            .replace("{{title}}", repo["name"])
            .replace("{{description}}", repo["description"])
            .replace("{{languages}}", comma_separated(repo["languages"]))
        for repo in repos
    )

    content = re.sub(
        r"(?<=<!-- Repos List -->)[\s\S]*?(?=<!-- /Repos List -->)",
        repos_html,
        content
    )

    with open(html_path, "w") as f: f.write(content)


def main():
    if len(sys.argv) < 2 or not os.path.isdir(sys.argv[1]):
        exit("Invalid argument")

    event = sys.argv[1]
    repos = load_repos(event, shuffle=True)
    update_website(event, repos)


if __name__ == "__main__":
    main()
