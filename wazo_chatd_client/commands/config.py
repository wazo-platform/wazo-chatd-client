# Copyright 2019-2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from .helpers.base import BaseCommand


class ConfigCommand(BaseCommand):
    resource = 'config'

    def get(self):
        headers = self._get_headers()
        r = self.session.get(self.base_url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def patch(self, config_patch):
        headers = self._get_headers()
        r = self.session.patch(self.base_url, headers=headers, json=config_patch)
        if r.status_code != 200:
            self.raise_from_response(r)
        return r.json()
