code = """import json
import pandas as pd
import numpy as np
from datetime import datetime

# Load price data
price_data_file = locals()['var_functions.query_db:16']
if isinstance(price_data_file, str) and price_data_file.endswith('.json'):
    with open(price_data_file, 'r') as f:
        price_data = json.load(f)
else:
    price_data = price_data_file

# Convert to DataFrame
df = pd.DataFrame(price_data)
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Index mapping with countries
index_mapping = {
    '000001.SS': {'exchange': 'Shanghai Stock Exchange', 'country': 'China'},
    '399001.SZ': {'exchange': 'Shenzhen Stock Exchange', 'country': 'China'},
    'GDAXI': {'exchange': 'Frankfurt Stock Exchange', 'country': 'Germany'},
    'GSPTSE': {'exchange': 'Toronto Stock Exchange', 'country': 'Canada'},
    'HSI': {'exchange': 'Hong Kong Stock Exchange', 'country': 'Hong Kong'},
    'IXIC': {'exchange': 'NASDAQ', 'country': 'USA'},
    'J203.JO': {'exchange': 'Johannesburg Stock Exchange', 'country': 'South Africa'},
    'N100': {'exchange': 'Euronext', 'country': 'Netherlands'},
    'N225': {'exchange': 'Tokyo Stock Exchange', 'country': 'Japan'},
    'NSEI': {'exchange': 'National Stock Exchange of India', 'country': 'India'},
    'NYA': {'exchange': 'New York Stock Exchange', 'country': 'USA'},
    'SSMI': {'exchange': 'SIX Swiss Exchange', 'country': 'Switzerland'},
    'TWII': {'exchange': 'Taiwan Stock Exchange', 'country': 'Taiwan'}
}

# Calculate returns for regular monthly investments (dollar-cost averaging)
monthly_investment = 100  # USD invested each month
results = []

for idx in df['Index'].unique():
    idx_data = df[df['Index'] == idx].copy()
    idx_data = idx_data.sort_values('Date')
    
    # Get monthly prices (first trading day of each month)
    idx_data['YearMonth'] = idx_data['Date'].dt.to_period('M')
    monthly_prices = idx_data.groupby('YearMonth').first().reset_index()
    
    # Filter from 2000 onwards
    monthly_prices = monthly_prices[monthly_prices['Date'] >= '2000-01-01']
    
    if len(monthly_prices) < 12:  # Need at least 12 months of data
        continue
    
    # Calculate DCA returns
    total_invested = 0
    total_shares = 0
    
    for _, row in monthly_prices.iterrows():
        shares_bought = monthly_investment / row['CloseUSD']
        total_shares += shares_bought
        total_invested += monthly_investment
    
    # Current value
    current_price = monthly_prices.iloc[-1]['CloseUSD']
    current_value = total_shares * current_price
    
    # Calculate returns
    total_return = current_value - total_invested
    total_return_pct = (total_return / total_invested) * 100
    
    # Annualized return (approximate)
    years = len(monthly_prices) / 12
    annualized_return = ((current_value / total_invested) ** (1/years) - 1) * 100
    
    results.append({
        'Index': idx,
        'Country': index_mapping.get(idx, {}).get('country', 'Unknown'),
        'TotalInvested': total_invested,
        'CurrentValue': current_value,
        'TotalReturnPct': total_return_pct,
        'AnnualizedReturn': annualized_return,
        'Years': round(years, 2)
    })

# Sort by total return percentage and get top 5
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('TotalReturnPct', ascending=False)
top_5 = results_df.head(5).copy()

# Reset index to get proper ranking
top_5.reset_index(drop=True, inplace=True)

print("Top 5 Indices by Regular Monthly Investment Returns since 2000:")
print("=" * 80)
for i, (_, row) in enumerate(top_5.iterrows(), 1):
    print(f"{i}. {row['Index']} - {row['Country']}")
    print(f"   Total Return: {row['TotalReturnPct']:.1f}%")
    print(f"   Annualized Return: {row['AnnualizedReturn']:.1f}%")
    print(f"   Period: {row['Years']} years")
    print()

# Create proper summary with ranks 1-5
summary = []
for i, (_, row) in enumerate(top_5.iterrows(), 1):
    summary.append({
        'rank': i,
        'index': row['Index'],
        'country': row['Country'],
        'total_return_pct': round(row['TotalReturnPct'], 2),
        'annualized_return_pct': round(row['AnnualizedReturn'], 2),
        'years': row['Years']
    })

print('__RESULT__:')
print(json.dumps(summary))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:13': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'status': 'data_loaded', 'num_indices': 13, 'indices': ['000001.SS', '399001.SZ', 'GDAXI', 'GSPTSE', 'HSI', 'IXIC', 'J203.JO', 'N100', 'N225', 'NSEI', 'NYA', 'SSMI', 'TWII']}, 'var_functions.execute_python:20': [{'rank': 6, 'index': 'IXIC', 'country': 'USA', 'total_return_pct': 378.6, 'annualized_return_pct': 7.58, 'years': 21.42}, {'rank': 2, 'index': '399001.SZ', 'country': 'China', 'total_return_pct': 134.45, 'annualized_return_pct': 4.04, 'years': 21.5}, {'rank': 3, 'index': 'GDAXI', 'country': 'Germany', 'total_return_pct': 131.94, 'annualized_return_pct': 4.01, 'years': 21.42}, {'rank': 13, 'index': 'TWII', 'country': 'Taiwan', 'total_return_pct': 131.52, 'annualized_return_pct': 4.0, 'years': 21.42}, {'rank': 10, 'index': 'NSEI', 'country': 'India', 'total_return_pct': 121.47, 'annualized_return_pct': 5.95, 'years': 13.75}]}

exec(code, env_args)
