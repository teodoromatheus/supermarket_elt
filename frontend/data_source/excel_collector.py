import pandas as pd
import openpyxl
from datetime import datetime

class ExcelCollector():
    def __init__(self, schema):
        self._schema = schema
        self._aws = None
        self._excel = None

    def start(self, arquivo_excel):
        data_frame = self.transformToDataFrame(arquivo=arquivo_excel)
        errors = self.validateDataFrame(dataframe=data_frame)
        return errors
        
    def transformToDataFrame(self, arquivo):
        data_frame = pd.read_excel(arquivo, parse_dates=['Data'])
        return data_frame

    def validateDataFrame(self, dataframe):
        errors = []
        for index, row in dataframe.iterrows():
            try:
                self._schema(**row.to_dict())
            except Exception as e:
                errors.append(f'Erro linha {index+2}: {e}')
        return errors