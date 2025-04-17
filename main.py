from dotenv import load_dotenv
from csv_reader import read_products_from_csv
from api_client import send_product_to_api

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def main():
    csv_file = "items.csv"  # arquivo CSV com os dados dos produtos
    raw_products = read_products_from_csv(csv_file)

    # Confirma que a leitura do CSV foi realizada
    print(f"✅ Leitura do arquivo '{csv_file}' concluída com sucesso. {len(raw_products)} produtos carregados.")

    for raw_product in raw_products:
        print(f"Processing product: {raw_product['codigo_interno']}")
        
        # Envia os dados do produto para a API da Instabuy
        # A função send_product_to_api deve fazer uma requisição PUT autenticada
        result = send_product_to_api(raw_product)

        if result and result.get("http_status") == 200:
            print(f"✅ Product {raw_product['codigo_interno']} updated successfully.")
        else:
            print(f"❌ Failed to update product {raw_product['codigo_interno']}.")

if __name__ == "__main__":
    main()
