import csv

def read_products_from_csv(file_path):
    products = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for line_number, row in enumerate(reader, start=1):
            try:
                # Check if required fields are present
                if not row["Código interno"] or not row["Nome"]:
                    raise ValueError("Missing required fields")
                
                # Normalize field names
                product = {
                    "internal_code": row.get("Código interno", "").strip(),
                    "barcode": row.get("Código de barras", "").strip(),
                    "name": row.get("Nome", "").strip(),
                    "regular_price": row.get("Preço regular", "").strip(),
                    "promo_price": row.get("Promocao", "").strip(),
                    "promo_start_at": row.get("Data inicio promocao", "").strip(),
                    "promo_end_at": row.get("Data termino promocao", "").strip(),
                    "stock": row.get("estoque", "").strip(),
                    "visible": row.get("ativo", "").strip().lower() == 'true',
                    "wholesale_price": row.get("preco atacado", "").strip(),
                    "wholesale_qtd": row.get("qtd minima atacado", "").strip(),
                    "weight": row.get("peso", "").strip(),
                    "length": row.get("comprimento", "").strip(),
                    "width": row.get("largura", "").strip(),
                    "height": row.get("altura", "").strip(),
                    "increment_value": row.get("incremento", "").strip(),
                    "unit_type": row.get("tipo unidade", "").strip() or "UNI",
                    "aux_codes": eval(row.get("codigos auxiliares", "[]")),
                    "auto_revoke_promo": row.get("remover promocao automatica", "").strip().lower() == 'true',
                    "subcategory_ids": eval(row.get("subcategorias", "[]")),
                    "force_subcategory": row.get("forcar subcategoria", "").strip().lower() == 'true',
                    "main_subcategory": row.get("subcategoria principal", "").strip()
                }
                
                products.append(product)

            except Exception as e:
                print(f"❌[Line {line_number}] Skipped due to error: {e}")
    return products
