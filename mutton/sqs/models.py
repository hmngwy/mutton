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


class SQSEventResponse(mutton.Response):
    """SQS Event Response class."""

    def __init__(self):
        super().__init__()

    @property
    def serialized(self):
        return None


class SQSMessage(object):
    """SQS Message class"""

    def __init__(self, record):
        super().__init__()
        self.__message_id = record["messageId"]
        self.__receipt_handle = record["receiptHandle"]
        self.__body = record["body"]
        self.__md5_of_body = record["md5OfBody"]
        self.__md5_of_message_attributes = record["md5OfMessageAttributes"]
        self.__event_source_arn = record["eventSourceArn"]
        self.__event_source = record["eventSource"]
        self.__aws_region = record["awsRegion"]
        self.__attributes = record["attributes"]
        self.__message_attributes = record["messageAttributes"]

    @cached_property
    def message_id(self):
        return str(self.__message_id)

    @cached_property
    def receipt_handle(self):
        return str(self.__receipt_handle)

    @cached_property
    def body(self):
        return str(self.__body)

    @cached_property
    def md5_of_body(self):
        return str(self.__md5_of_body)

    @cached_property
    def md5_of_message_attributes(self):
        return str(self.__md5_of_message_attributes)

    @cached_property
    def event_source_arn(self):
        return str(self.__event_source_arn)

    @cached_property
    def event_source(self):
        return str(self.__event_source)

    @cached_property
    def aws_region(self):
        return str(self.__aws_region)

    @cached_property
    def attributes(self):
        return self.__attributes

    @cached_property
    def message_attributes(self):
        return self.__message_attributes
