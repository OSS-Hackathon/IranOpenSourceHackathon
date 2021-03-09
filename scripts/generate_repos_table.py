import os
import sys
import yaml


def to_md_table(repos):
    columns = ["Name", "Owner", "Description", "Languages"]
    header = "| " + " | ".join(columns) + " |"

    seprator = "| " + " | ".join(map(lambda _: "---", columns)) + " |\n"

    rows = seprator.join(
        [
            "| "
            + " | ".join(
                [
                    f"[{repo['name']}]({repo['repository']})",
                    f"[{repo['owner']}](https://github.com/{repo['owner']})",
                    repo["description"],
                    ", ".join(repo["languages"]),
                ]
            )
            for repo in repos
        ]
    )

    return f"{header}\n{seprator}{rows}"


def main():
    if len(sys.argv) < 2 or not os.path.isdir(sys.argv[1]):
        print("Invalid argument")
        exit(1)

    repos = []
    for current_path, _, files in os.walk(sys.argv[1]):
        for file in files:
            with open(os.path.join(current_path, file)) as f:
                repo = yaml.full_load(f)
            repos.append(repo)

    print(to_md_table(repos))


if __name__ == "__main__":
    main()
