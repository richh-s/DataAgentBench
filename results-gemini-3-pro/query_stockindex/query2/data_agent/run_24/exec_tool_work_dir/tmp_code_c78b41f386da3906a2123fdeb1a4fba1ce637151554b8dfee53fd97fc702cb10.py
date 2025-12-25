code = """import json

# Load the result from the file
file_path = locals()['var_function-call-12600698245989262745']
with open(file_path, 'r') as f:
    data = json.load(f)

stats = {}

for row in data:
    idx = row['Index']
    open_p = float(row['Open'])
    close_p = float(row['Close'])
    
    if idx not in stats:
        stats[idx] = {'up': 0, 'down': 0}
    
    if close_p > open_p:
        stats[idx]['up'] += 1
    elif close_p < open_p:
        stats[idx]['down'] += 1

result_indices = []
print("Stats per index:")
for idx, counts in stats.items():
    print(f"{idx}: Up {counts['up']}, Down {counts['down']}")
    if counts['up'] > counts['down']:
        result_indices.append(idx)

print("__RESULT__:")
print(json.dumps(result_indices))"""

env_args = {'var_function-call-2512828619295309790': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-2512828619295308115': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-14525977137551414892': [{'Index': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}, {'Index': 'NYA', 'up_days': '36.0', 'down_days': '42.0'}], 'var_function-call-10327379880185848396': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_function-call-12600698245989262745': 'file_storage/function-call-12600698245989262745.json'}

exec(code, env_args)
