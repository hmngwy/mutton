#!/bin/bash

TEMPDIR=$(mktemp -d)
TEMPZIP=$(mktemp -d)
cp handler.py $TEMPDIR/
cp -R ../../* $TEMPDIR/

echo $TEMPDIR
(cd $TEMPDIR && zip -r - *) > $TEMPZIP/archive.zip

aws iam create-role \
    --role-name example-lambda-role \
    --assume-role-policy-document file://../role-policy.json

aws iam attach-role-policy \
    --role-name example-lambda-role \
    --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

sleep 3

ROLEARN=$(aws iam get-role --role-name example-lambda-role | cut -f2 | head -n1)

aws lambda create-function \
    --function-name aws-lambda-handler-basic-example \
    --zip-file fileb://$TEMPZIP/archive.zip \
    --role $ROLEARN \
    --handler handler.basic \
    --runtime python3.6

aws lambda invoke \
    --invocation-type RequestResponse \
    --function-name aws-lambda-handler-basic-example \
    --log-type Tail \
    --payload '{"echo":"me"}' \
    response.json

cat response.json
rm response.json

aws lambda delete-function \
    --function-name aws-lambda-handler-basic-example

aws iam detach-role-policy \
    --role-name example-lambda-role \
    --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
aws iam delete-role \
    --role-name example-lambda-role
