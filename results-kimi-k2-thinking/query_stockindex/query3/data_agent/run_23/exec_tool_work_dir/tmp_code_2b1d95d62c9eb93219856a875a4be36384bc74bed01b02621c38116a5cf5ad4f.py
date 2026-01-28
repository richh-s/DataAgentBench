code = """import json
import pandas as pd

# Load the data
storage_key = 'var_functions.query_db:12'
result_data = locals()[storage_key]

# Check type and load data
if isinstance(result_data, str):
    with open(result_data, 'r') as f:
        data = json.load(f)
else:
    data = result_data

# Create DataFrame
df = pd.DataFrame(data)

# Convert date strings to datetime objects
import re
def parse_date(date_str):
    if 'September' in date_str:
        return pd.to_datetime(date_str, format='%B %d, %Y at %I:%M %p')
    else:
        return pd.to_datetime(date_str)

df['Date'] = df['Date'].apply(parse_date)

# Filter for 2000 onwards
df_filtered = df[df['Date'] >= '2000-01-01'].copy()

# Group by index and process data
index_groups = df_filtered.groupby('Index')

results = []

for idx, group in index_groups:
    # Sort by date
    group_sorted = group.sort_values('Date')
    
    # Skip if less than 12 months of data
    if len(group_sorted) < 250:
        continue
    
    # Get start and end prices
    start_price = group_sorted.iloc[0]['CloseUSD']
    end_price = group_sorted.iloc[-1]['CloseUSD']
    
    if start_price == 0 or pd.isna(start_price) or pd.isna(end_price):
        continue
    
    # Calculate total return
    total_return = (end_price - start_price) / start_price
    
    # Calculate monthly investment simulation (dollar cost averaging)
    # Assume $100 invested at the start of each month
    monthly_investments = 100
    total_shares = 0
    total_invested = 0
    
    # Group by year-month
    group_sorted['YearMonth'] = group_sorted['Date'].dt.to_period('M')
    
    for ym, month_data in group_sorted.groupby('YearMonth'):
        # Get the first day's close price of the month
        first_day_price = month_data.iloc[0]['CloseUSD']
        if first_day_price > 0:
            shares = monthly_investments / first_day_price
            total_shares += shares
            total_invested += monthly_investments
    
    if total_invested > 0:
        final_value = total_shares * end_price
        dca_return = (final_value - total_invested) / total_invested
        
        results.append({
            'Index': idx,
            'Total_Invested': total_invested,
            'Final_Value': final_value,
            'DCA_Return': dca_return,
            'Years_of_Data': len(group_sorted) / 250,  # Rough estimate
            'Start_Price': start_price,
            'End_Price': end_price,
            'Simple_Return': total_return
        })

# Convert to DataFrame
results_df = pd.DataFrame(results)

# Sort by DCA return
results_sorted = results_df.sort_values('DCA_Return', ascending=False)

# Get top 5
top_5 = results_sorted.head(5)

# Convert to JSON for output
output_data = top_5.to_dict('records')
output_json = json.dumps(output_data, indent=2)

print('__RESULT__:')
print(output_json)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:6': ['index_trade'], 'var_functions.query_db:8': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:10': [{'Index': '000001.SS', 'min(Date)': '2000-01-04 00:00:00', 'max(Date)': 'September 30, 2015 at 12:00 AM', 'day_count': '4354'}, {'Index': '399001.SZ', 'min(Date)': '2000-01-05 00:00:00', 'max(Date)': 'September 30, 2015 at 12:00 AM', 'day_count': '4355'}, {'Index': 'GDAXI', 'min(Date)': '2000-01-05 00:00:00', 'max(Date)': 'September 30, 2016 at 12:00 AM', 'day_count': '5590'}, {'Index': 'GSPTSE', 'min(Date)': '2000-01-05 00:00:00', 'max(Date)': 'September 30, 2016 at 12:00 AM', 'day_count': '6506'}, {'Index': 'HSI', 'min(Date)': '2000-01-14 00:00:00', 'max(Date)': 'September 30, 2019 at 12:00 AM', 'day_count': '5604'}, {'Index': 'IXIC', 'min(Date)': '2000-01-06 00:00:00', 'max(Date)': 'September 30, 2015 at 12:00 AM', 'day_count': '7351'}, {'Index': 'J203.JO', 'min(Date)': '2012-02-08 00:00:00', 'max(Date)': 'September 30, 2019 at 12:00 AM', 'day_count': '1854'}, {'Index': 'N100', 'min(Date)': '2000-01-10 00:00:00', 'max(Date)': 'September 30, 2019 at 12:00 AM', 'day_count': '4245'}, {'Index': 'N225', 'min(Date)': '2000-01-04 00:00:00', 'max(Date)': 'September 30, 2020 at 12:00 AM', 'day_count': '7979'}, {'Index': 'NSEI', 'min(Date)': '2007-09-25 00:00:00', 'max(Date)': 'September 30, 2014 at 12:00 AM', 'day_count': '2577'}, {'Index': 'NYA', 'min(Date)': '2000-01-03 00:00:00', 'max(Date)': 'September 30, 2020 at 12:00 AM', 'day_count': '7960'}, {'Index': 'SSMI', 'min(Date)': '2000-01-05 00:00:00', 'max(Date)': 'September 30, 2020 at 12:00 AM', 'day_count': '5188'}, {'Index': 'TWII', 'min(Date)': '2000-01-17 00:00:00', 'max(Date)': 'September 30, 2020 at 12:00 AM', 'day_count': '4385'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
