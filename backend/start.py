from data_source.api_collector import APICollector
from contracts.schema import CompraSchema
from aws.client import S3Client

aws = S3Client()

teste_classe = APICollector(schema=CompraSchema, aws=aws).start(20)

print(teste_classe)