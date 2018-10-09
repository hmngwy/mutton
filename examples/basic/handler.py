#!/usr/bin/env python
# -*- coding: utf-8 -*-
import aws_lambda


class BasicHandler(aws_lambda.Handler):
    """Test handler."""

    def perform(self, request, **k):
        """Test perform method."""
        response = aws_lambda.Response()
        response.body = request.event
        return response


basic = BasicHandler()
