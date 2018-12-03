# -*- coding: utf-8 -*-

"""Console script for pychoreo."""
import sys
from subprocess import call

import click

from pychoreo.generator import compile_files
from pychoreo.pychoreo import Choreo


@click.group()
@click.pass_context
def main(ctx):
    """Console script for pychoreo."""
    pass


@main.command()
@click.pass_context
@click.option('-p', '--path', default="proto/svc")
def generate(ctx, path):
    """Generate protobuf definitions into module"""
    compile_files(path)
    return 0


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
@click.argument('request')
@click.argument('response')
def create(ctx, name):
    """Create a shell wrapped service by name"""
    click.echo(f"Launching service {name}")
    Choreo.create_shell_wrapper(name=name)
    Choreo.srv()
    return 0


@main.group()
@click.pass_context
def srv(ctx):
    """Create an echo service"""
    click.echo(f"Launching service")
    ch = Choreo.create_echo_server()
    ch.serve()
    return 0


@srv.command()
@click.pass_context
def echo(ctx):
    """Create an echo service"""
    click.echo(f"Service: echo")
    ch = Choreo.create_echo_server()
    ch.srv()
    return 0


@main.command()
@click.pass_context
@click.argument('text')
def echo2(ctx, text):
    """Create an echo service"""
    click.echo(f"Launching echo service")
    Choreo.create_echo(text=text)
    Choreo.serve()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
