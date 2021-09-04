from abc import abstractmethod

import mutton


class SQSEventHandler(mutton.Handler):

    def __init__(self):
        """Initialize the handler."""
        super().__init__()
        self.request_class = mutton.sqs.SQSEventRequest

    def perform(self, request, **kwargs):
        for record in request.records:
            self.process_message(record)
        return mutton.sqs.SQSEventResponse()

    @abstractmethod
    def process_message(self, message):
        pass