from getpass import getpass
from bisect import insort_left
from github import Github


def list_repositories(organisation_name: str, team: str) -> None:
    token = getpass(prompt="Token:")
    organisation = Github(base_url="https://api.github.com", login_or_token=token)\
        .get_organization(organisation_name)

    repos = []
    for repo in organisation.get_team_by_slug(team).get_repos():
        insort_left(repos, repo.name)

    for repo in repos:
        print(repo)
