#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=unused-argument
"""Test base objects."""
import aws_lambda


def test_base_request():
    """Test base Request."""
    request = aws_lambda.Request({}, {})
    request.event = {'hi': 'hello'}
    request.context = {'hi': 'hello'}
    assert request.event['hi'] == 'hello'
    assert request.context['hi'] == 'hello'


def test_base_handler():
    """Test base Handler."""

    class TestHandler(aws_lambda.Handler):
        """Test handler."""

        def perform(self, request, **k):
            """Test perform method."""
            response = aws_lambda.Response()
            response.body = self.request.event['att']
            return response

    test_handler = TestHandler()
    request_object = {'att': 1.0}
    invocation = test_handler(request_object, {})

    assert invocation['body'] == 1.0


def test_base_response():
    """Test base Response."""
    response = aws_lambda.Response()

    response['test'] = 'hi'
    assert response['test'] == 'hi'

    del response['test']
    assert 'test' not in response.to_dict()

    x = [x for x in response]
    assert x

    response.body = 'hello'
    assert response.to_dict()['body'] == 'hello'
    assert response['body'] == 'hello'

    response.key_map['test'] = 'test'
    response.test = 'hello'
    assert response['test'] == 'hello'

    assert len(response) == len('hello')
