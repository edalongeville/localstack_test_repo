import pulumi
from pulumi_aws import Provider, s3, route53, apigateway

awsProvider = Provider(
    "localstack",
    skip_credentials_validation=True,
    skip_metadata_api_check=True,
    s3_force_path_style=True,
    skip_requesting_account_id=True,
    access_key="mockAccessKey",
    secret_key="mockSecretKey",
    region="eu-west-1",
    endpoints=[{
        # "APIGateway": "http://localhost:4567",
        # "CloudFormation": "http://localhost:4581",
        # "CloudWatch": "http://localhost:4582",
        # "CloudWatchLogs": "http://localhost:4586",
        # "DynamoDB": "http://localhost:4569",
        # "DynamoDBStreams": "http://localhost:4570",
        # "Elasticsearch": "http://localhost:4571",
        # "ES": "http://localhost:4578",
        # "Firehose": "http://localhost:4573",
        # "IAM": "http://localhost:4593",
        # "Kinesis": "http://localhost:4568",
        # "KMS": "http://localhost:4584",
        # "Lambda": "http://localhost:4574",
        # "Redshift": "http://localhost:4577",
        "Route53": "http://localhost:4580",
        # "StepFunctions": "http://localhost:4585",
        "S3": "http://localhost:4572",
        # "SES": "http://localhost:4579",
        # "SNS": "http://localhost:4575",
        # "SQS": "http://localhost:4576",
        # "SSM": "http://localhost:4583",
        # "STS": "http://localhost:4592"
    }])

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket(
    'my-bucket',
    opts=pulumi.ResourceOptions(provider=awsProvider)
)

# Export the name of the bucket
pulumi.export(
    'bucket_name',
    bucket.id
)

zone = route53.Zone(
    resource_name="myzone",
    name="myzone.com",
    opts=pulumi.ResourceOptions(provider=awsProvider)
)

# Didn't get apigateway to work yet
# api = apigateway.RestApi(
#    resource_name=f"myapi",
#    description="API Gateway",
#    binary_media_types=["multipart/form-data"],
#    opts=pulumi.ResourceOptions(provider=awsProvider,),
# )
