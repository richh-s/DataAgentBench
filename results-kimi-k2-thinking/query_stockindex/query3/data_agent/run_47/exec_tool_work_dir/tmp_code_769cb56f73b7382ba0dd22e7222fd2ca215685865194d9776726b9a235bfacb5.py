code = """import json
import pandas as pd
from datetime import datetime

# Load the data from the file
with open('var_functions.query_db:8', 'r') as f:
    trade_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Filter data from 2000 onwards
df = df[df['Date'] >= '2000-01-01']

# Group by index and calculate monthly investments
indices = df['Index'].unique()

# Get index info data
index_info_data = [{"Exchange": "New York Stock Exchange", "Currency": "USD"}, 
                   {"Exchange": "NASDAQ", "Currency": "USD"}, 
                   {"Exchange": "Hong Kong Stock Exchange", "Currency": "HKD"}, 
                   {"Exchange": "Shanghai Stock Exchange", "Currency": "CNY"}, 
                   {"Exchange": "Tokyo Stock Exchange", "Currency": "JPY"}, 
                   {"Exchange": "Euronext", "Currency": "EUR"}, 
                   {"Exchange": "Shenzhen Stock Exchange", "Currency": "CNY"}, 
                   {"Exchange": "Toronto Stock Exchange", "Currency": "CAD"}, 
                   {"Exchange": "National Stock Exchange of India", "Currency": "INR"}, 
                   {"Exchange": "Frankfurt Stock Exchange", "Currency": "EUR"}, 
                   {"Exchange": "Korea Exchange", "Currency": "KRW"}, 
                   {"Exchange": "SIX Swiss Exchange", "Currency": "CHF"}, 
                   {"Exchange": "Taiwan Stock Exchange", "Currency": "TWD"}, 
                   {"Exchange": "Johannesburg Stock Exchange", "Currency": "ZAR"}]

# Map index symbols to exchanges and countries
index_to_exchange = {
    'N225': ('Tokyo Stock Exchange', 'Japan'),
    'HSI': ('Hong Kong Stock Exchange', 'Hong Kong'),
    '000001.SS': ('Shanghai Stock Exchange', 'China'),
    '399001.SZ': ('Shenzhen Stock Exchange', 'China'),
    'IXIC': ('NASDAQ', 'United States'),
    'NYA': ('New York Stock Exchange', 'United States'),
    'GDAXI': ('Frankfurt Stock Exchange', 'Germany'),
    'N100': ('Euronext', 'Netherlands/France/Belgium'),
    'GSPTSE': ('Toronto Stock Exchange', 'Canada'),
    'NSEI': ('National Stock Exchange of India', 'India'),
    'TWII': ('Taiwan Stock Exchange', 'Taiwan'),
    'SSMI': ('SIX Swiss Exchange', 'Switzerland'),
    'J203.JO': ('Johannesburg Stock Exchange', 'South Africa')
}

# Calculate returns for each index
results = []

for index in indices:
    idx_data = df[df['Index'] == index].copy()
    idx_data = idx_data.sort_values('Date')
    
    if len(idx_data) == 0:
        continue
    
    # Use CloseUSD for consistent USD pricing
    idx_data['CloseUSD'] = pd.to_numeric(idx_data['CloseUSD'])
    
    # Group by month and get the first trading day of each month
    idx_data['YearMonth'] = idx_data['Date'].dt.to_period('M')
    monthly_data = idx_data.groupby('YearMonth').first().reset_index()
    
    if len(monthly_data) < 12:  # Need at least 1 year of data
        continue
    
    # Simulate monthly investment of $100
    monthly_investment = 100
    total_invested = 0
    total_shares = 0
    
    for _, row in monthly_data.iterrows():
        price = row['CloseUSD']
        if price > 0:
            shares = monthly_investment / price
            total_shares += shares
            total_invested += monthly_investment
    
    # Calculate final value
    final_price = idx_data.iloc[-1]['CloseUSD']
    final_value = total_shares * final_price
    total_return = (final_value - total_invested) / total_invested * 100
    
    # Get exchange and country
    exchange, country = index_to_exchange.get(index, ('Unknown', 'Unknown'))
    
    results.append({
        'Index': index,
        'Exchange': exchange,
        'Country': country,
        'Total_Invested': total_invested,
        'Final_Value': final_value,
        'Total_Return_Pct': total_return,
        'Months': len(monthly_data)
    })

# Convert to DataFrame and sort by return
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Total_Return_Pct', ascending=False)

# Get top 5
top5 = results_df.head(5)

# Format the output
output = []
for _, row in top5.iterrows():
    output.append({
        'Index': row['Index'],
        'Exchange': row['Exchange'],
        'Country': row['Country'],
        'Total_Return_Pct': round(row['Total_Return_Pct'], 2),
        'Total_Invested': round(row['Total_Invested'], 2),
        'Final_Value': round(row['Final_Value'], 2)
    })

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:7': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
