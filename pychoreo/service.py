# -*- coding: utf-8 -*-

"""Service abstraction layer"""

from pychoreo.consul import ConsulFacade


class Service:
    _consul: ConsulFacade

    def __init__(self, **kwargs):
        self.app_name = kwargs.pop("app_name", __name__)
        self.service_name = kwargs.pop("service_name", None)
        self._consul = ConsulFacade(self.app_name, self.service_name, **kwargs)

    def start_service(self):
        return self._consul.create_service()

    def stop_service(self):
        return self._consul.remove_service()
