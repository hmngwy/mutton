#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=unused-argument
"""Test base objects."""
import pal


def test_base_request():
    """Test base Request."""
    request = pal.Request({}, {})
    assert request.event is not None
    assert request.context is not None


def test_base_handler():
    """Test base Handler."""

    class TestHandler(pal.Handler):
        """Test handler."""

        def perform(self, request, **k):
            """Test perform method."""
            response = pal.Response()
            response.body = self.request.event['att']
            return response

    test_handler = TestHandler()
    request_object = {'att': 1.0}
    invocation = test_handler(request_object, {})

    assert invocation['body'] == 1.0
