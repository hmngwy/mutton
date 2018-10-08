#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Base objects."""
from collections import namedtuple

import inflection
from cached_property import cached_property

import pal


class APIGatewayRequest(pal.Request):
    """API Gateway Request class."""

    def __init__(self, event, context):
        """Initialize the class."""
        super().__init__(event, context)
        self.__body = event.get('body', None)
        self.__path_parameters = event.get('pathParameters', {})
        self.__query_parameters = event.get('queryStringParameters', {})
        self.__request_context = event.get('requestContext', {})
        self.__headers = event.get('headers', {})

    @cached_property
    def body(self):
        """Return string repr of body."""
        return str(self.__body)

    @cached_property
    def headers(self):
        """Return request headers as namedtuple."""
        payload = {inflection.underscore(
            k): v for k, v, in self.__headers.items()}
        HeadersTuple = namedtuple('HeadersTuple', sorted(payload))
        the_tuple = HeadersTuple(**payload)
        return the_tuple

    @cached_property
    def path(self):
        """Return request path parameters as namedtuple."""
        payload = {inflection.underscore(
            k): v for k, v, in self.__path_parameters.items()}
        PathTuple = namedtuple('PathTuple', sorted(payload))
        the_tuple = PathTuple(**payload)
        return the_tuple

    @cached_property
    def query(self):
        """Return request query string as namedtuple."""
        payload = {inflection.underscore(
            k): v for k, v, in self.__query_parameters.items()}
        QueryTuple = namedtuple('QueryTuple', sorted(payload))
        the_tuple = QueryTuple(**payload)
        return the_tuple


class APIGatewayResponse(pal.Response):
    """API Gateway Response class."""

    def __init__(self, body='', status_code=200,
                 headers=None, is_base64=False):
        """Initialize instance with list, tuple, or dict."""
        super().__init__()
        self.store = {}
        self.__base_headers = {
            # 'Access-Control-Allow-Origin': '*',
            'X-Server': 'AWS λ'
        }
        self.key_map = {'status_code': 'statusCode',
                        'is_base64': 'isBase64Encoded',
                        'headers': 'headers',
                        'body': 'body'}

        # fool proofing checks
        if headers and not isinstance(headers, dict):
            raise ValueError('Headers value must be dict.')
        if not isinstance(status_code, int):
            raise ValueError('Status Code value must be int.')

        self.headers = {}
        if headers:
            self.headers = headers

        self.status_code = status_code
        self.body = body
        self.is_base64 = is_base64

    def __setattr__(self, name, value):
        """Set attribute with some manually managed attributes."""
        # prevent recursion
        if name in ['key_map', 'store']:
            super().__setattr__(name, value)
        # process managed atts
        if name in self.key_map.keys():
            store_key = self.key_map[name]
            if name == 'headers':
                self.store[store_key] = {**self.__base_headers, **value}
            elif name == 'body':
                self.store[store_key] = self.body_serializer(value)
            elif name in ('status_code', 'is_base64'):
                self.store[store_key] = value
        else:
            super().__setattr__(name, value)


class APIGatewayHandler(pal.Handler):

    def __init__(self):
        """Initialize the handler."""
        super().__init__()
        self.request_class = APIGatewayRequest
        self.request = None

    def perform(self, request, **kwargs):
        """Stub perform method."""
        raise NotImplementedError
