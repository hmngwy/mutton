#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=unused-argument
"""Test base objects."""
import mutton.sqs as mutton


def test_sqs_request():
    """Test SQS Request."""
    request = mutton.SQSEventRequest(
        {
            'Records': [
                {
                    'awsRegion': 'us-west-2',
                    'body': 'hello'
                }
            ]
        }, {})
    assert request.records[0]['awsRegion'] == "us-west-2"
    assert request.records[0]['body'] == "hello"
    assert request.context == {}


def test_sqs_response():
    """Test SQS Response."""
    response = mutton.SQSEventResponse()
    assert response.serialized == None


def test_sws_handler():
    """Test SQS Handler"""

    class TestHandler(mutton.SQSEventHandler):
        """Test handler."""

        def processMessage(self, message):
            """Test processMessage method."""
            assert message.awsRegion == "us-west-2"
            assert message.body == "hello"

    test_handler = TestHandler()
    request_object = {
        'Records': [
            {
                'awsRegion': 'us-west-2',
                'body': 'hello'
            }
        ]
    }
    invocation = test_handler(request_object, {})
    assert invocation == None
