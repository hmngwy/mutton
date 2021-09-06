from abc import ABC, abstractmethod

import mutton


class Handler(ABC):
    """Base Handler."""

    def __init__(self):
        """Initialize the handler."""
        self.request_class = mutton.Request
        self.request = None

    def __call__(self, event, context, **kwargs):
        """Wrap perform(), invoked by AWS Lambda."""
        self.__init__()  # reset the instance

        self.request = self.request_class(event, context)
        response = self.perform(self.request, **kwargs)

        return response.serialized

    @abstractmethod
    def perform(self, request, **kwargs):
        pass
