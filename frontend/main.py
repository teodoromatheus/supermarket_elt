import streamlit as st
import pandas as pd
from contracts.contrato_catalogo_produto import ExcelModel
from data_source.excel_collector import ExcelCollector

st.title('Importador de Excel')
st.header('Validador de Excel com o layout padrão')

arquivo = st.file_uploader('Envie seu arquivo e aguarde finalizar a validação:', type=['xlsx'])


if arquivo is not None:
    errors = ExcelCollector(schema=ExcelModel).start(arquivo_excel=arquivo)
    print(errors)
    if errors:
        for error in errors:
            st.error(error)
    
    else:
        st.success('Arquivo está OK!')
