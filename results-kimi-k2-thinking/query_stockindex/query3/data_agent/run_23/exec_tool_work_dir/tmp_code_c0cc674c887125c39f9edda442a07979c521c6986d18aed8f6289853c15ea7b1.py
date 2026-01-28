code = """import json
import pandas as pd
import numpy as np
import os

# Load the trade data
storage_key = 'var_functions.query_db:36'
result_data = locals()[storage_key]

# Read the data file
if isinstance(result_data, str) and os.path.exists(result_data):
    with open(result_data, 'r') as f:
        trade_data = json.load(f)
else:
    trade_data = result_data

print(f"Loaded {len(trade_data)} records")

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Parse dates - handle different formats
def parse_date(date_str):
    try:
        return pd.to_datetime(date_str)
    except:
        if 'September' in date_str:
            return pd.to_datetime(date_str, format='%B %d, %Y at %I:%M %p')
        else:
            return pd.NaT

df['Date'] = df['Date'].apply(parse_date)

# Convert CloseUSD to numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Filter for 2000 onwards
df = df[df['Date'] >= '2000-01-01'].copy()

print(f"Filtered to {len(df)} records from {df['Date'].min()} to {df['Date'].max()}")
print(f"Indices: {sorted(df['Index'].unique())}")

# Calculate DCA returns for each index
def calculate_dca_returns(group):
    if len(group) < 250:  # Less than ~1 year of data
        return None
    
    # Sort by date
    group = group.sort_values('Date')
    
    # Add YearMonth for grouping
    group['YearMonth'] = group['Date'].dt.to_period('M')
    
    # DCA parameters
    monthly_investment = 100
    total_invested = 0
    total_shares = 0
    
    # Invest at the first trading day of each month
    for ym, month_data in group.groupby('YearMonth'):
        first_day_price = month_data.iloc[0]['CloseUSD']
        if first_day_price > 0:
            shares = monthly_investment / first_day_price
            total_shares += shares
            total_invested += monthly_investment
    
    if total_invested == 0:
        return None
    
    # Final value
    final_price = group.iloc[-1]['CloseUSD']
    final_value = total_shares * final_price
    total_return = (final_value - total_invested) / total_invested
    
    # Also calculate simple buy-and-hold return for comparison
    start_price = group.iloc[0]['CloseUSD']
    simple_return = (final_price - start_price) / start_price if start_price > 0 else 0
    
    return {
        'total_invested': total_invested,
        'final_value': final_value,
        'total_return': total_return,
        'simple_return': simple_return,
        'years': len(group) / 250
    }

# Apply DCA calculation to each index
results = []
for index in df['Index'].unique():
    index_data = df[df['Index'] == index]
    dca_result = calculate_dca_returns(index_data)
    if dca_result:
        results.append({
            'Index': index,
            'Total_Invested': dca_result['total_invested'],
            'Final_Value': dca_result['final_value'],
            'Total_Return': dca_result['total_return'],
            'Simple_Return': dca_result['simple_return'],
            'Years': dca_result['years']
        })

# Convert to DataFrame and sort by total return
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Total_Return', ascending=False)

print(f"\nCalculated returns for {len(results_df)} indices")
print(results_df.head(10).to_string())

# Save results
output = results_df.to_dict('records')
print('\n__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:6': ['index_trade'], 'var_functions.query_db:8': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:10': [{'Index': '000001.SS', 'min(Date)': '2000-01-04 00:00:00', 'max(Date)': 'September 30, 2015 at 12:00 AM', 'day_count': '4354'}, {'Index': '399001.SZ', 'min(Date)': '2000-01-05 00:00:00', 'max(Date)': 'September 30, 2015 at 12:00 AM', 'day_count': '4355'}, {'Index': 'GDAXI', 'min(Date)': '2000-01-05 00:00:00', 'max(Date)': 'September 30, 2016 at 12:00 AM', 'day_count': '5590'}, {'Index': 'GSPTSE', 'min(Date)': '2000-01-05 00:00:00', 'max(Date)': 'September 30, 2016 at 12:00 AM', 'day_count': '6506'}, {'Index': 'HSI', 'min(Date)': '2000-01-14 00:00:00', 'max(Date)': 'September 30, 2019 at 12:00 AM', 'day_count': '5604'}, {'Index': 'IXIC', 'min(Date)': '2000-01-06 00:00:00', 'max(Date)': 'September 30, 2015 at 12:00 AM', 'day_count': '7351'}, {'Index': 'J203.JO', 'min(Date)': '2012-02-08 00:00:00', 'max(Date)': 'September 30, 2019 at 12:00 AM', 'day_count': '1854'}, {'Index': 'N100', 'min(Date)': '2000-01-10 00:00:00', 'max(Date)': 'September 30, 2019 at 12:00 AM', 'day_count': '4245'}, {'Index': 'N225', 'min(Date)': '2000-01-04 00:00:00', 'max(Date)': 'September 30, 2020 at 12:00 AM', 'day_count': '7979'}, {'Index': 'NSEI', 'min(Date)': '2007-09-25 00:00:00', 'max(Date)': 'September 30, 2014 at 12:00 AM', 'day_count': '2577'}, {'Index': 'NYA', 'min(Date)': '2000-01-03 00:00:00', 'max(Date)': 'September 30, 2020 at 12:00 AM', 'day_count': '7960'}, {'Index': 'SSMI', 'min(Date)': '2000-01-05 00:00:00', 'max(Date)': 'September 30, 2020 at 12:00 AM', 'day_count': '5188'}, {'Index': 'TWII', 'min(Date)': '2000-01-17 00:00:00', 'max(Date)': 'September 30, 2020 at 12:00 AM', 'day_count': '4385'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:34': [{'Index': '000001.SS', 'record_count': '4354'}, {'Index': '399001.SZ', 'record_count': '4355'}, {'Index': 'GDAXI', 'record_count': '5590'}, {'Index': 'GSPTSE', 'record_count': '6506'}, {'Index': 'HSI', 'record_count': '5604'}, {'Index': 'IXIC', 'record_count': '7351'}, {'Index': 'J203.JO', 'record_count': '1854'}, {'Index': 'N100', 'record_count': '4245'}, {'Index': 'N225', 'record_count': '7979'}, {'Index': 'NSEI', 'record_count': '2577'}, {'Index': 'NYA', 'record_count': '7960'}, {'Index': 'SSMI', 'record_count': '5188'}, {'Index': 'TWII', 'record_count': '4385'}], 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
