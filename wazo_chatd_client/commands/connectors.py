# Copyright 2026 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from .helpers.base import BaseCommand


class ConnectorCommand(BaseCommand):
    resource = 'connectors'

    def list(self, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        r = self.session.get(self.base_url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def identities(self, backend, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = f'{self.base_url}/{backend}/identities'
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def auth_schema(self, backend, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = f'{self.base_url}/{backend}/auth-schema'
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()
