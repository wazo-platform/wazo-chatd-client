# Copyright 2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from .helpers.base import BaseCommand


class RoomCommand(BaseCommand):

    resource = 'users/me/rooms'

    def list_from_user(self, **params):
        headers = self._get_headers()
        url = '{base}'.format(base=self.base_url)
        r = self.session.get(url, headers=headers, params=params)
        self.raise_from_response(r)
        return r.json()

    def create_from_user(self, room_args):
        headers = self._get_headers(write=True)
        url = '{base}'.format(base=self.base_url)
        r = self.session.post(url, json=room_args, headers=headers)
        self.raise_from_response(r)
        return r.json()
