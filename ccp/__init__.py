# -*- coding: utf-8 -*-

"""
Changelog Client Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic usage:

    >>>from ccp.client import Client
    >>>client = Client
    >>>result = client.send("This is an example message", "INFO", "misc")

:license: MIT, see LICENSE for more details.

"""

from pkg_resources import get_distribution

__title__ = 'ccp'
__version__ = get_distribution('ccp').version
__author__ = 'Adam Papai'
__license__ = 'MIT'