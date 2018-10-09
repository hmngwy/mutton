[![CircleCI](https://circleci.com/gh/hmngwy/py-aws-lambda-handler.svg?style=svg)](https://circleci.com/gh/hmngwy/py-aws-lambda-handler) [![codecov](https://codecov.io/gh/hmngwy/py-aws-lambda-handler/branch/develop/graph/badge.svg)](https://codecov.io/gh/hmngwy/py-aws-lambda-handler)

![](https://codecov.io/gh/hmngwy/py-aws-lambda-handler/branch/develop/graphs/tree.svg?height=70&width=898)

## aws-lambda-handlers

Better Python 3 AWS Lambda Handlers.

Currently, your only choice for making Python handlers for AWS Lambda is to create a function like so:

```
def handler(event, context):
    return True
```

This isn't ideal when you start dealing with more than one handler, or if you want to provide a configurable and reusable handler. This package provides three base classes, the `Handler`, the `Request`, and the `Response` handler.

The `Handler` class is a [callable](https://en.wikipedia.org/wiki/Callable_object), you create a subclass off of this, instantiate it, and that's what you configure AWSλ to invoke.

Your `Handler` has to have a `perform(self, request)` method, this is houses handler's business logic, `Handler.__call__` executes this function and expects a `Response` object.

The `Response` object behaves like a dictionary, because AWSλ expects a handler to return a dictionary, your `Response` object is finally serialized as a `dict`.

The `request` argument in `perform(self, request)` is a `Request` object, and it houses the `event` and `context` parameters that AWSλ passes to your handler. Packaging those handler arguments into an object makes these arguments available for transparent mutations, see [`aws_lambda.apig.APIGatewayRequest`](py-aws-lambda-handler/aws_lambda/apig/\_\_init\_\_.py) for reference.

The foundation of this library is tiny, I recommend reviewing the [main classes](py-aws-lambda-handler/aws_lambda/__init__.py) to further understand how to use this package.

### Usage

```
pip install aws-lambda-handler
```

```python
import aws_lambda

class EchoHandler(aws_lambda.Handler):
    """Echo handler."""

    def perform(self, request, **k):
        """Echo perform method."""
        response = aws_lambda.Response()
        response.body = self.request.event
        return response

echo_handler = EchoHandler()

# `echo_handler` is now a callable function you can map your AWS Lambda function to
```

### Develop

Fork this library and send over PRs, I will consider applications for contributors if two of your PRs gets merged and published.

```
pipenv sync --dev # setup
pipenv run pytest # test
```

### Supported Event Sources

- [x] API Gateway `aws_lambda.apig`
- [ ] S3
- [ ] DynamoDB
- [ ] SNS
- [ ] SES
- [ ] SQS
- [ ] Cognito
- [ ] Cloudwatch Logs, Events

#### Help

We want support for more event sources, I am willing to entertain PRs. You can use the `aws_lambda.apig` submodule as an example of implementing more event sources.
