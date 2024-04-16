#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Python script for changing static route configuration with RESTCONF.
"""

import requests
import urllib3
import jinja2
import yaml

urllib3.disable_warnings()

def edit_routes(ip, username, password, config):
    '''Edit routing configuration based on a configuration file.'''

    url = f"https://{ip}:443/restconf/data/Cisco-IOS-XE-native:native/ip/route"
    headers = {
        'Content-Type': 'application/yang-data+json',
        'Accept': 'application/yang-data+json',
    }
    auth = (username, password)

    response = requests.<TODO 1: replace with the correct method>(url, headers=headers, auth=auth, data=config, verify=False)
    print(f"Status code of deploying the configuration change: {response.status_code}")
    if not response.ok:
        print("Error:")
        print(response.text)

def create_config(template, values):
    '''Create a configuration from Jinja2 template and values from YAML file.'''

    with open(values, encoding="utf-8") as my_values:
        config = yaml.safe_load(my_values.read())
    
    with open(template, encoding="utf-8") as my_template:
        template =  # TODO 2: read the content of my_template and save it as a jinja2.Template object

    configuration = # TODO 3: render template with config["routes"]
    return configuration

if __name__ == "__main__":

    DEVICE_IP = "198.18.6.3"
    DEVICE_USER = "developer"
    DEVICE_PASSWORD = "C1sco12345"

    interface_config = create_config("template.j2", "static_routes.yaml")
    edit_routes(DEVICE_IP, DEVICE_USER, DEVICE_PASSWORD, interface_config)
