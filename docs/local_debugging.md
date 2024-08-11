## Debug in Local

### Start the localstack

Ref: https://docs.localstack.cloud/overview

Use docker-compose.yaml to start the localstack

```yaml
  localstack:
    container_name: "${LOCALSTACK_DOCKER_NAME:-localstack-main}"
    image: localstack/localstack
    ports:
      - "127.0.0.1:4566:4566"            # LocalStack Gateway
      - "127.0.0.1:4510-4559:4510-4559"  # external services port range
    environment:
      # LocalStack configuration: https://docs.localstack.cloud/references/configuration/
      - DEBUG=${DEBUG:-0}
      - SERVICES=s3
    volumes:
      - "${LOCALSTACK_VOLUME_DIR:-./volume}:/var/lib/localstack"
      - "/var/run/docker.sock:/var/run/docker.sock"
```

Install the localstack and awscli-local cli

```shell
brew install localstack/tap/localstack-cli
brew install awscli-local
```

Create a new S3 bucket

```shell
awslocal s3 mb s3://service-platform-local --region us-west-2
awslocal sqs create-queue --queue-name example-worker-local --region us-west-2
```

Create cors-config.json

```
{
  "CORSRules": [
    {
      "AllowedOrigins": ["*"],
      "AllowedMethods": ["GET", "PUT", "POST", "DELETE"],
      "AllowedHeaders": ["*"]
    }
  ]
}
```

```shell
awslocal s3api put-bucket-cors --bucket service-platform-local --cors-configuration file://{PATH_TO_YOUR_FOLDER}/cors-config.json
```

Use the environment variable to overwrite the AWS Endpoint URL by using localstack

```shell
AWS__ENDPOINT_URL=http://localhost.localstack.cloud:4566
AWS__SQS_QUEUE_URL=http://sqs.us-west-2.localhost.localstack.cloud:4566/000000000000/example-worker-local"
```

or update the `config.local.yaml` file

```yaml
aws:
  endpoint_url: "http://localhost.localstack.cloud:4566"
  sqs_queue_url: "http://sqs.us-west-2.localhost.localstack.cloud:4566/000000000000/example-worker-local"
```

List the current objects on localstack s3 bucket

```shell
awslocal s3api list-objects --bucket service-platform-local
```

```json
{
  "Contents": [
    {
      "Key": "36506883-4552-423d-9fc2-c2adf8dd46f8/cP8tFnYxnnHJaAI2jFUffejR7CCjEvFp.pdf",
      "LastModified": "2024-05-20T04:08:46+00:00",
      "ETag": "\"5afaf79789a776d81ec91ccbdc9fdaba\"",
      "Size": 142786,
      "StorageClass": "STANDARD",
      "Owner": {
        "DisplayName": "webfile",
        "ID": "75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a"
      }
    }
  ],
  "RequestCharged": null
}
```

list sqs message

```shell
awslocal sqs receive-message --queue-url http://sqs.us-west-2.localhost.localstack.cloud:4566/000000000000/locals3-sqs
```

```json
{
  "Messages": [
    {
      "MessageId": "3964f2b3-0afa-4520-88f3-a23dc7cb0606",
      "ReceiptHandle": "MTZhNDU1ZjctNjk0YS00ZjFmLWExZjYtMDg2YmRhMzU2MTkyIGFybjphd3M6c3FzOnVzLXdlc3QtMjowMDAwMDAwMDAwMDA6bG9jYWxzMy1zcXMgMzk2NGYyYjMtMGFmYS00NTIwLTg4ZjMtYTIzZGM3Y2IwNjA2IDE3MTYyODMxMTIuNjU4MTYx",
      "MD5OfBody": "7207c5c25dc295e037848f7917b60393",
      "Body": "{\"user_id\": \"9b31b971-273e-481a-a961-942f46f6b122\", \"s3_object\": \"documents/9b31b971-273e-481a-a961-942f46f6b122/4PuwOQFkp8FEJ07vbMG8dPH6Ey7W0tf6.pdf\"}"
    }
  ]
}
```
