"""Main module."""
import click

from .add_toggl_entry import add_toggl_entry
from .start_toggl_tracking import start_toggl_tracking


@click.group()
def cli():
    """
    Main group.
    """


@click.command()
def log_work():
    """
    Adds log record with some number of minutes spent.
    """
    add_toggl_entry()
    click.echo("Logged.")


@click.command()
def start_tracking():
    """
    Another example command.
    """
    start_toggl_tracking()
    click.echo("Started tracker.")


cli.add_command(log_work)
cli.add_command(start_tracking)
