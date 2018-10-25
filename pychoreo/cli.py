# -*- coding: utf-8 -*-

"""Console script for pychoreo."""
import sys
import click

from pychoreo.pychoreo import Choreo


@click.group()
@click.pass_context
def main(ctx):
    """Console script for pychoreo."""
    pass

@main.command()
@click.pass_context
@click.argument('name')
def destroy(ctx, name):
    """Destroy the service by name"""
    click.echo(f"Removing service {name}")
    Choreo.destroy(name=name)
    return 0

@main.command()
@click.pass_context
@click.argument('name')
def create(ctx, name):
    """Create the service by name"""
    click.echo(f"Launching service {name}")
    Choreo.create(name=name)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
