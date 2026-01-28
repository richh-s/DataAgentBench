code = """import pandas as pd
import numpy as np
import json

# Read the full data from the file
with open(var_functions.query_db:14, 'r') as f:
    trade_data = json.load(f)

# Create DataFrame
df = pd.DataFrame(trade_data)

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Convert CloseUSD to numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Filter out rows with missing values
df = df.dropna(subset=['Date', 'CloseUSD', 'Index'])

# Filter indices that have data since at least 2000-01-01
indices_to_check = df['Index'].unique()
viable_indices = []

for idx in indices_to_check:
    idx_data = df[df['Index'] == idx]
    min_date = idx_data['Date'].min()
    if min_date <= pd.Timestamp('2000-01-31'):
        viable_indices.append(idx)

print(f"Indices with data starting from 2000: {sorted(viable_indices)}")

# For each viable index, calculate dollar-cost-averaged returns since January 2000
results = []

for idx in viable_indices:
    idx_data = df[df['Index'] == idx].copy()
    idx_data = idx_data.sort_values('Date')
    
    # Filter from January 2000 onwards
    idx_data = idx_data[idx_data['Date'] >= '2000-01-01']
    
    if len(idx_data) == 0:
        continue
    
    # Get the first trading day of each month and its closing price
    idx_data['YearMonth'] = idx_data['Date'].dt.to_period('M')
    monthly_data = idx_data.groupby('YearMonth').agg({
        'Date': 'first',
        'CloseUSD': 'first'
    }).reset_index()
    
    # Invest $100 at the beginning of each month (or first trading day of that month)
    # Assume the investment is made at the closing price of the first trading day
    monthly_investment = 100
    monthly_data['Units_Bought'] = monthly_investment / monthly_data['CloseUSD']
    monthly_data['Total_Invested'] = monthly_investment
    
    # Calculate cumulative units and investments over time
    monthly_data['Cumulative_Units'] = monthly_data['Units_Bought'].cumsum()
    monthly_data['Cumulative_Investment'] = monthly_data['Total_Invested'].cumsum()
    
    # Get final values (last date for this index)
    final_price = idx_data['CloseUSD'].iloc[-1]
    final_date = idx_data['Date'].iloc[-1]
    total_units = monthly_data['Units_Bought'].sum()
    total_invested = monthly_data['Total_Invested'].sum()
    final_value = total_units * final_price
    total_return = final_value - total_invested
    return_pct = (total_return / total_invested) * 100
    
    # Determine country based on index symbol
    if idx == 'GDAXI':
        country = 'Germany'
        exchange = 'Frankfurt Stock Exchange'
    elif idx == 'GSPTSE':
        country = 'Canada'
        exchange = 'Toronto Stock Exchange'
    elif idx == 'HSI':
        country = 'Hong Kong'
        exchange = 'Hong Kong Stock Exchange'
    elif idx == 'IXIC':
        country = 'United States'
        exchange = 'NASDAQ'
    elif idx == 'N225':
        country = 'Japan'
        exchange = 'Tokyo Stock Exchange'
    elif idx == 'NYA':
        country = 'United States'
        exchange = 'New York Stock Exchange'
    elif idx == 'SSMI':
        country = 'Switzerland'
        exchange = 'Swiss Exchange'
    else:
        country = 'Unknown'
        exchange = 'Unknown'
    
    results.append({
        'Index': idx,
        'Country': country,
        'Exchange': exchange,
        'Total_Invested': total_invested,
        'Final_Value': final_value,
        'Total_Return': total_return,
        'Return_Percentage': return_pct,
        'Number_of_Months': len(monthly_data),
        'Start_Date': idx_data['Date'].min().strftime('%Y-%m-%d'),
        'End_Date': final_date.strftime('%Y-%m-%d')
    })

# Convert to DataFrame and sort by Return_Percentage
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Return_Percentage', ascending=False)

# Get top 5
top_5 = results_df.head(5)

print("TOP 5 INDICES BY DOLLAR-COST-AVERAGED RETURNS SINCE 2000:")
print("=" * 80)
for _, row in top_5.iterrows():
    print(f"\nIndex: {row['Index']}")
    print(f"Country: {row['Country']}")
    print(f"Exchange: {row['Exchange']}")
    print(f"Total Invested: ${row['Total_Invested']:,.2f}")
    print(f"Final Value: ${row['Final_Value']:,.2f}")
    print(f"Total Return: ${row['Total_Return']:,.2f}")
    print(f"Return: {row['Return_Percentage']:.2f}%")
    print(f"Period: {row['Start_Date']} to {row['End_Date']}")

# For JSON output
output_data = {
    'summary': top_5[['Index', 'Country', 'Return_Percentage', 'Total_Invested', 'Final_Value', 'Total_Return']].to_dict('records'),
    'all_results': results_df.to_dict('records')
}

print("\n" + "=" * 80)
print("JSON OUTPUT:")
print("=" * 80)
____RESULT____:
print(json.dumps(output_data, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:12': [{'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
