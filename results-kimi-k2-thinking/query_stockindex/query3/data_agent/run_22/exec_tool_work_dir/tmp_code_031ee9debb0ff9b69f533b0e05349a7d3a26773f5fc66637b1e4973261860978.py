code = """import json
import pandas as pd
import numpy as np

result_key = 'var_functions.query_db:8'
result_data = locals()[result_key]

# Load data (handle if it's a file path)
if isinstance(result_data, str):
    with open(result_data, 'r') as f:
        data = json.load(f)
else:
    data = result_data

df = pd.DataFrame(data)
print('Loaded data successfully')
print('Total records:', len(df))
print('Indices:', sorted(df['Index'].unique()))

# Convert types
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'])
df = df.dropna(subset=['CloseUSD'])

# Monthly aggregation
monthly_data = df.groupby(['Index', pd.Grouper(key='Date', freq='M')]).agg({'CloseUSD': 'last'}).reset_index()
monthly_data = monthly_data[monthly_data['Date'] >= '2000-01-01']

indices = sorted(monthly_data['Index'].unique())
print('Processing', len(indices), 'indices from 2000 onwards')

result = {
    'status': 'success',
    'indices': indices,
    'total_months': len(monthly_data)
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
