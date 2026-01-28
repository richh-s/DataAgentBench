code = """import json

# Load the data from the file
file_path = 'var_functions.query_db:10'
with open(file_path, 'r') as f:
    price_data = json.load(f)

print('Total records loaded: ' + str(len(price_data)))

# Group data by index
indices_data = {}
for record in price_data:
    idx = record['Index']
    if idx not in indices_data:
        indices_data[idx] = []
    indices_data[idx].append({
        'Date': record['Date'],
        'CloseUSD': float(record['CloseUSD'])
    })

# Display information about each index
print('\nIndices found (' + str(len(indices_data)) + ' total):')
for idx in sorted(indices_data.keys()):
    print('  ' + idx + ': ' + str(len(indices_data[idx])) + ' records')
    
# Show date ranges
print('\nDate ranges:')
for idx in sorted(indices_data.keys()):
    dates = [r['Date'] for r in indices_data[idx]]
    print('  ' + idx + ': ' + min(dates) + ' to ' + max(dates))

# Check if we have data from 2000 onwards
indices_from_2000 = []
for idx, data in indices_data.items():
    min_date = min([r['Date'] for r in data])
    if min_date <= '2000-12-31':
        indices_from_2000.append(idx)

print('\nIndices with data from 2000: ' + str(indices_from_2000))
print('Count: ' + str(len(indices_from_2000)))

# Store information about data structure
index_info = {}
for idx in indices_from_2000:
    data = indices_data[idx]
    index_info[idx] = {
        'count': len(data),
        'min_date': min([r['Date'] for r in data]),
        'max_date': max([r['Date'] for r in data]),
        'min_price': min([r['CloseUSD'] for r in data]),
        'max_price': max([r['CloseUSD'] for r in data])
    }

print('\n---BEGIN PRINT FORMAT---')
print('__RESULT__:')
print(json.dumps(index_info))
print('---END PRINT FORMAT---')"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
