from fastapi import FastAPI
from faker import Faker
import pandas as pd
import random

app = FastAPI()
fake = Faker()
df_products = pd.read_csv("back-end/API/products.csv",delimiter=";")
df_products['indice'] = range(1,len(df_products)+1)
df_products.set_index('indice',inplace=True)

@app.get("/gerar_compra")
async def gerar_compra():
    index = random.randint(1,len(df_products)+1)
    registro = df_products.iloc[index]
    return {
        "client": fake.name(),
        "creditCard": fake.credit_card_provider(),
        "ean": int(registro["ean"]),
        "productName": registro["product"],
        "price": round(float(registro["price"])*1.2,2),
        "store": 11,
        "dateTime": fake.iso8601(),
        "clientPosition": fake.location_on_land()
    }   