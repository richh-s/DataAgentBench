code = """import json
import pandas as pd

# Load all price data
with open(locals()['var_functions.query_db:12'], 'r') as f:
    price_data = json.load(f)

df = pd.DataFrame(price_data)
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date', 'CloseUSD'])
df = df.sort_values(['Index', 'Date'])

# Country mapping
index_to_country = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    'NYA': 'United States',
    'IXIC': 'United States',
    'GDAXI': 'Germany',
    'GSPTSE': 'Canada',
    'TWII': 'Taiwan',
    'SSMI': 'Switzerland',
    'N100': 'Netherlands',
    'J203.JO': 'South Africa',
    'NSEI': 'India',
    '000001.SS': 'China (Shanghai)',
    '399001.SZ': 'China (Shenzhen)'
}

# Calculate returns for each index
results = []

for index in df['Index'].unique():
    df_index = df[df['Index'] == index].copy()
    df_index = df_index.sort_values('Date')
    
    if len(df_index) < 12:
        continue
    
    # Get monthly data starting from 2000
    df_index['year'] = df_index['Date'].dt.year
    df_index['month'] = df_index['Date'].dt.month
    monthly_data = df_index.groupby(['year', 'month']).first().reset_index()
    monthly_data = monthly_data[monthly_data['year'] >= 2000]
    
    if len(monthly_data) < 12:
        continue
    
    total_invested = 0
    total_shares = 0
    monthly_investment = 100
    
    for _, row in monthly_data.iterrows():
        price = float(row['CloseUSD'])
        if price > 0:
            total_invested += monthly_investment
            total_shares += monthly_investment / price
    
    current_price = float(monthly_data['CloseUSD'].iloc[-1])
    current_value = total_shares * current_price
    total_return = current_value - total_invested
    total_return_pct = (total_return / total_invested) * 100 if total_invested > 0 else 0
    
    results.append({
        'index': index,
        'country': index_to_country.get(index, 'Unknown'),
        'invested': round(total_invested, 2),
        'value': round(current_value, 2),
        'return_pct': round(total_return_pct, 2),
        'num_months': len(monthly_data)
    })

# Sort by return percentage
top_5 = sorted(results, key=lambda x: x['return_pct'], reverse=True)[:5]

print('__RESULT__:')
print(json.dumps({'top_5': top_5, 'all_count': len(results)}, default=str))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Index': 'NYA', 'Date': '2000-01-03 00:00:00', 'Open': '6762.109863', 'High': '6762.109863', 'Low': '6762.109863', 'Close': '6762.109863', 'Adj Close': '6762.109863', 'CloseUSD': '6762.109863'}, {'Index': '000001.SS', 'Date': '2000-01-04 00:00:00', 'Open': '1368.692993', 'High': '1407.517944', 'Low': '1361.213989', 'Close': '1406.370972', 'Adj Close': '1406.370972', 'CloseUSD': '225.01935552'}, {'Index': 'N225', 'Date': '2000-01-04 00:00:00', 'Open': '18937.44922', 'High': '19187.60938', 'Low': '18937.44922', 'Close': '19002.85938', 'Adj Close': '19002.85938', 'CloseUSD': '190.0285938'}, {'Index': '000001.SS', 'Date': '2000-01-05 00:00:00', 'Open': '1407.828979', 'High': '1433.780029', 'Low': '1398.322998', 'Close': '1409.682007', 'Adj Close': '1409.682007', 'CloseUSD': '225.54912112'}, {'Index': '399001.SZ', 'Date': '2000-01-05 00:00:00', 'Open': '3500.129883', 'High': '3589.179932', 'Low': '3468.689941', 'Close': '3486.290039', 'Adj Close': '3486.250977', 'CloseUSD': '557.80640624'}], 'var_functions.execute_python:10': {'index_info_sample': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'index_symbols': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'price_sample': [{'Index': 'NYA', 'Date': '2000-01-03 00:00:00', 'Open': '6762.109863', 'High': '6762.109863', 'Low': '6762.109863', 'Close': '6762.109863', 'Adj Close': '6762.109863', 'CloseUSD': '6762.109863'}, {'Index': '000001.SS', 'Date': '2000-01-04 00:00:00', 'Open': '1368.692993', 'High': '1407.517944', 'Low': '1361.213989', 'Close': '1406.370972', 'Adj Close': '1406.370972', 'CloseUSD': '225.01935552'}, {'Index': 'N225', 'Date': '2000-01-04 00:00:00', 'Open': '18937.44922', 'High': '19187.60938', 'Low': '18937.44922', 'Close': '19002.85938', 'Adj Close': '19002.85938', 'CloseUSD': '190.0285938'}, {'Index': '000001.SS', 'Date': '2000-01-05 00:00:00', 'Open': '1407.828979', 'High': '1433.780029', 'Low': '1398.322998', 'Close': '1409.682007', 'Adj Close': '1409.682007', 'CloseUSD': '225.54912112'}, {'Index': '399001.SZ', 'Date': '2000-01-05 00:00:00', 'Open': '3500.129883', 'High': '3589.179932', 'Low': '3468.689941', 'Close': '3486.290039', 'Adj Close': '3486.250977', 'CloseUSD': '557.80640624'}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:18': {'total_records': 67948, 'unique_indices': 13, 'indices_summary': [{'index': '000001.SS', 'country': 'China', 'records': 4354, 'start_date': '2000-01-04 00:00:00', 'end_date': 'September 30, 2015 at 12:00 AM'}, {'index': '399001.SZ', 'country': 'China', 'records': 4355, 'start_date': '2000-01-05 00:00:00', 'end_date': 'September 30, 2015 at 12:00 AM'}, {'index': 'GDAXI', 'country': 'Germany', 'records': 5590, 'start_date': '2000-01-05 00:00:00', 'end_date': 'September 30, 2016 at 12:00 AM'}, {'index': 'GSPTSE', 'country': 'Canada', 'records': 6506, 'start_date': '2000-01-05 00:00:00', 'end_date': 'September 30, 2016 at 12:00 AM'}, {'index': 'HSI', 'country': 'Hong Kong', 'records': 5604, 'start_date': '2000-01-14 00:00:00', 'end_date': 'September 30, 2019 at 12:00 AM'}, {'index': 'IXIC', 'country': 'USA', 'records': 7351, 'start_date': '2000-01-06 00:00:00', 'end_date': 'September 30, 2015 at 12:00 AM'}, {'index': 'J203.JO', 'country': 'South Africa', 'records': 1854, 'start_date': '2012-02-08 00:00:00', 'end_date': 'September 30, 2019 at 12:00 AM'}, {'index': 'N100', 'country': 'Netherlands/Europe', 'records': 4245, 'start_date': '2000-01-10 00:00:00', 'end_date': 'September 30, 2019 at 12:00 AM'}, {'index': 'N225', 'country': 'Japan', 'records': 7979, 'start_date': '2000-01-04 00:00:00', 'end_date': 'September 30, 2020 at 12:00 AM'}, {'index': 'NSEI', 'country': 'India', 'records': 2577, 'start_date': '2007-09-25 00:00:00', 'end_date': 'September 30, 2014 at 12:00 AM'}, {'index': 'NYA', 'country': 'USA', 'records': 7960, 'start_date': '2000-01-03 00:00:00', 'end_date': 'September 30, 2020 at 12:00 AM'}, {'index': 'SSMI', 'country': 'Switzerland', 'records': 5188, 'start_date': '2000-01-05 00:00:00', 'end_date': 'September 30, 2020 at 12:00 AM'}, {'index': 'TWII', 'country': 'Taiwan', 'records': 4385, 'start_date': '2000-01-17 00:00:00', 'end_date': 'September 30, 2020 at 12:00 AM'}]}}

exec(code, env_args)
