code = """import json

exchanges = locals()['var_function-call-1755041149458284533']
trade_stats = locals()['var_function-call-1755041149458281546']

# Map Index to Exchange/Region manually based on standard tickers
# NYA -> NYSE (US)
# IXIC -> NASDAQ (US)
# GSPTSE -> TSX (Canada)
# Rest are not North American
na_indices = ['NYA', 'IXIC', 'GSPTSE']

results = []
for record in trade_stats:
    idx = record['Index']
    if idx in na_indices:
        up = float(record['up_days'])
        down = float(record['down_days'])
        if up > down:
            results.append(idx)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-1755041149458284533': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-1755041149458281546': [{'Index': 'J203.JO', 'up_days': '37.0', 'down_days': '44.0'}, {'Index': 'N225', 'up_days': '32.0', 'down_days': '42.0'}, {'Index': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'NSEI', 'up_days': '40.0', 'down_days': '39.0'}, {'Index': 'GDAXI', 'up_days': '50.0', 'down_days': '48.0'}, {'Index': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}, {'Index': 'NYA', 'up_days': '37.0', 'down_days': '42.0'}, {'Index': 'N100', 'up_days': '32.0', 'down_days': '36.0'}, {'Index': '399001.SZ', 'up_days': '33.0', 'down_days': '43.0'}, {'Index': '000001.SS', 'up_days': '47.0', 'down_days': '37.0'}, {'Index': 'SSMI', 'up_days': '54.0', 'down_days': '39.0'}, {'Index': 'TWII', 'up_days': '39.0', 'down_days': '39.0'}, {'Index': 'HSI', 'up_days': '44.0', 'down_days': '42.0'}]}

exec(code, env_args)
