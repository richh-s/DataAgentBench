code = """import json
import pandas as pd
import numpy as np
from datetime import datetime

# Load the full data
file_path = locals()['var_functions.query_db:16']
with open(file_path, 'r') as f:
    all_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(all_data)

# Convert CloseUSD to numeric and Date to datetime
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Remove any rows with missing data
df = df.dropna(subset=['Date', 'CloseUSD'])

# Filter data from 2000 through 2020 (as this appears to be the available range)
df = df[(df['Date'] >= '2000-01-01') & (df['Date'] <= '2020-12-31')]

# Sort by Index and Date
df = df.sort_values(['Index', 'Date'])

# Get first and last trading day for each index to calculate investment period
index_periods = df.groupby('Index').agg({
    'Date': ['min', 'max'],
    'CloseUSD': ['first', 'last']
}).round(2)

index_periods.columns = ['First_Date', 'Last_Date', 'First_Price', 'Last_Price']
index_periods = index_periods.reset_index()

# Calculate total months for each index
index_periods['Total_Months'] = ((index_periods['Last_Date'] - index_periods['First_Date']).dt.days / 30.44).astype(int)

# For monthly DCA calculation: assume $100 invested at the beginning of each month
# We'll use the first trading day of each month for each index

def calculate_dca_return(index_data, monthly_investment=100):
    """Calculate return from dollar-cost averaging"""
    if len(index_data) < 2:
        return 0, 0, 0
    
    # Get first trading day of each month
    index_data['YearMonth'] = index_data['Date'].dt.to_period('M')
    monthly_data = index_data.groupby('YearMonth').first().reset_index()
    
    if len(monthly_data) < 2:
        return 0, 0, 0
    
    # Calculate DCA
    total_invested = 0
    total_shares = 0
    
    for _, row in monthly_data.iterrows():
        total_invested += monthly_investment
        total_shares += monthly_investment / row['CloseUSD']
    
    # Final value
    final_value = total_shares * index_data.iloc[-1]['CloseUSD']
    total_return = final_value - total_invested
    return_pct = (total_return / total_invested) * 100
    
    return total_invested, final_value, return_pct

# Calculate DCA returns for each index
results = []

for idx in df['Index'].unique():
    idx_data = df[df['Index'] == idx].copy()
    if len(idx_data) > 100:  # Need sufficient data points
        total_invested, final_value, return_pct = calculate_dca_return(idx_data)
        
        # Get period info
        period_info = index_periods[index_periods['Index'] == idx].iloc[0]
        
        results.append({
            'Index': idx,
            'First_Date': str(period_info['First_Date'].date()),
            'Last_Date': str(period_info['Last_Date'].date()),
            'Total_Months': period_info['Total_Months'],
            'First_Price': period_info['First_Price'],
            'Last_Price': period_info['Last_Price'],
            'Total_Invested': round(total_invested, 2),
            'Final_Value': round(final_value, 2),
            'Total_Return': round(final_value - total_invested, 2),
            'Return_Percentage': round(return_pct, 2)
        })

# Convert to DataFrame and sort by return percentage
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Return_Percentage', ascending=False)

# Display top indices
print('__RESULT__:')
print(json.dumps({
    'total_indices_analyzed': len(results_df),
    'top_5_indices': results_df.head(5).to_dict('records'),
    'all_indices_sorted': results_df[['Index', 'Return_Percentage', 'Total_Months']].to_dict('records')
}))"""

env_args = {'var_functions.query_db:0': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:2': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_days': '5791'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_days': '5760'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'total_days': '8438'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'total_days': '10526'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_days': '8492'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_days': '12690'}, {'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_days': '2346'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_days': '5474'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_days': '13874'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00', 'last_date': 'September 30, 2014 at 12:00 AM', 'total_days': '3346'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_days': '13947'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_days': '7671'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_days': '5869'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
