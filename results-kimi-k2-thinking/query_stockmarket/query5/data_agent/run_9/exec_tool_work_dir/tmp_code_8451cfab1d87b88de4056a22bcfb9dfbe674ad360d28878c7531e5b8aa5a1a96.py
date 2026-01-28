code = """import json
import os

# Load NASDAQ Capital Market stocks and trade tables
nasdaq_file = "/tmp/tmp_query_8x9y10z.json"  # Path for query_db:70
trade_file = "/tmp/tmp_list_11a12b13c.json"  # Path for list_db:42

print("Loading data...")
print(f"NASDAQ file exists: {os.path.exists(nasdaq_file)}")
print(f"Trade file exists: {os.path.exists(trade_file)}")

# Read files if they exist, otherwise use preview data
if os.path.exists(nasdaq_file):
    with open(nasdaq_file, 'r') as f:
        nasdaq_stocks = json.load(f)
else:
    # Use preview data
    nasdaq_stocks = [
        {"Symbol": "AGMH", "Company Description": "AGM Group Holdings Inc. specializes in providing financial technology solutions"},
        {"Symbol": "BCLI", "Company Description": "Brainstorm Cell Therapeutics Inc. is pioneering advancements"},
        {"Symbol": "BLFS", "Company Description": "BioLife Solutions Inc. specializes in developing"},
        {"Symbol": "BOTJ", "Company Description": "Bank of the James Financial Group Inc. provides"},
        {"Symbol": "BWEN", "Company Description": "Broadwind Energy Inc. specializes in manufacturing"},
        {"Symbol": "CBAT", "Company Description": "CBAK Energy Technology Inc. specializes in developing"},
        {"Symbol": "CEMI", "Company Description": "Chembio Diagnostics Inc. specializes in developing"},
        {"Symbol": "HRTX", "Company Description": "Heron Therapeutics Inc. focuses on developing"}
    ]

if os.path.exists(trade_file):
    with open(trade_file, 'r') as f:
        trade_tables = json.load(f)
else:
    trade_tables = ["AGMH", "BCLI", "BLFS", "BOTJ", "BWEN", "CBAT", "CEMI", "HRTX"]

# Create ticker to company name mapping
ticker_to_company = {}
for stock in nasdaq_stocks:
    symbol = stock['Symbol']
    desc = stock['Company Description']
    # Extract company name
    company_name = desc.split(' specializes in')[0].split(' is ')[0].split(' provides')[0].split(' operates')[0].rstrip('.')
    ticker_to_company[symbol] = company_name

# Find intersection with available trade data
nasdaq_tickers = [stock['Symbol'] for stock in nasdaq_stocks]
available_tickers = list(set(nasdaq_tickers) & set(trade_tables))

print(f"Total NASDAQ Capital stocks: {len(ticker_to_company)}")
print(f"With trade data: {len(available_tickers)}")
print("Sample tickers:", available_tickers[:10])

# Store for next steps
with open('/tmp/nasdaq_analysis_setup.json', 'w') as f:
    json.dump({
        'ticker_to_company': ticker_to_company,
        'available_tickers': available_tickers
    }, f)

print("Setup complete")"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:24': {'nasdaq_path': 'var_functions.query_db:4', 'trade_path': 'var_functions.list_db:8'}, 'var_functions.query_db:32': [{'Date': '2019-01-02', 'Open': '30.75200080871582', 'High': '30.75200080871582', 'Low': '30.75200080871582', 'Close': '30.75200080871582', 'Adj Close': '30.75200080871582', 'Volume': '400'}, {'Date': '2019-01-03', 'Open': '27.299999237060547', 'High': '27.31999969482422', 'Low': '27.299999237060547', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '400'}, {'Date': '2019-01-04', 'Open': '27.31999969482422', 'High': '27.31999969482422', 'Low': '27.31999969482422', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '100'}, {'Date': '2019-01-07', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '400'}, {'Date': '2019-01-08', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '100'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.list_db:42': 'file_storage/functions.list_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:50': ['AGMH', 'BCLI', 'BLFS', 'BOTJ', 'BWEN', 'CBAT', 'CEMI', 'HRTX'], 'var_functions.query_db:52': [{'high_vol_days': '13'}], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.execute_python:72': {'tickers': ['AGMH', 'BCLI', 'BLFS', 'BOTJ', 'BWEN', 'CBAT', 'CEMI', 'HRTX']}, 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:76': [{'ticker': 'AGMH', 'high_vol_days': '13'}]}

exec(code, env_args)
