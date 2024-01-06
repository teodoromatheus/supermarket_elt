from typing import Union, Dict

GenericSchema = Dict[str, Union[str, int, float]]

CompraSchema: GenericSchema = {
    "ean" : int,
    "price" : float,
    "store" : int,
    "dateTime" : str
}