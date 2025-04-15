def format_product_data(raw_product):
    return {
        "name": raw_product["name"],
        "sku": raw_product["sku"],
        "price": float(raw_product.get("price", 0)),
        "stock": int(raw_product.get("stock", 0)),
        # Adicione campos conforme necessário, baseando-se na API
    }
