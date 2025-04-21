from dotenv import load_dotenv
from csv_reader import read_products_from_csv
from api_client import send_product_to_api

# Loads environment variables from the .env file
load_dotenv()

def main():
    csv_file = "items.csv"  # CSV file containing product data
    raw_products = read_products_from_csv(csv_file)

    # Confirms that the CSV file was successfully read
    print(f"✅ File '{csv_file}' read successfully. {len(raw_products)} products loaded.")

    for raw_product in raw_products:
        print(f"Processing product: {raw_product['codigo_interno']}")
        
        # Sends the product data to the Instabuy API
        # The send_product_to_api function should make an authenticated PUT request
        result = send_product_to_api(raw_product)

        if result and result.get("http_status") == 200:
            print(f"✅ Product {raw_product['codigo_interno']} updated successfully.")
        else:
            print(f"❌ Failed to update product {raw_product['codigo_interno']}.")

if __name__ == "__main__":
    main()
