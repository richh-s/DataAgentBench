code = """import json, pandas as pd
file_path = locals()['var_functions.query_db:8']
with open(file_path, 'r') as f:
    trade_data = json.load(f)
df = pd.DataFrame(trade_data)
print('Shape:', df.shape)
print('Columns:', list(df.columns))
print('Unique indices:', df['Index'].nunique())
print('Date range:', df['Date'].min(), 'to', df['Date'].max())
print('Indices:', df['Index'].unique()[:10])
df['Date'] = pd.to_datetime(df['Date'])
print('Types:', df.dtypes.to_dict())
print('First 3 rows:', df.head(3).to_dict('records'))
print('__RESULT__:')
print('Data loaded')"""

env_args = {'var_functions.list_db:0': ['index_trade'], 'var_functions.list_db:2': ['index_info'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
