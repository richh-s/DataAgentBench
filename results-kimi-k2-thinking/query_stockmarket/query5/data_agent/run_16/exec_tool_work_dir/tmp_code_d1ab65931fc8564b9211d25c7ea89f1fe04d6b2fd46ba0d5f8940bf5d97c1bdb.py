code = """import json

# Read the stock info result file
with open('var_functions.query_db:18.json', 'r') as f:
    stockinfo_data = json.load(f)

print("Number of NASDAQ Capital Market stocks:", len(stockinfo_data))
print("First few entries:", stockinfo_data[:3])

# Extract tickers and company descriptions
tickers_info = {}
for item in stockinfo_data:
    tickers_info[item['Symbol']] = item['Company Description']

print(f"Sample tickers: {list(tickers_info.keys())[:5]}")"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
