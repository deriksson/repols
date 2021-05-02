from typing import Sequence, Dict

from github import Github

from repols.csv import quote
from repols.insort import insort_any_type_left

FIELDS = {
    "archived": lambda repo: str(repo.archived),
    "created_at": lambda repo: repo.created_at.strftime("%Y-%m-%dT%H:%M"),
    "description": lambda repo: quote(repo.description) if repo.description else "",
    "name": lambda repo: repo.name,
}


def list_repositories(
    organisation_name: str,
    team: str,
    included_fields: Sequence[str],
    token: str,
    configuration: Dict,
) -> None:
    organisation = Github(
        base_url="https://api.github.com", login_or_token=token
    ).get_organization(organisation_name)

    repos = organisation.get_team_by_slug(team).get_repos()
    desired_fields = included_fields if included_fields else ("name",)

    if configuration["headers"]:
        print(",".join(repo_metadata(desired_fields, FIELDS, lambda field: field)))

    output_repo_list(
        sorted_repos(repos, FIELDS, desired_fields[0])
        if configuration["sort"]
        else repos,
        print,
        desired_fields,
        FIELDS,
    )


def output_repo_list(team_repos, print_function, included_fields, available_fields):
    for repo in team_repos:
        print_function(
            ",".join(
                repo_metadata(
                    included_fields,
                    available_fields,
                    lambda field, r=repo: available_fields[field](r),
                )
            )
        )


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


def repo_metadata(included_fields, available_fields, report_field):
    return [
        report_field(field) for field in included_fields if field in available_fields
    ]
