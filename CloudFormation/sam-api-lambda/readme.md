* SAM Commands


sam validate --template sam_template.yaml

SKIP: sam build --build-dir lambda --template sam_template.yaml

sam package --template-file sam_template.yaml --s3-bucket jimsbigdata --output-template-file cf_template.yaml

sam deploy  --template-file cf_template.yaml --stack-name serverless-time-fcn --capabilities CAPABILITY_IAM

aws cloudformation describe-stack-resources --stack-name serverless-time-fcn

sam logs --stack-name serverless-time-fcn --name TimeFunction --tail


aws cloudformation delete-stack --stack-name serverless-time-fcn

* TEST API:

curl https://APIIDGOESHERE.execute-api.us-east-1.amazonaws.com/Prod/time
