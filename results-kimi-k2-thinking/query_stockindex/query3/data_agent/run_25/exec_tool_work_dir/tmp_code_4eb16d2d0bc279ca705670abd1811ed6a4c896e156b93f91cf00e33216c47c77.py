code = """import json
import pandas as pd
from datetime import datetime

# Read the query result from the file
file_path = locals()['var_functions.query_db:8']

with open(file_path, 'r') as f:
    trade_data = json.load(f)

print(f"Loaded {len(trade_data)} records")

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Convert Date to datetime and CloseUSD to float
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = df['CloseUSD'].astype(float)

# Filter data from 2000 onward
df_2000 = df[df['Date'] >= '2000-01-01'].copy()

# Map indices to exchanges and countries based on the hint
index_mapping = {
    'N225': {'Exchange': 'Tokyo Stock Exchange', 'Country': 'Japan'},
    'HSI': {'Exchange': 'Hong Kong Stock Exchange', 'Country': 'Hong Kong'},
    '000001.SS': {'Exchange': 'Shanghai Stock Exchange', 'Country': 'China'},
    '399001.SZ': {'Exchange': 'Shenzhen Stock Exchange', 'Country': 'China'},
    'GDAXI': {'Exchange': 'Frankfurt Stock Exchange', 'Country': 'Germany'},
    'GSPTSE': {'Exchange': 'Toronto Stock Exchange', 'Country': 'Canada'},
    'J203.JO': {'Exchange': 'Johannesburg Stock Exchange', 'Country': 'South Africa'},
    'N100': {'Exchange': 'Euronext', 'Country': 'Netherlands'},
    'NSEI': {'Exchange': 'National Stock Exchange of India', 'Country': 'India'},
    'NYA': {'Exchange': 'New York Stock Exchange', 'Country': 'USA'},
    'IXIC': {'Exchange': 'NASDAQ', 'Country': 'USA'},
    'SSMI': {'Exchange': 'SIX Swiss Exchange', 'Country': 'Switzerland'},
    'TWII': {'Exchange': 'Taiwan Stock Exchange', 'Country': 'Taiwan'}
}

print(f"Indices to analyze: {list(index_mapping.keys())}")

# Calculate monthly returns for regular monthly investment
def calculate_monthly_returns(df, index_symbol):
    """Calculate returns from regular monthly investments"""
    index_data = df[df['Index'] == index_symbol].copy()
    
    if len(index_data) == 0:
        return None
    
    # Ensure we have data sorted by date
    index_data = index_data.sort_values('Date')
    
    # Group by month and get first trading day of each month
    index_data['YearMonth'] = index_data['Date'].dt.to_period('M')
    monthly_first = index_data.groupby('YearMonth').first().reset_index()
    
    if len(monthly_first) < 2:
        return None
    
    # Simulate investing $100 at the beginning of each month
    investment = 100
    total_invested = 0
    total_shares = 0
    
    for _, row in monthly_first.iterrows():
        total_invested += investment
        total_shares += investment / row['CloseUSD']
    
    # Get final value
    final_value = total_shares * index_data.iloc[-1]['CloseUSD']
    total_return = (final_value - total_invested) / total_invested
    
    return {
        'Index': index_symbol,
        'Total_Invested': total_invested,
        'Final_Value': final_value,
        'Total_Return': total_return,
        'Years': len(monthly_first) / 12
    }

# Calculate returns for all indices
results = []
for index_symbol in index_mapping.keys():
    result = calculate_monthly_returns(df_2000, index_symbol)
    if result:
        result['Country'] = index_mapping[index_symbol]['Country']
        result['Exchange'] = index_mapping[index_symbol]['Exchange']
        results.append(result)

# Sort by total return descending
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Total_Return', ascending=False)

print("Top 5 indices by total return:")
for i, row in results_df.head().iterrows():
    print(f"{row['Index']}: {row['Total_Return']:.2%} return ({row['Country']})")

# Prepare final answer
top_5 = results_df.head(5)

output = []
for i, row in top_5.iterrows():
    output.append(f"{row['Index']} ({row['Country']}): {row['Total_Return']:.2%} total return")

final_answer = "; ".join(output)

print("__RESULT__:")
print(final_answer)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
