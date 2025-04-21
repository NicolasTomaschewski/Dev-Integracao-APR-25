# 📦 CSV to API Uploader

This project reads product data from a CSV file and sends it to an external API. It's ideal for syncing local product databases with online systems.

## 🛠️ Technologies

- Python 3  
- `requests` for HTTP requests  
- `python-dotenv` for environment variable management  
- `csv` for file parsing  

## 📁 Project Structure

```
.
├── api_client.py         # Builds and sends data to the API
├── csv_reader.py         # Reads and processes the CSV file
├── config.py             # Loads variables from .env
├── .env                  # Contains API_TOKEN and BASE_URL
├── requirements.txt      # List of project dependencies
└── main.py               # (Optional) Main entry point to run everything
```

## 🔐 `.env` File

The `.env` file should be created in the root directory with the following variables:

```
API_TOKEN=your_token_here
BASE_URL=https://yourapi.com/api/v1/
```

> **Important**: Make sure the `BASE_URL` ends with a `/`.

## 📄 CSV Example

The `.csv` file example is available in the repository as `items.csv`.

## 🚀 How to Use

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Create your `.env` file with the correct token and API URL.

3. Run the script to read and send the data (example using `main.py`):
   ```
   python3 main.py
   ```

4. Done! The products will be sent to the API.

## ✅ Validations and Error Handling

1. **Required fields validation**  
   During the CSV parsing, the script checks if the fields `Internal Code` and `Name` are present and filled. These fields are essential to identify each product. If any of them is missing or empty, the corresponding line is considered invalid.

2. **Per-line error handling**  
   Each CSV row is processed individually. If any error occurs in data formatting or conversion (such as malformed values, missing fields, or incorrect list syntax), the line is skipped. An error message is displayed in the terminal with the line number and the reason for the failure. This ensures that issues in a few rows do not interrupt the import process for the rest.

3. **Measurement unit normalization**  
   The field for unit type (e.g., "UNI", "KG", etc.) is validated to ensure it matches the accepted values by the API. If the provided unit is not among the accepted types (`UNI`, `KG`, `BOX`, `M2`, `M`, `L`), the system automatically sets the default type to `UNI`.
