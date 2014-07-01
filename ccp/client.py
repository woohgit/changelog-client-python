# -*- coding: utf-8 -*-
"""
ccp.client
~~~~~~~~~~~~

This module implements the Changelog API.

:license: MIT, see LICENSE for more details.

"""

import requests
import json
from time import time
import logging
from pkg_resources import get_distribution

API_HOST = "localhost"
API_PORT = 5000

SEVERITY = dict(INFO=1, NOTIFICATION=2, WARNING=3, ERROR=4, CRITICAL=5)


class Client(object):

    def __init__(self, host=API_HOST, port=API_PORT):
        self.host = host
        self.port = port
        self.endpoint = "/api/events"
        self.logger = logging.getLogger('changelog_client')

    def send(self, message, severity, category="misc"):
        headers = {
            "User-Agent": "ccp/client v.%s" % get_distribution("ccp").version
        }

        url = self.get_url()
        self.logger.info('Sending changelog event to %s' % url)
        headers["Content-Type"] = "application/json"
        data = {
            "criticality": "%d" % SEVERITY[severity],
            "unix_timestamp": "%d" % time(),
            "category": category,
            "description": message
        }
        try:
            response = requests.post(url, headers=headers, data=json.dumps(data))

            if "OK" in response.text:
                return True
            else:
                self.logger.error("Failed to send changelog message to server: %s" % response.text)
        except Exception as e:
            raise("Failed to send message to server: %s" % e)

    def get_url(self):
        port = "" if self.port == 80 else ":%d" % self.port
        protocol = "http://"
        base_full_url = "%s%s%s%s" % (protocol, self.host, port, self.endpoint)
        return base_full_url
