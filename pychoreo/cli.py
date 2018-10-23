# -*- coding: utf-8 -*-

"""Console script for pychoreo."""
import sys
import click

from pychoreo.pychoreo import Choreo


@click.command()
@click.option('-d', '--delete', flag=True,
        help="Remove the service from the service registry")
@click.argument('name')
def main(flag, name, args=None):
    """Console script for pychoreo."""
    click.echo(f"Launching service {name}")
    c = Choreo(name, {})
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
