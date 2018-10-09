#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Base objects."""
import collections


class Request():
    """Base Request."""

    def __init__(self, event, context):
        """Initialize the request."""
        self.__event = event
        self.__context = context

    @property
    def event(self):
        """Return AWS Lambda Event Object."""
        return self.__event

    @event.setter
    def event(self, value):
        self.__event = value
        return self.__event

    @property
    def context(self):
        """Return AWS Lambda Context Object."""
        return self.__context

    @context.setter
    def context(self, value):
        self.__context = value
        return self.__context


class Response(collections.MutableMapping):
    """Base Response class."""

    key_map = {}
    store = {}

    def __init__(self, body=None):
        """Initialize instance."""
        super().__init__()
        self.key_map = {'body': 'body'}
        self.store = {'body': body}

    def __setattr__(self, name, value):
        """Set attribute with some manually managed attributes."""
        if name in super().__getattribute__('key_map').keys():
            store_key = self.key_map[name]
            if name == 'body':
                value = self.body_serializer(value)
            self.store[store_key] = value
        else:
            super().__setattr__(name, value)

    def __getattribute__(self, name):
        """Return attributes with some manually managed attributes."""
        if name in super().__getattribute__('key_map').keys():
            store_key = self.key_map[name]
            return self.store[store_key]
        return super().__getattribute__(name)

    def __getitem__(self, key):
        """Get subscript item."""
        return self.store[key]

    def __setitem__(self, key, value):
        """Set subscript item."""
        self.store[key] = value

    def __delitem__(self, key):
        """Delete subscript item."""
        del self.store[key]

    def __iter__(self):
        """Iterator."""
        return iter(self.store)

    def __len__(self):
        """Return response content length."""
        return len(self.store['body'])

    @staticmethod
    def body_serializer(value):
        """Stub serializer."""
        return value

    def to_dict(self):
        """Return dictionary version."""
        return self.store


class Handler():
    """Base Handler."""

    def __init__(self):
        """Initialize the handler."""
        self.request_class = Request
        self.request = None

    def __call__(self, event, context, **kwargs):
        """Wrap perform(), invoked by AWS Lambda."""
        self.__init__()  # reset the instance

        self.request = self.request_class(event, context)
        response = self.perform(self.request, **kwargs)

        return response.to_dict()

    def perform(self, request, **kwargs):
        """Stub perform method."""
        raise NotImplementedError
