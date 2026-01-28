code = """import json
import pandas as pd
from datetime import datetime

# Read the data from the file path stored in the variable
# The variable name is 'var_functions.query_db:10' but we need to access it via locals()
data_file = locals()['var_functions.query_db:10']

# Read the data
with open(data_file, 'r') as f:
    all_data = json.load(f)

# Rest of the analysis
df = pd.DataFrame(all_data)
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df[df['Date'] >= '2000-01-01']

# Map indices to countries
index_to_country = {
    '000001.SS': 'China', '399001.SZ': 'China', 'GDAXI': 'Germany',
    'GSPTSE': 'Canada', 'HSI': 'Hong Kong', 'IXIC': 'USA',
    'J203.JO': 'South Africa', 'N100': 'Belgium', 'N225': 'Japan',
    'NSEI': 'India', 'NYA': 'USA', 'SSMI': 'Switzerland', 'TWII': 'Taiwan'
}

results = []

for index in df['Index'].unique():
    index_data = df[df['Index'] == index].copy().sort_values('Date')
    
    if index_data.empty:
        continue
    
    start_date = index_data['Date'].min()
    end_date = index_data['Date'].max()
    monthly_dates = pd.date_range(start=start_date, end=end_date, freq='MS')
    
    total_investment = 0
    total_shares = 0
    
    for month_start in monthly_dates:
        month_data = index_data[index_data['Date'] >= month_start]
        if not month_data.empty:
            investment = 100
            price = month_data.iloc[0]['CloseUSD']
            if pd.notna(price) and price > 0:
                shares = investment / price
                total_investment += investment
                total_shares += shares
    
    if total_shares > 0:
        final_price = index_data.iloc[-1]['CloseUSD']
        final_value = total_shares * final_price
        total_return = final_value - total_investment
        return_pct = (total_return / total_investment) * 100 if total_investment > 0 else 0
        
        results.append({
            'Index': index,
            'Country': index_to_country.get(index, 'Unknown'),
            'Total_Investment': total_investment,
            'Final_Value': final_value,
            'Return_Percentage': return_pct,
            'Start_Date': start_date.strftime('%Y-%m-%d'),
            'End_Date': end_date.strftime('%Y-%m-%d'),
            'Months_Invested': len(monthly_dates)
        })

results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Return_Percentage', ascending=False)

top_5 = results_df.head(5)

# Format output
final_result = top_5[['Index', 'Country', 'Return_Percentage', 'Total_Investment', 'Final_Value']].copy()
final_result['Return_Percentage'] = final_result['Return_Percentage'].round(2)
final_result['Total_Investment'] = final_result['Total_Investment'].round(2)
final_result['Final_Value'] = final_result['Final_Value'].round(2)

result_json = final_result.to_json(orient='records')

print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:6': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:8': [{'Index': '000001.SS', 'min_date': '2000-01-04 00:00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'day_count': '4354'}, {'Index': '399001.SZ', 'min_date': '2000-01-05 00:00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'day_count': '4355'}, {'Index': 'GDAXI', 'min_date': '2000-01-05 00:00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'day_count': '5590'}, {'Index': 'GSPTSE', 'min_date': '2000-01-05 00:00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'day_count': '6506'}, {'Index': 'HSI', 'min_date': '2000-01-14 00:00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'day_count': '5604'}, {'Index': 'IXIC', 'min_date': '2000-01-06 00:00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'day_count': '7351'}, {'Index': 'J203.JO', 'min_date': '2012-02-08 00:00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'day_count': '1854'}, {'Index': 'N100', 'min_date': '2000-01-10 00:00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'day_count': '4245'}, {'Index': 'N225', 'min_date': '2000-01-04 00:00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'day_count': '7979'}, {'Index': 'NSEI', 'min_date': '2007-09-25 00:00:00', 'max_date': 'September 30, 2014 at 12:00 AM', 'day_count': '2577'}, {'Index': 'NYA', 'min_date': '2000-01-03 00:00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'day_count': '7960'}, {'Index': 'SSMI', 'min_date': '2000-01-05 00:00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'day_count': '5188'}, {'Index': 'TWII', 'min_date': '2000-01-17 00:00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'day_count': '4385'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
