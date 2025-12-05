code = """import pandas as pd, json
index_info = pd.DataFrame(var_call_ABvtFo70iXeVCuPtTx7LW85R)
indices = pd.DataFrame(var_call_l37l8TcG7N4Zarqe6hxDCnoO)
# Map exchanges to their major indices
exchange_to_index = {
    'Tokyo Stock Exchange': 'N225',
    'Hong Kong Stock Exchange': 'HSI',
    'Shanghai Stock Exchange': '000001.SS',
    'Shenzhen Stock Exchange': '399001.SZ',
    'National Stock Exchange of India': 'NSEI',
    'Korea Exchange': None,  # no direct index in list
    'Taiwan Stock Exchange': 'TWII',
}
# Determine Asia indices present in index_trade
asia_indices = []
for exch, idx in exchange_to_index.items():
    if idx is not None and idx in set(indices['Index']):
        asia_indices.append(idx)
result = json.dumps(asia_indices)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_P0yfUlSD6Dta6quzekVqwA6t': ['index_info'], 'var_call_5GyY5LtS0YQH3BYpKIbDsKe4': ['index_trade'], 'var_call_ABvtFo70iXeVCuPtTx7LW85R': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_l37l8TcG7N4Zarqe6hxDCnoO': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}]}

exec(code, env_args)
