import requests
from config import API_TOKEN, BASE_URL

def send_product_to_api(product_data):
    url = f"{BASE_URL}products"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.put(url, json=product_data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error sending product {product_data.get('sku')}: {e}")
        return None
