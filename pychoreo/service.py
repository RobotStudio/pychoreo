# -*- coding: utf-8 -*-

"""Service abstraction layer"""

from pychoreo.consul import ConsulFacade


class Service:
    _consul: ConsulFacade

    def __init__(self, app_name, service_name, *args, **kwargs):
        self.app_name = app_name
        self.name = service_name
        self._consul = ConsulFacade(app_name, service_name, *args, **kwargs)
        self.service = self._consul.create_service()

