code = """import json
# var_call_w0m33sLQKWyteufc89Sa0DHv is available from previous query
data = var_call_w0m33sLQKWyteufc89Sa0DHv
# Normalize and find indices with more up days than down days
result = []
for rec in data:
    idx = rec.get('Index')
    up = int(float(rec.get('up_days', 0)))
    down = int(float(rec.get('down_days', 0)))
    flat = int(float(rec.get('flat_days', 0)))
    total = int(float(rec.get('total_days', 0)))
    if up > down:
        result.append({'Index': idx, 'up_days': up, 'down_days': down, 'flat_days': flat, 'total_days': total})
# Prepare JSON string
out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_UVobKpfZV1lS4IitBRh3g0tG': ['index_trade'], 'var_call_1sF1x3KpLF8HTFZ1n9hYtE5m': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_oMCuTvXr8qFWGdt3nPjHtfP2': ['index_info'], 'var_call_dNtN3kBI7r4w7gU6teKVzkBH': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_w0m33sLQKWyteufc89Sa0DHv': [{'Index': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0', 'flat_days': '1.0', 'total_days': '86'}, {'Index': 'NYA', 'up_days': '36.0', 'down_days': '42.0', 'flat_days': '0.0', 'total_days': '78'}, {'Index': 'IXIC', 'up_days': '44.0', 'down_days': '31.0', 'flat_days': '0.0', 'total_days': '75'}]}

exec(code, env_args)
