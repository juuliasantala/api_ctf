#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Python sample script for retrieving infomration on the static route
configuration with RESTCONF.
"""

from pprint import pprint
import requests
import urllib3

urllib3.disable_warnings()

def get_routes(ip, username, password):
    '''Get interfaces using RESTCONF'''

    url = f"https://{ip}:443/restconf/data/Cisco-IOS-XE-native:native/ip/route"
    headers = {
        'Content-Type': 'application/yang-data+json',
        'Accept': 'application/yang-data+json',
    }
    auth = (username, password)

    response = requests.get(url, headers=headers, auth=auth, verify=False)
    print(f"\nThe response body for static routes on device {ip}:\n")
    if not response.ok:
        print("Error:")
        print(response.text)

    pprint(response.json())


if __name__ == "__main__":

    DEVICE_IP = "198.18.6.3"
    DEVICE_USER = "developer"
    DEVICE_PASSWORD = "C1sco12345"

    get_routes(DEVICE_IP, DEVICE_USER, DEVICE_PASSWORD)
