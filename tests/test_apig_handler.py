#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=unused-argument
"""Test base objects."""
import pytest
import aws_lambda.apig as aws_lambda


def test_apig_request():
    """Test APIG Request."""
    request = aws_lambda.APIGatewayRequest({
        'body': 'hello',
        'headers': {
            'X-Client': 'APIG-REQUEST-TEST'
        },
        'pathParameters': {
            'user-id': 'user-1234'
        },
        'queryStringParameters': {
            'filter-x': 'asc'
        }
    }, {})
    assert request.body == "hello"
    assert request.headers.x_client == 'APIG-REQUEST-TEST'
    assert request.path.user_id == 'user-1234'
    assert request.query.filter_x == 'asc'
    assert request.context == {}


def test_apig_response():
    """Test APIG Response."""
    response = aws_lambda.APIGatewayResponse('Hi', 200)
    assert response.status_code == 200

    response.body = 'test body'
    assert response.body == 'test body'

    response.headers = {
        'X-Custom': 'Custom Header'
    }
    assert response.headers['X-Custom'] == 'Custom Header'

    assert not response.is_base64
    response.is_base64 = True
    assert response.is_base64

    response.__setattr__('asd', 'qwe')
    assert response.asd == 'qwe'

    response.test = 'hey'
    assert response.test == 'hey'

    response.status_code = 400
    as_dict = response.to_dict()
    assert as_dict['statusCode'] == 400
    assert as_dict['body'] == 'test body'
    assert as_dict['isBase64Encoded']
    assert 'X-Custom' in as_dict['headers']

    response = aws_lambda.APIGatewayResponse('Hi',
                                             status_code=200,
                                             headers={'X-Custom': 'defined on init'})
    assert response.headers['X-Custom'] == 'defined on init'


def test_apig_handler():
    """Test APIG Handler"""

    class TestHandler(aws_lambda.APIGatewayHandler):
        """Test handler."""

        def perform(self, request, **k):
            """Test perform method."""
            response = aws_lambda.APIGatewayResponse('', 200)
            response.body = request.path.user_id + request.query.filter_x
            response.headers = {'X-Custom': 'test'}
            return response

    test_handler = TestHandler()
    request_object = {
        'body': 'hello',
        'headers': {
            'X-Client': 'APIG-REQUEST-TEST'
        },
        'pathParameters': {
            'user-id': 'user-1234'
        },
        'queryStringParameters': {
            'filter-x': 'asc'
        }
    }
    invocation = test_handler(request_object, {})
    assert invocation['body'] == 'user-1234asc'
    assert 'X-Custom' in invocation['headers']


def test_apig_bad_response():
    """Test raised exceptions."""
    with pytest.raises(ValueError):
        aws_lambda.APIGatewayResponse(
            'Hi', headers='bad headers', status_code=200)
    with pytest.raises(ValueError):
        aws_lambda.APIGatewayResponse('Hi', status_code='not-an-int')
