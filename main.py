#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Code that makes an initial pre-test, configures devices, makes post-test
to verify that the test passes after the change.
"""

from deploy_route_change import edit_routes, create_config
from ping_test import make_ping_test

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

    # Run a pre ping test
    pre_test = make_ping_test(TESTBED, PING_DESTINATIONS)

    # Todo 1: Make the config change using route template and route values

    # Todo 2: Run a post ping test
