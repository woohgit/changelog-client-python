CCP: Changelog Client Python
============================

Send an event to a Changelog_ server.

.. _Changelog: https://github.com/prezi/changelog

Installation
------------

To install ccp, simply: ::

    $ pip install ccp
    

Supported severities
--------------------

1. INFO
2. NOTIFICATION
3. WARNING
4. ERROR
5. CRITICAL

Example
-------

It is pretty easy to use: ::

    from ccp.client import Client
    
    client = Client("localhost", "80")
    client.send("This is a simple message", "INFO", "category")

You can pass a in a dict to specify additional HTTP headers, for example to do authentication::

    client.send("Message", "INFO", "category", {"Authorization", "Basic base64encoded"})

Logging
-------
Logging happens into the logger called ``changelog_client`` by default. You can override it by setting the ``logger``
property of a client instance to a ``Logger`` object.
