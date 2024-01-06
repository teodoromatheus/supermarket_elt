from data_source.api_collector import APICollector
from contracts.schema import CompraSchema

teste_classe = APICollector(schema=CompraSchema).start(20)

print(teste_classe)