code = """import json
import pandas as pd
from pathlib import Path

# Read the data from the file
result_file = var_functions.query_db:8
if isinstance(result_file, str) and result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        data = json.load(f)
else:
    data = var_functions.query_db:8

# Convert to DataFrame
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = df['CloseUSD'].astype(float)

# Create index to exchange/country mapping
index_mapping = {
    'N225': {'exchange': 'Tokyo Stock Exchange', 'country': 'Japan'},
    'HSI': {'exchange': 'Hong Kong Stock Exchange', 'country': 'Hong Kong'},
    '000001.SS': {'exchange': 'Shanghai Stock Exchange', 'country': 'China'},
    '399001.SZ': {'exchange': 'Shenzhen Stock Exchange', 'country': 'China'},
    'NYA': {'exchange': 'New York Stock Exchange', 'country': 'United States'},
    'IXIC': {'exchange': 'NASDAQ', 'country': 'United States'},
    'GDAXI': {'exchange': 'Frankfurt Stock Exchange', 'country': 'Germany'},
    'GSPTSE': {'exchange': 'Toronto Stock Exchange', 'country': 'Canada'},
    'SSMI': {'exchange': 'SIX Swiss Exchange', 'country': 'Switzerland'},
    'NSEI': {'exchange': 'National Stock Exchange of India', 'country': 'India'},
    'J203.JO': {'exchange': 'Johannesburg Stock Exchange', 'country': 'South Africa'},
    'TWII': {'exchange': 'Taiwan Stock Exchange', 'country': 'Taiwan'},
    'N100': {'exchange': 'Euronext', 'country': 'Europe (Multiple)'}
}

# Get unique indices
indices = df['Index'].unique()

# Calculate returns for each index with monthly DCA
monthly_investment = 100  # Fixed monthly investment amount
results = []

for index in indices:
    index_data = df[df['Index'] == index].copy()
    
    if index_data.empty:
        continue
    
    # Filter data from 2000 onwards
    index_data = index_data[index_data['Date'] >= '2000-01-01']
    
    if index_data.empty:
        continue
    
    # Group by month and get the first available price for each month
    index_data['YearMonth'] = index_data['Date'].dt.to_period('M')
    monthly_data = index_data.groupby('YearMonth').first().reset_index()
    monthly_data = monthly_data.sort_values('Date')
    
    if monthly_data.empty:
        continue
    
    # Simulate DCA: invest monthly_investment at each month's price
    monthly_data['Units'] = monthly_investment / monthly_data['CloseUSD']
    monthly_data['Total_Units'] = monthly_data['Units'].cumsum()
    monthly_data['Total_Invested'] = monthly_investment * (monthly_data.index + 1)
    
    # Get the final value
    final_value = monthly_data['Total_Units'].iloc[-1] * monthly_data['CloseUSD'].iloc[-1]
    total_invested = monthly_data['Total_Invested'].iloc[-1]
    total_return = final_value - total_invested
    return_pct = (total_return / total_invested) * 100
    
    # Get country information
    country = index_mapping.get(index, {}).get('country', 'Unknown')
    
    results.append({
        'Index': index,
        'Country': country,
        'Total_Invested': total_invested,
        'Final_Value': final_value,
        'Total_Return': total_return,
        'Return_Percentage': return_pct,
        'Start_Date': monthly_data['Date'].min(),
        'End_Date': monthly_data['Date'].max(),
        'Months': len(monthly_data)
    })

# Convert to DataFrame and sort by return percentage
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Return_Percentage', ascending=False)

# Get top 5
top_5 = results_df.head(5)

print('__RESULT__:')
print(top_5.to_json(orient='records', indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
