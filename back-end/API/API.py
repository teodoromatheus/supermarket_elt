from fastapi import FastAPI
from faker import Faker

app = FastAPI()
fake = Faker()

@app.get("/gerar_compra")
async def gerar_compra():
    return {
        "client": fake.name(),
        "creditCard": fake.credit_card_provider(),
        "ean": "Código de Barra",
        "price": "Preço do produto",
        "store": 11,
        "dateTime": fake.iso8601(),
        "clientPosition": fake.location_on_land()
    }