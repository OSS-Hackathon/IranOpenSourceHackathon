import os
import sys
import json

from util.markdown import comma_separated, md_table, NEWLINE
from util.github import github_user_link, github_repo_link, github_repo_pr_search_link

README_FILE = "README.md"
STATS_FILE = "stats.json"
CONTRIBUTORS_STATS = "CONTRIBUTORS_STATS"
REPOS_STATS = "REPOS_STATS"


def contributors_stats_table(stats):
    contributors = {}
    for repo in stats:
        for pr in stats[repo]:
            username = pr["user"]["login"]
            if username in contributors:
                contributors[username]["total_prs"] += 1
                contributors[username]["repos"].append(repo)
            else:
                contributors[username] = dict(
                    username=username,
                    total_prs=1,
                    repos=[repo],
                )

    return md_table(
        {
            "Contributor": lambda contributor: github_user_link(
                contributor["username"]
            ),
            "Total PRs": lambda contributor: str(contributor["total_prs"]),
            "Repos": lambda contributor: comma_separated(
                set(github_repo_link(repo, repo) for repo in contributor["repos"])
            ),
        },
        sorted(
            contributors.values(),
            key=lambda contributor: contributor["total_prs"],
            reverse=True,
        ),
    )


def repos_stats_table(stats):
    return md_table(
        {
            "Repo": lambda repo: github_repo_pr_search_link(
                repo["name"],
                repo["name"],
            ),
            "Total PRs": lambda repo: str(repo["total_prs"]),
            "Contributors": lambda repo: comma_separated(repo["contributors"]),
        },
        sorted(
            filter(
                lambda repo: repo["total_prs"] > 0,
                map(
                    lambda repo: dict(
                        name=repo,
                        total_prs=len(stats[repo]),
                        contributors=map(
                            lambda contributor: github_user_link(contributor),
                            set(
                                map(
                                    lambda pr: pr["user"]["login"],
                                    stats[repo],
                                )
                            ),
                        ),
                    ),
                    stats,
                ),
            ),
            key=lambda repo: repo["total_prs"],
            reverse=True,
        ),
    )


def write_stats(event, table, stats_type):
    START_MARK = f"<!-- {stats_type} TABLE -->"
    END_MARK = f"<!-- /{stats_type} TABLE -->"

    readme = os.path.join(event, README_FILE)
    with open(readme, "r") as f:
        data = f.read()
        pre = data.index(START_MARK) + len(START_MARK)
        post = data.index(END_MARK)

    with open(readme, "w") as f:
        f.write(data[:pre] + NEWLINE + table + NEWLINE + data[post:])


def load_stats(event):
    with open(os.path.join(event, STATS_FILE)) as f:
        return json.load(f)


def main():
    if len(sys.argv) < 2 or not os.path.isdir(sys.argv[1]):
        print("Invalid argument")
        exit(1)

    event = sys.argv[1]
    stats = load_stats(event)
    contributors_table = contributors_stats_table(stats)
    write_stats(event, contributors_table, CONTRIBUTORS_STATS)
    repos_table = repos_stats_table(stats)
    write_stats(event, repos_table, REPOS_STATS)


if __name__ == "__main__":
    main()
