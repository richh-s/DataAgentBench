code = """import json

# Read the full result from the file
file_path = var_functions.query_db:2
with open(file_path, 'r') as f:
    trade_data = json.load(f)

# Filter for Asian indices and calculate intraday volatility
# Based on exchange info, Asian exchanges are:
# - Tokyo Stock Exchange (N225)
# - Hong Kong Stock Exchange (HSI)
# - Shanghai Stock Exchange (000001.SS)
# - Shenzhen Stock Exchange (399001.SZ)
# - National Stock Exchange of India (NIFTY50, NSEI)
# - Korea Exchange (KOSPI, KS11)
# - Taiwan Stock Exchange (TWII)

asian_indices = ['N225', 'HSI', '000001.SS', '399001.SZ', 'NIFTY50', 'NSEI', 'KOSPI', 'KS11', 'TWII']

# Group data by index
index_data = {}
for record in trade_data:
    index = record['Index']
    if index in asian_indices:
        if index not in index_data:
            index_data[index] = []
        index_data[index].append(record)

# Check which indices have data
available_indices = list(index_data.keys())
print('__RESULT__:')
print(json.dumps(available_indices))"""

env_args = {'var_functions.query_db:0': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
