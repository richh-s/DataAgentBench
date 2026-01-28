code = """# Load NASDAQ Capital Market tickers
import json
import os

# Read the NASDAQ Capital Market data file
nasdaq_file_path = "/tmp/stockinfo_query_result_20241225_101010.json"
with open(nasdaq_file_path, 'r') as f:
    nasdaq_cap_stocks = json.load(f)

# Read the trade tables file  
trade_file_path = "/tmp/trade_tables_list_20241225_101020.json"
with open(trade_file_path, 'r') as f:
    trade_tables = json.load(f)

# Extract tickers and company names
ticker_to_company = {}
for stock in nasdaq_cap_stocks:
    ticker = stock['Symbol']
    # Clean company name
    desc = stock['Company Description']
    company_name = desc.split(' specializes in')[0].split(' is ')[0].split(' provides ')[0].rstrip('.')
    ticker_to_company[ticker] = company_name

print(f"NASDAQ Capital Market stocks: {len(ticker_to_company)}")
print(f"Trade tables available: {len(trade_tables)}")

# Find intersection - NASDAQ Cap stocks with trade data
available_tickers = list(set(ticker_to_company.keys()) & set(trade_tables))
print(f"Stocks with trade data: {len(available_tickers)}")
print("Sample:", available_tickers[:10])"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json'}

exec(code, env_args)
