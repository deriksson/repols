from getpass import getpass
from bisect import insort_left
from github import Github


def list_repositories(organisation: str, team: str) -> None:
    token = getpass(prompt="Token:")

    g = Github(base_url="https://api.github.com", login_or_token=token)
    o = g.get_organization(organisation)

    repos = []
    for repo in o.get_team_by_slug(team).get_repos():
        insort_left(repos, repo.name)

    for repo in repos:
        print(repo)
