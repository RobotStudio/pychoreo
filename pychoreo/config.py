# -*- coding: utf-8 -*-

"""Main module."""

import time
import os

import hcl

from pychoreo.service import Service


class Config(dict):
    """Configuration dictionary with a little added functionality"""
    def __init__(self, **kwargs) -> None:
        self._conf = self._load_config(kwargs.pop("config", None))

        super().__init__(self._conf)

        # Push configuration out to consul and stay in sync
        #self._sync_config()

    def _load_config(self, config):
        """Look for and load a configuration from HCL or JSON.

        By default will attempt to load config.hcl or config.json from the
        local directory, if the parameter isn't provided.
        """
        root_path = os.path.dirname(os.path.abspath(__file__))
        config_file = config

        if config_file is None:
            if os.path.isfile(f"{root_path}/config.hcl"):
                config_file = f"{root_path}/config.hcl"
            elif os.path.isfile(f"{root_path}/config.json"):
                config_file = f"{root_path}/config.json"

        # Try loading it as hcl
        if config_file is not None:
            if os.path.isfile(config_file):
                with open(config_file, 'r') as f_p:
                    return hcl.load(f_p)

        # Default to an empty config
        return {}

    def _sync_config(self):
        pass
