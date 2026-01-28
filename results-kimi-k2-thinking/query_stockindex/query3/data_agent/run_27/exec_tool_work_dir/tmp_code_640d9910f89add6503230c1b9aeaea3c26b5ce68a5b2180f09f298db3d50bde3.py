code = """import json
import pandas as pd
import os

# Check available variables
print("Available variables in locals:")
available_vars = [k for k in locals().keys()]
print([k for k in available_vars if k.startswith('var_')])

# Load actual data
var_query5 = locals()['var_functions.query_db:5']  # index info
var_query2 = locals()['var_functions.query_db:2']  # indices list
var_query6 = locals()['var_functions.query_db:6']  # trade data path

print("\nIndex info:", var_query5[:2])
print("Indices:", var_query2)
print("Trade data path:", var_query6)

# Map index symbols to exchanges
index_exchange_map = {
    'N225': 'Tokyo Stock Exchange',
    'HSI': 'Hong Kong Stock Exchange',
    '000001.SS': 'Shanghai Stock Exchange',
    '399001.SZ': 'Shenzhen Stock Exchange',
    'GDAXI': 'Frankfurt Stock Exchange',
    'GSPTSE': 'Toronto Stock Exchange',
    'IXIC': 'NASDAQ',
    'NYA': 'New York Stock Exchange',
    'N100': 'Euronext',
    'SSMI': 'SIX Swiss Exchange',
    'TWII': 'Taiwan Stock Exchange',
    'NSEI': 'National Stock Exchange of India',
    'J203.JO': 'Johannesburg Stock Exchange'
}

print("\nMapped indices:", len(index_exchange_map))
print("Mapping:", index_exchange_map)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
