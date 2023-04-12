# Copyright 2019-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from .helpers.base import BaseCommand


class UserPresenceCommand(BaseCommand):
    resource = 'users'

    def list(self, **params):
        headers = self._get_headers(**params)
        if 'user_uuids' in params:
            params['user_uuid'] = ','.join(params.pop('user_uuids'))

        url = f'{self.base_url}/presences'
        r = self.session.get(url, headers=headers, params=params)
        self.raise_from_response(r)
        return r.json()

    def get(self, user_uuid, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = f'{self.base_url}/{user_uuid}/presences'
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def update(self, user_args, tenant_uuid=None):
        user_uuid = user_args['uuid']
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = f'{self.base_url}/{user_uuid}/presences'
        r = self.session.put(url, json=user_args, headers=headers)
        self.raise_from_response(r)
