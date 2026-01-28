code = """import json
import pandas as pd

# Read Asia indices data from the file
file_path = locals()['var_functions.query_db:10']
with open(file_path, 'r') as f:
    data = json.load(f)

# Create dataframe with all data
df_all = pd.DataFrame(data)

# Map indices to their exchanges and regions (Asia)
asia_mappings = {
    'N225': 'Tokyo Stock Exchange',
    'HSI': 'Hong Kong Stock Exchange',
    '000001.SS': 'Shanghai Stock Exchange',
    '399001.SZ': 'Shenzhen Stock Exchange',
    'NSEI': 'National Stock Exchange of India',
    'TWII': 'Taiwan Stock Exchange'
}

# Filter for Asia indices only
asia_indices = list(asia_mappings.keys())
df_asia = df_all[df_all['Index'].isin(asia_indices)].copy()

# Convert numeric columns
df_asia['Open'] = pd.to_numeric(df_asia['Open'])
df_asia['High'] = pd.to_numeric(df_asia['High'])
df_asia['Low'] = pd.to_numeric(df_asia['Low'])
df_asia['Close'] = pd.to_numeric(df_asia['Close'])

# Calculate intraday volatility: (High - Low) / Open
df_asia['Intraday_Volatility'] = (df_asia['High'] - df_asia['Low']) / df_asia['Open']

# Group by index and calculate average volatility since 2020
volatility_results = []
for idx in asia_indices:
    df_idx = df_asia[df_asia['Index'] == idx]
    if not df_idx.empty:
        avg_volatility = df_idx['Intraday_Volatility'].mean()
        trading_days = len(df_idx)
        exchange = asia_mappings[idx]
        volatility_results.append({
            'Index': idx,
            'Exchange': exchange,
            'Avg_Intraday_Volatility': round(avg_volatility, 6),
            'Trading_Days': trading_days
        })

# Convert to DataFrame and sort by volatility
results_df = pd.DataFrame(volatility_results)
results_df = results_df.sort_values('Avg_Intraday_Volatility', ascending=False)

# Get the highest
highest = results_df.iloc[0]

# Format results
output = {
    'asia_indices_volatility': results_df.to_dict('records'),
    'highest_volatility_index': {
        'Index': highest['Index'],
        'Exchange': highest['Exchange'],
        'Avg_Intraday_Volatility': highest['Avg_Intraday_Volatility'],
        'Trading_Days': highest['Trading_Days']
    }
}

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:6': ['index_trade'], 'var_functions.query_db:8': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'399001.SZ': {'Avg_Intraday_Volatility': 0.020202, 'Trading_Days': 2719}, '000001.SS': {'Avg_Intraday_Volatility': 0.017311, 'Trading_Days': 2752}, 'NSEI': {'Avg_Intraday_Volatility': 0.015852, 'Trading_Days': 1610}, 'HSI': {'Avg_Intraday_Volatility': 0.013823, 'Trading_Days': 4006}, 'TWII': {'Avg_Intraday_Volatility': 0.013488, 'Trading_Days': 2751}, 'N225': {'Avg_Intraday_Volatility': 0.008721, 'Trading_Days': 6349}}, 'var_functions.query_db:16': [], 'var_functions.query_db:18': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}]}

exec(code, env_args)
