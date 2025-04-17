import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
BASE_URL = os.getenv("BASE_URL")

def parse_date(data_str):
    try:
        return datetime.strptime(data_str, "%d/%m/%Y").isoformat() + "Z"
    except:
        return None

def send_product_to_api(product):
    if not API_TOKEN or not BASE_URL:
        raise ValueError("API_TOKEN ou BASE_URL não foram carregados corretamente do .env")

    url = f"{BASE_URL}products"
    headers = {
        "api-key": API_TOKEN,
        "Content-Type": "application/json"
    }

    payload = {
        "internal_code": product["codigo_interno"],
        "name": product["nome"],
        "unit_type": product.get("tipo_unidade") if product.get("tipo_unidade") in ["UNI", "KG", "BOX", "M2", "M", "L"] else "UNI",
        "price": float(product["preco_regular"].replace(",", ".")) if product["preco_regular"] else 0.0,
        "visible": bool(product.get("ativo", True)),
        "stock": float(product["estoque"]) if product["estoque"] else 0.0,
        "barcodes": [product["codigo_de_barras"]] if product["codigo_de_barras"] else [],
        "promo_price": float(product["promocao"].replace(",", ".")) if product["promocao"] else None,
        "promo_start_at": parse_date(product["data_inicio_promocao"]),
        "promo_end_at": parse_date(product["data_termino_promocao"]),
        "aux_codes": product.get("codigos_auxiliares", []),
        "auto_revoke_promo": bool(product.get("remover_promocao_automatica", False)),
        "wholesale_price": float(product["preco_atacado"].replace(",", ".")) if product["preco_atacado"] else None,
        "wholesale_qtd": float(product["qtd_minima_atacado"]) if product["qtd_minima_atacado"] else None,
        "weight": float(product["peso"]) if product["peso"] else None,
        "length": float(product["comprimento"]) if product["comprimento"] else None,
        "width": float(product["largura"]) if product["largura"] else None,
        "height": float(product["altura"]) if product["altura"] else None,
        "increment_value": float(product["incremento"]) if product["incremento"] else None,
        "subcategory_ids": product.get("subcategorias", []),
        "force_subcategory": bool(product.get("forcar_subcategoria", False)),
        "main_subcategory": product.get("subcategoria_principal") or None
    }

    try:
        response = requests.put(url, json={"products": [payload]}, headers=headers)
        response.raise_for_status()
        return {"http_status": response.status_code}
    except requests.HTTPError as e:
        return {
            "error": True,
            "status_code": e.response.status_code,
            "message": e.response.text
        }
