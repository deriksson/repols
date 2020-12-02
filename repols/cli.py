"""Handle command line arguments.

"""
import click

from repols.list_repositories import list_repositories


@click.command()
@click.version_option()
@click.argument('organisation')
@click.argument('team')
def cli(owner: str, csv: str) -> None:
    """A tool for archiving GitHub repositories.

    """
    list_repositories(owner, csv)
