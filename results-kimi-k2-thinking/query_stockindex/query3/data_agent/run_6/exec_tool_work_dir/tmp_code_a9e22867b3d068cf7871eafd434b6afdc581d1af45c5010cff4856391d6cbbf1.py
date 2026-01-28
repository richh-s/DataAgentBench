code = """import json
import pandas as pd

# The data is stored in a file, get the path
file_path = var_functions.query_db:22

# Read the data from the file
with open(file_path, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Parse dates
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Filter for data from 2000 onwards
df_2000 = df[df['Year'] >= 2000].copy()

# Create Year-Month column for grouping
df_2000['YearMonth'] = df_2000['Date'].dt.to_period('M')

# For each index and month, get the first available closing price
monthly_prices = df_2000.groupby(['Index', 'YearMonth']).agg({
    'CloseUSD': 'first',
    'Date': 'first'
}).reset_index()

# Sort by index and date
monthly_prices = monthly_prices.sort_values(['Index', 'Date'])

# Calculate DCA returns for each index
dca_results = []
monthly_investment = 100  # $100 per month

for idx in monthly_prices['Index'].unique():
    idx_data = monthly_prices[monthly_prices['Index'] == idx].copy()
    
    if len(idx_data) == 0:
        continue
    
    # Calculate cumulative shares and investment
    idx_data['Shares_Purchased'] = monthly_investment / idx_data['CloseUSD']
    idx_data['Cumulative_Shares'] = idx_data['Shares_Purchased'].cumsum()
    idx_data['Cumulative_Investment'] = monthly_investment * (range(1, len(idx_data) + 1))
    
    # Final values
    total_invested = idx_data['Cumulative_Investment'].iloc[-1]
    total_shares = idx_data['Cumulative_Shares'].iloc[-1]
    final_price = idx_data['CloseUSD'].iloc[-1]
    final_value = total_shares * final_price
    total_return = final_value - total_invested
    return_pct = (total_return / total_invested) * 100
    
    dca_results.append({
        'Index': idx,
        'Months': len(idx_data),
        'Total_Invested': round(total_invested, 2),
        'Final_Value': round(final_value, 2),
        'Total_Return': round(total_return, 2),
        'Return_Percentage': round(return_pct, 2)
    })

# Convert to DataFrame and sort by return percentage
results_df = pd.DataFrame(dca_results).sort_values('Return_Percentage', ascending=False)

# Map indices to countries
index_country_map = {
    'N225': 'Japan',
    'IXIC': 'USA',
    'NYA': 'USA',
    'HSI': 'Hong Kong',
    'GDAXI': 'Germany',
    'GSPTSE': 'Canada',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Europe (Euronext)',
    '000001.SS': 'China (Shanghai)',
    '399001.SZ': 'China (Shenzhen)',
    'NSEI': 'India',
    'J203.JO': 'South Africa'
}

results_df['Country'] = results_df['Index'].map(index_country_map)

# Get top 5 indices
top_5 = results_df.head(5)

# Prepare output
output = {
    'top_5_indices': top_5.to_dict('records'),
    'all_returns': results_df.to_dict('records')
}

print('__RESULT__:')
print(json.dumps(output, default=str))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'record_count': '5791'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'record_count': '5760'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'record_count': '8438'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'record_count': '10526'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'record_count': '8492'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'record_count': '12690'}, {'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'record_count': '2346'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'record_count': '5474'}, {'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'record_count': '13874'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM', 'record_count': '3346'}, {'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'record_count': '13947'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'record_count': '7671'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'record_count': '5869'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:20': [{'Index': '000001.SS', 'Date': '2000-01-04 00:00:00', 'CloseUSD': '225.01935552'}, {'Index': '000001.SS', 'Date': '2000-01-05 00:00:00', 'CloseUSD': '225.54912112'}, {'Index': '000001.SS', 'Date': '2000-01-10 00:00:00', 'CloseUSD': '247.21792976'}, {'Index': '000001.SS', 'Date': '2000-01-12 00:00:00', 'CloseUSD': '230.0832032'}, {'Index': '000001.SS', 'Date': '2000-01-14 00:00:00', 'CloseUSD': '225.41568352'}, {'Index': '000001.SS', 'Date': '2000-01-19 00:00:00', 'CloseUSD': '230.51583984'}, {'Index': '000001.SS', 'Date': '2000-01-20 00:00:00', 'CloseUSD': '234.69808592'}, {'Index': '000001.SS', 'Date': '2000-01-27 00:00:00', 'CloseUSD': '241.08271488'}, {'Index': '000001.SS', 'Date': '2000-01-28 00:00:00', 'CloseUSD': '245.59951168'}, {'Index': '000001.SS', 'Date': '2000-02-14 00:00:00', 'CloseUSD': '267.83087888'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
