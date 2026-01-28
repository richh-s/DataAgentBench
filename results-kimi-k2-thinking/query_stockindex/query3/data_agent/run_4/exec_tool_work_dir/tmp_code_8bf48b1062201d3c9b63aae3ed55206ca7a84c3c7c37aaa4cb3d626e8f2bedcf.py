code = """import json
import pandas as pd
from datetime import datetime, date
import numpy as np

# Load the data from the database queries
rl_index_info = locals()['var_functions.query_db:2']
rl_index_data_file = locals()['var_functions.query_db:10']

# Read the full index price data from the file
if isinstance(rl_index_data_file, str) and rl_index_data_file.endswith('.json'):
    with open(rl_index_data_file, 'r') as f:
        index_data_all = json.load(f)
else:
    index_data_all = rl_index_data_file

# Create index to exchange/country mapping
index_to_country = {
    '000001.SS': {'exchange': 'Shanghai Stock Exchange', 'country': 'China'},
    '399001.SZ': {'exchange': 'Shenzhen Stock Exchange', 'country': 'China'},
    'GDAXI': {'exchange': 'Frankfurt Stock Exchange', 'country': 'Germany'},
    'GSPTSE': {'exchange': 'Toronto Stock Exchange', 'country': 'Canada'},
    'HSI': {'exchange': 'Hong Kong Stock Exchange', 'country': 'Hong Kong'},
    'IXIC': {'exchange': 'NASDAQ', 'country': 'USA'},
    'J203.JO': {'exchange': 'Johannesburg Stock Exchange', 'country': 'South Africa'},
    'N100': {'exchange': 'Euronext', 'country': 'France/Europe'},
    'N225': {'exchange': 'Tokyo Stock Exchange', 'country': 'Japan'},
    'NSEI': {'exchange': 'National Stock Exchange of India', 'country': 'India'},
    'NYA': {'exchange': 'New York Stock Exchange', 'country': 'USA'},
    'SSMI': {'exchange': 'SIX Swiss Exchange', 'country': 'Switzerland'},
    'TWII': {'exchange': 'Taiwan Stock Exchange', 'country': 'Taiwan'}
}

# Convert to DataFrame
df = pd.DataFrame(index_data_all)

# Convert Date to datetime and sort
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])
df = df.sort_values(['Index', 'Date'])

# Filter data from Jan 2000 onwards
df = df[df['Date'] >= '2000-01-01']

# Get the list of unique indices
indices = df['Index'].unique()
print(f"Found {len(indices)} indices: {list(indices)}")

# Group by month and get first trading day of each month for each index
df['YearMonth'] = df['Date'].dt.to_period('M')
monthly_prices = df.groupby(['Index', 'YearMonth']).first().reset_index()

# Calculate Dollar-Cost Averaging returns for each index
# Assume $100 invested at the beginning of each month
dca_results = []

for index in indices:
    index_data = monthly_prices[monthly_prices['Index'] == index].copy()
    
    if len(index_data) < 12:  # Need at least 12 months of data
        continue
    
    # Calculate DCA
    monthly_investment = 100  # USD
    total_invested = 0
    total_shares = 0
    
    for _, row in index_data.iterrows():
        price = row['CloseUSD']
        if price > 0:
            shares = monthly_investment / price
            total_shares += shares
            total_invested += monthly_investment
    
    # Current value (using most recent price)
    if len(index_data) > 0:
        current_price = index_data.iloc[-1]['CloseUSD']
        current_value = total_shares * current_price
        total_return = current_value - total_invested
        return_percent = (total_return / total_invested) * 100 if total_invested > 0 else 0
        
        # Get country info
        country_info = index_to_country.get(index, {'exchange': 'Unknown', 'country': 'Unknown'})
        
        dca_results.append({
            'Index': index,
            'Exchange': country_info['exchange'],
            'Country': country_info['country'],
            'Total_Invested': total_invested,
            'Current_Value': current_value,
            'Total_Return': total_return,
            'Return_Percent': return_percent,
            'Months': len(index_data),
            'Start_Date': index_data['Date'].min(),
            'End_Date': index_data['Date'].max()
        })

# Sort by total return percentage
dca_results_df = pd.DataFrame(dca_results)
dca_results_df = dca_results_df.sort_values('Return_Percent', ascending=False)

# Get top 5 indices
top_5 = dca_results_df.head(5)

# Print results in the required format
result_json = top_5.to_json(orient='records', indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
