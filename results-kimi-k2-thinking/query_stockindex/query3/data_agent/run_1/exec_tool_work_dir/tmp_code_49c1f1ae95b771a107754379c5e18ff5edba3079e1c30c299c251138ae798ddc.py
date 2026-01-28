code = """import json
import pandas as pd
import numpy as np
from datetime import datetime

# Get price data file path
data_key = 'var_functions.query_db:10'
price_data_file = locals()[data_key]

# Read and process data
with open(price_data_file, 'r') as f:
    price_data = json.load(f)

df = pd.DataFrame(price_data)
df['Date_parsed'] = pd.to_datetime(df['Date'], errors='coerce')
df_clean = df.dropna(subset=['Date_parsed']).copy()
df_clean['CloseUSD'] = pd.to_numeric(df_clean['CloseUSD'], errors='coerce')
df_clean = df_clean[df_clean['Date_parsed'] >= pd.Timestamp('2000-01-01')]
df_clean['YearMonth'] = df_clean['Date_parsed'].dt.to_period('M')

# Map indices to countries
index_country_map = {
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'GDAXI': 'Germany',
    'GSPTSE': 'Canada',
    'HSI': 'Hong Kong',
    'IXIC': 'USA',
    'J203.JO': 'South Africa',
    'N100': 'Europe',
    'N225': 'Japan',
    'NSEI': 'India',
    'NYA': 'USA',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan'
}

# Calculate dollar-cost averaging returns for each index
dca_results = []

for idx in df_clean['Index'].unique():
    if pd.isna(idx):
        continue
        
    idx_data = df_clean[df_clean['Index'] == idx].copy()
    
    # Get monthly prices (last trading day of each month)
    monthly_prices = []
    for ym, group in idx_data.groupby('YearMonth'):
        latest_row = group.loc[group['Date_parsed'].idxmax()]
        monthly_prices.append({
            'Date': latest_row['Date_parsed'],
            'Price': latest_row['CloseUSD']
        })
    
    if len(monthly_prices) < 12:  # Need at least 1 year of data
        continue
    
    # Sort by date
    monthly_prices.sort(key=lambda x: x['Date'])
    
    # Calculate DCA return
    total_invested = 0
    total_shares = 0
    monthly_investment = 100.0  # Assume $100 monthly investment
    
    for month_data in monthly_prices:
        price = month_data['Price']
        if pd.notna(price) and price > 0:
            shares = monthly_investment / price
            total_shares += shares
            total_invested += monthly_investment
    
    if total_invested > 0 and len(monthly_prices) > 0:
        final_price = monthly_prices[-1]['Price']
        if pd.notna(final_price) and final_price > 0:
            final_value = total_shares * final_price
            total_return = (final_value / total_invested) - 1
            
            dca_results.append({
                'Index': str(idx),
                'Country': index_country_map.get(str(idx), 'Unknown'),
                'TotalReturn': float(total_return),
                'FinalValue': float(final_value),
                'TotalInvested': float(total_invested),
                'NumMonths': len(monthly_prices),
                'StartDate': monthly_prices[0]['Date'].strftime('%Y-%m-%d'),
                'EndDate': monthly_prices[-1]['Date'].strftime('%Y-%m-%d')
            })

# Sort by total return descending
dca_results.sort(key=lambda x: x['TotalReturn'], reverse=True)

# Get top 5
top_5 = dca_results[:5]

# Format results as percentage returns
formatted_results = []
for i, result in enumerate(top_5, 1):
    formatted_results.append({
        'Rank': i,
        'Index': result['Index'],
        'Country': result['Country'],
        'TotalReturn_Pct': round(result['TotalReturn'] * 100, 2),
        'FinalValue': round(result['FinalValue'], 2),
        'TotalInvested': round(result['TotalInvested'], 2),
        'Period': f"{result['StartDate']} to {result['EndDate']}"
    })

print('__RESULT__:')
print(json.dumps(formatted_results, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}, {'Index': 'HSI', 'Date': '1987-01-08 00:00:00', 'Open': '2603.300049', 'High': '2603.300049', 'Low': '2603.300049', 'Close': '2603.300049', 'Adj Close': '2603.300049', 'CloseUSD': '338.42900637'}, {'Index': 'HSI', 'Date': '1987-01-09 00:00:00', 'Open': '2561.699951', 'High': '2561.699951', 'Low': '2561.699951', 'Close': '2561.699951', 'Adj Close': '2561.699951', 'CloseUSD': '333.02099363'}, {'Index': 'HSI', 'Date': '1987-01-12 00:00:00', 'Open': '2614.899902', 'High': '2614.899902', 'Low': '2614.899902', 'Close': '2614.899902', 'Adj Close': '2614.899902', 'CloseUSD': '339.93698726'}, {'Index': 'HSI', 'Date': '1987-01-13 00:00:00', 'Open': '2590.800049', 'High': '2590.800049', 'Low': '2590.800049', 'Close': '2590.800049', 'Adj Close': '2590.800049', 'CloseUSD': '336.80400637'}, {'Index': 'HSI', 'Date': '1987-01-14 00:00:00', 'Open': '2578.199951', 'High': '2578.199951', 'Low': '2578.199951', 'Close': '2578.199951', 'Adj Close': '2578.199951', 'CloseUSD': '335.16599363'}], 'var_functions.query_db:8': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:16': {'num_indices': 13, 'total_months': 3105, 'date_range': '2000-01-26 to 2021-06-02', 'indices': ['000001.SS', '399001.SZ', 'GDAXI', 'GSPTSE', 'HSI', 'IXIC', 'J203.JO', 'N100', 'N225', 'NSEI', 'NYA', 'SSMI', 'TWII']}}

exec(code, env_args)
