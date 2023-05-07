from argparse import ArgumentParser, Namespace
import subprocess
from typing import List

GITHUB_HTTP = "https://github.com/{}"
GITHUB_SSH = "git@github.com:{}"

REPOS: List[str] = [
    "sometimes-youwin/tls-core.git",
    "sometimes-youwin/tls-server.git"
]


def main() -> None:
    parser = ArgumentParser(prog="TlsWorkspaceSetup",
                            description="Setup The Last Sostrum workspace")
    parser.add_argument("type", type=str, choices=["http", "ssh"])

    args: Namespace = parser.parse_args()

    formatter: str = ""

    if args.type == "http":
        formatter = GITHUB_HTTP
    elif args.type == "ssh":
        formatter = GITHUB_SSH

    if len(formatter) < 1:
        raise Exception("No formatter found for repos, aborting!")

    failed_repos: List[str] = []
    for repo in REPOS:
        repo = formatter.format(repo)
        print("\n---\nCloning: {}\n---\n".format(repo), flush=True)

        res = subprocess.run("git clone {}".format(repo))
        if res.returncode != 0:
            failed_repos.append(repo)

    if len(failed_repos) > 0:
        print("Failed to clone the following repos:")
        for repo in failed_repos:
            print(repo)

        exit(1)


if __name__ == "__main__":
    main()
