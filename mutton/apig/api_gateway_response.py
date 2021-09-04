import mutton


class APIGatewayResponse(mutton.Response):
    """API Gateway Response class."""

    def __init__(self, body='', status_code=200,
                 headers=None, is_base64=False):
        """Initialize instance with list, tuple, or dict."""
        super().__init__()
        self.store = {}
        self.__base_headers = {
            # 'Access-Control-Allow-Origin': '*',
            'X-Server': 'AWS λ'
        }
        self.key_map = {'status_code': 'statusCode',
                        'is_base64': 'isBase64Encoded',
                        'headers': 'headers',
                        'body': 'body'}

        # fool proofing checks
        if headers and not isinstance(headers, dict):
            raise ValueError('Headers value must be dict.')
        if not isinstance(status_code, int):
            raise ValueError('Status Code value must be int.')

        self.headers = {}
        if headers:
            self.headers = headers

        self.status_code = status_code
        self.body = body
        self.is_base64 = is_base64

    def __setattr__(self, name, value):
        """Set attribute with some manually managed attributes."""
        # prevent recursion
        if name in ['key_map', 'store']:
            super().__setattr__(name, value)
        # process managed attrs
        if name in self.key_map.keys():
            store_key = self.key_map[name]
            if name == 'headers':
                value = {**self.__base_headers, **value}
            self.store[store_key] = value
        else:
            super().__setattr__(name, value)

    @property
    def serialized(self):
        return self.store
