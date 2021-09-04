from abc import ABCMeta

import mutton


class APIGatewayHandler(mutton.Handler, metaclass=ABCMeta):

    def __init__(self):
        """Initialize the handler."""
        super().__init__()
        self.request_class = mutton.apig.APIGatewayRequest
        self.request = None
