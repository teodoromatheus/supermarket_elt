import requests
from contracts.schema import GenericSchema
from typing import List
from io import BytesIO
from datetime import datetime
import pyarrow.parquet as pq
import pandas as pd

class APICollector:
    def __init__ (self, schema, aws):
        self._schema = schema
        self._aws = aws
        self._buffer = None
        return
    
    def start(self, param: int):
        response = self.getData(param)
        resp = self.extractData(response)
        df = self.transformDF(resp)
        parquet_file = self.convertToParquet(df)

        if parquet_file is not None:
            file_name = self.fileName()
            self._aws.upload_file(data=parquet_file, s3_key=file_name)
            return True
        
        return False
    
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
    
    def transformDF(self, response):
        df = pd.DataFrame(response)
        return df
    
    def convertToParquet(self, df):
        self._buffer = BytesIO()
        try:
            df.to_parquet(self._buffer)
            return self._buffer
        except:
            print('Erro ao transformar o DataFrame em Parquet')
            self._buffer = None
    
    def fileName(self):
        data_atual = datetime.now().isoformat()
        match = data_atual.split(".")
        return f'api/api-response-compra-{match[0]}.parquet'