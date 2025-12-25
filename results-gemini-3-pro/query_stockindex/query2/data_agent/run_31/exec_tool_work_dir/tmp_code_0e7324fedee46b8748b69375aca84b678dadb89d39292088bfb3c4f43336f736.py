code = """import json

# Load the result from the file
with open(locals()['var_function-call-14057108216755507726'], 'r') as f:
    data = json.load(f)

# Initialize counters
stats = {} # {index: {'up': 0, 'down': 0}}

for row in data:
    idx = row['Index']
    open_price = float(row['Open'])
    close_price = float(row['Close'])
    
    if idx not in stats:
        stats[idx] = {'up': 0, 'down': 0}
        
    if close_price > open_price:
        stats[idx]['up'] += 1
    elif close_price < open_price:
        stats[idx]['down'] += 1

# Filter indices
result_indices = []
for idx, counts in stats.items():
    if counts['up'] > counts['down']:
        result_indices.append(idx)

print("__RESULT__:")
print(json.dumps(result_indices))"""

env_args = {'var_function-call-12647511661849871000': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-12647511661849872821': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_function-call-6522930887672667334': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-14057108216755507726': 'file_storage/function-call-14057108216755507726.json'}

exec(code, env_args)
