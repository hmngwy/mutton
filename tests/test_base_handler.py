#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=unused-argument
"""Test base objects."""
import aws_lambda as al


def test_base_request():
    """Test base Request."""
    request = al.Request({}, {})
    assert request.event is not None
    assert request.context is not None


def test_base_handler():
    """Test base Handler."""

    class TestHandler(al.Handler):
        """Test handler."""

        def perform(self, request, **k):
            """Test perform method."""
            body = self.request.event['att']
            response = al.Response()
            response.body = body
            return response

    test_handler = TestHandler()
    invocation = test_handler({'att': 1.0}, {})

    assert invocation['body'] == 1.0
