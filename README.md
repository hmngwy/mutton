[![CircleCI](https://circleci.com/gh/hmngwy/mutton.svg?style=svg)](https://circleci.com/gh/hmngwy/mutton) [![codecov](https://codecov.io/gh/hmngwy/mutton/branch/develop/graph/badge.svg)](https://codecov.io/gh/hmngwy/mutton)

![](https://codecov.io/gh/hmngwy/mutton/branch/develop/graphs/tree.svg?height=70&width=898)

## mutton

Better Python 3 AWS Lambda Handlers.

Currently, your only choice for making Python handlers for AWS Lambda is to create a function like so:

```
def handler(event, context):
    return True
```

This isn't ideal when you start dealing with more than one handler, or if you want to provide a configurable and reusable handler. This package provides three base classes, the `Handler`, the `Request`, and the `Response` handler.

The `Handler` class is a [callable](https://en.wikipedia.org/wiki/Callable_object), you create a subclass off of this, instantiate it, and that's what you configure AWSλ to invoke.

Your `Handler` has to have a `perform(self, request)` method, this houses your handler's business logic, `Handler.__call__` executes this function and expects a `Response` object.

The `Response` object behaves like a dictionary and an object, an attribute called `serialized` is returned to AWSλ.

The `request` argument in `perform(self, request)` is a `Request` object, and it houses the `event` and `context` parameters that AWSλ passes to your handler. Packaging those handler arguments into an object makes them available for transparent mutations, see [`mutton.apig.APIGatewayRequest`](mutton/mutton/apig/\_\_init\_\_.py) for reference.

The foundation of this library is tiny, I recommend reviewing the [main classes](mutton/mutton/__init__.py) to further understand how to use this package.

### Usage

```
pip install mutton
```

```python
import mutton

class EchoHandler(mutton.Handler):
    """Echo handler."""

    def perform(self, request, **k):
        """Echo perform method."""
        response = mutton.Response()
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

- [x] API Gateway `mutton.apig`
- [ ] S3
- [ ] DynamoDB
- [ ] SNS
- [ ] SES
- [x] SQS `mutton.sqs`
- [ ] Cognito
- [ ] Cloudwatch Logs, Events

#### Help

We want support for more event sources, I am willing to entertain PRs. You can use the `mutton.apig` submodule as an example of implementing more event sources.
