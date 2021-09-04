from cached_property import cached_property

import mutton


class SQSEventRequest(mutton.Request):
    """SQS Event Request class."""

    def __init__(self, event, context):
        """Initialize the class."""
        super().__init__(event, context)
        self.__records = event['Records']

    @cached_property
    def records(self):
        records = []
        for record in self.__records:
            message = mutton.sqs.SQSMessage(record)
            records.append(message)
        return records
