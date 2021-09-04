#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Base objects."""

from abc import abstractmethod

import mutton
from cached_property import cached_property


class SQSEventRequest(mutton.Request):
    """SQS Event Request class."""

    def __init__(self, event, context):
        """Initialize the class."""
        super().__init__(event, context)
        self.__records = event['Records']

    @cached_property
    def records(self):
        return self.__records


class SQSEventResponse(mutton.Response):
    """SQS Event Response class."""

    def __init__(self):
        super().__init__()

    @property
    def serialized(self):
        return None


class SQSMessage(object):
    """SQS Message class"""

    def __init__(self, record):
        super().__init__()
        self.__awsRegion = record["awsRegion"]
        self.__body = record["body"]

    @cached_property
    def awsRegion(self):
        """Return string repr of body."""
        return str(self.__awsRegion)

    @cached_property
    def body(self):
        return str(self.__body)


class SQSEventHandler(mutton.Handler):

    def __init__(self):
        """Initialize the handler."""
        super().__init__()
        self.request_class = SQSEventRequest
        self.request = None

    def perform(self, request, **kwargs):
        for record in request.records:
            message = SQSMessage(record)
            self.processMessage(message)
        return SQSEventResponse()

    @abstractmethod
    def processMessage(self, message):
        pass
