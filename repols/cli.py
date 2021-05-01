"""Handle command line arguments.

"""
from sys import stdin
from typing import Sequence

import click

from repols.list_repositories import list_repositories


@click.command()
@click.version_option()
@click.option("--include", multiple=True, help="Fields to include")
@click.option("--sort", multiple=False, is_flag=True, help="Output a sorted list")
@click.argument("organisation")
@click.argument("team")
def cli(organisation: str, team: str, include: Sequence[str], sort: bool) -> None:
    """A tool for archiving GitHub repositories."""
    list_repositories(organisation, team, include, stdin.readline().strip(), sort)
