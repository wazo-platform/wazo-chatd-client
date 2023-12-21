# Copyright 2019-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client.command import RESTCommand

from .exceptions import ChatdError, ChatdServiceUnavailable, InvalidChatdError


class ChatdCommand(RESTCommand):
    @staticmethod
    def raise_from_response(response):
        if response.status_code == 503:
            raise ChatdServiceUnavailable(response)

        try:
            raise ChatdError(response)
        except InvalidChatdError:
            RESTCommand.raise_from_response(response)
