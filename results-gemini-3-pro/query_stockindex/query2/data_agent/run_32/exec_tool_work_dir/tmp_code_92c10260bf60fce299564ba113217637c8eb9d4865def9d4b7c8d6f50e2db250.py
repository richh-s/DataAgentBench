code = """import json
from collections import defaultdict

# Load the data from the file provided in previous step
with open(locals()['var_function-call-12500423420913579103'], 'r') as f:
    data = json.load(f)

up_counts = defaultdict(int)
down_counts = defaultdict(int)

for row in data:
    idx = row['Index']
    try:
        # Open and Close are strings in the JSON preview, need to convert to float
        open_price = float(row['Open'])
        close_price = float(row['Close'])
        
        if close_price > open_price:
            up_counts[idx] += 1
        elif close_price < open_price:
            down_counts[idx] += 1
    except ValueError:
        continue

results = {}
for idx in up_counts.keys():
    results[idx] = {
        'up': up_counts[idx],
        'down': down_counts[idx],
        'more_up': up_counts[idx] > down_counts[idx]
    }

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-4237108260261069676': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-4237108260261069309': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'HSI'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-11518169540799162858': [{'Index': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'NYA', 'up_days': '36.0', 'down_days': '42.0'}, {'Index': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}], 'var_function-call-10312917885997782843': [{'Date': '05 Feb 1971, 00:00'}, {'Date': '08 Feb 1971, 00:00'}, {'Date': '1971-02-09 00:00:00'}, {'Date': '1971-02-10 00:00:00'}, {'Date': '11 Feb 1971, 00:00'}], 'var_function-call-12500423420913579103': 'file_storage/function-call-12500423420913579103.json'}

exec(code, env_args)
