# -*- coding: utf-8 -*-

"""Console script for pychoreo."""
import sys
import click

from pychoreo.pychoreo import Choreo


@click.command()
def main(args=None):
    """Console script for pychoreo."""
    click.echo("Replace this message by putting your code into "
               "pychoreo.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    c = Choreo()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
