from pydantic import BaseModel, PositiveFloat, EmailStr
from enum import Enum
from datetime import date

class CategoriaEnum(str, Enum):
    Categoria1 = 'Categoria 1'
    Categoria2 = 'Categoria 2'
    Categoria3 = 'Categoria 3'
    Categoria4 = 'Categoria 4'
    Categoria5 = 'Categoria 5'
    Categoria6 = 'Categoria 6'
    Categoria7 = 'Categoria 7'
    Categoria8 = 'Categoria 8'
    Categoria9 = 'Categoria 9'

class ExcelModel(BaseModel):
    ean : int
    Produto : str
    Categoria : CategoriaEnum
    Descrição : str
    Preço : PositiveFloat
    Fornecedor : EmailStr
    Data : date

