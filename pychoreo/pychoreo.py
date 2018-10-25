# -*- coding: utf-8 -*-

"""Main module."""

import time
import os

import hcl

from pychoreo.service import Service
from pychoreo.config import Config


class Choreo:
    def __init__(self, **kwargs) -> None:
        self.config = Config(**kwargs)
        self.name = kwargs.pop("name", __name__)
        self.svc = Service(app_name=self.name, **kwargs)

    @classmethod
    def create(cls, **kwargs):
        inst = cls(**kwargs)
        inst.svc.start_service()
        return inst

    @classmethod
    def destroy(cls, **kwargs):
        inst = cls(**kwargs)
        inst.svc.stop_service()
        return inst

    def start(self):
        """Launch the configured API"""

    def stop(self):
        """Shutdown the configured API"""
