# -*- coding: utf-8 -*-
# Copyright 2019-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client.client import BaseClient


class ChatdClient(BaseClient):

    namespace = 'wazo_chatd_client.commands'

    def __init__(self, host, port=443, prefix='/api/chatd', version='1.0', **kwargs):
        super(ChatdClient, self).__init__(
            host=host, port=port, prefix=prefix, version=version, **kwargs
        )
