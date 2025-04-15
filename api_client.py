import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
BASE_URL = os.getenv("BASE_URL")

def send_product_to_api(product):
    if not API_TOKEN or not BASE_URL:
        raise ValueError("API_TOKEN ou BASE_URL não foram carregados corretamente do .env")

    url = f"{BASE_URL}products"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "sku": product["codigo_interno"],
        "barcode": product["codigo_de_barras"],
        "name": product["nome"],
        "price": float(product["preco_regular"].replace(",", ".")),
        "promo_price": float(product["promocao"].replace(",", ".")) if product["promocao"] else None,
        "promo_end": product["data_termino_promocao"] if product["data_termino_promocao"] else None,
        "stock": int(product["estoque"]),
        "active": product["ativo"]
    }

    try:
        response = requests.put(url, json=payload, headers=headers)
        response.raise_for_status()
        return {"http_status": response.status_code}
    except requests.HTTPError as e:
        print(f"Error sending product {product['codigo_interno']}: {e}")
        return None
