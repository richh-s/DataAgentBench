code = """import json
import pandas as pd
import numpy as np

# Load data from file
file_path = var_functions.query_db:10
with open(file_path, 'r') as f:
    all_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(all_data)

# Convert data types
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Remove missing data
df = df.dropna(subset=['Date', 'CloseUSD'])

# Load index info
index_info = var_functions.query_db:12

# Map exchanges to countries
exchange_to_country = {
    'New York Stock Exchange': 'United States',
    'NASDAQ': 'United States', 
    'Hong Kong Stock Exchange': 'Hong Kong',
    'Shanghai Stock Exchange': 'China',
    'Tokyo Stock Exchange': 'Japan',
    'Euronext': 'Europe',
    'Shenzhen Stock Exchange': 'China',
    'Toronto Stock Exchange': 'Canada',
    'National Stock Exchange of India': 'India',
    'Frankfurt Stock Exchange': 'Germany',
    'Korea Exchange': 'South Korea',
    'SIX Swiss Exchange': 'Switzerland',
    'Taiwan Stock Exchange': 'Taiwan',
    'Johannesburg Stock Exchange': 'South Africa'
}

# Map indices to exchanges
index_to_exchange = {
    'NYA': 'New York Stock Exchange',
    'IXIC': 'NASDAQ',
    'HSI': 'Hong Kong Stock Exchange',
    '000001.SS': 'Shanghai Stock Exchange',
    '399001.SZ': 'Shenzhen Stock Exchange',
    'N225': 'Tokyo Stock Exchange',
    'N100': 'Euronext',
    'GDAXI': 'Frankfurt Stock Exchange',
    'NSEI': 'National Stock Exchange of India',
    'GSPTSE': 'Toronto Stock Exchange',
    'SSMI': 'SIX Swiss Exchange',
    'TWII': 'Taiwan Stock Exchange',
    'J203.JO': 'Johannesburg Stock Exchange'
}

# Calculate returns for each index using dollar cost averaging
results = []
for index_name in df['Index'].unique():
    idx_data = df[df['Index'] == index_name].copy()
    idx_data = idx_data.sort_values('Date')
    
    # Filter data from 2000 onwards
    idx_data = idx_data[idx_data['Date'] >= '2000-01-01']
    
    if len(idx_data) < 12:  # Need at least a year of data
        continue
    
    # Monthly investment - invest $100 at the beginning of each month
    monthly_investment = 100
    total_invested = 0
    total_shares = 0
    
    # Group by month and get the first trading day of each month
    idx_data['YearMonth'] = idx_data['Date'].dt.to_period('M')
    monthly_data = idx_data.groupby('YearMonth').first().reset_index()
    
    for _, row in monthly_data.iterrows():
        price = row['CloseUSD']
        if price > 0:
            total_invested += monthly_investment
            total_shares += monthly_investment / price
    
    # Calculate final value
    final_price = idx_data.iloc[-1]['CloseUSD']
    final_value = total_shares * final_price
    total_return = final_value - total_invested
    return_percent = (total_return / total_invested) * 100 if total_invested > 0 else 0
    
    # Get country
    exchange = index_to_exchange.get(index_name, 'Unknown')
    country = exchange_to_country.get(exchange, 'Unknown')
    
    # Calculate total time period
    days = (idx_data['Date'].max() - idx_data['Date'].min()).days
    years = days / 365.25
    
    # Calculate annualized return
    if years > 0:
        annualized_return = ((final_value / total_invested) ** (1/years) - 1) * 100 if total_invested > 0 else 0
    else:
        annualized_return = 0
    
    results.append({
        'Index': index_name,
        'Exchange': exchange,
        'Country': country,
        'Total_Invested': total_invested,
        'Final_Value': final_value,
        'Total_Return': total_return,
        'Return_Percent': return_percent,
        'Years': years,
        'Annualized_Return': annualized_return,
        'First_Date': str(idx_data['Date'].min().date()),
        'Last_Date': str(idx_data['Date'].max().date())
    })

# Sort by total return and get top 5
results_df = pd.DataFrame(results)
top_5 = results_df.nlargest(5, 'Return_Percent')

print('Top 5 Indices by Dollar Cost Averaging Return since 2000:')
print(top_5[['Index', 'Country', 'Return_Percent', 'Annualized_Return', 'Years']].to_string(index=False))

# Store for final answer
top_indices_data = top_5.to_dict('records')

# Also show summary stats for all indices
print('\nAll Indices Summary:')
summary_stats = results_df[['Index', 'Country', 'Return_Percent', 'Annualized_Return']].sort_values('Return_Percent', ascending=False)
print(summary_stats.to_string(index=False))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Index': '000001.SS', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': '399001.SZ', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'GDAXI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'GSPTSE', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'HSI', 'first_date': '2000-01-14 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'IXIC', 'first_date': '2000-01-06 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'J203.JO', 'first_date': '2012-02-08 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N100', 'first_date': '2000-01-10 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N225', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'NSEI', 'first_date': '2007-09-25 00:00:00', 'last_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'NYA', 'first_date': '2000-01-03 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'SSMI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'first_date': '2000-01-17 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
