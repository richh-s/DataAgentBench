code = """import pandas as pd
import numpy as np
import json

# Load the index data
indices = ["J203.JO", "IXIC", "N225", "GSPTSE", "NSEI", "GDAXI", "NYA", "000001.SS", "SSMI", "TWII", "N100", "399001.SZ", "HSI"]

# Country mapping
index_to_country = {
    "N225": "Japan",
    "HSI": "Hong Kong",
    "000001.SS": "China",
    "399001.SZ": "China",
    "GDAXI": "Germany",
    "NYA": "USA",
    "IXIC": "USA",
    "GSPTSE": "Canada",
    "NSEI": "India",
    "TWII": "Taiwan",
    "SSMI": "Switzerland",
    "J203.JO": "South Africa",
    "N100": "Europe"
}

print("__RESULT__:")
print(json.dumps({"status": "mapping loaded", "count": len(index_to_country)}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'HSI'}]}

exec(code, env_args)
