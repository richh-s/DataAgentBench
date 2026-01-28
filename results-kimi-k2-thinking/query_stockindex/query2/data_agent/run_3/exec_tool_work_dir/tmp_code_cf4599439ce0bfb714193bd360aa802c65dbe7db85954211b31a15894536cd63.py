code = """import json
import os
import re
from datetime import datetime

# Get the results
result_key = 'var_functions.query_db:16'
result_data = locals().get(result_key, '[]')

# If result_data is a string (file path), read the file
if isinstance(result_data, str) and os.path.exists(result_data):
    with open(result_data, 'r') as f:
        result_data = json.load(f)

# Function to extract year from various date formats
def extract_year(date_str):
    # Look for 4-digit year pattern
    match = re.search(r'(\d{4})', date_str)
    if match:
        return match.group(1)
    return None

# Filter for 2018 data
indices = ['NYA', 'IXIC', 'GSPTSE']
trade_data = []

for record in result_data:
    year = extract_year(record['Date'])
    if year == '2018' and record['Index'] in indices:
        try:
            # Convert to float
            open_price = float(record['Open'])
            close_price = float(record['Close'])
            trade_data.append({
                'Index': record['Index'],
                'Date': record['Date'],
                'Open': open_price,
                'Close': close_price
            })
        except (ValueError, TypeError):
            continue

# Group by index and analyze up/down days
results = {}
for index in indices:
    index_data = [d for d in trade_data if d['Index'] == index]
    up_days = 0
    down_days = 0
    total_days = 0
    
    for day in index_data:
        total_days += 1
        if day['Close'] > day['Open']:
            up_days += 1
        elif day['Close'] < day['Open']:
            down_days += 1
        # Equal days are neither up nor down
    
    results[index] = {
        'up_days': up_days,
        'down_days': down_days,
        'total_days': total_days,
        'diff': up_days - down_days
    }

# Check which indices have more up days
indices_with_more_up = [index for index, data in results.items() if data['diff'] > 0]

print('__RESULT__:')
print(json.dumps({
    'analysis': results,
    'indices_with_more_up': indices_with_more_up
}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:6': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}, {'Index': 'HSI', 'Date': '1987-01-08 00:00:00', 'Open': '2603.300049', 'High': '2603.300049', 'Low': '2603.300049', 'Close': '2603.300049', 'Adj Close': '2603.300049', 'CloseUSD': '338.42900637'}, {'Index': 'HSI', 'Date': '1987-01-09 00:00:00', 'Open': '2561.699951', 'High': '2561.699951', 'Low': '2561.699951', 'Close': '2561.699951', 'Adj Close': '2561.699951', 'CloseUSD': '333.02099363'}, {'Index': 'HSI', 'Date': '1987-01-12 00:00:00', 'Open': '2614.899902', 'High': '2614.899902', 'Low': '2614.899902', 'Close': '2614.899902', 'Adj Close': '2614.899902', 'CloseUSD': '339.93698726'}, {'Index': 'HSI', 'Date': '1987-01-13 00:00:00', 'Open': '2590.800049', 'High': '2590.800049', 'Low': '2590.800049', 'Close': '2590.800049', 'Adj Close': '2590.800049', 'CloseUSD': '336.80400637'}, {'Index': 'HSI', 'Date': '1987-01-14 00:00:00', 'Open': '2578.199951', 'High': '2578.199951', 'Low': '2578.199951', 'Close': '2578.199951', 'Adj Close': '2578.199951', 'CloseUSD': '335.16599363'}], 'var_functions.query_db:8': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_records': 753, 'sample_records': [{'Index': 'GSPTSE', 'Date': '01 Mar 2018, 00:00', 'Open': '15452.7002', 'Close': '15394.0'}, {'Index': 'GSPTSE', 'Date': '01 May 2018, 00:00', 'Open': '15592.5', 'Close': '15618.90039'}, {'Index': 'GSPTSE', 'Date': '01 Oct 2018, 00:00', 'Open': '16152.29981', 'Close': '16104.40039'}, {'Index': 'GSPTSE', 'Date': '02 Nov 2018, 00:00', 'Open': '15204.29981', 'Close': '15119.29981'}, {'Index': 'GSPTSE', 'Date': '03 Dec 2018, 00:00', 'Open': '15358.90039', 'Close': '15275.0'}]}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
