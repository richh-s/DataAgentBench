code = """import json
import pandas as pd
import os

available_vars = [k for k in locals().keys() if str(k).startswith('var_')]

index_info = locals()['var_functions.query_db:5']
indices_list = locals()['var_functions.query_db:2']
trade_path = locals()['var_functions.query_db:6']

index_exchange_map = {}
index_exchange_map['N225'] = 'Tokyo Stock Exchange'
index_exchange_map['HSI'] = 'Hong Kong Stock Exchange'
index_exchange_map['000001.SS'] = 'Shanghai Stock Exchange'
index_exchange_map['399001.SZ'] = 'Shenzhen Stock Exchange'
index_exchange_map['GDAXI'] = 'Frankfurt Stock Exchange'
index_exchange_map['GSPTSE'] = 'Toronto Stock Exchange'
index_exchange_map['IXIC'] = 'NASDAQ'
index_exchange_map['NYA'] = 'New York Stock Exchange'
index_exchange_map['N100'] = 'Euronext'
index_exchange_map['SSMI'] = 'SIX Swiss Exchange'
index_exchange_map['TWII'] = 'Taiwan Stock Exchange'
index_exchange_map['NSEI'] = 'National Stock Exchange of India'
index_exchange_map['J203.JO'] = 'Johannesburg Stock Exchange'

result = {
    'available_vars': available_vars,
    'index_info_count': len(index_info),
    'indices_count': len(indices_list),
    'trade_path': trade_path,
    'map_size': len(index_exchange_map)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
