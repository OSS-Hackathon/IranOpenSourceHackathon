# Scripts

These are useful scripts for management of the hackathon. These scripts are intended for the organizers of the hackathon only.

<br>

## Validating Repositories

This script will check if entered repository information is correct, according to
[this section of the hackathon readme](https://github.com/OSS-Hackathon/IranOpenSourceHackathon#repositories).
The script will run automatically on pushes to main and on pull requests, but if you need to run it manually follow these steps:

1. [Install Python 3](https://www.python.org/downloads/)
1. Install dependencies:
  ```bash
  pip3 install pyyaml
  ```
1. Run this:
  ```bash
  python3 ./scripts/validate_repos.py <event>
  ```
  For example:
  ```bash
  python3 ./scripts/validate_repos.py first
  ```

<br>

## Generating Repository Table

This script will update
[this section of the hackathon readme](https://github.com/OSS-Hackathon/IranOpenSourceHackathon#repositories)
from repositories specified in `<event>/repos` sub-directory,
according to [these rules](https://github.com/OSS-Hackathon/IranOpenSourceHackathon#i-am-a-maintainer-can-i-add-my-repos-to-this-hackathon).
This script will be run automatically on pushes to main, but
if you need to run it manually follow these steps:

1. [Install Python 3](https://www.python.org/downloads/)
1. Install dependencies:
  ```bash
  pip3 install pyyaml
  ```
1. Run this:
  ```bash
  python3 ./scripts/generate_repos_table.py <event>
  ```
  For example:
  ```bash
  python3 ./scripts/generate_repos_table.py first
  ```
