code = """import json
import pandas as pd
from datetime import datetime

# Read the historical data from file
file_path = locals()['var_functions.query_db:12']
with open(file_path, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Convert CloseUSD to float (if it's stored as string)
df['CloseUSD'] = df['CloseUSD'].astype(float)

print('Data loaded:')
print(f'Shape: {df.shape}')
print(f'Indices: {df["Index"].nunique()}')
print(f'Date range: {df["Date"].min()} to {df["Date"].max()}')

# Map indices to exchanges
index_to_exchange = {
    '000001.SS': 'Shanghai Stock Exchange',
    '399001.SZ': 'Shenzhen Stock Exchange', 
    'GDAXI': 'Frankfurt Stock Exchange',
    'GSPTSE': 'Toronto Stock Exchange',
    'HSI': 'Hong Kong Stock Exchange',
    'IXIC': 'NASDAQ',
    'N100': 'Euronext',
    'N225': 'Tokyo Stock Exchange',
    'NYA': 'New York Stock Exchange',
    'SSMI': 'SIX Swiss Exchange',
    'TWII': 'Taiwan Stock Exchange',
    'NSEI': 'National Stock Exchange of India'
}

# Read exchange data
exchange_data = locals()['var_functions.query_db:2']
df_exchanges = pd.DataFrame(exchange_data)

print('\nExchange data:')
print(df_exchanges)

# Map exchanges to countries (based on geographic knowledge)
exchange_to_country = {
    'Shanghai Stock Exchange': 'China',
    'Shenzhen Stock Exchange': 'China',
    'Frankfurt Stock Exchange': 'Germany',
    'Toronto Stock Exchange': 'Canada',
    'Hong Kong Stock Exchange': 'Hong Kong',
    'NASDAQ': 'United States',
    'Euronext': 'Netherlands/France/Belgium',
    'Tokyo Stock Exchange': 'Japan',
    'New York Stock Exchange': 'United States',
    'SIX Swiss Exchange': 'Switzerland',
    'Taiwan Stock Exchange': 'Taiwan',
    'National Stock Exchange of India': 'India'
}

print('\nCountry mapping:')
for idx, exchange in index_to_exchange.items():
    print(f'{idx}: {exchange_to_country[exchange]}')

# Calculate dollar-cost averaging returns
monthly_investment = 100  # $100 per month
results = []

for index in df['Index'].unique():
    index_data = df[df['Index'] == index].copy()
    index_data = index_data.sort_values('Date')
    index_data['YearMonth'] = index_data['Date'].dt.to_period('M')
    
    # Group by month and get first trading day of each month
    monthly_prices = index_data.groupby('YearMonth').first().reset_index()
    
    if len(monthly_prices) == 0:
        continue
    
    # Simulate monthly investments
    monthly_prices['Units'] = monthly_investment / monthly_prices['CloseUSD']
    monthly_prices['Cumulative_Units'] = monthly_prices['Units'].cumsum()
    monthly_prices['Cumulative_Investment'] = range(1, len(monthly_prices) + 1) * monthly_investment
    
    # Current value
    current_value = monthly_prices['Cumulative_Units'].iloc[-1] * monthly_prices['CloseUSD'].iloc[-1]
    total_invested = monthly_prices['Cumulative_Investment'].iloc[-1]
    total_return = current_value - total_invested
    return_pct = (total_return / total_invested) * 100
    
    # Get country
    country = exchange_to_country[index_to_exchange[index]]
    exchange = index_to_exchange[index]
    
    results.append({
        'Index': index,
        'Exchange': exchange,
        'Country': country,
        'Total_Invested': total_invested,
        'Current_Value': current_value,
        'Total_Return': total_return,
        'Return_Percentage': return_pct,
        'Months': len(monthly_prices)
    })

# Create results DataFrame
df_results = pd.DataFrame(results)
df_results = df_results.sort_values('Return_Percentage', ascending=False)

print('\nTop indices by returns:')
print(df_results.head(10))

print('__RESULT__:')
print(df_results.to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Index': '000001.SS', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_records': '4354'}, {'Index': '399001.SZ', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_records': '4355'}, {'Index': 'GDAXI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'total_records': '5590'}, {'Index': 'GSPTSE', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'total_records': '6506'}, {'Index': 'HSI', 'first_date': '2000-01-14 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_records': '5604'}, {'Index': 'IXIC', 'first_date': '2000-01-06 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_records': '7351'}, {'Index': 'J203.JO', 'first_date': '2012-02-08 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_records': '1854'}, {'Index': 'N100', 'first_date': '2000-01-10 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_records': '4245'}, {'Index': 'N225', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_records': '7979'}, {'Index': 'NSEI', 'first_date': '2007-09-25 00:00:00', 'last_date': 'September 30, 2014 at 12:00 AM', 'total_records': '2577'}, {'Index': 'NYA', 'first_date': '2000-01-03 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_records': '7960'}, {'Index': 'SSMI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_records': '5188'}, {'Index': 'TWII', 'first_date': '2000-01-17 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_records': '4385'}], 'var_functions.execute_python:10': [{'Index': '000001.SS', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_records': '4354'}, {'Index': '399001.SZ', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_records': '4355'}, {'Index': 'GDAXI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'total_records': '5590'}, {'Index': 'GSPTSE', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'total_records': '6506'}, {'Index': 'HSI', 'first_date': '2000-01-14 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_records': '5604'}, {'Index': 'IXIC', 'first_date': '2000-01-06 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_records': '7351'}, {'Index': 'J203.JO', 'first_date': '2012-02-08 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_records': '1854'}, {'Index': 'N100', 'first_date': '2000-01-10 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_records': '4245'}, {'Index': 'N225', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_records': '7979'}, {'Index': 'NSEI', 'first_date': '2007-09-25 00:00:00', 'last_date': 'September 30, 2014 at 12:00 AM', 'total_records': '2577'}, {'Index': 'NYA', 'first_date': '2000-01-03 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_records': '7960'}, {'Index': 'SSMI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_records': '5188'}, {'Index': 'TWII', 'first_date': '2000-01-17 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_records': '4385'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
