#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=unused-argument
"""Test base objects."""
import mutton


def test_base_request():
    """Test base Request."""
    request = mutton.Request({}, {})
    request.event = {'hi': 'hello'}
    request.context = {'hi': 'hello'}
    assert request.event['hi'] == 'hello'
    assert request.context['hi'] == 'hello'


def test_base_handler():
    """Test base Handler."""

    class TestHandler(mutton.Handler):
        """Test handler."""

        def perform(self, request, **k):
            """Test perform method."""
            response = mutton.Response()
            response.body = self.request.event['value']
            return response

    test_handler = TestHandler()
    request_object = {'value': 1.0}
    invocation = test_handler(request_object, {})

    assert invocation == '1.0'


def test_base_response():
    """Test base Response."""
    response = mutton.Response()

    # test setitem
    response['test'] = 'hi'
    assert response['test'] == 'hi'

    # test delitem
    del response['test']
    assert 'test' not in response.store

    x = [x for x in response]
    assert x

    response.body = 'hello'
    assert response.serialized == 'hello'
    assert response['body'] == 'hello'

    response.key_map['test'] = 'test'
    response.test = 'hello'
    assert response['test'] == 'hello'

    assert len(response) == len('hello')
