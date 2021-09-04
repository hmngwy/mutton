class Request:
    """Base Request."""

    def __init__(self, event, context):
        """Initialize the request."""
        self.__event = event
        self.__context = context

    @property
    def event(self):
        """Return AWS Lambda Event Object."""
        return self.__event

    @event.setter
    def event(self, value):
        self.__event = value

    @property
    def context(self):
        """Return AWS Lambda Context Object."""
        return self.__context

    @context.setter
    def context(self, value):
        self.__context = value
