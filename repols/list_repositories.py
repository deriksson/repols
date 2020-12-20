from getpass import getpass
from typing import Sequence

from github import Github

from repols.insort import insort_any_type_left

FIELDS = {
    "archived": lambda repo: str(repo.archived),
    "created_at": lambda repo: repo.created_at.strftime("%Y-%m-%dT%H:%M"),
    "description": lambda repo: repo.description if repo.description else "",
    "name": lambda repo: repo.name,
}


def list_repositories(
    organisation_name: str, team: str, included_fields: Sequence[str]
) -> None:
    token = getpass(prompt="Token:")
    organisation = Github(
        base_url="https://api.github.com", login_or_token=token
    ).get_organization(organisation_name)

    output_repo_list(
        organisation.get_team_by_slug(team).get_repos(),
        print,
        included_fields if included_fields else ("name",),
        FIELDS,
    )


def output_repo_list(team_repos, print_function, included_fields, available_fields):
    for repo in sorted_repos(team_repos, available_fields, included_fields[0]):
        print_function(",".join(repo_metadata(included_fields, available_fields, repo)))


def sorted_repos(team_repos, available_fields, field):
    repos = []
    for repo in team_repos:
        insort_any_type_left(
            repos,
            repo,
            lambda lhs, rhs: available_fields[field](lhs)
            < available_fields[field](rhs),
        )
    return repos


def repo_metadata(included_fields, available_fields, repository):
    return [
        available_fields[field](repository)
        for field in included_fields
        if field in available_fields
    ]
