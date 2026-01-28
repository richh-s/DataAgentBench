code = """import json
rows = var_call_IYT0dVCdVqZ4fxS4fZ3GBQKE
country_map = {
    'IXIC': 'United States',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'TWII': 'Taiwan',
    '399001.SZ': 'China'
}
for r in rows:
    r['Country'] = country_map.get(r['Index'], r.get('Country','Unknown'))
print('__RESULT__:')
print(json.dumps(rows))"""

env_args = {'var_call_yLEqysLvcLFy5q5ogsDokRKE': 'file_storage/call_yLEqysLvcLFy5q5ogsDokRKE.json', 'var_call_rjr7nTeDTr2TPNINZNtzjKhk': ['index_info'], 'var_call_AYSYWAtWG7s9sDyAbJGpxYwX': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_IYT0dVCdVqZ4fxS4fZ3GBQKE': [{'Index': 'IXIC', 'overall_return_multiple': 4.816205036184268, 'Country': 'Unknown'}, {'Index': 'NSEI', 'overall_return_multiple': 2.3564091777426452, 'Country': 'Unknown'}, {'Index': 'GDAXI', 'overall_return_multiple': 2.3537005565588847, 'Country': 'Unknown'}, {'Index': '399001.SZ', 'overall_return_multiple': 2.3383811889670953, 'Country': 'China'}, {'Index': 'TWII', 'overall_return_multiple': 2.2447368452852596, 'Country': 'Unknown'}]}

exec(code, env_args)
