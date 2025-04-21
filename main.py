from dotenv import load_dotenv
from csv_reader import read_products_from_csv
from api_client import send_product_to_api

# Load environment variables from the .env file
load_dotenv()

def main():
    csv_file = "items.csv"  # CSV file with product data
    raw_products = read_products_from_csv(csv_file)

    # Confirm that the CSV reading was successful
    print(f"✅ Reading the file '{csv_file}' completed successfully. {len(raw_products)} products loaded.")

    for raw_product in raw_products:
        print(f"Processing product: {raw_product['internal_code']}")
        
        # Send product data to the Instabuy API
        # The function send_product_to_api should make an authenticated PUT request
        result = send_product_to_api(raw_product)

        if result and result.get("http_status") == 200:
            print(f"✅ Product {raw_product['internal_code']} updated successfully.")
        else:
            print(f"❌ Failed to update product {raw_product['internal_code']}.")

if __name__ == "__main__":
    main()
