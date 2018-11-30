# -*- coding: utf-8 -*-

"""Main module."""

import time
import os

import hcl

#from pychoreo import echo
from pychoreo.service import Service
from pychoreo.config import Config


class Choreo:
    def __init__(self, **kwargs) -> None:
        self.config = Config(**kwargs)
        self.name = kwargs.pop("name", __name__)
        self.svc = Service(app_name=self.name, **kwargs)
        #self.echo = echo.Echo()

    @classmethod
    def create(cls, **kwargs):
        inst = cls(**kwargs)
        inst.svc.start_service()
        return inst

    @classmethod
    def create_shell_wrapper(cls, **kwargs):
        inst = cls(**kwargs)
        return inst

    @classmethod
    def destroy(cls, **kwargs):
        inst = cls(**kwargs)
        inst.svc.stop_service()
        return inst

    def serve(self, grpc_parameters=None):
        """Launch the configured API"""
        self.svc.start_service()
        #echo.serve()

    def start(self):
        """Launch the configured API"""

    def stop(self):
        """Shutdown the configured API"""


if __name__ == "__main__":
    choreo = Choreo(name='echo')
    choreo.serve()
