"""Handle command line arguments.

"""
from getpass import getpass
from typing import Sequence

import click

from repols.list_repositories import list_repositories


@click.command()
@click.version_option()
@click.option("--include", multiple=True, help="Fields to include")
@click.argument("organisation")
@click.argument("team")
def cli(organisation: str, team: str, include: Sequence[str]) -> None:
    """A tool for archiving GitHub repositories."""
    list_repositories(organisation, team, include, getpass(prompt="Token:"))
