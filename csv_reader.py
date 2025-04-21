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
                    "codigo_interno": row.get("Código interno", "").strip(),
                    "codigo_de_barras": row.get("Código de barras", "").strip(),
                    "nome": row.get("Nome", "").strip(),
                    "preco_regular": row.get("Preço regular", "").strip(),
                    "promocao": row.get("Promocao", "").strip(),
                    "data_inicio_promocao": row.get("Data inicio promocao", "").strip(),
                    "data_termino_promocao": row.get("Data termino promocao", "").strip(),
                    "estoque": row.get("estoque", "").strip(),
                    "ativo": row.get("ativo", "").strip().lower() == 'true',
                    "preco_atacado": row.get("preco atacado", "").strip(),
                    "qtd_minima_atacado": row.get("qtd minima atacado", "").strip(),
                    "peso": row.get("peso", "").strip(),
                    "comprimento": row.get("comprimento", "").strip(),
                    "largura": row.get("largura", "").strip(),
                    "altura": row.get("altura", "").strip(),
                    "incremento": row.get("incremento", "").strip(),
                    "tipo_unidade": row.get("tipo unidade", "").strip() or "UNI",
                    "codigos_auxiliares": eval(row.get("codigos auxiliares", "[]")),
                    "remover_promocao_automatica": row.get("remover promocao automatica", "").strip().lower() == 'true',
                    "subcategorias": eval(row.get("subcategorias", "[]")),
                    "forcar_subcategoria": row.get("forcar subcategoria", "").strip().lower() == 'true',
                    "subcategoria_principal": row.get("subcategoria principal", "").strip()
                }
                
                products.append(product)

            except Exception as e:
                print(f"❌[Line {line_number}] Skipped due to error: {e}")
    return products