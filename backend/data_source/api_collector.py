import requests
from contracts.schema import GenericSchema
from typing import List

class APICollector:
    def __init__ (self, schema):
        self._schema = schema
        self._aws = None
        self._buffer = None
        return
    
    def start(self, param: int):
        response = self.getData(param)
        resp = self.extractData(response)
        return resp
    
    def getData(self, param: int):
        response = None
        if param > 1:
            response = requests.get(f'http://127.0.0.1:8000/gerar_compra/{param}').json()
        else:
            response = requests.get(f'http://127.0.0.1:8000/gerar_compra').json()
        return response
    
    def extractData(self, response):
        result: List[GenericSchema] = []

        for item in response:
            index = {}
            for key, value in self._schema.items():
                if type(item[key]) == value:
                    index[key] = item[key]
                else:
                    index[key] = None
            result.append(index)
        return result
    
    def transformDF(self):
        return