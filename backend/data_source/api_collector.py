import requests

class APICollector:
    def __init__ (self):
        self._schema = None
        self._aws = None
        self._buffer = None
        return
    
    def start(self):
        return
    
    def getData(self, param: int):
        response = None
        if param > 1:
            response = requests.get(f'http://127.0.0.1:8000/gerar_compra/{param}').json()
        else:
            response = requests.get(f'http://127.0.0.1:8000/gerar_compra').json()
        return response
    
    def extractData(self):
        return
    
    def transformDF(self):
        return