code = """import json
import pandas as pd
import os

# Load trade data from file
trade_path = locals()['var_functions.query_db:6']
with open(trade_path, 'r') as f:
    trade_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Convert Date to datetime - handle format explicitly
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
df['YearMonth'] = df['Date'].dt.to_period('M')

# Filter data from 2000 onwards
df_2000 = df[df['Date'] >= '2000-01-01'].copy()

# Map indices to countries
index_country_map = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China', 
    'GDAXI': 'Germany',
    'GSPTSE': 'Canada',
    'IXIC': 'United States',
    'NYA': 'United States',
    'N100': 'Netherlands/Europe',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'NSEI': 'India',
    'J203.JO': 'South Africa'
}

# For each index, calculate returns from monthly investing since 2000
results = []

for index in df_2000['Index'].unique():
    idx_data = df_2000[df_2000['Index'] == index].copy()
    
    # Get first trading day of each month
    monthly_first = idx_data.groupby('YearMonth')['Date'].first().reset_index()
    monthly_first = monthly_first.merge(idx_data[['Date', 'CloseUSD']], on='Date')
    
    # Calculate returns assuming $100 invested monthly
    total_invested = len(monthly_first) * 100
    shares = 0
    
    for _, row in monthly_first.iterrows():
        shares += 100 / float(row['CloseUSD'])
    
    # Get final value using last available price
    final_price = float(idx_data.iloc[-1]['CloseUSD'])
    final_value = shares * final_price
    total_return = final_value - total_invested
    return_pct = (total_return / total_invested) * 100
    
    results.append({
        'Index': index,
        'Country': index_country_map.get(index, 'Unknown'),
        'TotalReturnPct': return_pct,
        'TotalInvested': total_invested,
        'FinalValue': final_value,
        'Months': len(monthly_first)
    })

# Sort by total return
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('TotalReturnPct', ascending=False)

print('__RESULT__:')
print(json.dumps(results_df.head(10).to_dict('records')))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'available_vars': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6'], 'index_info_count': 14, 'indices_count': 13, 'trade_path': 'file_storage/functions.query_db:6.json', 'map_size': 13}}

exec(code, env_args)
