code = """import json
import pandas as pd
import os

# Load trade data from file
trade_path = locals()['var_functions.query_db:6']
with open(trade_path, 'r') as f:
    trade_data = json.load(f)

print('Trade data loaded, records:', len(trade_data))

# Convert to DataFrame
df = pd.DataFrame(trade_data)
print('Columns:', df.columns.tolist())
print('Date range:', df['Date'].min(), 'to', df['Date'].max())
print('Unique indices:', df['Index'].nunique())

# Convert Date to datetime and extract month/year
df['Date'] = pd.to_datetime(df['Date'])
df['YearMonth'] = df['Date'].dt.to_period('M')

# Filter data from 2000 onwards
df_2000 = df[df['Date'] >= '2000-01-01'].copy()
print('Records from 2000:', len(df_2000))
print('Indices from 2000:', df_2000['Index'].nunique())

# Get first trading day of each month for each index (for monthly investment)
monthly_investment_days = df_2000.groupby(['Index', 'YearMonth'])['Date'].first().reset_index()
print('Potential monthly investment days:', len(monthly_investment_days))

result = {
    'total_records': len(trade_data),
    'records_from_2000': len(df_2000),
    'unique_indices': df_2000['Index'].nunique(),
    'date_min': str(df_2000['Date'].min()),
    'date_max': str(df_2000['Date'].max())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'available_vars': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6'], 'index_info_count': 14, 'indices_count': 13, 'trade_path': 'file_storage/functions.query_db:6.json', 'map_size': 13}}

exec(code, env_args)
