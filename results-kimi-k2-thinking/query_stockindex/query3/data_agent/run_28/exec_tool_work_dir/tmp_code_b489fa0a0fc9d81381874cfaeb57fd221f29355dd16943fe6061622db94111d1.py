code = """import json
import pandas as pd
import numpy as np

# The data is stored in a file, get the path
file_path = var_functions.query_db:44  # This has the aggregated stats

# Actually I need the full data, let's use the first query result
# But I need to load the actual data file
# Let me check what the file path is
print('Checking file path structure...')
print('Type:', type(var_functions.query_db:44))
print('Content:', var_functions.query_db:44)

# Load the full dataset from the file path we got earlier
full_data_path = var_functions.query_db:10

# Read the data
with open(full_data_path, 'r') as f:
    data = json.load(f)

print(f'Loaded {len(data)} records')

# Convert to DataFrame
df = pd.DataFrame(data)

# Clean and convert data types
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Filter valid data from 2000 onwards
df = df.dropna(subset=['Date', 'CloseUSD'])
df = df[df['CloseUSD'] > 0]
df = df[df['Date'] >= '2000-01-01']

print(f'Valid records from 2000 onwards: {len(df)}')
print(f'Indices: {sorted(df["Index"].unique())}')

# Map indices to countries
country_map = {
    'NYA': 'United States',
    'IXIC': 'United States',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China', 
    'N225': 'Japan',
    'N100': 'Europe',
    'GDAXI': 'Germany',
    'NSEI': 'India',
    'GSPTSE': 'Canada',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'J203.JO': 'South Africa'
}

# Calculate dollar-cost averaging returns for each index
results = []

for index_symbol in sorted(df['Index'].unique()):
    index_data = df[df['Index'] == index_symbol].copy()
    
    if len(index_data) < 12:  # Need at least 12 months
        continue
    
    # Sort by date
    index_data = index_data.sort_values('Date')
    
    # Get first trading day of each month
    index_data['YearMonth'] = index_data['Date'].dt.to_period('M')
    monthly_data = index_data.groupby('YearMonth').first().reset_index()
    
    if len(monthly_data) == 0:
        continue
    
    # Dollar-cost averaging: invest $100 at the start of each month
    total_invested = 0.0
    total_shares = 0.0
    
    for _, row in monthly_data.iterrows():
        price = row['CloseUSD']
        if price > 0:
            total_invested += 100.0
            total_shares += 100.0 / price
    
    if total_invested == 0:
        continue
    
    # Calculate final portfolio value
    final_price = index_data['CloseUSD'].iloc[-1]
    final_value = total_shares * final_price
    
    # Calculate return metrics
    total_return = final_value - total_invested
    return_percent = (total_return / total_invested) * 100.0
    
    # Calculate time period in years
    days = (index_data['Date'].iloc[-1] - index_data['Date'].iloc[0]).days
    years = days / 365.25
    
    # Annualized return
    annualized_return = 0.0
    if years > 0:
        annualized_return = ((final_value / total_invested) ** (1.0 / years) - 1.0) * 100.0
    
    country = country_map.get(index_symbol, 'Unknown')
    
    results.append({
        'Index': index_symbol,
        'Country': country,
        'Total_Invested': round(total_invested, 2),
        'Final_Value': round(final_value, 2),
        'Total_Return': round(total_return, 2),
        'Return_Percent': round(return_percent, 2),
        'Years': round(years, 1),
        'Annualized_Return': round(annualized_return, 2),
        'Months': len(monthly_data)
    })

# Sort by return percentage
top_5 = sorted(results, key=lambda x: x['Return_Percent'], reverse=True)[:5]

print('\\nTop 5 indices by dollar-cost averaging return since 2000:')
for i, item in enumerate(top_5, 1):
    print(f"{i}. {item['Index']} ({item['Country']}) - {item['Return_Percent']}% total return ({item['Years']} years)")

print('\\nAll indices results:')
for item in sorted(results, key=lambda x: x['Return_Percent'], reverse=True):
    print(f"{item['Index']}: {item['Return_Percent']}% ({item['Country']})")

result_json = json.dumps(top_5)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Index': '000001.SS', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': '399001.SZ', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'GDAXI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'GSPTSE', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'HSI', 'first_date': '2000-01-14 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'IXIC', 'first_date': '2000-01-06 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'J203.JO', 'first_date': '2012-02-08 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N100', 'first_date': '2000-01-10 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N225', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'NSEI', 'first_date': '2007-09-25 00:00:00', 'last_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'NYA', 'first_date': '2000-01-03 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'SSMI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'first_date': '2000-01-17 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.execute_python:30': [], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': [{'Index': 'J203.JO', 'start_date': '2012-02-08 00:00:00', 'end_date': 'September 30, 2019 at 12:00 AM', 'records': '1854'}, {'Index': 'HSI', 'start_date': '2000-01-14 00:00:00', 'end_date': 'September 30, 2019 at 12:00 AM', 'records': '5604'}, {'Index': 'NYA', 'start_date': '2000-01-03 00:00:00', 'end_date': 'September 30, 2020 at 12:00 AM', 'records': '7960'}, {'Index': 'N100', 'start_date': '2000-01-10 00:00:00', 'end_date': 'September 30, 2019 at 12:00 AM', 'records': '4245'}, {'Index': '399001.SZ', 'start_date': '2000-01-05 00:00:00', 'end_date': 'September 30, 2015 at 12:00 AM', 'records': '4355'}, {'Index': 'N225', 'start_date': '2000-01-04 00:00:00', 'end_date': 'September 30, 2020 at 12:00 AM', 'records': '7979'}, {'Index': 'GSPTSE', 'start_date': '2000-01-05 00:00:00', 'end_date': 'September 30, 2016 at 12:00 AM', 'records': '6506'}, {'Index': 'NSEI', 'start_date': '2007-09-25 00:00:00', 'end_date': 'September 30, 2014 at 12:00 AM', 'records': '2577'}, {'Index': 'GDAXI', 'start_date': '2000-01-05 00:00:00', 'end_date': 'September 30, 2016 at 12:00 AM', 'records': '5590'}, {'Index': '000001.SS', 'start_date': '2000-01-04 00:00:00', 'end_date': 'September 30, 2015 at 12:00 AM', 'records': '4354'}, {'Index': 'SSMI', 'start_date': '2000-01-05 00:00:00', 'end_date': 'September 30, 2020 at 12:00 AM', 'records': '5188'}, {'Index': 'TWII', 'start_date': '2000-01-17 00:00:00', 'end_date': 'September 30, 2020 at 12:00 AM', 'records': '4385'}, {'Index': 'IXIC', 'start_date': '2000-01-06 00:00:00', 'end_date': 'September 30, 2015 at 12:00 AM', 'records': '7351'}]}

exec(code, env_args)
