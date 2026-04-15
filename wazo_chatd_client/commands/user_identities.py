# Copyright 2026 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from .helpers.base import BaseCommand


class UserIdentityCommand(BaseCommand):
    resource = 'users'

    def list(self, user_uuid, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = f'{self.base_url}/{user_uuid}/identities'
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def list_from_user(self, room_uuid=None):
        headers = self._get_headers()
        url = f'{self.base_url}/me/identities'
        params = {}
        if room_uuid:
            params['room_uuid'] = str(room_uuid)
        r = self.session.get(url, headers=headers, params=params)
        self.raise_from_response(r)
        return r.json()

    def get(self, user_uuid, identity_uuid, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = f'{self.base_url}/{user_uuid}/identities/{identity_uuid}'
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def create(self, user_uuid, identity_args, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = f'{self.base_url}/{user_uuid}/identities'
        r = self.session.post(url, json=identity_args, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def update(self, user_uuid, identity_uuid, identity_args, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = f'{self.base_url}/{user_uuid}/identities/{identity_uuid}'
        r = self.session.put(url, json=identity_args, headers=headers)
        self.raise_from_response(r)

    def delete(self, user_uuid, identity_uuid, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = f'{self.base_url}/{user_uuid}/identities/{identity_uuid}'
        r = self.session.delete(url, headers=headers)
        self.raise_from_response(r)
