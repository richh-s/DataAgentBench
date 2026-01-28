code = """import json
import pandas as pd
from datetime import datetime

# The data is stored in locals() with the key from the previous query
# Let's access it through the variable name
raw_data = var_functions.query_db:10

# Convert to DataFrame
df = pd.DataFrame(raw_data)

# Parse dates
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year

# Filter for data from 2000 onwards
df_2000 = df[df['Year'] >= 2000].copy()

# Group by index and calculate monthly aggregated data
monthly_data = []
for idx in df_2000['Index'].unique():
    idx_data = df_2000[df_2000['Index'] == idx].copy()
    idx_data['YearMonth'] = idx_data['Date'].dt.to_period('M')
    
    # For each month, get the first available day's closing price
    monthly_closes = idx_data.groupby('YearMonth').agg({
        'CloseUSD': 'first',
        'Date': 'first'
    }).reset_index()
    
    monthly_closes['Index'] = idx
    monthly_data.append(monthly_closes)

combined_monthly = pd.concat(monthly_data, ignore_index=True)

# Calculate DCA returns for each index
results = []
monthly_investment = 100  # $100 per month

for idx in combined_monthly['Index'].unique():
    idx_data = combined_monthly[combined_monthly['Index'] == idx].sort_values('Date')
    
    if len(idx_data) == 0:
        continue
    
    # Calculate shares purchased each month
    idx_data['Shares'] = monthly_investment / idx_data['CloseUSD']
    idx_data['Cumulative_Shares'] = idx_data['Shares'].cumsum()
    idx_data['Cumulative_Invested'] = monthly_investment * range(1, len(idx_data) + 1)
    
    # Final values
    total_invested = idx_data['Cumulative_Invested'].iloc[-1]
    total_shares = idx_data['Cumulative_Shares'].iloc[-1]
    final_value = total_shares * idx_data['CloseUSD'].iloc[-1]
    total_return = final_value - total_invested
    return_pct = (total_return / total_invested) * 100
    
    results.append({
        'Index': idx,
        'Total_Invested': total_invested,
        'Final_Value': final_value,
        'Total_Return': total_return,
        'Return_Percentage': return_pct,
        'Months': len(idx_data)
    })

# Convert to DataFrame and sort by return percentage
results_df = pd.DataFrame(results).sort_values('Return_Percentage', ascending=False)

# Map indices to countries (based on the index symbols and exchanges)
index_country_map = {
    'N225': 'Japan',
    'IXIC': 'USA',
    'NYA': 'USA',
    'HSI': 'Hong Kong',
    'GDAXI': 'Germany',
    'GSPTSE': 'Canada',
    'SSMI': 'Switzerland'
}

results_df['Country'] = results_df['Index'].map(index_country_map)

# Display top 5
top_5 = results_df.head(5)

result_output = {
    'top_5_indices': top_5.to_dict('records'),
    'all_returns': results_df.to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result_output, default=str))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'record_count': '5791'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'record_count': '5760'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'record_count': '8438'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'record_count': '10526'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'record_count': '8492'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'record_count': '12690'}, {'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'record_count': '2346'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'record_count': '5474'}, {'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'record_count': '13874'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM', 'record_count': '3346'}, {'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'record_count': '13947'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'record_count': '7671'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'record_count': '5869'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
