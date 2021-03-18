#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2019-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import setup
from setuptools import find_packages

setup(
    name='wazo_chatd_client',
    version='1.0',
    description='a simple client library for the wazo chatd HTTP interface',
    author='Wazo Authors',
    author_email='dev@wazo.community',
    url='http://wazo.community',
    packages=find_packages(),
    entry_points={
        'wazo_chatd_client.commands': [
            'config = wazo_chatd_client.commands.config:ConfigCommand',
            'rooms = wazo_chatd_client.commands.rooms:RoomCommand',
            'status = wazo_chatd_client.commands.status:StatusCommand',
            'user_presences = wazo_chatd_client.commands.user_presences:UserPresenceCommand',
        ],
    },
)
