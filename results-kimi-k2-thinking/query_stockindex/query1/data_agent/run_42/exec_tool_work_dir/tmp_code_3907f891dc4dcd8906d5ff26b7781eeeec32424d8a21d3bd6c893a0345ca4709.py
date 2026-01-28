code = """import json, os

# Load trade data
trade_data = locals().get('var_functions.query_db:6', [])

# Handle file path or direct data
index_trade = []
if isinstance(trade_data, str) and os.path.exists(trade_data):
    with open(trade_data, 'r') as f:
        index_trade = json.load(f)
else:
    index_trade = trade_data

print('Total records loaded:', len(index_trade))
print('First record:', index_trade[0] if index_trade else 'None')

# Asia indices present
asia_indices = ['000001.SS', '399001.SZ', 'HSI', 'N225', 'NSEI', 'TWII']

# Filter and calculate
results = {}
for idx in asia_indices:
    volatilities = []
    for record in index_trade:
        if record.get('Index') == idx:
            date_str = record.get('Date', '')
            if any(year in date_str for year in ['2020', '2021', '2022', '2023']):
                try:
                    o = float(record.get('Open', 0))
                    h = float(record.get('High', 0))
                    l = float(record.get('Low', 0))
                    if o > 0:
                        vol = (h - l) / o
                        volatilities.append(vol)
                except:
                    pass
    
    if volatilities:
        avg_vol = sum(volatilities) / len(volatilities)
        results[idx] = {'avg': avg_vol, 'count': len(volatilities)}

# Sort and find highest
sorted_results = sorted(results.items(), key=lambda x: x[1]['avg'], reverse=True)

print('Sorted results:')
for sym, data in sorted_results:
    print(sym, data['avg'], data['count'])

best = sorted_results[0] if sorted_results else None

# Format final answer
final = None
if best:
    final = {'symbol': best[0], 'avg_volatility': best[1]['avg']}

print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'total_records': 48151, 'first_record': {'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, 'last_record': {'Index': 'J203.JO', 'Date': '31 May 2021, 00:00', 'Open': '67554.85938', 'High': '68140.85156', 'Low': '67554.85938', 'Close': '67964.03906', 'Adj Close': '67964.03906', 'CloseUSD': '4757.4827342'}, 'unique_indices': ['000001.SS', '399001.SZ', 'GDAXI', 'GSPTSE', 'HSI', 'IXIC', 'J203.JO', 'N100', 'N225', 'NSEI', 'NYA', 'SSMI', 'TWII']}}

exec(code, env_args)
