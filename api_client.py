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
        "api-key": f"{API_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "internal_code": product["codigo_interno"],
        "name": product["nome"],
        "unit_type": product.get("tipo_unidade", "UNI"),  # Ex: UNI, KG, BOX, etc.
        "price": float(product["preco_regular"].replace(",", ".")),
        "visible": product.get("ativo", True),
        "stock": float(product.get("estoque", 0)),

        "barcodes": [product["codigo_de_barras"]] if product.get("codigo_de_barras") else [],

        "promo_price": float(product["promocao"].replace(",", ".")) if product.get("promocao") else None,
        "promo_start_at": product.get("data_inicio_promocao"),
        "promo_end_at": product.get("data_termino_promocao"),

        "aux_codes": product.get("codigos_auxiliares", []),
        "auto_revoke_promo": product.get("remover_promocao_automatica", False),

        "wholesale_price": float(product["preco_atacado"].replace(",", ".")) if product.get("preco_atacado") else None,
        "wholesale_qtd": float(product["qtd_minima_atacado"]) if product.get("qtd_minima_atacado") else None,

        "weight": float(product["peso"]) if product.get("peso") else None,
        "length": float(product["comprimento"]) if product.get("comprimento") else None,
        "width": float(product["largura"]) if product.get("largura") else None,
        "height": float(product["altura"]) if product.get("altura") else None,

        "increment_value": float(product["incremento"]) if product.get("incremento") else None,

        "subcategory_ids": product.get("subcategorias", []),
        "force_subcategory": product.get("forcar_subcategoria", False),
        "main_subcategory": product.get("subcategoria_principal")
    }

    try:
        response = requests.put(url, json=payload, headers=headers)
        response.raise_for_status()
        return {"http_status": response.status_code}
    except requests.HTTPError as e:
        print(f"Error sending product {product['codigo_interno']}: {e}")
        return None
