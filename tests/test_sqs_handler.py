#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=unused-argument
"""Test base objects."""
import mutton.sqs as mutton


def test_sqs_handler():
    """Test SQS Handler"""

    class TestHandler(mutton.SQSEventHandler):
        """Test handler."""

        def processMessage(self, message):
            """Test processMessage method."""
            assert message.message_id == "1111"
            assert message.receipt_handle == "2222"
            assert message.body == "hello"
            assert message.md5_of_body == "3333"
            assert message.md5_of_message_attributes == "4444"
            assert message.event_source_arn == "arn"
            assert message.event_source == "source"
            assert message.aws_region == "us-west-2"
            assert message.attributes['messageDeduplicationId'] == "5555"
            assert message.attributes['messageGroupId'] == "6666"
            assert message.message_attributes['correlationId']['stringValue'] == "7777"
            assert message.message_attributes['correlationId']['dataType'] == "String"

    test_handler = TestHandler()
    request_object = {
        'Records': [
            {
                'messageId': '1111',
                'receiptHandle': '2222',
                'body': 'hello',
                'md5OfBody': '3333',
                'md5OfMessageAttributes': '4444',
                'eventSourceArn': 'arn',
                'eventSource': 'source',
                'awsRegion': 'us-west-2',
                'attributes': {
                    'messageDeduplicationId': '5555',
                    'messageGroupId': '6666'
                },
                'messageAttributes': {
                    'correlationId': {
                        'stringValue': '7777',
                        'dataType': 'String'
                    }
                }
            }
        ]
    }
    invocation = test_handler(request_object, {})
    assert invocation == None
