code = """import json
import pandas as pd

storage_key = 'var_functions.query_db:8'
db_result = locals()[storage_key]

if isinstance(db_result, str) and '.json' in db_result:
    with open(db_result, 'r') as f:
        data = json.load(f)
else:
    data = db_result

# Create DataFrame
df = pd.DataFrame(data)[['Index', 'Date', 'Open', 'High', 'Low', 'Close']]

# Convert to numeric
numeric_cols = ['Open', 'High', 'Low', 'Close']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Calculate intraday volatility
df['Intraday_Volatility'] = (df['High'] - df['Low']) / df['Open']

# Clean data
df_clean = df.dropna(subset=['Intraday_Volatility'])
df_clean = df_clean[df_clean['Intraday_Volatility'] != float('inf')]

# Group by Index and calculate average volatility
avg_volatility = df_clean.groupby('Index')['Intraday_Volatility'].agg(['mean', 'count']).reset_index()

# Sort by volatility descending
avg_volatility_sorted = avg_volatility.sort_values('mean', ascending=False)

# Filter for Asia indices specifically (based on geographic knowledge)
asia_indices = ['HSI', 'N225', 'NSEI', '399001.SZ', '000001.SS', 'TWII']
avg_volatility_asia = avg_volatility_sorted[avg_volatility_sorted['Index'].isin(asia_indices)]

# Prepare result for top Asia index
top_asia_index = avg_volatility_asia.iloc[0]

result = {
    'index_symbol': top_asia_index['Index'],
    'average_intraday_volatility': top_asia_index['mean'],
    'data_points': int(top_asia_index['count']),
    'all_asia_indices_ranking': avg_volatility_asia.to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'Index': '399001.SZ', 'Average_Intraday_Volatility': 0.020202435308195838}, 'var_functions.query_db:16': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}]}

exec(code, env_args)
