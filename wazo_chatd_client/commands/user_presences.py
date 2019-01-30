# Copyright 2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from .helpers.base import BaseCommand


class UserPresenceCommand(BaseCommand):

    resource = 'users/presences'

    def list(self, **params):
        headers = self._get_headers(**params)
        r = self.session.get(self.base_url, headers=headers, params=params)
        self.raise_from_response(r)
        return r.json()
