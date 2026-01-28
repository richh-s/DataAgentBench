code = """import pandas as pd
import numpy as np
import json

file_path = '/tmp/results_14.json'
with open(file_path, 'r') as f:
    trade_data = json.load(f)

df = pd.DataFrame(trade_data)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['Date', 'CloseUSD', 'Index'])

indices_with_2000_data = []
for idx in df['Index'].unique():
    idx_min_date = df[df['Index'] == idx]['Date'].min()
    if idx_min_date <= pd.Timestamp('2000-12-31'):
        indices_with_2000_data.append(idx)

results = []
for idx in sorted(indices_with_2000_data):
    idx_data = df[df['Index'] == idx].copy().sort_values('Date')
    idx_data_2000 = idx_data[idx_data['Date'] >= '2000-01-01'].copy()
    
    if len(idx_data_2000) == 0:
        continue
    
    idx_data_2000['YearMonth'] = idx_data_2000['Date'].dt.to_period('M')
    monthly_prices = idx_data_2000.groupby('YearMonth')['CloseUSD'].first().reset_index()
    
    monthly_investment = 100
    monthly_prices['Investment'] = monthly_investment
    monthly_prices['Units'] = monthly_investment / monthly_prices['CloseUSD']
    
    total_invested = monthly_prices['Investment'].sum()
    total_units = monthly_prices['Units'].sum()
    final_price = idx_data_2000['CloseUSD'].iloc[-1]
    final_value = total_units * final_price
    total_return = final_value - total_invested
    return_pct = (total_return / total_invested) * 100
    
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
    
    country = country_map.get(idx, 'Other')
    
    results.append({
        'Index': idx,
        'Country': country,
        'Total_Invested': float(round(total_invested, 2)),
        'Final_Value': float(round(final_value, 2)),
        'Return_Pct': float(round(return_pct, 2)),
        'Months': len(monthly_prices),
        'Start_Date': idx_data_2000['Date'].min().strftime('%Y-%m-%d'),
        'End_Date': idx_data_2000['Date'].max().strftime('%Y-%m-%d')
    })

results_sorted = sorted(results, key=lambda x: x['Return_Pct'], reverse=True)
top_5 = results_sorted[:5]

output = []
for item in top_5:
    output.append({
        'Index': item['Index'],
        'Country': item['Country'],
        'Return_Percentage': item['Return_Pct'],
        'Total_Invested_USD': item['Total_Invested'],
        'Final_Value_USD': item['Final_Value'],
        'Total_Return_USD': float(round(item['Final_Value'] - item['Total_Invested'], 2)),
        'Period': f"{item['Start_Date']} to {item['End_Date']}"
    })

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:12': [{'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
