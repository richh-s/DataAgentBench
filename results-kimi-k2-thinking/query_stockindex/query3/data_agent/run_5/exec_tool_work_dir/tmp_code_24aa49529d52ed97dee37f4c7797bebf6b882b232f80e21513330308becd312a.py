code = """import json
import pandas as pd
from datetime import datetime

# Read the data from the file
with open(var_functions.query_db:10, 'r') as f:
    all_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(all_data)

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Convert CloseUSD to numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Filter data from 2000 onwards
df = df[df['Date'] >= '2000-01-01']

# Group by index
indices = df['Index'].unique()

print(f"Total indices: {len(indices)}")
print(f"Indices: {list(indices)}")

# Create a mapping of index to exchange/country based on hints and domain knowledge
index_to_country = {
    '000001.SS': 'China',  # Shanghai Stock Exchange
    '399001.SZ': 'China',  # Shenzhen Stock Exchange
    'GDAXI': 'Germany',    # DAX - Frankfurt Stock Exchange
    'GSPTSE': 'Canada',    # TSX Composite - Toronto Stock Exchange
    'HSI': 'Hong Kong',    # Hang Seng Index - Hong Kong Stock Exchange
    'IXIC': 'USA',         # NASDAQ Composite
    'J203.JO': 'South Africa',  # Johannesburg Stock Exchange
    'N100': 'Belgium',     # Euronext 100
    'N225': 'Japan',       # Nikkei 225 - Tokyo Stock Exchange
    'NSEI': 'India',       # NIFTY 50 - National Stock Exchange of India
    'NYA': 'USA',          # NYSE Composite - New York Stock Exchange
    'SSMI': 'Switzerland', # Swiss Market Index - SIX Swiss Exchange
    'TWII': 'Taiwan'       # Taiwan Weighted Index - Taiwan Stock Exchange
}

# Calculate returns for regular monthly investments for each index
results = []

for index in indices:
    index_data = df[df['Index'] == index].copy()
    index_data = index_data.sort_values('Date')
    
    if index_data.empty:
        continue
    
    # Create monthly dates from start to end
    start_date = index_data['Date'].min()
    end_date = index_data['Date'].max()
    
    # Generate first trading day of each month
    monthly_dates = pd.date_range(start=start_date, end=end_date, freq='MS')
    
    # For each month, find the closest trading day
    total_investment = 0
    total_shares = 0
    
    for month_start in monthly_dates:
        # Find the first trading day in this month or the next available day
        month_data = index_data[index_data['Date'] >= month_start]
        if not month_data.empty:
            # Invest $100 each month
            investment = 100
            price = month_data.iloc[0]['CloseUSD']
            
            if pd.notna(price) and price > 0:
                shares = investment / price
                total_investment += investment
                total_shares += shares
    
    if total_shares > 0:
        # Calculate final value using the last available price
        final_price = index_data.iloc[-1]['CloseUSD']
        final_value = total_shares * final_price
        
        # Calculate total return
        total_return = final_value - total_investment
        return_pct = (total_return / total_investment) * 100 if total_investment > 0 else 0
        
        results.append({
            'Index': index,
            'Country': index_to_country.get(index, 'Unknown'),
            'Total_Investment': total_investment,
            'Final_Value': final_value,
            'Total_Return': total_return,
            'Return_Percentage': return_pct,
            'Start_Date': start_date.strftime('%Y-%m-%d'),
            'End_Date': end_date.strftime('%Y-%m-%d'),
            'Months_Invested': len(monthly_dates)
        })

# Sort by return percentage
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Return_Percentage', ascending=False)

top_5 = results_df.head(5)

print("\nTop 5 Indices by Regular Monthly Investment Returns:")
print(top_5.to_string(index=False))

# Prepare final answer
final_result = top_5[['Index', 'Country', 'Return_Percentage', 'Total_Investment', 'Final_Value']].copy()
final_result['Return_Percentage'] = final_result['Return_Percentage'].round(2)
final_result['Total_Investment'] = final_result['Total_Investment'].round(2)
final_result['Final_Value'] = final_result['Final_Value'].round(2)

result_json = final_result.to_json(orient='records', indent=2)

print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:6': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:8': [{'Index': '000001.SS', 'min_date': '2000-01-04 00:00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'day_count': '4354'}, {'Index': '399001.SZ', 'min_date': '2000-01-05 00:00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'day_count': '4355'}, {'Index': 'GDAXI', 'min_date': '2000-01-05 00:00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'day_count': '5590'}, {'Index': 'GSPTSE', 'min_date': '2000-01-05 00:00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'day_count': '6506'}, {'Index': 'HSI', 'min_date': '2000-01-14 00:00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'day_count': '5604'}, {'Index': 'IXIC', 'min_date': '2000-01-06 00:00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'day_count': '7351'}, {'Index': 'J203.JO', 'min_date': '2012-02-08 00:00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'day_count': '1854'}, {'Index': 'N100', 'min_date': '2000-01-10 00:00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'day_count': '4245'}, {'Index': 'N225', 'min_date': '2000-01-04 00:00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'day_count': '7979'}, {'Index': 'NSEI', 'min_date': '2007-09-25 00:00:00', 'max_date': 'September 30, 2014 at 12:00 AM', 'day_count': '2577'}, {'Index': 'NYA', 'min_date': '2000-01-03 00:00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'day_count': '7960'}, {'Index': 'SSMI', 'min_date': '2000-01-05 00:00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'day_count': '5188'}, {'Index': 'TWII', 'min_date': '2000-01-17 00:00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'day_count': '4385'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
