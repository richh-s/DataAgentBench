code = """import json
import pandas as pd
from datetime import datetime

# Read the full price data from the file
price_data_file = locals()['var_functions.query_db:2']
with open(price_data_file, 'r') as f:
    price_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(price_data)

# Convert Date to datetime with mixed format handling
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
df['CloseUSD'] = pd.to_datetime(df['CloseUSD'], format='mixed')

# Filter from January 2000 onwards
df = df[df['Date'] >= '2000-01-01']

# Get monthly data (last trading day of each month)
df['YearMonth'] = df['Date'].dt.to_period('M')
monthly_data = df.groupby(['Index', 'YearMonth']).agg({
    'Date': 'max',
    'CloseUSD': 'last'
}).reset_index()

# Drop YearMonth column
monthly_data = monthly_data.drop('YearMonth', axis=1)

# Sort by Index and Date
monthly_data = monthly_data.sort_values(['Index', 'Date'])

# For each index, calculate DCA returns
indices = monthly_data['Index'].unique()
results = []

for index in indices:
    index_data = monthly_data[monthly_data['Index'] == index].copy()
    
    # Check if we have sufficient data (at least 12 months)
    if len(index_data) < 12:
        continue
    
    # Simulate $100 monthly investment
    monthly_investment = 100
    shares = 0
    
    # Buy at each month-end price
    for _, row in index_data.iterrows():
        price = row['CloseUSD']
        if price > 0:  # Avoid division by zero
            shares += monthly_investment / price
    
    # Calculate final value using the last price
    final_price = index_data['CloseUSD'].iloc[-1]
    total_value = shares * final_price
    total_invested = len(index_data) * monthly_investment
    
    # Calculate total return
    total_return = (total_value - total_invested) / total_invested * 100
    
    results.append({
        'Index': index,
        'TotalReturnPct': total_return,
        'TotalInvested': total_invested,
        'FinalValue': total_value,
        'NumMonths': len(index_data)
    })

# Convert to DataFrame and sort by returns
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('TotalReturnPct', ascending=False)

# Get top 5 indices
top5_indices = results_df.head(5)

print('__RESULT__:')
print(top5_indices.to_json(orient='records'))"""

env_args = {'var_functions.query_db:0': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['index_info'], 'var_functions.query_db:6': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
