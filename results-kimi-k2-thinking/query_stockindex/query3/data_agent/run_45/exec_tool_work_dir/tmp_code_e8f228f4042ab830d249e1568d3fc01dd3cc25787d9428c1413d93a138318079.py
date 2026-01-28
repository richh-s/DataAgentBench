code = """import pandas as pd
import numpy as np
import json

# Load trade data from the file
file_path = locals()['var_functions.query_db:14']
with open(file_path, 'r') as f:
    trade_data = json.load(f)

# Create DataFrame
df = pd.DataFrame(trade_data)

# Convert Date to datetime and CloseUSD to numeric
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Remove rows with missing values
df_clean = df.dropna(subset=['Date', 'CloseUSD', 'Index']).copy()

# Filter indices that have data from 2000 or earlier
index_start_dates = df_clean.groupby('Index')['Date'].min().reset_index()
indices_with_2000_data = index_start_dates[index_start_dates['Date'] <= '2000-12-31']['Index'].tolist()

# Calculate dollar-cost-averaged returns for each index since 2000
results = []

for idx in indices_with_2000_data:
    # Filter data for this index from 2000 onwards
    idx_data = df_clean[df_clean['Index'] == idx].copy()
    idx_data_2000 = idx_data[idx_data['Date'] >= '2000-01-01'].sort_values('Date')
    
    if len(idx_data_2000) == 0:
        continue
    
    # Group by month: get first trading day price for each month
    idx_data_2000['YearMonth'] = idx_data_2000['Date'].dt.to_period('M')
    monthly_data = idx_data_2000.groupby('YearMonth').agg({
        'CloseUSD': 'first',
        'Date': 'first'
    }).reset_index()
    
    # Simulate investing $100 at the start of each month
    monthly_investment = 100
    monthly_data['Investment'] = monthly_investment
    monthly_data['Units'] = monthly_investment / monthly_data['CloseUSD']
    
    # Calculate totals
    total_invested = monthly_data['Investment'].sum()
    total_units = monthly_data['Units'].sum()
    final_price = idx_data_2000['CloseUSD'].iloc[-1]
    final_value = total_units * final_price
    total_return = final_value - total_invested
    return_pct = (total_return / total_invested) * 100
    
    # Map index to country
    country_map = {
        'GDAXI': 'Germany',
        'GSPTSE': 'Canada', 
        'HSI': 'Hong Kong',
        'IXIC': 'United States',
        'N225': 'Japan',
        'NYA': 'United States',
        'SSMI': 'Switzerland',
        'TWII': 'Taiwan',
        '000001.SS': 'China',
        '399001.SZ': 'China',
        'N100': 'Belgium'
    }
    
    country = country_map.get(idx, 'Unknown')
    
    results.append({
        'Index': idx,
        'Country': country,
        'Total_Invested': float(round(total_invested, 2)),
        'Final_Value': float(round(final_value, 2)),
        'Total_Return': float(round(total_return, 2)),
        'Return_Pct': float(round(return_pct, 2)),
        'Months': len(monthly_data),
        'Start_Date': idx_data_2000['Date'].min().strftime('%Y-%m-%d'),
        'End_Date': idx_data_2000['Date'].max().strftime('%Y-%m-%d')
    })

# Sort by return percentage in descending order
results_sorted = sorted(results, key=lambda x: x['Return_Pct'], reverse=True)

# Get top 5 indices
top_5_indices = results_sorted[:5]

print("__RESULT__:")
print(json.dumps(top_5_indices, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:12': [{'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:34': {'file_path': 'file_storage/functions.query_db:14.json'}, 'var_functions.execute_python:38': {'total_records': 21342, 'date_min': '2000-01-03 00:00:00', 'date_max': '2021-06-02 00:00:00', 'unique_indices': ['000001.SS', '399001.SZ', 'GDAXI', 'GSPTSE', 'HSI', 'IXIC', 'J203.JO', 'N100', 'N225', 'NSEI', 'NYA', 'SSMI', 'TWII'], 'indices_with_2000_data': ['000001.SS', '399001.SZ', 'GDAXI', 'GSPTSE', 'HSI', 'IXIC', 'N100', 'N225', 'NYA', 'SSMI', 'TWII']}}

exec(code, env_args)
