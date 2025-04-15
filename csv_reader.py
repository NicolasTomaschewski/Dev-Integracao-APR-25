import csv

def read_products_from_csv(file_path):
    products = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        headers = [h.strip().lower() for h in headers]  # Normaliza os cabeçalhos
        for line_number, row in enumerate(reader, start=2):  # Começa da linha 2 por causa do cabeçalho
            try:
                product = dict(zip(headers, row))
                
                # Verifica se os campos obrigatórios existem no cabeçalho
                if "name" not in product or "sku" not in product:
                    raise ValueError("Missing 'name' or 'sku' in headers")

                # Verifica se os campos obrigatórios estão preenchidos
                if not product["name"].strip() or not product["sku"].strip():
                    raise ValueError("Empty 'name' or 'sku'")

                products.append(product)

            except Exception as e:
                print(f"[Line {line_number}] Skipped due to error: {e}")
    return products
