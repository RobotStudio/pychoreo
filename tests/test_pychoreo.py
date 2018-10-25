#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pychoreo` package."""

import pytest

from click.testing import CliRunner

from pychoreo import pychoreo
from pychoreo import cli


def test_cli():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ['--help'])
    assert result.exit_code == 0
    assert 'Show this message and exit.' in result.output


def test_cli_with_name():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ['test'])
    assert result.exit_code == 0
    assert 'Launching service test' in result.output


def test_cli_remove_name():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ['-d', 'test'])
    assert result.exit_code == 0
    assert 'Removing service test' in result.output
