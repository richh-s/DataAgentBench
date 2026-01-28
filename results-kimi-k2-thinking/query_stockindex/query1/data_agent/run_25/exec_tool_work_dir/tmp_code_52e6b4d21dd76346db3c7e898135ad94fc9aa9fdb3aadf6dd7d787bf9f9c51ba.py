code = """import json
import pandas as pd

# Get previous results from storage
index_data = locals().get('var_functions.query_db:0', [])
exchanges_data = locals().get('var_functions.query_db:2', [])

print("Index data retrieved:", index_data)
print("Exchange data retrieved:", exchanges_data)

# Extract index symbols
if index_data:
    index_symbols = [item['Index'] for item in index_data]
    print("Available index symbols:", index_symbols)
else:
    index_symbols = []
    print("No index data found")

# Identify Asian indices based on known symbols
# N225 = Nikkei 225 (Japan)
# HSI = Hang Seng (Hong Kong)  
# 000001.SS = Shanghai Composite (China)
# TWII = Taiwan Weighted (Taiwan)
# 399001.SZ = Shenzhen Component (China)
# NSEI = NIFTY 50 (India)

asian_indices = [idx for idx in index_symbols if idx in ['N225', 'HSI', '000001.SS', 'TWII', '399001.SZ', 'NSEI']]
print("Identified Asian indices:", asian_indices)"""

env_args = {'var_functions.query_db:0': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
