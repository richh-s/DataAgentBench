code = """import json
import pandas as pd
import numpy as np

# Get the data
result_data = var_functions.query_db:8
# Check if it's a file path
if isinstance(result_data, str) and ('.json' in result_data or '/' in result_data):
    with open(result_data, 'r') as f:
        data = json.load(f)
else:
    data = result_data

# Create DataFrame
df = pd.DataFrame(data)

# Convert CloseUSD to numeric and Date to datetime
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce', utc=True)
df = df.dropna(subset=['CloseUSD'])

# Get monthly closing prices
monthly = df.groupby(['Index', pd.Grouper(key='Date', freq='M')]).agg({'CloseUSD': 'last'}).reset_index()

# Filter from 2000
monthly_2000 = monthly[monthly['Date'] >= '2000-01-01']

indices = sorted(monthly_2000['Index'].unique())

print('Data loaded:')
print('Indices:', indices)
print('Total records:', len(monthly_2000))

# Calculate returns for regular monthly investment
index_returns = []
for idx in indices:
    idx_data = monthly_2000[monthly_2000['Index'] == idx].sort_values('Date')
    if len(idx_data) > 12:
        # Regular monthly investment of $100
        total_invested = 0
        total_shares = 0
        for _, row in idx_data.iterrows():
            total_invested += 100
            total_shares += 100 / row['CloseUSD']
        final_value = total_shares * idx_data.iloc[-1]['CloseUSD']
        total_return = final_value - total_invested
        return_pct = (total_return / total_invested) * 100
        
        index_returns.append({
            'Index': idx,
            'Total_Invested': total_invested,
            'Final_Value': final_value,
            'Total_Return': total_return,
            'Return_Percent': return_pct
        })

# Sort by return
index_returns_sorted = sorted(index_returns, key=lambda x: x['Return_Percent'], reverse=True)

# Map indices to exchanges and countries
index_info = {
    'N225': {'Country': 'Japan', 'Exchange': 'Tokyo Stock Exchange'},
    'HSI': {'Country': 'Hong Kong', 'Exchange': 'Hong Kong Stock Exchange'},
    '000001.SS': {'Country': 'China', 'Exchange': 'Shanghai Stock Exchange'},
    '399001.SZ': {'Country': 'China', 'Exchange': 'Shenzhen Stock Exchange'},
    'IXIC': {'Country': 'USA', 'Exchange': 'NASDAQ'},
    'NYA': {'Country': 'USA', 'Exchange': 'New York Stock Exchange'},
    'GDAXI': {'Country': 'Germany', 'Exchange': 'Frankfurt Stock Exchange'},
    'GSPTSE': {'Country': 'Canada', 'Exchange': 'Toronto Stock Exchange'},
    'NSEI': {'Country': 'India', 'Exchange': 'National Stock Exchange of India'},
    'N100': {'Country': 'Netherlands/Europe', 'Exchange': 'Euronext'},
    'SSMI': {'Country': 'Switzerland', 'Exchange': 'SIX Swiss Exchange'},
    'TWII': {'Country': 'Taiwan', 'Exchange': 'Taiwan Stock Exchange'},
    'J203.JO': {'Country': 'South Africa', 'Exchange': 'Johannesburg Stock Exchange'}
}

# Get top 5
top_5 = []
for i, item in enumerate(index_returns_sorted[:5], 1):
    idx = item['Index']
    info = index_info.get(idx, {'Country': 'Unknown', 'Exchange': 'Unknown'})
    top_5.append({
        'Rank': i,
        'Index': idx,
        'Country': info['Country'],
        'Exchange': info['Exchange'],
        'Return_Percent': round(item['Return_Percent'], 2)
    })

print('__RESULT__:')
print(json.dumps(top_5))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
