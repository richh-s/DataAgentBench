code = """import json

# Load NASDAQ Capital Market tickers from the stored file
result_file = "/tmp/stockinfo_query_20240125_123456.json"
with open(result_file, 'r') as f:
    nasdaq_cap_stocks = json.load(f)

# Extract tickers and map to company names
ticker_to_company = {}
for stock in nasdaq_cap_stocks:
    ticker = stock['Symbol']
    company_desc = stock['Company Description']
    # Extract company name (usually before the description)
    company_name = company_desc.split('.')[0] if '.' in company_desc else company_desc
    ticker_to_company[ticker] = company_name

print(f"Total NASDAQ Capital Market stocks: {len(ticker_to_company)}")
print("Sample:", list(ticker_to_company.items())[:5])"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json'}

exec(code, env_args)
