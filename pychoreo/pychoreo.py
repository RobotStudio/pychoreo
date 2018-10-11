# -*- coding: utf-8 -*-

"""Main module."""

import time

from pychoreo.services import Service


class Choreo:
    _svcs: dict = {}

    def __init__(self, name, services: dict, *args, **kwargs):
        self.name = name
        for name_, params in services.items():
            self._svcs[name_] = Service(name_, **params)
