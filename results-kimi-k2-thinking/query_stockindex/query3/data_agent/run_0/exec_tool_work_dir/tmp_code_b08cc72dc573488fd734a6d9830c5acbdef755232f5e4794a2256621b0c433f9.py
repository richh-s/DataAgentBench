code = """import json
import pandas as pd
import numpy as np

# Read the data from storage
data_file = locals()['var_functions.query_db:8']
with open(data_file, 'r') as f:
    trade_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Strip any whitespace from column names
df.columns = df.columns.str.strip()

# Convert Date to datetime with errors='coerce'
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Ensure CloseUSD is numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Drop rows with invalid dates or prices
df = df.dropna(subset=['Date', 'CloseUSD'])

# Filter for dates from 2000 onwards
df = df[df['Date'] >= '2000-01-01']

# Sort by Index and Date
df = df.sort_values(['Index', 'Date'])

# Map indices to their exchanges and countries
index_mapping = {
    'N225': {'exchange': 'Tokyo Stock Exchange', 'country': 'Japan', 'region': 'Asia'},
    'NYA': {'exchange': 'New York Stock Exchange', 'country': 'USA', 'region': 'North America'},
    'IXIC': {'exchange': 'NASDAQ', 'country': 'USA', 'region': 'North America'},
    'GSPTSE': {'exchange': 'Toronto Stock Exchange', 'country': 'Canada', 'region': 'North America'},
    'HSI': {'exchange': 'Hong Kong Stock Exchange', 'country': 'Hong Kong', 'region': 'Asia'},
    'GDAXI': {'exchange': 'Frankfurt Stock Exchange', 'country': 'Germany', 'region': 'Europe'},
    'SSMI': {'exchange': 'SIX Swiss Exchange', 'country': 'Switzerland', 'region': 'Europe'},
    'TWII': {'exchange': 'Taiwan Stock Exchange', 'country': 'Taiwan', 'region': 'Asia'},
    '399001.SZ': {'exchange': 'Shenzhen Stock Exchange', 'country': 'China', 'region': 'Asia'},
    '000001.SS': {'exchange': 'Shanghai Stock Exchange', 'country': 'China', 'region': 'Asia'},
    'N100': {'exchange': 'Euronext', 'country': 'Netherlands/France', 'region': 'Europe'},
    'NSEI': {'exchange': 'National Stock Exchange of India', 'country': 'India', 'region': 'Asia'},
    'J203.JO': {'exchange': 'Johannesburg Stock Exchange', 'country': 'South Africa', 'region': 'Africa'}
}

# For each index, calculate dollar-cost averaging returns
monthly_investment = 100  # Fixed monthly investment in USD
results = []

for index in df['Index'].unique():
    index_data = df[df['Index'] == index].copy()
    
    if len(index_data) < 12:  # Skip if less than a year of data
        continue
    
    # Get first trading day of each month
    index_data['YearMonth'] = index_data['Date'].dt.to_period('M')
    monthly_first = index_data.groupby('YearMonth').first().reset_index()
    
    # Calculate DCA
    total_shares = 0
    total_invested = 0
    
    for _, row in monthly_first.iterrows():
        shares = monthly_investment / row['CloseUSD']
        total_shares += shares
        total_invested += monthly_investment
    
    # Get final value
    final_price = index_data.iloc[-1]['CloseUSD']
    final_value = total_shares * final_price
    total_return = final_value - total_invested
    percent_return = (total_return / total_invested) * 100
    
    # Calculate additional metrics
    total_months = len(monthly_first)
    years = total_months / 12
    
    # Annualized return (approximation)
    if total_invested > 0:
        annualized_return = ((final_value / total_invested) ** (1/years) - 1) * 100
    else:
        annualized_return = 0
    
    results.append({
        'Index': index,
        'Exchange': index_mapping.get(index, {}).get('exchange', 'Unknown'),
        'Country': index_mapping.get(index, {}).get('country', 'Unknown'),
        'Region': index_mapping.get(index, {}).get('region', 'Unknown'),
        'Total_Months': total_months,
        'Years': round(years, 1),
        'Total_Invested': round(total_invested, 2),
        'Final_Value': round(final_value, 2),
        'Total_Return': round(total_return, 2),
        'Percent_Return': round(percent_return, 2),
        'Annualized_Return': round(annualized_return, 2)
    })

# Convert to DataFrame and sort by percent return
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Percent_Return', ascending=False)

# Get top 5
top_5 = results_df.head(5)

# Convert to JSON for printing
json_result = {
    'top_5_indices': top_5.to_dict('records'),
    'all_indices': results_df.to_dict('records')
}

print('__RESULT__:')
print(json.dumps(json_result, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'N225', 'count': '7979'}, {'Index': 'NYA', 'count': '7960'}, {'Index': 'IXIC', 'count': '7351'}, {'Index': 'GSPTSE', 'count': '6506'}, {'Index': 'HSI', 'count': '5604'}, {'Index': 'GDAXI', 'count': '5590'}, {'Index': 'SSMI', 'count': '5188'}, {'Index': 'TWII', 'count': '4385'}, {'Index': '399001.SZ', 'count': '4355'}, {'Index': '000001.SS', 'count': '4354'}, {'Index': 'N100', 'count': '4245'}, {'Index': 'NSEI', 'count': '2577'}, {'Index': 'J203.JO', 'count': '1854'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'total_records': 21342, 'indices_count': 13, 'indices': ['000001.SS', '399001.SZ', 'GDAXI', 'GSPTSE', 'HSI', 'IXIC', 'J203.JO', 'N100', 'N225', 'NSEI', 'NYA', 'SSMI', 'TWII']}, 'var_functions.query_db:16': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
