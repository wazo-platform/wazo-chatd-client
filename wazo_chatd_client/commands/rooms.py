# Copyright 2019-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from .helpers.base import BaseCommand
import logging

logger = logging.getLogger(__name__)


class RoomCommand(BaseCommand):
    resource = 'users/me/rooms'

    def list_from_user(self, **params):
        headers = self._get_headers()
        if 'user_uuids' in params:
            params['user_uuid'] = ','.join(params.pop('user_uuids'))
        url = f'{self.base_url}'
        r = self.session.get(url, headers=headers, params=params)
        self.raise_from_response(r)
        return r.json()

    def create_from_user(self, room_args):
        headers = self._get_headers()
        url = f'{self.base_url}'
        r = self.session.post(url, json=room_args, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def list_messages_from_user(self, room_uuid, **params):
        headers = self._get_headers()
        url = f'{self.base_url}/{room_uuid}/messages'
        r = self.session.get(url, headers=headers, params=params)
        self.raise_from_response(r)
        return r.json()

    def create_message_from_user(self, room_uuid, message_args):
        headers = self._get_headers()
        url = f'{self.base_url}/{room_uuid}/messages'
        r = self.session.post(url, json=message_args, headers=headers)
        logger.warning('------message-test------')
        logger.warning(r)
        self.raise_from_response(r)
        return r.json()

    def search_messages_from_user(self, **params):
        headers = self._get_headers()
        url = f'{self.base_url}/messages'
        r = self.session.get(url, headers=headers, params=params)
        self.raise_from_response(r)
        return r.json()

    def set_activity_from_user(self, room_uuid, activity_args):
        headers = self._get_headers()
        url = '{base}/{room_uuid}/activities'.format(
            room_uuid=room_uuid, base=self.base_url
        )
        logger.warning('------activity-test------')
        r = self.session.post(url, json=activity_args, headers=headers)
        logger.warning(r)
        self.raise_from_response(r)
        return r.json()
