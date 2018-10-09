[![CircleCI](https://circleci.com/gh/hmngwy/py-aws-lambda-handler.svg?style=svg)](https://circleci.com/gh/hmngwy/py-aws-lambda-handler) [![codecov](https://codecov.io/gh/hmngwy/py-aws-lambda-handler/branch/develop/graph/badge.svg)](https://codecov.io/gh/hmngwy/py-aws-lambda-handler)

![](https://codecov.io/gh/hmngwy/py-aws-lambda-handler/branch/develop/graphs/tree.svg?height=70&width=898)

### aws-lambda-handlers

Better Python 3 AWS Lambda Handlers.


##### Usage

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

##### Develop

```
pipenv sync --dev # setup
pipenv run pytest # test
```

##### Supported Event Sources

- [x] API Gateway `aws_lambda.apig`
- [ ] S3
- [ ] DynamoDB
- [ ] SNS
- [ ] SES
- [ ] SQS
- [ ] Cognito
- [ ] Cloudwatch Logs, Events

###### Help

We want support for more event sources, I am willing to entertain PRs. You can use the `aws_lambda.apig` submodule as an example of implementing more event sources.
