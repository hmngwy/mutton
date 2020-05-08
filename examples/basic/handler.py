#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mutton


class BasicHandler(mutton.Handler):
    """Test handler."""

    def perform(self, request, **k):
        """Test perform method."""
        response = mutton.Response()
        response.body = request.event
        return response


basic = BasicHandler()
