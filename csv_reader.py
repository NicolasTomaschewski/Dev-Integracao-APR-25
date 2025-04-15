import csv

def read_products_from_csv(file_path):
    products = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for line_number, row in enumerate(reader, start=1):
            try:
                # Verifica se os campos obrigatórios estão presentes
                if not row["Código interno"] or not row["Nome"]:
                    raise ValueError("Missing required fields")
                
                # Normaliza os nomes dos campos
                product = {
                    "codigo_interno": row["Código interno"].strip(),
                    "codigo_de_barras": row["Código de barras"].strip(),
                    "nome": row["Nome"].strip(),
                    "preco_regular": row["Preço regular"].strip(),
                    "promocao": row["Promocao"].strip(),
                    "data_termino_promocao": row["Data termino promocao"].strip(),
                    "estoque": row["estoque"].strip(),
                    "ativo": row["ativo"].strip().lower() == 'true'  # Converte para booleano
                }

                products.append(product)

            except Exception as e:
                print(f"❌[Line {line_number}] Skipped due to error: {e}")
    return products
