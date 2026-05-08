# Copyright 2026 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from .helpers.base import BaseCommand


class IdentityCommand(BaseCommand):
    resource = 'identities'

    def list(self, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        r = self.session.get(self.base_url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def get(self, identity_uuid, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = f'{self.base_url}/{identity_uuid}'
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def create(self, identity_args, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        r = self.session.post(self.base_url, json=identity_args, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def update(self, identity_uuid, identity_args, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = f'{self.base_url}/{identity_uuid}'
        r = self.session.put(url, json=identity_args, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def delete(self, identity_uuid, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = f'{self.base_url}/{identity_uuid}'
        r = self.session.delete(url, headers=headers)
        self.raise_from_response(r)
