# Launching AWS Lambda fronted with AWS API Gateway using AWS SAM CLI

This is a simple example which uses a Lambda function written in Python. These services are deployed using AWS Serverless Application Model (SAM). SAM is a superset of AWS CloudFormation.

*Prerequisites:*
1. Have AWS access key installed.
2. Have SAM CLI installed:
https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html
3. Have access to an S3 bucket where the SAM deployment/config information will be stored.

## Get this code

```
git clone git://github.com/jhough/examples.git
cd examples/CloudFormation/sam-api-lambda/
```

## SAM Commands

```
sam validate --template sam_template.yaml

sam package --template-file sam_template.yaml --s3-bucket jimsbigdata --output-template-file cf_template.yaml

sam deploy  --template-file cf_template.yaml --stack-name serverless-time-fcn --capabilities CAPABILITY_IAM

aws cloudformation describe-stack-resources --stack-name serverless-time-fcn
```
Look for the RestApi PhysicalResourceId and copy it for below.


You can open a second command line window and enter this to get the log file output:
```
sam logs --stack-name serverless-time-fcn --name TimeFunction --tail
```

## Test The API:

```
curl --include --request GET --header "Content-Type: application/json" https://RESTAPI-PHYSICALRESOURCEID.execute-api.us-east-1.amazonaws.com/Prod/time
```

## Delete the SAM/CloudFormation stack:

```
aws cloudformation delete-stack --stack-name serverless-time-fcn
```
