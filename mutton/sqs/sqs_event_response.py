import mutton


class SQSEventResponse(mutton.Response):
    """SQS Event Response class."""

    def __init__(self):
        super().__init__()

    @property
    def serialized(self):
        return None
