code = """import json

# top indices from var_call_Hzz2vBRrMnirRNXSFj5aPEoA
result = var_call_Hzz2vBRrMnirRNXSFj5aPEoA

# map indices to countries using domain knowledge
index_country = {
    'IXIC': 'United States',        # NASDAQ Composite
    'NSEI': 'India',               # Nifty 50 (NSE)
    'GDAXI': 'Germany',            # DAX
    '399001.SZ': 'China',          # SZSE Component Index
    'TWII': 'Taiwan'               # TAIEX
}

for r in result:
    r['Country'] = index_country.get(r['Index'], 'Unknown')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_kPM8xWZRBlknO5G3x9PzeZs9': 'file_storage/call_kPM8xWZRBlknO5G3x9PzeZs9.json', 'var_call_GgXUvBZrMoBR1VMpYx451GC0': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_Hzz2vBRrMnirRNXSFj5aPEoA': [{'Index': 'IXIC', 'return_multiple': 4.822046767118095}, {'Index': 'NSEI', 'return_multiple': 2.3608849755128487}, {'Index': 'GDAXI', 'return_multiple': 2.3474623836455386}, {'Index': '399001.SZ', 'return_multiple': 2.344569158738743}, {'Index': 'TWII', 'return_multiple': 2.237413269332176}]}

exec(code, env_args)
