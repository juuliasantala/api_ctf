#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Sample code that makes an initial pre-test, configures devices, makes post-test
to verify that the test passes after the change.

Copyright (c) 2024 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

from deploy_route_change import edit_routes, create_config
from ping_test import make_ping_test

__copyright__ = "Copyright (c) 2024 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

# SETUP: DEFINING GLOBAL VARIABLES:
DEVICE_IP = "198.18.6.3"
DEVICE_USER = "developer"
DEVICE_PASSWORD = "C1sco12345"

ROUTE_TEMPLATE = 'template.j2'
ROUTE_VALUES = 'static_routes.yaml'

TESTBED = 'testbed.yaml'
PING_DESTINATIONS = ('198.18.18.101', '198.18.6.1')

# THE FLOW IS EXECUTED WHEN THIS main.py SCRIPT IS RUN:
if __name__ == "__main__":
    # 1. MAKE A TEST BEFORE APPLYING THE CHANGE
    pre_test = make_ping_test(TESTBED, PING_DESTINATIONS)

    # 2. MAKE CONFIG CHANGE
    configuration = create_config(ROUTE_TEMPLATE, ROUTE_VALUES)
    edit_routes(DEVICE_IP, DEVICE_USER, DEVICE_PASSWORD, configuration)

    # 3 MAKE A TEST AFTER APPLYING THE CHANGE
    post_test = make_ping_test(TESTBED, PING_DESTINATIONS)
