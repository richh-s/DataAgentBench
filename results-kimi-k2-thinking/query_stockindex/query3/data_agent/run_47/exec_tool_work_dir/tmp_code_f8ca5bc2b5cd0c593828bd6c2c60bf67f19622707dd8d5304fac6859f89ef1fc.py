code = """import json
import pandas as pd
from datetime import datetime

# Read the data from the file path stored in the variable
file_path = 'var_functions.query_db:12'

with open(file_path, 'r') as f:
    trade_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Convert columns to appropriate types
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Filter data from 2000 onwards
df = df[df['Date'] >= '2000-01-01'].copy()

# Map index symbols to exchanges and countries
index_to_country = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'IXIC': 'United States',
    'NYA': 'United States',
    'GDAXI': 'Germany',
    'N100': 'Netherlands/France/Belgium',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'TWII': 'Taiwan',
    'SSMI': 'Switzerland',
    'J203.JO': 'South Africa'
}

# Calculate returns for each index
results = []
monthly_investment = 100  # $100 per month

for index in df['Index'].unique():
    idx_data = df[df['Index'] == index].copy()
    idx_data = idx_data.sort_values('Date')
    
    if len(idx_data) < 12:  # Need at least 1 year of data
        continue
    
    # Get first trading day of each month
    idx_data['YearMonth'] = idx_data['Date'].dt.to_period('M')
    monthly_data = idx_data.groupby('YearMonth').first().reset_index()
    
    # Simulate monthly investments
    total_invested = 0
    total_shares = 0
    
    for _, row in monthly_data.iterrows():
        price = row['CloseUSD']
        if price > 0:
            shares = monthly_investment / price
            total_shares += shares
            total_invested += monthly_investment
    
    # Calculate final value and return
    final_price = idx_data.iloc[-1]['CloseUSD']
    final_value = total_shares * final_price
    total_return_pct = (final_value - total_invested) / total_invested * 100
    
    country = index_to_country.get(index, 'Unknown')
    
    results.append({
        'Index': index,
        'Country': country,
        'Total_Return_Pct': round(total_return_pct, 2),
        'Total_Invested': round(total_invested, 2),
        'Final_Value': round(final_value, 2),
        'Months': len(monthly_data)
    })

# Sort by return and get top 5
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Total_Return_Pct', ascending=False)
top5 = results_df.head(5)

# Format output
output = top5[['Index', 'Country', 'Total_Return_Pct', 'Total_Invested', 'Final_Value']].to_dict('records')

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:7': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
