from csv_reader import read_products_from_csv
from product_formatter import format_product_data
from api_client import send_product_to_api
from utils import log_success, log_failure

def main():
    csv_file = "items.csv"  # você pode alterar para o nome do seu arquivo
    raw_products = read_products_from_csv(csv_file)

    for raw_product in raw_products:
        formatted = format_product_data(raw_product)
        result = send_product_to_api(formatted)

        if result and result.get("http_status") == 200:
            log_success(formatted["sku"])
        else:
            log_failure(formatted["sku"])

if __name__ == "__main__":
    main()
