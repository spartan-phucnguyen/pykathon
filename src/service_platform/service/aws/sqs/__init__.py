from service_platform.settings import settings

from .. import aws_credentials_dummy
from .consumer import SQSConsumer
from .producer import SQSJobProducer

if settings.aws.sqs.localstack is True:
    endpoint_url = settings.aws.endpoint_url
    aws_credentials = aws_credentials_dummy
else:
    endpoint_url = None
    aws_credentials = {}
