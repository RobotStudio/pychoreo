# -*- coding: utf-8 -*-

"""Consul module for interfacing with a Consul backend"""

import socket
from contextlib import closing
import json

from consul import Consul


class ConsulFacade:
    _consul = Consul()
    _events: list
    _services: list
    _dcs: list

    port: int = 0

    def __init__(self, app_name, service_name=None, datacenter='dc1'):
        self.app_name = app_name
        self.service_name = app_name if service_name is None else service_name
        self.dc = datacenter

        self.update()

    def update(self):
        self._events = self._consul.event.list()
        self._services = self._consul.catalog.services()
        self._nodes = self._consul.catalog.nodes()
        self._dcs = self._consul.catalog.datacenters()

    def _get_new_port(self) -> int:
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.bind(('', 0))
            return sock.getsockname()[1]

    def create_service(self, **kwargs) -> int:
        port = kwargs.pop('port', None)
        port_ = self._get_new_port() if port is None else port
        if self._consul.agent.service.register(self.service_name, **kwargs):
            self.port = port_
            return True
        raise ResourceWarning("Could not register new service '{name}'.")
        return False

    def get_service(self, service_name=None) -> dict:
        name = self.service_name if service_name is None else service_name
        return json.loads(self._consul.catalog.service(name))[0]

    def remove_service(self, service=None) -> bool:
        name = self.service_name if service is None else service['ServiceName']
        return self._consul.agent.service.deregister(name)

    def get(self, key=None, app_name=None, service_name=None):
        app_name_ = self.app_name if app_name is None else app_name
        service_name_ = self.service_name if service_name is None else service_name
        if key is None:
            return self._consul.kv.list(f"{app_name_}/{service_name_}")
        return self._consul.kv.get(f"{app_name_}/{service_name_}/{key}")
