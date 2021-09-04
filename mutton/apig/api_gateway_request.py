from collections import namedtuple

import inflection
from cached_property import cached_property

import mutton


class APIGatewayRequest(mutton.Request):
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
